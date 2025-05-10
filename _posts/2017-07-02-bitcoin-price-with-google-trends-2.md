---
layout: "post"
title: "Bitcoin price with google trends"
date: "2017-07-02 22:24:00 +0000"
author: "Vladimir"
wordpress_id: "9295"
status: "publish"
categories:
  - "crypto"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<div dir="ltr" style="text-align: left;">
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">A long ago I want to experiment and deal with a question of how Google trends can be implemented to analyze the financial markets. Here the opportunity has just turned up.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> The main idea consists in the following: As the price is functioning of supply and demand, increase in demand for an asset will cause the growth of the price. The decrease in demand, or increase in the supply, respectively attracts reduction of the price. The assumption which I will check in at research is that the statistics of search queries on "hot trends" can correlate and advance price dynamics of a relevant "hot" asset.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">In the beginning, I have decided to observe BITCOIN cryptocurrency. Today he more than "hot" because of the media interest and big volatility in a price.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> We will need the following tools:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> 1. Data from the Google trend.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> Google trends tools - the excellent example of a BIG DATA implementation. It shows dynamics of the popularity of a particular search query in time. Also, service provides tools for the analysis changes in inquiry and allows to compare keywords among themselves.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> 2. Historical quotes of BTC/USD</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> For that end, it can be used the quotas export from the MT4 terminal which is provided by the BTCe exchange.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> After export of all data and formatting, I applied both lines in one chart. Here is the following graph:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="336" src="https://lh3.googleusercontent.com/3NjHavMUskDczjnLHdL9rqXMND1DbEyUDrkuKV9m2pIp7wNMA5ZgxaTNEwUG-oB9mUlQoXpfz2vXH0oTPFKhAktaFpXCmhKigwFt6A6UwKd4akJQXg8IsJxJbGcsi02I3k4vGr3o" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">The blue line is BTC/USD price, orange - the frequency of "bitcoin" query in Google search engine.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> Already at this stage it evident that there is the correlation between both lines and dependence can be calculated. Here are the outputs:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="151" src="https://lh6.googleusercontent.com/_An4v2jTeiVkflx69f0ycCEI7N2DZ5kTKIXgep5tIJ6Xuy4sGRC_pziZ_1DBoVZtK-4l7GqjZH9oLayBBabbhEN3X4sh9K7fafO6cyZMcjX-FRb8axO2vqxOlN0cC4fvlk4Tl2Ga" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">We see that the correlation is 80.74%. It is evident that there are connections.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> Unfortunately, Google doesn't provide detailed statistics for the entire period, so it can’t be calculated more even. With this data, there is a high error of approximation. Most precisely the dependence is reflected by exponential and polynomial regression:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="396" src="https://lh4.googleusercontent.com/uvpq3IwveBzFHfrLbH9NpIK-PcesxlAfM_aHLfBFK_ra_54VWC-YHX79pS_EkMvXz4BbGICuSWLmahhtHYt51mpcqrz899dX_OX9ekXutd5BjvE6BYX0zL-PQwY9iUVpBA05UAs8" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="396" src="https://lh5.googleusercontent.com/JQMjN2n_ku8ZFjP0gOEeCk_GhZZRbHSt8EsViU3EDGJx9QtxFoxj9izA-lQcWy_QMm8Czuw6kqJ7bPi2zeyCGU5djlbnFiGCgcTOqV-dvYjSQJNEO6lYKhxWt7cRPiM_KtfZVLrz" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> Unfortunately, no conclusions at this stage can be drawn. While the data volume is extremely deficient, it can’t be the forecasting tool. Of Course, I need to consider the broader array of factors. For example, the decision of the Central Bank of Japan about legalization cryptocurrency increased interest to Bitcoin, which affect the price of BTCUSD.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> At the following stage, I will try to find the big database which can be applied to the analysis effectively. I’ll see if they're available open sources solution, such as Quandl, for example.</span></div>
<br />
<br /></div>
</div>