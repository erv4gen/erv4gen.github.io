---
layout: post
title: "A Calibration Curve: A Statistical Look at Prediction Market Pricing Part 2"
date: 2026-10-28 00:00:00 +00:00
categories:
  - Finance
tags:
  - finance
  - statistics
published: false
author:
  login: Vladimir
  email: eremin.vladimir.d@gmail.com
  display_name: Vladimir
  first_name: ''
  last_name: ''
---

Part 1 of this post was an introduction to estimating the fair price of the hypothetical coin-flipping game. The example was quite abstract, and I feel I need to properly connect the coin game with financial markets.

## Noise, information and the fair price

From Part 1, we know that the fair price relates to the concept of *knowledge* about the game (or the market). If both parties share the same knowledge (e.g., playing the fair coin game), then nobody has an edge, i.e., the long-term expected value of the game is zero for both:

$$
E = \tfrac{1}{2}(+1) + \tfrac{1}{2}(-1) = 0.
$$

Nobody will play this game except out of boredom.

But as we illustrated in Part 1, the situation changes when the players' odds of winning are not known. If two players play a coin game where they have to guess or otherwise estimate the probability, their own estimate will move the expected value one way or another. They'll agree to bet against each other only if they *both* think they have a positive expectation. But this cannot be true — one of the players *must be wrong, i.e., they made their estimate based on noise.

Decisions based on noise are the reason financial markets exist and why they're actively traded. Unlike a simple coin-flip game, market prices carry both information and noise. If they carried only information, nobody would trade it — or they'd trade infrequently, only when new information arrives (a player with new information would trade with someone who lags the new knowledge). That, in fact, is one of the drivers of the momentum strategy.

![Information-only trading](/assets/hosea-part-2/fig1-information-only-tape.png)
*Information-only trading (illustrative).*

A reader familiar with market microstructure may recognize this chart: it looks like a tick-level tape print.

> "Noise creates the opportunity to trade profitably, but at the same time makes it difficult to trade profitably."
> — Fischer Black, *Noise* (1986)

Black tells us that noise is injected into the market not only by misestimation of the true value, but also by informed actors capturing the margin. Markets fundamentally consist of two players: **makers** (they post resting orders) and **takers** (they take orders from the book).

If a taker knows the true value of an asset and sees a maker's offer away from it, they'll immediately execute the trade, capturing the spread between the value (fair price) and the quoted price.

For a maker who knows the true value, the way to profit is to post an order at a spread from the true value and wait for an uninformed taker to take it. This is how informed actors introduce noise into the system. The same works for actors who think they estimated value off information when in fact it was noise.

This is why it's hard to differentiate a true mispricing of an asset from the artifacts of informed traders' actions. We'll demonstrate this in the study of prediction markets, where the effect is more visible.

This instantaneous noise makes market forecasts extremely hard over short intervals, but possible over longer time windows, when the noise cancels out. This is how the Royal Swedish Academy of Sciences summarized the work of Eugene Fama — the author of the efficient market hypothesis — and his co-laureates when awarding them the 2013 Nobel Prize in economics:

> "There is no way to predict the price of stocks and bonds over the next few days or weeks. But it is quite possible to foresee the broad course of these prices over longer periods, such as the next three to five years."

This gives us a working definition of noise:

> **Noise is the part of the price that the objective features of an asset cannot explain.**

For example, Fama and French (1988) found that "dividend yields typically explain less than 5% of the variances of monthly or quarterly returns," yet "often explain more than 25% of the variances of two- to four-year returns."

## Prediction markets have deadlines

Equity markets don't have deadlines, so there's a constant inflow of both information and noise into prices. Modern prediction markets are different — they have deadlines: they resolve and close on a given date under a given condition. This creates a setting where the information-to-noise proportion changes, and markets become less noisy as resolution approaches.

