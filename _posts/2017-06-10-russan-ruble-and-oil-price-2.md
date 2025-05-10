---
layout: "post"
title: "Russan ruble and oil price"
date: "2017-06-10 15:04:00 +0000"
author: "Vladimir"
wordpress_id: "9297"
status: "publish"
categories:
  - "finance"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<div dir="ltr" style="text-align: left;">
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Everyone knows how the impact what oil has on the Russian economy. But how it can be explained in the context of math and how it changes in time? I calculated the regression equation and pairwise comparisons for BR futures and USDRUB. All data I took from FINAM open database.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">The first thing I did was import data arrays over a period of the 2012-2017 year.After a simple transformation of data the following</span></div>
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">the chart has turned out:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="224" src="https://lh3.googleusercontent.com/d0D7fA2tTbZ0F72-T0tPy7DoTskwjm5mV2kFA0Hl-XKo5H9LuGTrAGaneGll_fVrIAPYGANvxtfKQXMf3y5pZ3g_UNWzVfSV756epqmEtxlxYc-zNTfVFS9NUi3SM_nnmgFkQ_gK" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">On a vertical axis is a price of USDRUB, on a horizontal axis - BRENT future price. Even on this step, we see high dependence.</span></div>
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Output calculations will be the following:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="48" src="https://lh3.googleusercontent.com/eXfdH-YvDxGGxuc8gdcG8_4we74AblRFUWkv1DIRrlqHn9ZQw-LThq1omYgq4RXDKIGf0xrfFvarwncYb_Ek_K1IEgmKQXx4JQ-ZXcn7i2y4V2Xa8BZD-0EJBbErngiXVTV5V7jG" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="265" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">The regression equation is:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="128" src="https://lh5.googleusercontent.com/07uLfv7849zZvdoJC73F9sq3IVrShg2_lHryyaV4TBKaPjiFGQdwZwc6ms0ske3sZkfYwY6wDe-lxQA_bBipSlCZ4uENSt7ROUZjXyKk2hLW0HxIpjvS9blfaluJ07OfmY7opadM" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="300" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">With the main coefficients:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="300" src="https://lh5.googleusercontent.com/hCAIA69wwTwoTqneGiOJ1TxhXofTgmnc_StdSki_Rt0rMhBKUg9ssgrDBMohH3khu6I2iq3F9rfRxQ0p45OkwvGq-fs8PM6cEUgna8FJSIhHWyUminjPFlPvwr1VG8bKUXAtu3bh" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.656; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Variable A in the red square is approximation error.We see it goes least at exponential regression.&nbsp;Hereafter we’ll use this particular kind of regression. Here are the output charts:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="236" src="https://lh4.googleusercontent.com/uOlTRRgN7sasXDvjtWzpXf_VsZ9RR56lIOV8ugJehPp7qjEqrKZ-Kpv3ycvmUUZP5rC9qtl5xdihKHXYhbCzEwo0ypdO2vkh8a5nefBixig3L8MrJJpI01_2evAg58EiPZswxaJ9" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Blue line - &nbsp;line regression, Red- exponential.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Chart also shows the exponential dependence between USDRUB and BRENT price over the five years distances. </span></div>
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">During that period share of oil and gas incomes in Russian trade balance have been about 47,6% (statistic average).Currently, the percentage has been declined to the smaller amount.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">The table below shows how oil and gas share have been changing during the last decade.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="277" src="https://lh6.googleusercontent.com/G5kwx4cDGrNd-spsPa3AZj2LlPKEjkG5H0Fuy2W8TFLoMFluXKNLXktvKI1oAero3SBwXvR8l71M5DMXUo2587EI3_mK9e0u2xLJzvDle_fhVVaApdmY6uLTbPnGfwSn8162rK6k" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="427" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Let’s explore how the correlation between USDRUB and BRENT was changing at this period. Likely that dependence should decline with reduct&nbsp;considering the part of oil and gas share in the trade balance. Here what show statistical calculations:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">We should keep in mind that Central Bank of Russia moved to floating rate policy towards national currency in November of 2017. It reflected in investigating dependence. Remind that Central Bank of Russia had controlled ruble’s price by сorridor rule.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">It shows how correlation had changed after removal the corridor rule. Best seen displays 2013 and 2014 year chart. Since 2014 USDRUB/BRENT have begun to obey the power low and we can see how correlation increased compared to previous periods.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="239" src="https://lh5.googleusercontent.com/N46jItqicn7-FuRGg0ONQWfga0WjvzPb5JkDrPQ6OMp_iHdw-fy7BVzOIBZsf0Bb4LOOlxLnNIai5g3tzeLjKkmOAJUHw1XP__UAqqGy0wlh0eq4xANHJj8aYWrKk4GULliYWtDq" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">2013 year</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="236" src="https://lh3.googleusercontent.com/Arrt5rqY97fl641QkivSPiWYQf0k6i_XtJcyR7QCIaof4tNNJGEu_PjroS4GW4jb20_KmhyJvTx0UBswm_0ntITPYXcERSR53LhJFv6D9eP8Rin31Nf87iV5Jxz0M8d4nbqRZI1r" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">2014 year</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">This kind of dependence is observing up to the 2017 year. In sum, this gives a high statistical significance for prediction power of this model. Here is the equal for 2016:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="52" src="https://lh6.googleusercontent.com/9JAFZQX4eKJ1Cl_ohE1ELHUdFIDV8z99-i2oe1l4cffrq13wWQmMR6rTA6wDx8lY6mOFXASTxxazGx7A877GU3ZdTGyTC2QjqFTa-NNIyM4_ARhSRju5R5wJTEqXs7NtbLN5qE8s" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="427" /></span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">However, there is one question left: Why the correlation has&nbsp;been reminding at the high level during the 2012 year? I’ll gonna think about it in upcoming research. </span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">If calculates the theoretical price of Russian ruble with this formula, the following value will be around $64.99 (BRENT = 48.99). Considering that USDRUB is equal 57.04, we get the 14% error.It’s more than enough to say that similar ceased to reflect the reality.Also, the chart for 2017 shows the same:</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-left: 11pt; margin-right: 11pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img height="239" src="https://lh5.googleusercontent.com/lbjx-MBAPj0twGKw1BocdSEjsyEtm_y2dq1JXnATh_Gr5IfAy8fGzXpcKrvFZ6jMobbZIEGMiw9p5WE-wUf47-ioIirugDCljGsB6ebq6jYWEtybeM-TYk6lEkqqYWyN7cNJC2-H" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);" width="624" /></span></div>
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-align: center;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">BR/USDRUB 2017</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">It is evident that power dependence disappeared utterly. The correlation falls to 37.89%, which is the lowest since 2012. Why does it happen? It’ll be more clear at the end of 2017 when I can calculate the total data.In any case, it’s clear that the Russian economy is changing, as reflected in the graphs.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">The main conclusion I drow from this research is that in the long term period there is a high power dependence between the USDRUB and oil price. This instrument can become useful for macroeconomic forecast inside trading strategies.</span></div>
<b style="font-weight: normal;"><br /></b>
<br />
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">In fact, I found more questions than answers, so the investigation keeps up.Next time I’ll take a more significant time period with other macroeconomic indicators.</span></div>
<div dir="ltr" style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;">
<span style="background-color: transparent; color: black; font-family: &quot;arial&quot;; font-size: 11pt; font-style: normal; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">For those purposes, I need the stronger tool than excel.I think about R. let's see.</span></div>
<br /></div>