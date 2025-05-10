---
layout: "post"
title: "Option spread SBRF"
date: "2017-05-14 19:04:00 +0000"
author: "Vladimir"
wordpress_id: "22"
status: "publish"
categories:
  - "finance"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<div dir="ltr" style="text-align: left;">
Hi, everybody!<br />
I think it is time, to sum up, the intermediate results on option spread which I opened approximately a month ago.<br />
The spread consisted of two bought options. At the same time all options of one strike, but a different type. Such spread is usually called long straddle.<br />
Structure of an options portfolio:<br />
<br />
<i>Long&nbsp;&nbsp;Call -&nbsp;SBRF-12.16M141216CA 15000</i><br />
<i>Long&nbsp;&nbsp;Put-&nbsp;SBRF-12.16M141216PA 15000</i><br />
<br />
The general idea was following. The future for stocks of Sberbank about the beginning of year technically strongly rose, having updated the maxima. The paper showing new Huy against the background of a decrease in the revenue suggests an idea that technical correction has to follow strong growth.<br />
So the daily chart of SBRF at the time of opening of straddle looked:<br />
<br />
<center>
 <center>
 <a href="https://vk.com/photo15018174_456239066" title=""><img alt="" height="297" src="https://pp.userapi.com/c626523/v626523174/4cc9a/4uwOWBX3YRM.jpg" title="" width="600" /></a></center>
</center>
Considering that the Russian market quite high, and the probability of the continuation of a rally is also present, to open an uncovered short position it was too risky.<br />
Just the long spread of volatility very well is suitable for such situation.<br />
<br />
The position profile on an expiration in spread looks as follows:<br />
<br />
<center>
 <a href="https://vk.com/photo15018174_456239064" title=""><img alt="" height="318" src="https://pp.userapi.com/c626523/v626523174/4cc87/scZbD85tBHI.jpg" title="" width="600" /></a></center>
<br />
<br />
По горизонтали отложены цены базового актива. Тут видно, что пока фьючерс находится в диапазоне стоимость опионов перекрывает прирост их доходности, иными словами позиция оценивается ниже нуля. Для того, чтобы доходность перекрыла премию по опционам, базовый актив должен либо продолжить рост, либо начать падать.<br />
<br />
Вот что происходило дальше:<br />
<br />
<center>
 <a href="https://vk.com/photo15018174_456239067" title=""><img alt="" height="258" src="https://pp.userapi.com/c626523/v626523174/4ccab/x2hhks9WbuU.jpg" title="" width="600" /></a></center>
<br />
Apparently, from the chart, the price derated twice, and indicators of sensitivity changed respectively:<br />
<br />
<center>
 <a href="https://vk.com/photo15018174_456239069" title=""><img alt="" height="103" src="https://pp.userapi.com/c626523/v626523174/4ccbc/oAnxnAXT1xc.jpg" title="" width="409" /></a></center>
Apparently, the delta jumped from-60 to +90. It created floating profit in the spread. But as I did not use a delta hedge in work, with each return to a strike profit on the monetary option was nullified.<br />
Initially, I did not plan to hedge the delta, and I not especially worry about it. Just now I know as it is correct to do it and further I will surely watch the delta of a position closely. I will use most likely a contour for maintenance it about zero.<br />
Besides the delta, the long spread still has one crucial risk - it is Teta, time disintegration of the option. As all my options bought, time works for me, and every day they lose the temporary cost. Considering what in approach to the expiration of the tet amplifies, now its profile looks as follows:<br />
<br />
<center>
 <a href="https://vk.com/photo15018174_456239070" title=""><img alt="" height="324" src="https://pp.userapi.com/c626523/v626523174/4ccc3/-_awG79oN80.jpg" title="" width="600" /></a></center>
<br />
Time here is shown by the movement from the red line to dark blue. Apparently, it not linearly influences my spread.<br />
As before an expiration, there were only about 2 weeks, and the probability of leaving in the left leg promptly decreases, the decision to close risk on tet was made, having sold out.<br />
As a result at present, my spread passed a position on the option call into ordinary Long.<br />
The current risk profile looks as follows:<br />
<br />
<center>
 <a href="https://vk.com/photo15018174_456239071" title=""><img alt="" height="331" src="https://pp.userapi.com/c626523/v626523174/4cccc/S3myDrFPseI.jpg" title="" width="600" /></a></center>
<br />
<a href="https://www.blogger.com/null" name="Краткие результаты по портфелю опционов ( за месяц):"></a><br />
<div>
Short results on a portfolio of options (in a month):</div>
<br />
<ul><br />
<li><span>&nbsp;Calls up to: 84%</span></li>
<br />
<li><span>total income: 4.02 %</span></li>
</ul>
<br />
<a href="https://www.blogger.com/null" name="Следующие действия:"></a><br />
<div>
Following actions:</div>
<br />
<ul><br />
<li><span>The Call will be held either before an expiration, or to the purpose on profitability (RR=3)</span></li>
<br />
<li><span>I will monitor changes of the delta from now on and in time to hedge it to a contour not to lose profit.</span></li>
</ul>
</div>