Prediction markets operate as probability-estimation machines for a given event. Kalshi Research (Kagan and Baiocchi, 2026) did a comprehensive study of more than 2.2 million resolved Kalshi markets and concluded that prices on prediction markets are, in fact, good estimators of event probability.

How can you decide whether the forecast you provide is, in fact, a probability estimate?

In 1950, Glenn Brier, a researcher at the U.S. Weather Bureau, proposed a way to score forecasts stated as probabilities (the Brier score is now the standard measure). It works like this: for each forecast stating a *p*% chance of rain *n* days ahead, take the history of all such forecasts, form a cohort, and measure how often it actually rained. If it rained about *p*% of the time, the forecast is **well-calibrated** and reliable to use.

Murphy and Winkler (1977) built a reliability diagram of weather forecasts: it plots forecast probability against observed frequency. I'll refer to this as a **calibration curve**, and it is the subject of this post. We'll construct a calibration curve from Polymarket trades and study how well it is calibrated — and the common pitfalls in measuring how well a market is calibrated.

The motivation for this post comes from two observations:

1. My own experience using calibration curves to construct portfolios on Polymarket that aim to capture statistical-arbitrage opportunities (miscalibrations).
2. Recent publications on this topic (Kalshi Research, Becker) that use calibration curves, constructed differently, to draw different conclusions.

To construct a calibration curve and measure its predictive power, we first need to understand two important things: the ways to construct the curve, and what exactly the Brier score tells us about our probability estimate.

## Two ways to build a curve

We'll start by examining the two main ways publicly reported curves were constructed: Becker (2026) and Kalshi Research.

You start by constructing pairs of observations $(x_i, y_i)$, where $y_i \in \{0, 1\}$ is a binary outcome. The calibration curve is an aggregate of these two vectors:

$$
C = f(X, Y).
$$

Becker used **all trades** as observation points (72.1 million Kalshi trades); Kalshi Research used **markets**, with the price at a given horizon (stratified by volume, market and horizon).

Because the price can take multiple forms — last trade, mid price, VWAP, average or close of the interval — the way you construct $x_i$ imposes different levels of noise on the estimate.

As mentioned earlier, when measuring price efficiency from the price tape alone, you also measure the spread the maker imposes on the price. Hence, any miscalibration found in the trade tape can be attributed to it. The Becker paper found exactly that.

In contrast, Kalshi Research reported that, measured by the Brier score, prediction markets become better calibrated the closer they get to resolution: the Brier score falls from roughly 0.08–0.09 at a three-month horizon to roughly 0.02 at close.

Even though this is likely true, the Brier score by itself is not enough to answer the question. The Brier score (as decomposed by Murphy, 1973) is *reliability − resolution + uncertainty*. It mixes calibration with how well the price separates winners from losers.

The topic of this post is to ask what a calibration curve can measure at all — what information we can extract from it, and whether Brier's framework is suitable for judging prediction markets in the first place.

## Probability needs a reference class

When we want to assess whether market prices are probabilities — whether they're calibrated — we must commit to the fact that a probability describes a **reference class**, because probability is only meaningful relative to a **population** of comparable events. And when we group markets (or, more specifically, events), we assume their independence and exchangeability.

For this reason, it's easy to see why the Brier score and the probabilistic framework suit weather forecasts but not an arbitrary composition of events. The trick is that prediction markets are neither one nor the other. Below is the composition of markets by volume and category.

<!-- FIGURE TODO: market composition by category vs. volume.
     Sketch: categories on the y-axis, cumulative volume on the x-axis;
     sports, crypto and weather dominate the top of the volume. -->

At the top of the volume sit markets that are naturally similar: weather, crypto, sports. These markets group well, so the probabilistic structure is suitable. But this doesn't apply to tailored, one-off markets that don't form a group.

This brings us to the main point of this post: **the Brier score is a noisy estimate for testing the efficiency of prediction markets.** The argument is as follows:

