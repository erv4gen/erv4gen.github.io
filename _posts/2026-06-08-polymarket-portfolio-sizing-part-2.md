---
layout: post
title: "Polymarket Portfolio Sizing, Part 2: Estimation Uncertainty, Correlation, and Kelly"
date: 2026-06-08 12:00:00 +00:00
categories:
  - Finance
tags:
  - polymarket
  - quantitative-finance
  - portfolio-construction
published: true
---

## 4. Incorporating Estimation Uncertainty

The misprice $μ$ is itself an estimate from the calibration curve. The bootstrap gives us a confidence interval, from which we recover the standard error of the estimate:

$$SE_\mu \approx \frac{\text{misprice\_ci\_high} - \text{misprice\_ci\_low}}{2 \times 1.96}$$

Two independent sources of uncertainty:

| Source      | Variance | What it captures                 |
| ----------- | -------- | -------------------------------- |
| Estimation  | SE_μ²    | Uncertainty in the true misprice |
| Realization | σ²/N     | Finite portfolio sampling noise  |

Since they're independent, total variance adds:
$$\text{Var}_{\text{total}} = SE_\mu^2 + \frac{\sigma^2}{N}$$

**Combined profitability condition:**

$$\hat{\mu} - z_\alpha \cdot \sqrt{SE_\mu^2 + \frac{\sigma^2}{N}} > 0$$

Solving for $N$:

$$\boxed{N > \frac{\sigma^2}{\hat{\mu}^2 / z_\alpha^2 - SE_\mu^2}}$$


The formula only has a solution when the denominator is positive:

$$\frac{\hat{\mu}^2}{z_\alpha^2} > SE_\mu^2 \implies \frac{\hat{\mu}}{SE_\mu} > z_\alpha$$

This is exactly the z-test for statistical significance of the misprice. **If the bootstrap CI for misprice crosses zero, no portfolio size can guarantee profitability.** You cannot diversify away estimation error.

This is what `significant_after_fdr` captures in the calibration output — it's a necessary condition before portfolio sizing even applies.

---

## 7. Practical Considerations

### 7.1 Effective Sample Size Under Correlation

The portfolio sizing formulas assume independent bets. When markets are correlated (same event cluster, related outcomes), the effective sample size shrinks.

Given N bets with pairwise correlation matrix **Σ** (estimated from the price correlation pipeline), the portfolio variance of equal-weighted average profit is:

$$\text{Var}(\bar{X}) = \frac{1}{N^2} \mathbf{1}^T \mathbf{\Sigma}_{\text{profit}} \mathbf{1}$$

where **Σ_profit** is the N×N covariance matrix of bet profits, with entries:

$$\Sigma_{ij} = \text{Cov}(X_i, X_j) = \rho_{ij} \cdot \sigma_i \cdot \sigma_j$$

Here ρ_ij comes from the price correlation matrix and σ_i = √(p_i(1 - p_i)).

For independent bets this reduces to σ²/N. With correlation, it's larger. Define the **effective sample size** as the number of independent bets that would give the same portfolio variance:

$$N_{\text{eff}} = \frac{N \cdot \bar{\sigma}^2}{\frac{1}{N} \mathbf{1}^T \mathbf{\Sigma}_{\text{profit}} \mathbf{1}}$$

where σ̄² is the average single-bet variance.

**Simplified approximation** when all bets have similar σ and average pairwise correlation ρ̄:

$$\text{Var}(\bar{X}) = \frac{\sigma^2}{N}\left[1 + (N-1)\bar{\rho}\right]$$

$$\boxed{N_{\text{eff}} = \frac{N}{1 + (N-1)\bar{\rho}}}$$

| N   | ρ̄   | N_eff | Interpretation                                   |
| --- | ---- | ----- | ------------------------------------------------ |
| 100 | 0.00 | 100   | Independent — full diversification               |
| 100 | 0.05 | 17    | Mild correlation — 83% diversification loss      |
| 100 | 0.20 | 5     | Moderate correlation — nearly 5 independent bets |
| 100 | 0.50 | 2     | High correlation — effectively 2 bets            |

**Takeaway**: Use the similarity/correlation graph to select markets with low average pairwise correlation. Replace N with N_eff in all portfolio sizing formulas.

### 7.2 Kelly Criterion with Portfolio Weight Constraint

