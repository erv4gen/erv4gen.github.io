---
layout: "post"
title: "Optimizing Risks for a Portfolio of Cryptocurrencies"
date: "2021-08-18 17:07:07 +0000"
author: "Vladimir"
wordpress_id: "84"
status: "publish"
categories:
  - "crypto"
  - "data-science"
  - "finance"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<span style="background-color: var(--wp--preset--color--background); color: var(--wp--preset--color--foreground); font-family: var(--wp--preset--font-family--system-font); font-size: var(--wp--preset--font-size--medium);">Created together with </span><a class="markup--anchor markup--p-anchor" style="background-color: var(--wp--preset--color--background); font-family: var(--wp--preset--font-family--system-font); font-size: var(--wp--preset--font-size--medium);" href="https://medium.com/@korotkov.maxim" target="_blank" rel="noopener" data-href="https://medium.com/@korotkov.maxim">Maxim Korotkov</a><span style="background-color: var(--wp--preset--color--background); color: var(--wp--preset--color--foreground); font-family: var(--wp--preset--font-family--system-font); font-size: var(--wp--preset--font-size--medium);"> and</span><a class="markup--anchor markup--p-anchor" style="background-color: var(--wp--preset--color--background); font-family: var(--wp--preset--font-family--system-font); font-size: var(--wp--preset--font-size--medium);" href="https://medium.com/@dmytro.karabash" target="_blank" rel="noopener" data-href="https://medium.com/@dmytro.karabash"> Dmytro Karabash</a>

<article class="h-entry">
<section class="e-content" data-field="body">
<section class="section section--body section--first section--last">
<div class="section-content">
<div class="section-inner sectionLayout--insetColumn">
<p id="100a" class="graf graf--p graf-after--h4">Image credit <a class="markup--anchor markup--figure-anchor" href="https://pixabay.com/fr/users/geralt-9301/" target="_blank" rel="noopener" data-href="https://pixabay.com/fr/users/geralt-9301/">geralt </a>at pixabay</p>
<p id="4811" class="graf graf--p graf-after--figure">In this post we will talk about optimizing a simple portfolio of cryptocurrency. The approaches below have been successfully applied to stock options trading and, as we see, work quite well for crypto. Also, crypto is great to learn and try modern trading strategies as you can get required historical currency data for free (we will show how below). In this post we do a simple portfolio composition and apply CVXPY optimization to introduce library and methods and we will go into more complex Stochastic Discount Factor based strategies in the next post.</p>
<p id="b5ea" class="graf graf--p graf-after--p">You are welcome to open our <a class="markup--anchor markup--p-anchor" href="https://yourdatablog.com/cryptopt/" target="_blank" rel="noopener" data-href="https://yourdatablog.com/cryptopt/">notebook </a>on colab and see full working code, here we hide some technical parts.</p>

<h3 id="d6e8" class="graf graf--h3 graf-after--p">Data Acquisition</h3>
<p id="4878" class="graf graf--p graf-after--h3">The data for this exercise was obtained from the Binance API using the Python API client <code class="markup--code markup--p-code">python-binance</code>. While obtaining similar data for stock market would have been quite a task on its own (unless you work for a trading firm), in crypto worlds it is done easily.</p>
<p id="a2ee" class="graf graf--p graf-after--p">An example of the data acquisition code:</p>

<blockquote id="2eb2" class="graf graf--blockquote graf-after--p"><strong class="markup--strong markup--blockquote-strong"><em class="markup--em markup--blockquote-em">Note: </em></strong><em class="markup--em markup--blockquote-em">Install the module if needed using pip (</em>pip install python-binance)</blockquote>
<pre id="cd0e" class="graf graf--pre graf-after--blockquote">from binance.client import Client
binance_api_key = 'YOUR-API-KEY'
binance_api_secret = 'YOUR-API-SECRET'
binance_client = Client(api_key=binance_api_key
                ,api_secret=binance_api_secret)
klines = binance_client.get_historical_klines(symbol
                 ,kline_size, date_from, date_to)
data = pd.DataFrame(klines, columns = [COLUMNS])</pre>
<p id="028e" class="graf graf--p graf-after--pre">Following daily pairs was downloaded and formatted to pd DataFrame:</p>

<ol class="postList">
 	<li id="88ef" class="graf graf--li graf-after--p">BTCUSDT</li>
 	<li id="e14d" class="graf graf--li graf-after--li">ETHUSDT</li>
 	<li id="6b34" class="graf graf--li graf-after--li">BNBUSDT</li>
 	<li id="d808" class="graf graf--li graf-after--li">LTCUSDT</li>