1. **Not all markets qualify for the probabilistic framework and the grouping assumption.** The parameters estimated from a group are highly sensitive to the group's composition. We call this the *estimand error* — the error term that comes from the model's composition. We argue that to assess the probabilistic nature of these tailored markets, a prior–posterior framework is better suited.
2. **The Brier score, by Murphy's decomposition, measures a blend** of market-specific separation versus group calibration and uncertainty noise.

The rest of the post covers the second part.

## Decomposing the Brier score

If the price $P_t$ is a fair forecast of the outcome $Y$, the law of total variance splits the uncertainty of the outcome into two parts:

$$
\operatorname{Var}(Y) = p_0(1 - p_0) = \operatorname{Var}(P_t) + \mathbb{E}\big[P_t(1 - P_t)\big]
$$

which is the familiar

$$
\operatorname{Var}(Y) = \underbrace{\operatorname{Var}\big(\mathbb{E}[Y \mid X]\big)}_{\text{between}} + \underbrace{\mathbb{E}\big[\operatorname{Var}(Y \mid X)\big]}_{\text{within}}
$$

or, over groups $k$ with weights $p_k$, means $\mu_k$ and variances $\sigma_k^2$:

$$
\operatorname{Var}(Y) = \underbrace{\sum_k p_k \sigma_k^2}_{\text{within}} + \underbrace{\sum_k p_k (\mu_k - \mu)^2}_{\text{between}}.
$$

The total uncertainty $\operatorname{Var}(Y) = p_0(1-p_0)$ cannot exceed $0.5^2 = 0.25$, reached at $p_0 = 0.5$. Assume the contract starts trading at 0.50, implying maximum uncertainty. We can write the price as the true probability plus noise:

$$
P_t = q_t + \eta_t .
$$

At settlement both sides equal the outcome, and hence the noise part disappears:

$$
P_{t^*} = q_{t^*}.
$$

We can also express the expected squared error (the expected Brier score) for a contract:

$$
\mathbb{E}\big[(P_t - Y)^2\big] = (P_t - q_t)^2 + q_t(1 - q_t).
$$

For a perfectly calibrated market, the $(P_t - q_t)^2$ part equals zero, leaving the expected Brier score equal to the irreducible noise term $q_t(1-q_t)$.

This implies that the fall in the Brier score is produced by the **time component that reduces the noise**, and the Brier score alone cannot tell us anything about the calibration of the market.

<!-- FIGURE TODO: Brier score vs. horizon (out to ~2 days), split into the
     noise (open uncertainty) component and the calibration part. -->

At every horizon, the calibration part is between 0.1% and 1%; nearly all the rest is the uncertainty still open.

There's another reason calibration (predictability) and undecidedness are hard to separate in price data: the information that decides a market doesn't always arrive gradually, reducing uncertainty along the way. Sometimes it arrives all at once and the price jumps, collapsing all uncertainty.

![Price jump on a decisive event](/assets/hosea-part-2/fig2-price-jump.png)
*A decisive event collapses uncertainty at once (illustrative).*

Such markets can be quite far from resolution, yet all the information has already arrived: the price no longer tracks a prediction, it tracks a fact — and the Brier score will falsely attribute this to calibration.

## Effective sample size

These are further challenges in assessing the calibration of prediction markets, beyond the natural noise in prices.

In our squared-error decomposition of the Brier score, we assume $P_t$ to be a bucket in which we can construct a cohort and estimate $\hat{q}_t$ as the average resolution frequency $\bar{y}_t$.

What's extremely common in prediction markets is that many markets have relatively few events behind them (weather, politics and crypto each resolve multiple markets at once). If $N$ markets share some average outcome correlation $\bar{\rho}$, the effective sample size for the cohort is

$$
N_{\text{eff}} = \frac{N}{1 + (N - 1)\bar{\rho}} \;\xrightarrow{N \to \infty}\; \frac{1}{\bar{\rho}},
$$

which can never exceed $1/\bar{\rho}$. Below is a chart similar to the one I reported in Part 1.

![Effective sample size](/assets/hosea-part-2/fig3-effective-sample-size.png)

