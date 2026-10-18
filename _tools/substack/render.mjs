// Render TeX to PNG with MathJax (same engine the site uses) and resvg.
// stdin: JSON [{tex, display, out}]; writes each PNG to `out`.
import { readFileSync, writeFileSync } from "node:fs";
import { Resvg } from "@resvg/resvg-js";
import { mathjax } from "mathjax-full/js/mathjax.js";
import { TeX } from "mathjax-full/js/input/tex.js";
import { AllPackages } from "mathjax-full/js/input/tex/AllPackages.js";
import { SVG } from "mathjax-full/js/output/svg.js";
import { liteAdaptor } from "mathjax-full/js/adaptors/liteAdaptor.js";
import { RegisterHTMLHandler } from "mathjax-full/js/handlers/html.js";

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const doc = mathjax.document("", {
  InputJax: new TeX({ packages: AllPackages }),
  OutputJax: new SVG({ fontCache: "none" }),
});

const jobs = JSON.parse(readFileSync(0, "utf8"));
let failed = 0;
for (const { tex, display, out } of jobs) {
  try {
    const node = doc.convert(tex, { display, em: 16, ex: 8, containerWidth: 1200 });
    const svg = adaptor.innerHTML(node);
    if (svg.includes("data-mjx-error") || svg.includes('fill="red"')) throw new Error("TeX error");
    const png = new Resvg(svg, {
      fitTo: { mode: "zoom", value: 2.5 },
      background: "white",
    }).render().asPng();
    writeFileSync(out, png);
  } catch (e) {
    failed++;
    console.error(`FAIL ${tex}: ${e.message}`);
  }
}
console.error(`rendered ${jobs.length - failed}/${jobs.length}`);