</ol>
<p id="c1d9" class="graf graf--p graf-after--li">For each timepoint, Binance provides conventional OHLC (Open, High, Low, Close) and Volume data. In this exercise, we used only the <code class="markup--code markup--p-code">Close</code> column. One might consider the combination of all five values and come up with a different (and potentially more reliable) metric, for example: the weighted average price. We will limit to the basic one for the sake of simplicity</p>
<p id="4213" class="graf graf--p graf-after--p">The data is loaded and transformed:</p>

<pre id="a62d" class="graf graf--pre graf-after--p">fuldf = (pd.read_csv('https://raw.githubusercontent.com/h17/fastreport/master/data/cryptosdf/data.csv',parse_dates=['timestamp'])
        .set_index('timestamp')
        )
y_label = fuldf.columns[0]
factors = (fuldf
           .columns
            .tolist()
          )

total_size = fuldf.shape[0]

train_set = .8

train_id = int( total_size * train_set)
df_train = fuldf.iloc[:train_id]
df_test = fuldf.iloc[train_id:]
split_index = fuldf.iloc[train_id].name</pre>
<p id="e488" class="graf graf--p graf-after--pre">The joint time-series of four crypto assets looks the following:</p>

<pre id="665f" class="graf graf--pre graf-after--p">df_train.head()</pre>
<figure id="3b11" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*SQow2AfSCF8eLAFyQS4ZWA.png" data-image-id="1*SQow2AfSCF8eLAFyQS4ZWA.png" data-width="612" data-height="404" />
<figcaption class="imageCaption">input dataframe</figcaption></figure>
<p id="f781" class="graf graf--p graf-after--figure">Each trading pair has a different amount of data available: The oldest tradable crypto instruments on Binance are BTCUSDT and ETHUSDT — data points are available from <em class="markup--em markup--p-em">2017–08–17</em>. For BNBUSDT and LTCUSDT first trading days are <em class="markup--em markup--p-em">2017–11–06</em> and <em class="markup--em markup--p-em">2017–12–13</em>, respectively.</p>
<p id="6f1e" class="graf graf--p graf-after--p">We joined these time series together on the earliest common trading date: <em class="markup--em markup--p-em">2017–12–13</em> up to <em class="markup--em markup--p-em">2021–06–14</em>. The full joint dataset size is equal to 1280 samples. In order to properly train the model, We split the dataset into training and testing sets at <em class="markup--em markup--p-em">2020–10–02</em>.</p>
<p id="24ea" class="graf graf--p graf-after--p">Training interval: <em class="markup--em markup--p-em">2017–12–13</em> to <em class="markup--em markup--p-em">2020–10–02</em> (1024 data points).</p>
<p id="88c4" class="graf graf--p graf-after--p">Below is the joint plot of the full dataset in the logarithmic scale. The dotted line represents the train-test split at <em class="markup--em markup--p-em">2020–10–02</em></p>

<pre id="2fdc" class="graf graf--pre graf-after--p">plot_data =np.log(fuldf)
fig , ax = plt.subplots(figsize=(12,7))
plot_data.plot(ax=ax,alpha=0.8)
ax.legend(loc=0)
ax.set(title='Assets',xlabel='Date',ylabel='price, log scale');

ax.axvline(split_index,color='grey', linestyle='--', lw=2);</pre>
<figure id="bf61" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*_snNed3u9ZOyMqH-oOy5JA.png" data-image-id="1*_snNed3u9ZOyMqH-oOy5JA.png" data-width="1034" data-height="639" />
<figcaption class="imageCaption">log prices of crypto assets</figcaption></figure>
<pre id="a84c" class="graf graf--pre graf-after--figure">#Transform raw data to log-return format:
lret_data = np.log1p(df_train.pct_change()).dropna(axis=0,how='any')</pre>
<h3 id="f34b" class="graf graf--h3 graf-after--pre">Data Transformation</h3>
<p id="1196" class="graf graf--p graf-after--h3">In order to be properly trained, input time series has to be transfored into the log-return format:</p>

<figure id="1b10" class="graf graf--figure graf-after--p"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*rJ2JzET0bNlqdAKRErhq_g.png" data-image-id="1*rJ2JzET0bNlqdAKRErhq_g.png" data-width="179" data-height="67" /></figure>
<p id="ee37" class="graf graf--p graf-after--figure">Where <em class="markup--em markup--p-em">P_t​ </em>is a price of the asset at time <em class="markup--em markup--p-em">t</em>. The model needs vector <em class="markup--em markup--p-em">I</em> to perform the optimization:</p>

<figure id="f1cd" class="graf graf--figure graf-after--p"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*sKGazCeB0YJmE8SX7sHvyw.png" data-image-id="1*sKGazCeB0YJmE8SX7sHvyw.png" data-width="401" data-height="164" /></figure>
<p id="9d91" class="graf graf--p graf-after--figure">Where <em class="markup--em markup--p-em">l</em> is the number of features in the model.</p>

<pre id="840b" class="graf graf--pre graf-after--p">I = (lret_data[factors].iloc[1:].values)

