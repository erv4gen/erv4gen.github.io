---
layout: "post"
title: "Volatility Estimation Using MCMC"
date: "2019-05-22 04:15:55 +0000"
author: "Vladimir"
wordpress_id: "288"
status: "publish"
categories:
  - "data-science"
  - "finance"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<!-- wp:html -->
[mathjax]
<!-- /wp:html -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Problem</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In the financial world, it is often can be found examples of the application of the modeling price return distribution with an assumption of its normality. Applying the normal distribution in the price simulation makes the model relatively simple and computational chip. It also a very convenient solution when an analyst doesn't have any additional information about the underlying financial asset. Such assumptions can lead to the underestimation of the "long tail" type evens, such as market shocks/recessions and so fore.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This research is exploring how to estimate a price distribution from the historical data and use it in the "Mont Carlo" price simulations.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Plan</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Acquire at least a last ten years of historical market data for major public trading companies.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Using a stock performance, generate an empirical distribution for each financial asset</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Fit different probability density functions and estimate the likelihood for each of them</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Create a Markov Chain Monte Carlo hierarchical model for volatility simulations.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Use samples from the stimulation to estimate the cumulative distribution function for price volatility.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Intro</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Volatility can be identified as a difference between the minimum and maximum price in the defined period. If the initial stock price and monthly volatility are known, a risk of the high volatility can be estimated. In another world, the probability that stock's price at the end of the month will be lower than at the beginning.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<p>
$$ \text{Risk}=\mathbb{E}(\text{price}_a < \text{price}_b)$$
</p>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Where $latex \text{price}_a$ is simulated current/ending price of the period, and $latex \text{price}_b$ is a starting price of the period.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then we can set up the "<em>risk thresholds</em>" that could be identified as: "If an asset has more than $latex n%$ risk of negative return, we should consider it as non-inestimable" or "If an asset has more than $latex n%$ risk of negative return we won't open a short option position on it"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>"Simulated" price means a theoretical price drown from the approximate distribution of the asset volatility. If the distribution is known (or at least the most appropriate one) we can use Monte Carlo simulations to "look to the future" and estimate where price could be after n-periods of time.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Data Source</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The data source I used for this research Yahoo Finance, an open online database for economic and financial data. Historical quotes were loaded directly using R API without any changes and preprocessing.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Model</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To calculate monthly volatility, I got historic market data from yahoo finance, aggregated it by month and estimated relative volatility with:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<p>
$$ 
\text{Vol} = \frac{\max(\text{price}) - \min(\text{price})}{\min(\text{price})}
$$
</p>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>It's important to mention that this formula is allowed only for intraday behavior. Applied to monthly/yearly aggregated data it won't represent the risk of investment because it doesn't consider hidden action of the asset.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To estimate stock's monthly volatility, we need to find it's mean daily volatility, calculate the variance for each day observation and then sum it over.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Assuming that each volatility observation is independent, the monthly volatility can be expressed from daily volatility using the following expression:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<p>
$$ \widehat{\mathrm{Var}}(x_{t+1} + \ldots + x_{t+K}) = \widehat{\mathrm{Var}}(x_{t+1}) + \ldots + \widehat{\mathrm{Var}}(x_{t+K}).$$
</p>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Here's a density plot of the monthly stock volatility and fitted normal distribution function:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":307,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-full"><img src="/media/2023/11/image-12.png" alt="" class="wp-image-307"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As we see, the most decency mass is concentrated in 0%-4% range. We also recognize that there was a couple of month with extremely high volatility when stock returned around 6% ROI.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's also clear that the Normal distribution cannot be used for volatility approximation. The normal distribution underestimates the probability of medium and high volatility. We need to consider using more "fat tail" like a model.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, let us try to fit different probability density functions and see which one will work the best. To find it out we need to find parsimonious approximate descriptions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's a plot of the kurtosis and squared skewness of our samples:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":308,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-full"><img src="/media/2023/11/image-13.png" alt="" class="wp-image-308"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>It gives some basic estimations about potential candidates for theoretical distribution.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We see that the closest estimation will be a lognormal distribution.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The AIC statistics for Weibull, normal, gamma and log-normal are the following:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>&gt;aic_df

   weibull    gamma     norm    lnorm

1 550.6034 525.3154 609.4202 520.4791</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>As we see, both gamma and log-normal distribution have fit the data well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I'll test both gamma and lnorm models separately and see which gives a better return on the backtesting stage. Let's start with a gamma distribution. Because it has higher kurtosis, it better represents the underlying asset behavior.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Solving Maximum Likelihood estimation for the Gamma distribution, we can get the best fitted (Shape, Rate) parameters:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>> fit_stat&#91;&#91;1]]$gamma$estimate
   shape     rate
