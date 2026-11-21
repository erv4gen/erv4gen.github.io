# /// script
# dependencies = ["feedparser", "httpx"]
# ///
"""Build substack.xml: the site's live feed, rewritten so Substack's importer keeps the math.

Substack's importer has no math support, so:
  - display math (\\[...\\], $$...$$) becomes a PNG rendered by MathJax (render.mjs),
    hosted under /assets/substack-math/ and named by a hash of its TeX;
  - inline math (\\(...\\), $...$) becomes Unicode text, since Substack has no inline images;
  - tables become PNGs too (a MathJax array), since the importer flattens <table> into one line;
  - relative and github.io URLs become absolute veremin.net URLs;
  - the script removes images that return 404, so Substack does not import empty boxes.

usage (from the repo root):
  cd _tools/substack && npm install && cd ../..
  uv run _tools/substack/build_feed.py
Then commit substack.xml, the substack-feeds/ and assets/substack-math/ folders, and push.
In Substack, open Settings > Import/Export > Import posts and paste the feed URL:
https://veremin.net/substack.xml
To import one post at a time, paste its own feed instead:
https://veremin.net/substack-feeds/<slug>.xml (one file per post, same content)
"""
import hashlib
import html
import json
import re
import subprocess
import sys
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import httpx

SITE = "https://veremin.net"
OLD_SITE = "https://erv4gen.github.io"
REPO = Path(__file__).resolve().parents[2]
MATH_DIR = REPO / "assets" / "substack-math"
OUT = REPO / "substack.xml"
PER_POST = REPO / "substack-feeds"  # one feed per post, to import posts one at a time
# posts left out of the Substack import, by their veremin.net URL
EXCLUDE = {
    f"{SITE}/my-experiments-with-an-ai-assistant-or-how-not-to-search-for-shows-in-nyc/",
    f"{SITE}/introducing-wadset-the-building-block-of-defi/",
    f"{SITE}/what-is-liquidity-management-2/",
    f"{SITE}/optimizing-risks-for-a-portfolio-of-cryptocurrencies-2/",
}

SYMBOLS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ",
    "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "phi": "φ", "varphi": "φ", "chi": "χ",
    "psi": "ψ", "omega": "ω", "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ",
    "Pi": "Π", "Sigma": "Σ", "Phi": "Φ", "Omega": "Ω",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠", "approx": "≈",
    "sim": "~", "times": "×", "cdot": "·", "pm": "±", "infty": "∞", "to": "→",
    "rightarrow": "→", "leftarrow": "←", "Rightarrow": "⇒", "in": "∈", "notin": "∉",
    "subset": "⊂", "cup": "∪", "cap": "∩", "ldots": "…", "cdots": "⋯", "dots": "…",
    "sum": "Σ", "prod": "Π", "partial": "∂", "nabla": "∇", "forall": "∀", "exists": "∃",
    "propto": "∝", "equiv": "≡", "neg": "¬", "land": "∧", "lor": "∨", "mid": "|",
    "lfloor": "⌊", "rfloor": "⌋", "lceil": "⌈", "rceil": "⌉", "langle": "⟨", "rangle": "⟩",
    "log": "log", "ln": "ln", "exp": "exp", "max": "max", "min": "min", "lim": "lim",
    "sin": "sin", "cos": "cos", "Pr": "Pr", "%": "%", "$": "$", "{": "{", "}": "}",
    "ast": "∗", "star": "⋆", "prime": "′",
    "_": "_", "&": "&", ",": " ", ";": " ", ":": " ", "!": "", " ": " ", "quad": " ", "qquad": " ",
}
BLACKBOARD = {"E": "𝔼", "R": "ℝ", "N": "ℕ", "Z": "ℤ", "Q": "ℚ", "P": "ℙ", "C": "ℂ"}
SUP = dict(zip("0123456789+-=()abcdefghijklmnoprstuvwxyzT∗′",
               "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᵀ*′"))