print(I.shape,'\n',I[:10,:])</pre>
<figure id="5998" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*wOMjufDbPqeEguTyJK0uSg.png" data-image-id="1*wOMjufDbPqeEguTyJK0uSg.png" data-width="1010" data-height="319" /></figure>
<pre id="1fd7" class="graf graf--pre graf-after--figure">F = pd.DataFrame(I)
F.columns = factors#+ [y_label]
F.cov()</pre>
<figure id="1618" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*uKON9uKXTuWyjYzeTHjMOw.png" data-image-id="1*uKON9uKXTuWyjYzeTHjMOw.png" data-width="586" data-height="290" />
<figcaption class="imageCaption">covariance matrix</figcaption></figure>
<pre id="cbce" class="graf graf--pre graf-after--figure">f = plt.figure(figsize=(10, 10))
cov_data = F.cov()
mask = np.triu(np.ones_like(cov_data))
dataplot = sb.heatmap(cov_data.corr(), cmap="YlGnBu", annot=True, mask=mask)
plt.title('Covariance Matrix', fontsize=16);</pre>
<figure id="3d8f" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*Ja8u1xZ-9nzscsESLhUCDg.png" data-image-id="1*Ja8u1xZ-9nzscsESLhUCDg.png" data-width="863" data-height="872" />
<figcaption class="imageCaption">covariance matrix plot</figcaption></figure>
<h3 id="efda" class="graf graf--h3 graf-after--figure">Model</h3>
<p id="1514" class="graf graf--p graf-after--h3">Our goal is to explain the differences in the cross-section of returns <em class="markup--em markup--p-em">R </em>for individual stocks.</p>
<p id="b193" class="graf graf--p graf-after--p">Let <em class="markup--em markup--p-em">I</em> denote the return of crypto assets at time <em class="markup--em markup--p-em">t</em>. We try to obtain weights <em class="markup--em markup--p-em">w</em> that minimize risk given fixed return. The portfolio return <em class="markup--em markup--p-em">R</em> can be expressed as follows:</p>

<figure id="3cff" class="graf graf--figure graf-after--p"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*P_uJ-eP5DFCKd6IGoHrjUA.png" data-image-id="1*P_uJ-eP5DFCKd6IGoHrjUA.png" data-width="131" data-height="39" /></figure>
<p id="ae7c" class="graf graf--p graf-after--figure">For this model portfolio, we target a 100% return, which is quite expected in the crypto world. We will only model investments held for one period.
The problem can be expressed as:</p>

<figure id="ac09" class="graf graf--figure graf-after--p"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*HTfVxkNryw1g5HnnyUZ09Q.png" data-image-id="1*HTfVxkNryw1g5HnnyUZ09Q.png" data-width="308" data-height="79" /></figure>
<p id="b435" class="graf graf--p graf-after--figure">Since the above problem is convex, we can estimate the <em class="markup--em markup--p-em">w</em> for the model portfolio using the <code class="markup--code markup--p-code">cvxpy</code> framework.</p>