3.848280 2.952326</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Then, using these parameters, we can create a simple hierarchical Bayesian model for sampling monthly stock volatility. To create the MCMC model, we'll use JAGS, and it's R API. The string representation of the model looks following:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Using these parameters we drown random vector form Gamma (shape, rate) using founded parameters. After that, we can calculate the Kolmogorov-Smirnov test to identify what is the probability that simulated and observed data points are from the same Gamma distribution.The Kolmogorov–Smirnov statistic is 0.041. Hence, for the significance level 0.01 level, the<em> p-value</em> is 0.072, we can strongly assume that the observed samples are drowned from a Gamma distribution.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We can now use the obtained distribution as a prior distribution for a Bayesian model for volatility simulation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For simulations, we'll use JAGS, and it's R API. Here's a model's string for rjags:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>"model {
  #Likelihood
  for(i in 1:n) {
    y&#91;i] ~ dgamma(alpha,beta)
  }
  #Prior
  alpha ~ dnorm(a_mu,1.0/sig_sq)
  beta ~ dnorm(b_mu, 1.0/sig_sq)
  "</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Datapoints are draws from Gamma distribution with alpha and beta parameters. Alpha and beta for their part are drowned from a normal distribution with $latex \mu$ and $latex \frac{1}{\sigma^2}$ square parameters. Mu parameter is set up as an MLE from the KS test, while $latex \sigma^2$ is remaining free.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The simulations were run in three chains with <em>1e5</em> iterations each. The burn-in period was set up to <em>1e3</em> iterations.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's a trace plot for the simulations:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The trace plot for the model looks the following:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":309,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/media/2023/11/image-14-1024x526.png" alt="" class="wp-image-309"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Autocorrelation levels and Gelman-Rubin diagnostic looks good:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>>autocorr.diag(mod_sim)
               alpha         beta
Lag 0   1.0000000000 1.0000000000
Lag 1   0.0020603758 0.0017301907
Lag 5   0.0003452382 0.0004947912
Lag 10  0.0007025614 0.0007559833
Lag 50 -0.0005045586 0.0023457908
>gelman.diag(mod_sim)
Potential scale reduction factors:

      Point est. Upper C.I.
alpha          1          1
beta           1          1

Multivariate psrf

1</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>We can reasonably assume that the chain converted and exploring stationary distribution.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, let's tweak the model to find the best fit for the real-life patterns. Using the free sigma parameter, we can control the maximum "allowed" size of outliers in volatility and probability of high volatility periods.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's a result of ten simulations with gradually decreasing sigma from 80 to 0.07:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>&gt;results
       Sigma Mean.Volatility Max.Volatility High.Volatility.Probability
1  3.200000e+02      0.01474138     0.09212599                 0.004666667
2  1.600000e+02      0.01548248     0.10307916                 0.011666667
3  8.000000e+01      0.01668404     0.11868926                 0.021166667
4  4.000000e+01      0.01837978     0.14249831                 0.046666667
5  2.000000e+01      0.02086177     0.21776297                 0.086000000
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And the summary from observed data:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>
> mean(empirical_distribution> 3*mean(empirical_distribution))
&#91;1] 0.003521127
> summary(empirical_distribution)
    Min.  1st Qu.   Median     Mean  3rd Qu.     Max.
0.002717 0.008045 0.011309 0.013035 0.016699 0.056315</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>High.Volatility.Probability column is defined as a probability that monthly volatility will be more than three times higher than average.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We see that the best fit to empirical data will be a model with a sigma parameter equal to 40.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The boxplot for the result distribution is the following:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":310,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-15.png" alt="" class="wp-image-310"/></figure>
<!-- /wp:image -->

<!-- wp:code -->
<pre class="wp-block-code"><code>>mean(y_hat)
&#91;1] 0.06417608</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>We see that most of the distribution mass lay around 6% with high volatility outliers. Indeed, the AAPL stock price had 20% volatility in late 2018 after more than ten years of stable growth.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Conclusion</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As it was shown, JAGS simulations yield a realistic distribution which accounts low-probability "tails" events. Estimated values generated by JAGS can be used to define the probability for the different price levels and use them to evaluate the risk of the specific finance asset.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">References</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Hardy, R. (2016, 08 25). <em>How to convert daily volatility to monthly?</em> Retrieved from stats.stackexchange.com: <a href="https://stats.stackexchange.com/q/231713">https://stats.stackexchange.com/q/231713</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Heiner, M. (n.d.). <em>Bayesian Statistics: Techniques and Models.</em> Retrieved from Coursera.org: <a href="https://www.coursera.org/learn/mcmc-bayesian-statistics">https://www.coursera.org/learn/mcmc-bayesian-statistics</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Ricci, V. (2005, 02). <em>FITTING DISTRIBUTIONS WITH R.</em> Retrieved from <a href="https://cran.r-project.org/doc/contrib/Ricci-distributions-en.pdf">https://cran.r-project.org/doc/contrib/Ricci-distributions-en.pdf</a></p>
<!-- /wp:paragraph -->