SUB = dict(zip("0123456789+-=()aeoxhklmnpstijruv", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ"))
SUB[","] = SUP[","] = ","  # S_{n,i} reads as Sₙ,ᵢ
ACCENTS = {"hat": "̂", "widehat": "̂", "bar": "̄", "tilde": "̃",
           "widetilde": "̃", "overline": "̅"}  # combining characters
CALLIGRAPHIC = {"B": "ℬ", "L": "ℒ", "N": "𝒩", "F": "ℱ", "H": "ℋ", "M": "ℳ", "E": "ℰ", "P": "𝒫"}
WRAPPERS = ("text", "mathrm", "mathit", "mathbf", "textbf", "textit", "operatorname", "mathsf", "boldsymbol")


def group(s, i):
    """Return (content, next_index) for the TeX argument starting at s[i]."""
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        depth, j = 1, i + 1
        while j < len(s) and depth:
            depth += {"{": 1, "}": -1}.get(s[j], 0)
            j += 1
        return s[i + 1:j - 1], j
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def script(text, table, mark):
    if all(c in table for c in text):
        return "".join(table[c] for c in text)
    return f"{mark}{text}" if text.isalnum() else f"{mark}({text})"


def tex_to_unicode(tex):
    """Convert inline TeX to readable Unicode; return (text, clean) where clean=False means a lossy degrade."""
    out, i, clean = [], 0, True
    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", tex[i:])
            name, i = m.group(1), i + len(m.group(0))
            if name in WRAPPERS:
                arg, i = group(tex, i)
                out.append(tex_to_unicode(arg)[0])
            elif name in ("mathbb", "mathcal"):
                arg, i = group(tex, i)
                out.append((BLACKBOARD if name == "mathbb" else CALLIGRAPHIC).get(arg, arg))
            elif name in ("frac", "dfrac", "tfrac"):
                a, i = group(tex, i)
                b, i = group(tex, i)
                a, b = tex_to_unicode(a)[0], tex_to_unicode(b)[0]
                wrap = lambda x: x if re.fullmatch(r"[\w.]+", x) else f"({x})"
                out.append(f"{wrap(a)}/{wrap(b)}")
            elif name == "sqrt":
                a, i = group(tex, i)
                a = tex_to_unicode(a)[0]
                out.append(f"√{a}" if len(a) == 1 else f"√({a})")
            elif name in ("left", "right", "big", "Big", "bigl", "bigr", "displaystyle"):
                pass
            elif name in ACCENTS:
                a, i = group(tex, i)
                out.append(tex_to_unicode(a)[0] + ACCENTS[name])
            elif name in SYMBOLS:
                out.append(SYMBOLS[name])
            else:
                out.append(name)
                clean = False
        elif c in "^_":
            arg, i = group(tex, i + 1)
            text = tex_to_unicode(arg)[0]
            conv = script(text, SUP if c == "^" else SUB, c)
            clean &= not conv.startswith(c)
            out.append(conv)
        elif c in "{}":
            i += 1
        else:
            out.append(c)
            i += 1
    text = re.sub(r"\s+", " ", "".join(out)).strip()
    text = re.sub(r"([{(\[]) | ([})\]])", r"\1\2", text)  # "\left\{ S\right\}" -> "{S}"
    return text, clean


def is_currency(body):
    """'$52 (Save $' is two prices, but '$1-K$' and '$0.1$' are math: a price is a number followed by a space."""
    return bool(re.match(r"\d[\d,.]*\s", body)) and not re.search(r"[\\^_{]", body)


class Converter:
    def __init__(self):
        self.jobs, self.residue, self.inline_count, self.display_count = {}, [], 0, 0

    def display(self, tex, alt=None):
        # WordPress-era posts carry <br> tags inside the TeX; MathJax on the site skips them
        tex = re.sub(r"<br\s*/?>", " ", html.unescape(tex)).strip()
        digest = hashlib.sha1(tex.encode()).hexdigest()[:12]
        out = MATH_DIR / f"{digest}.png"
        # a bare # is a TeX error; MathJax 2 on the site tolerates it, MathJax 3 does not
        self.jobs[digest] = {"tex": re.sub(r"(?<!\\)#", r"\\#", tex), "display": True, "out": str(out)}
        self.display_count += 1
        alt = html.escape(alt or tex, quote=True)
        return f'<img src="{SITE}/assets/substack-math/{digest}.png" alt="{alt}" />'

    def inline(self, tex, post):
        tex = re.sub(r"<br\s*/?>", " ", html.unescape(tex))
        if re.search(r"\\begin|\\choose|\\binom", tex):
            # no readable one-line text form; show it as an equation image on its own line
            return self.display(html.escape(tex, quote=False))
        text, clean = tex_to_unicode(tex)
        self.inline_count += 1
        if not clean:
            self.residue.append((post, tex, text))
        return html.escape(text, quote=False)

    def math(self, chunk, post):
        chunk = re.sub(r"\\\[(.+?)\\\]", lambda m: self.display(m.group(1)), chunk, flags=re.S)
        chunk = re.sub(r"\$\$(.+?)\$\$", lambda m: self.display(m.group(1)), chunk, flags=re.S)
        chunk = re.sub(r"\\\((.+?)\\\)", lambda m: self.inline(m.group(1), post), chunk, flags=re.S)

        def single(m):
            body = m.group(1)
            if is_currency(body):
                return m.group(0)
            return self.inline(body, post)

        # MathJax accepts "$ k$" with inner spaces, so this does too; prices are left alone
        return re.sub(r"(?<![\\$])\$([^$<>]+?)\$(?!\d)", single, chunk)

    def table(self, m):
        """Render an HTML table as a MathJax array image; cells keep their $...$ math."""
        rows = [[html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
                 for c in re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", tr, flags=re.S | re.I)]
                for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", m.group(0), flags=re.S | re.I)]
        rows = [r for r in rows if any(r)]  # WordPress tables often have an empty header row
        if not rows:
            return ""
        width = max(map(len, rows))
        rows = [r + [""] * (width - len(r)) for r in rows]
        keep = [j for j in range(width) if any(r[j] for r in rows)]
        rows = [[r[j] for j in keep] for r in rows]

        greek = {v: k for k, v in SYMBOLS.items() if k.isalpha() and "\u0370" <= v <= "\u03ff"}

        def cell(c, bold):
            out = []
            for k, part in enumerate(re.split(r"\$([^$]+)\$", c)):
                if k % 2:
                    # the MathJax SVG font has no glyph for a literal σ; \sigma it does
                    out.append("".join(rf"\{greek[ch]} " if ch in greek else ch for ch in part))
                elif part.strip():
                    text = re.sub(r"([\\{}_%&#$^~])", lambda x: {"\\": r"\textbackslash{}", "^": r"\^{}",
                                                                 "~": r"\~{}"}.get(x.group(1), "\\" + x.group(1)), part)
                    out.append(rf"\textbf{{{text}}}" if bold else rf"\text{{{text}}}")
            return " ".join(out)

        lines = [" & ".join(cell(c, i == 0) for c in r) for i, r in enumerate(rows)]
        tex = (r"\begin{array}{" + "l" * len(keep) + "}" + lines[0] + r" \\ \hline "
               + r" \\ ".join(lines[1:]) + r"\end{array}")
        alt = "; ".join(", ".join(re.sub(r"\$", "", c) for c in r) for r in rows)
        return "<p>" + self.display(html.escape(tex, quote=False), alt=alt) + "</p>"

    def content(self, body, post):
        body = re.sub(r"<table\b.*?</table>", self.table, body, flags=re.S | re.I)
        # leave <pre>/<code> untouched
        parts = re.split(r"(<pre\b.*?</pre>|<code\b.*?</code>)", body, flags=re.S | re.I)
        return "".join(p if i % 2 else self.math(p, post) for i, p in enumerate(parts))


def excerpt(body, length=280):
    """Plain-text start of the converted post, for <description>. The feed's own summary
    cuts equations in half, so the converter cannot read its math."""
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= length else text[:length].rsplit(" ", 1)[0] + "…"


def absolutize(body):
    body = body.replace(OLD_SITE, SITE)
    return re.sub(r'(src|href)="/(?!/)', rf'\1="{SITE}/', body)


def drop_dead_images(body, client, post, dropped):
    def check(m):
        src = m.group(1)
        if "/assets/substack-math/" in src:
            return m.group(0)
        try:
            ok = client.head(src).status_code < 400
        except httpx.HTTPError:
            ok = False
        if not ok:
            dropped.append((post, src))
        return m.group(0) if ok else ""

    return re.sub(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>', check, body)


def cdata(s):
    return "<![CDATA[" + s.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def main():
    feed = feedparser.parse(httpx.get(f"{SITE}/feed.xml", follow_redirects=True).text, sanitize_html=False)
    conv, dropped = Converter(), []
    client = httpx.Client(follow_redirects=True, timeout=30)
    items = []  # (slug, <item> xml)
    for e in feed.entries:
        link = e.link.replace(OLD_SITE, SITE)
        if link in EXCLUDE:
            continue
        body = absolutize(e.content[0].value)
        body = conv.content(body, e.title)
        body = drop_dead_images(body, client, e.title, dropped)
        published = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
        slug = link.rstrip("/").rsplit("/", 1)[-1].removesuffix(".html")
        items.append((slug, f"""    <item>
      <title>{html.escape(e.title)}</title>
      <link>{link}</link>
      <guid isPermaLink="true">{link}</guid>
      <pubDate>{format_datetime(published)}</pubDate>
      <description>{cdata(excerpt(body))}</description>
      <content:encoded>{cdata(body)}</content:encoded>
    </item>"""))

    MATH_DIR.mkdir(parents=True, exist_ok=True)
    todo = [j for j in conv.jobs.values() if not Path(j["out"]).exists()]
    if todo:
        r = subprocess.run(["node", str(Path(__file__).with_name("render.mjs"))],
                           input=json.dumps(todo), text=True, capture_output=True)
        sys.stderr.write(r.stderr)
    missing = [j["tex"] for j in conv.jobs.values() if not Path(j["out"]).exists()]
    if missing:
        sys.exit(f"{len(missing)} display equations failed to render; substack.xml not written")

    def rss(xml_items):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{html.escape(feed.feed.title)}</title>
    <link>{SITE}/</link>
    <description>{html.escape(feed.feed.get("subtitle", ""))}</description>
{chr(10).join(xml_items)}
  </channel>
</rss>
"""

    OUT.write_text(rss([x for _, x in items]))
    PER_POST.mkdir(exist_ok=True)
    for old in PER_POST.glob("*.xml"):
        old.unlink()
    for slug, x in items:
        (PER_POST / f"{slug}.xml").write_text(rss([x]))
    print(f"wrote {OUT.relative_to(REPO)}: {len(items)} posts, "
          f"{conv.display_count} display equations ({len(conv.jobs)} unique images), "
          f"{conv.inline_count} inline expressions")
    print(f"wrote {PER_POST.relative_to(REPO)}/: one feed per post")
    for slug, _ in items:
        print(f"  {SITE}/{PER_POST.name}/{slug}.xml")
    if dropped:
        print(f"\ndropped {len(dropped)} dead images:")
        for post, src in dropped:
            print(f"  [{post[:40]}] {src}")
    if conv.residue:
        print(f"\n{len(conv.residue)} inline expressions degraded (check these read OK):")
        for post, tex, text in conv.residue:
            print(f"  [{post[:40]}] {tex!r} -> {text!r}")


if __name__ == "__main__":
    main()