<blockquote id="2dcc" class="graf graf--blockquote graf-after--p"><strong class="markup--strong markup--blockquote-strong">Note: </strong>in reality, you want to get maximum return given fixed risk, but due to the way CVXPY and semi-linear programming is setup, this formulation does not follow Disciplined Convex Programming rules (see <a class="markup--anchor markup--blockquote-anchor" href="https://dcp.stanford.edu/" target="_blank" rel="noopener" data-href="https://dcp.stanford.edu/">https://dcp.stanford.edu/</a>), so we use the former formulation as it is equivalent. Also, you might need fix return and low risk models depending on type of business your are in and your risk appetite.</blockquote>
<pre id="eb0d" class="graf graf--pre graf-after--blockquote">#define weights
w = cp.Variable(shape=(I.shape[1]
                        ,1),nonneg=True)

#Define expression
R = I @ w

#Construct the problem
prob = cp.Problem(cp.Minimize( cp.norm(R) )
                 , [ cp.sum(R) == 1 
                    ,cp.sum(w) == 1
                    ]
                  
                )
prob.solve(verbose=True)

print('weights for the model:\n',dict(zip(factors,w.value)))</pre>
<p id="c1e4" class="graf graf--p graf-after--pre">CVXPY output for the optimization run:</p>

<figure id="ea79" class="graf graf--figure graf-after--p"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*VYQQsIhoLq97EZi_2iJaYA.png" data-image-id="1*VYQQsIhoLq97EZi_2iJaYA.png" data-width="922" data-height="407" /></figure>
<h3 id="54d7" class="graf graf--h3 graf-after--figure">Results</h3>
<p id="ba9b" class="graf graf--p graf-after--h3">Let’s define utility functions to analyze our model portfolio:</p>

<pre id="0da0" class="graf graf--pre graf-after--p">def sharpe(x):
  return (x.mean() / x.std() * np.sqrt(365))

def calc_metrics(data):
  p_return = ((data[factors].pct_change().fillna(0))
              .apply(lambda x: (x @ w.value)[0] ,axis =1)
              .rename('Model Portfolio')
              )
  returns = data.pct_change().fillna(0)
  returns['Model Portfolio'] = p_return
  sharpes = returns.apply(np.log1p).apply(sharpe)
  pnls = (returns.apply(np.log1p).sum().apply(np.expm1)).apply(lambda x:f'{100*x:4.2f}%')
  result = pd.concat([sharpes,pnls],axis=1)
  result.columns='sharpes pnls'.split()
  return result

def plot_return(data,title):
  datac = data.copy()
  fig , ax = plt.subplots(figsize=(13,5))

  y_return = (datac[factors].pct_change().fillna(0)+1)
  
  p_return = ((datac[factors].pct_change().fillna(0) + 1)
              .apply(lambda x: (x @ w.value)[0] ,axis =1)
              .rename('Model Portfolio')
              )
  
  p_return_c = p_return.cumprod()
  y_return_c = y_return.cumprod()
  portfolio_benchmark = pd.concat([y_return_c,p_return_c],axis=1)

  #change to the log scale 
  portfolio_benchmark = np.log1p(portfolio_benchmark)
  portfolio_benchmark[factors].plot(ax=ax,alpha=.5)
  portfolio_benchmark['Model Portfolio'].plot(ax=ax,alpha=.7,color='black')
  ax.legend(loc=0)
  ax.set(title=title,ylabel='growth factor',xlabel='date')
  
  return portfolio_benchmark</pre>
<p id="2d6d" class="graf graf--p graf-after--pre">Below is the result of computing the Model Portfolio on the training dataset and plotting it against the index portfolio (BTCUSDT):</p>

<pre id="208b" class="graf graf--pre graf-after--p">calc_metrics(df_train)</pre>
<figure id="8aad" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*YJYarPMNaCwfXo65xJd3lw.png" data-image-id="1*YJYarPMNaCwfXo65xJd3lw.png" data-width="363" data-height="312" />
<figcaption class="imageCaption">In-sample performance</figcaption></figure>
<pre id="bed2" class="graf graf--pre graf-after--figure">portfolio_benchmark = plot_return(df_train,'In-sample: Performance of the Model Portfolio')</pre>
<figure id="0e3a" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*EosvyoK9g6Qqkvu7ugRUiA.png" data-image-id="1*EosvyoK9g6Qqkvu7ugRUiA.png" data-width="946" data-height="421" />
<figcaption class="imageCaption">in-sample results</figcaption></figure>
<p id="d7b8" class="graf graf--p graf-after--figure">Resulted plot and metrics for the hold-out dataset:</p>

<pre id="408e" class="graf graf--pre graf-after--p">calc_metrics(df_test)</pre>
<figure id="7ac6" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*KQn3H9TQA7si5bzNKq0yUQ.png" data-image-id="1*KQn3H9TQA7si5bzNKq0yUQ.png" data-width="365" data-height="314" />
<figcaption class="imageCaption">Out-of-sample performance</figcaption></figure>
<pre id="6a4a" class="graf graf--pre graf-after--figure">portfolio_benchmark_ho = plot_return(df_test,'Out-of-sample: Performance of the Model Portfolio')</pre>
<figure id="3469" class="graf graf--figure graf-after--pre"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*gW4cIzwGcOk8SJfkxlYwUQ.png" data-image-id="1*gW4cIzwGcOk8SJfkxlYwUQ.png" data-width="939" data-height="410" />
<figcaption class="imageCaption">Out-of-sample results</figcaption></figure>
<h3 id="e758" class="graf graf--h3 graf-after--figure">Conclusion</h3>
<p id="f476" class="graf graf--p graf-after--h3">In this exercise, we fixed the return of our portfolio and minimized the risk — we get better sharp than any of the coins and performance between best and second-best performing coin.</p>

<blockquote id="2a21" class="graf graf--blockquote graf-after--p"><em class="markup--em markup--blockquote-em">Disclaimer: authors of this paper do not use these methods for any investments and do not recommend to use this paper for investment. It is just for demonstration purposes of the CVXPY. The material presented here is done without a backtest, daily simulation or cutting-edge libraries. We would recommend to use MOSEK library and more rigorous approach.</em></blockquote>
<p id="bcbe" class="graf graf--p graf-after--blockquote">Originally published at <a class="markup--anchor markup--p-anchor" href="https://yourdatablog.com" target="_blank" rel="nofollow noopener" data-href="https://yourdatablog.com">https://yourdatablog.com</a></p>

</div>
</div>
</section>
</section>
</article>&nbsp;