In equity research, long-horizon return regressions use overlapping windows, so each two-year return shares most of its months with the next one. Boudoukh, Richardson and Whitelaw (2008) showed that, for regressors as persistent as dividend yields, the 1- and 2-year horizon estimators are 99% correlated under the null of no predictability, and that OLS coefficients and $R^2$ come out roughly proportional to the horizon under that same null. In other words, the horizon where the signal looks strongest is usually the one with the fewest independent events.

We can restate the calibration part of the score in terms of the Z-score distance from the calibration line. A significant deviation from the 1:1 line can then be classified as $|Z| > 2$, where

$$
Z = \frac{\hat{q}_t - P_t}{\sqrt{\sigma^2 / N}} .
$$

If we used the number of *markets* in this estimate instead of the number of *events*, we'd come up with an inflated Z-score and falsely classify the cell's deviation as miscalibration.

We can demonstrate that the curve constructed from markets performs worse at predicting the outcomes of individual markets by comparing its Brier score with the individual markets' Brier scores.

<!-- FIGURE TODO: box plots of (curve Brier − price Brier), ×10⁻⁴,
     for "curve, holdout" vs. "control, synthetic". -->

Another important factor is that not all markets on prediction markets share similar probabilistic structures. The Brier score and probability calibration were designed for events that are i.i.d. by nature. Weather forecasts follow this, as do short-term directional bets on crypto markets. But political and economic markets are cross-dependent, share information and time intervals, and don't form cohorts naturally — which means the calibration estimator is not only extremely noisy but also depends heavily on the cohort's composition.

## How to construct a robust curve

Now we arrive at the main question of this post: given all the nuances described above, what is a robust way of constructing a calibration curve?

1. **Construct cohorts of independent events.** Markets in a cohort shouldn't share underlying events.
2. **Include only markets where the deciding information has not yet arrived** — not all open markets.

This way we're measuring the *prediction*, not materialized information.

Following the very formula I described in Part 1, the number of markets the cohort needs to detect an edge $\mu$ at 95% confidence is

$$
N > \left[\frac{1.96\,\sigma}{\mu}\right]^2, \qquad \sigma = \sqrt{p(1-p)} .
$$

![Markets required to detect an edge](/assets/hosea-part-2/fig4-required-markets.png)

This chart tells a clear story: even if the gap between the cohort's frequency and the price is discovered with statistical robustness, it can be extremely challenging to capture it in a real market setting. It requires constructing enormous portfolios of thousands of markets — usually beyond the correlation ceiling — which makes capturing small spreads extremely difficult.

## References

- Black, F. (1986). Noise. *The Journal of Finance*, 41(3), 529–543.
- Boudoukh, J., Richardson, M., & Whitelaw, R. (2008). The Myth of Long-Horizon Predictability. *Review of Financial Studies*, 21(4).
- Brier, G. W. (1950). Verification of Forecasts Expressed in Terms of Probability. *Monthly Weather Review*, 78(1).
- Fama, E. F., & French, K. R. (1988). Dividend Yields and Expected Stock Returns. *Journal of Financial Economics*, 22(1).
- Murphy, A. H. (1973). A New Vector Partition of the Probability Score. *Journal of Applied Meteorology*, 12(4).
- Murphy, A. H., & Winkler, R. L. (1977). Reliability of Subjective Probability Forecasts of Precipitation and Temperature. *Journal of the Royal Statistical Society, Series C*, 26(1).
- Becker, J. (2026). The Microstructure of Wealth Transfer in Prediction Markets. Blog post.
- Kagan, N., & Baiocchi, R. (2026). Calibration in Prediction Markets: Theory and Evidence. Kalshi Research working paper. <https://kalshi.com/research/publications/calibration>
- Royal Swedish Academy of Sciences (2013). The Prize in Economic Sciences 2013 — press release. <https://www.nobelprize.org/prizes/economic-sciences/2013/press-release/>