The single-bet Kelly fraction for the YES side is:

$$f_i^* = \frac{p_i - K_i}{1 - K_i}$$

For the NO side:

$$f_i^* = \frac{K_i - p_i}{K_i}$$

These are the fractions of total bankroll to allocate to each bet. They naturally sum to whatever they sum to — there's no guarantee Σf_i = 1. In practice we need weights that sum to 1 (fully invested, no leverage).

**Normalized Kelly**: Scale all fractions proportionally:

$$w_i = \frac{f_i^*}{\sum_{j=1}^{N} f_j^*}$$

This preserves the relative allocation (higher-conviction mispricings get more weight) while ensuring Σw_i = 1.

**Fractional Kelly**: In practice, full Kelly is too aggressive (optimizes geometric growth but has high drawdowns). Use a Kelly fraction λ ∈ (0, 1):

$$w_i = \lambda \cdot \frac{f_i^*}{\sum_{j=1}^{N} f_j^*}$$

The remaining (1 - λ) stays in cash. Common choice: λ = 0.5 (half-Kelly) — captures 75% of the growth rate with substantially lower variance.

**With correlation**: The multivariate Kelly solution accounts for covariance:

$$\mathbf{f}^* = \mathbf{\Sigma}^{-1} \boldsymbol{\mu}$$

where **μ** is the vector of expected profits and **Σ** is the profit covariance matrix. This automatically reduces allocation to correlated positions. Normalize as above if a weight constraint is needed.

### 7.3 Same-Vintage Cross-Section Portfolio

We construct portfolios from a single calibration vintage (as_of_date), selecting markets that all resolve within the same time window. This simplifies the framework:

**Advantages:**
- **Single resolution event**: All bets resolve simultaneously, so realized portfolio return = Σw_i X_i with no path dependency
- **Clean P&L attribution**: One entry point, one exit — no rolling or rebalancing needed
- **Direct calibration match**: The misprice estimate comes from the same horizon bucket (e.g., all 7-day markets), so p is estimated from a homogeneous cohort
- **Horizon-matched correlation**: The price correlation matrix from the same trailing window is directly applicable — no need to adjust for different time-to-resolution

**Portfolio construction for a single vintage:**

1. Fix (category, horizon_days) from the calibration curve
2. Select all active markets in the corresponding price bucket with significant misprice
3. Compute pairwise correlations from trailing OHLCV bars
4. Compute N_eff from the correlation structure (Section 7.1)
5. Check N_eff satisfies the minimum portfolio size from Section 4
6. Allocate weights via normalized Kelly (Section 7.2)
7. All positions enter simultaneously and resolve together

**Portfolio variance for a single vintage:**

$$\text{Var}(\text{portfolio profit}) = \mathbf{w}^T \mathbf{\Sigma}_{\text{profit}} \mathbf{w}$$

**Combined profitability condition** (incorporating estimation uncertainty, correlation, and Kelly weights):

$$\mathbf{w}^T \boldsymbol{\mu} - z_\alpha \cdot \sqrt{SE_\mu^2 + \mathbf{w}^T \mathbf{\Sigma}_{\text{profit}} \mathbf{w}} > 0$$

where **w**ᵀ**μ** is the portfolio's expected profit and the square root term combines estimation uncertainty with the correlated realization uncertainty.



## 6. Worked Example

A calibration bucket with:
- μ̂ = 0.04 (4% misprice)
- misprice_ci = [0.019, 0.061]
- Region: longshots (σ = 0.26)
- Confidence: 95% (z = 1.96)

**Step 1**: Recover estimation SE

$$SE_\mu = \frac{0.061 - 0.019}{2 \times 1.96} = \frac{0.042}{3.92} \approx 0.0107$$

**Step 2**: Check significance

$$\frac{\hat{\mu}}{SE_\mu} = \frac{0.04}{0.0107} = 3.74 > 1.96 \checkmark$$

**Step 3**: Compute minimum N

$$N > \frac{0.26^2}{0.04^2 / 1.96^2 - 0.0107^2} = \frac{0.0676}{0.000416 - 0.000115} = \frac{0.0676}{0.000301} \approx 225$$

**Comparison:**

| Model | N_min | Notes |
|-------|-------|-------|
| Realization only | 163 | Assumes μ is known exactly |
| With estimation uncertainty | 225 | +38% more bets needed |

---
