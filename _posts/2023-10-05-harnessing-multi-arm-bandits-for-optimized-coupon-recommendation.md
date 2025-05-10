---
layout: "post"
title: "Multi-Arm Bandits for Recommendation Systems"
date: "2023-10-05 18:12:50 +0000"
author: "Vladimir"
wordpress_id: "90"
status: "publish"
categories:
  - "data-science"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<!-- wp:shortcode -->
[mathjax]
<!-- /wp:shortcode -->

<!-- wp:paragraph -->
<p>Envision yourself as a store owner looking to boost foot traffic. You hatch a plan: stand at the front and actively promote your items to those walking by. With enthusiasm, you quickly wear a striking outfit and hold up a blank board, ready to publicize a special deal. However, when it's time to pen the actual offer, you're stumped. A "10% discount on everything" could work, but you're torn between it being too small to matter or too large to remain profitable. A flat "$2 off your initial buy" crosses your mind, but could this be overly generous for just any passerby? Then the idea of "Free gift with every purchase" springs forth. It's intriguing, but will it genuinely enhance the day's revenue?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You quickly realize that what you truly need is some sort of method, capable of predicting the most appealing offer for each potential customer.<br>Welcome to the intricate and intriguing realm of recommendation systems, where algorithms help to match the right offer to the right customer, improving your chances of conversion and sales.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Recommendation systems is all about data</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>When we talk about recommendation systems, we talk big data! Abundance of data ensures a higher level of confidence about user preferences. In contrast, when there is limited data, there is a lack of certainty about what users might prefer. However, even in the face of such uncertainty, recommenders tend to prioritize and suggest items that have received a higher level of engagement previously.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For instance, with collaborative filtering, a most popular method typically used by recommender systems, users are matched based on their past behaviors or ratings. A user may be recommended a movie that other similar users have enjoyed.</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://blog.griddynamics.com/content/images/2023/09/multi-armed_bandits_1.jpg" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Meanwhile, item-based similarity approaches would recommend items that are similar to ones the user has previously interacted with or rated highly. For instance, if a user liked a certain science fiction book, they would be recommended other books in the same genre or by the same author.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>However, these methods can contribute to a <strong>feedback loop</strong>, where items that aren't initially recommended continue to receive low to no engagement. This results in a cycle where those items that were initially popular and recommended continue to get promoted, while potentially relevant items get ignored. This might lead to the problem of overfitting, where only a limited set of items get recommended over and over, while a large variety of other potentially interesting items are not discovered or recommended. As a result, the system fails to explore the breadth of user preferences, limiting the overall user experience.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Mastering Multi-Arm Bandits</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There are several approaches that can solve this type of overfitting, the Multi-Arm Bandits is one of the most powerful and commonly used ones. Bandit algorithms propose a solution to this feedback-loop problem by modeling uncertainty and intentionally exploring to minimize it. This strategy embodies the concept of '<em>exploration vs exploitation</em>', where '<em>exploitation</em>' is using the knowledge we already have to recommend the most engaging items, while '<em>exploration</em>' involves suggesting less-known items to gather more information about user preferences.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By acknowledging the inherent uncertainty in the data, bandits actively engage in exploration to reduce it, thereby learning about the potential relevance of previously unexplored or underexplored items. For instance, instead of continually recommending the best-performing item (a best-selling menu item, for example), a bandit algorithm might occasionally recommend a less popular item (perhaps a new item or previously unpopular). This explorative approach provides an opportunity to discover whether users might like this less-known item, thereby expanding the scope of recommendations.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Moreover, bandits incorporate a system of rewards, where a successful recommendation (like a user clicking on a recommended item) garners a '<strong>reward</strong>'. Over time, these rewards inform the algorithm about the likelihood of different items being appreciated by different users, further refining the recommendation process. This harmonious blend of uncertainty, exploration, and learning makes bandit algorithms a compelling approach to mitigating the issues prevalent in the realm of recommendation systems.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Reward is usually denoted as $latex R_t $</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>Every time an action is taken a reward is obtained. Each time an action is taken the reward returned can have a different value.</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Below is few more definition that are used to define the Bandit model:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>The number of available actions is denoted by the letter $latex k$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Action</strong>: the action taken at time-step $latex t$ is denoted as $latex A_t$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Each of the available $latex k$ actions has an <strong>expected reward: Q(a):</strong><br>$$Q(a) = E[R_t | A_t = a]$$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The most simple example of the reward function is a Sample Average Estimates:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$Q_{t+1}(a) = \frac{1}{n} \sum_{i=1}^{n} R_i$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Choosing The Right Bandit</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Choosing different design of the reward function yield different types of Bandits.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In the following sections, we will touch upon three fundamental bandit algorithms: epsilon-greedy, Upper Confidence Bound (UCB), and Thomson Sampling.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li><strong>Epsilon-Greedy</strong>: This algorithm operates by using a probability $latex ε$ to determine if it will explore or exploit. So, the reward function could be represented like:</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>$$R_t = \begin{cases} \text{argmax}_{a} Q_t(a), &amp; \text{with probability } 1 - ε \\ \text{a random action}, &amp; \text{with probability } ε \end{cases}$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Where</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>$latex R_t$ represents the chosen action at time $latex t$,</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$latex Q_t(a)$ is the estimated value of action $latex a$ at time $latex t$, and</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$latex ε$ is the probability of choosing to explore rather than exploit.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li><strong>Upper Confidence Bound (UCB)</strong>: The UCB algorithm adds a confidence interval to the estimated reward for each action. The action chosen is the one with the highest upper confidence bound. This could be represented like:</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>$$A_t = \text{argmax}_{a} \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Where $latex A_t$ is the action chosen at time $latex t$, $latex Q_t(a)$ is the estimated value of action $latex a$ at time $latex t$, $latex c$ is a constant determining the level of exploration, $latex N_t(a)$ is the number of times action $latex a$ has been chosen up to time $latex t$, and $latex l_n$ is the natural logarithm.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>Thomson Sampling.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In this algorithm, an action is chosen based on the highest sample from each action's reward distribution. This could be represented like:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$A_t = \text{argmax}_{a} \left[ \text{Sample from } β(R_{1:t-1}(a), T_{1:t-1}(a)) \right]$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Where $latex A_t$ is the action chosen at time $latex t$, $latex β$ represents a Beta distribution (commonly used in Thompson Sampling when rewards are binary), $latex R_{1:t-1}(a)$ is the sum of rewards for action $latex a$ up to time $latex t-1$, and $latex T_{1:t-1}(a)$ is the total number of times action $latex a$ has been chosen up to time $latex t-1$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our primary focus will be on Thomson Sampling, as it frequently surpasses both epsilon-greedy and UCB algorithms in performance. For readers interested in delving deeper into each algorithm and exploring a comprehensive comparison between them, we've included pertinent links in the reference section.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Data For Bandits</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Returning to our shopkeeper scenario, after acquiring a solid understanding of multi-arm bandits and different reward functions, our shopkeeper resolves to employ the Thompson Sampling technique to identify the optimal offer for each of his patrons. His store, being somewhat removed from the bustling main street, sees a regular flow of three individuals passing by daily - we'll denote these as Person $latex P_1$, $latex P_2$, and $latex P_3$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For each individual $latex P_i$ (where $latex i$ ranges from 1 to 3), there are five potential offers (or actions) that the shopkeeper could extend, denoted as $latex a_1, a_2, \ldots, a_5$. Notably, he also posits that not all individuals may necessarily need an offer to visit the store. To verify this hypothesis, he decides to occasionally abstain from extending any offers at all, thereby establishing a control observation for his experiment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With each passing day, the shopkeeper observes the interactions of each individual with the varying offers (including the no-offer scenario), aiming to discern the optimal action $latex A_i$ for each person $latex i$. This optimal action would not only encourage a higher frequency of store visits (improving conversion rates), but also exhibit an uplift over the control scenario of no offers. In doing so, the shopkeeper can ensure his marketing campaign is cost-efficient, only extending offers when they demonstrably enhance store visitation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Defining The Learner</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>With a clear strategy in mind, the shopkeeper set forth on a two-month experiment. Each day, he displayed a distinct offer (or no offer at all) to each of the three individuals, and meticulously recorded the outcome or "reward" ($latex R$) as either a conversion (1) or non-conversion (0):</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$R_{t,i,a} =<br>\begin{cases}<br>1 &amp; \text{if conversion} \\<br>0 &amp; \text{if non-conversion}<br>\end{cases}$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this formula, $latex t$ denotes the time step or day index, $latex i$ signifies the person, and $latex a$ indicates the offer index.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The shopkeeper then updated the parameters of the Beta distribution for each person's offer preference using the following rules:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>$latex \alpha_{t,i,a} := \alpha_{t-1,i,a} + R_{t,i,a}$ (representing the number of successes)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$latex \beta_{t,i,a} := \beta_{t-1,i,a} + (1 - R_{t,i,a})$ (representing the number of failures)</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Here, $latex \alpha_{t,i,a}$ and $latex \beta_{t,i,a}$ denote the parameters of the Beta distribution for person $latex i$, action $latex a$ at time step $latex t$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These updates provided the shopkeeper an estimated conversion probability $latex P_{i}(X|a)$ for each individual and offer. This probability followed a Beta distribution:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$P_{i}(X|a) \sim \text{Beta}(\alpha_{t,i,a},\beta_{t,i,a})$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, to decide which offer to show next, the shopkeeper chose the action $a$ that yielded the maximum expected reward. He used the following strategy to select the action:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$A_{t+1,i} = \text{argmax}_{a} \left[ \text{Sample from } \text{Beta}(\alpha_{t,i,a}, \beta_{t,i,a}) \right]$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Running the Model</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>After two months of diligent experimentation, the shopkeeper had amassed a rich collection of data for each passerby, shedding light on their distinct preferences. The shopkeeper meticulously recorded a sequence of observations:</p>
<!-- /wp:paragraph -->

<!-- wp:table -->
<figure class="wp-block-table"><table><thead><tr><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th><th>&nbsp;</th></tr></thead><tbody><tr><td>customer_id</td><td>day_index</td><td>offer_index</td><td>success</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>This table delineates the data he recorded. The <code>day_index</code> column begins from 0, representing the first day of the experiment. The <code>customer_id</code> could be either 0, 1, or 2, indicating the individual to whom an offer was presented. The <code>offer_index</code> reflects the specific offer shown - ranging from 1 to 5, with '-1' indicating a control experiment where no offer was presented. Finally, the <code>success</code> column is a binary marker showing whether the individual visited the shop after seeing the offer, with '1' indicating a visit and '0' representing no visit.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Armed with this data, the shopkeeper dusted off his seldom-used laptop and entered these records into a Jupyter Notebook to analyze and visualize the results. His analysis culminated in a series of animated plots demonstrating the convergence of the Beta distribution for each individual over time.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":9471,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-full"><img src="/media/2024/03/Multi-armed-bandits-results-1.gif" alt="" class="wp-image-9471"/></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/media/2024/01/Multi-armed-bandits-results-1.gif" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>For the first customer, the plot reveals a surprising trend. This customer demonstrated the largest response in the control observations, suggesting that the mere presentation of an offer discouraged them from entering the store. In marketing terminology, this segment of customers is known as 'sleeping dogs,' who are best left undisturbed.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:image {"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/media/2024/01/Multi-armed-bandits-results-2-1.gif" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>In stark contrast, the second customer showed a strong preference for a specific offer. The offer $latex a^{(1)}$ yielded a clear uplift in store visits compared to other offers and the control group. This data suggests that the individual was persuadable and therefore worth the investment in marketing efforts.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:image {"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/media/2024/01/Multi-armed-bandits-results-2-1.gif" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>The third customer, however, painted a completely different picture. The response rate was uniform across all offers, including the control group. This was a clear indication that regardless of the marketing efforts or offers, this individual's decision to visit the store remained unchanged. As such, including this individual in the target audience would not result in incremental net sales and would be an inefficient use of resources</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In conclusion, the shopkeeper's innovative application of Thompson Sampling provided him with invaluable insights. It empowered him to tailor his marketing strategy for each individual customer, enhancing efficiency and cost-effectiveness.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By mapping customer responses to offers, he could discern the impact of different marketing efforts. This data-driven approach enabled more effective customer segmentation. Instead of a one-size-fits-all strategy, he could now tailor offers based on individual preferences, optimizing the value of his marketing budget.<br>Moreover, he could identify customers who remained unaffected by offers, thereby avoiding unnecessary marketing expenditure. On the flip side, he recognized customers who would purchase irrespective of promotions, saving resources on unneeded incentives.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In essence, the shopkeeper's strategic use of Thompson Sampling refined his marketing from broad-strokes to precision-guided. This case underscores the potential of machine learning algorithms in enhancing marketing effectiveness and customer segmentation while ensuring optimal return on marketing investment.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">References</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>“How to Build and Evaluate a Next Best Action Model,” Grid Dynamics Blog, July 29, 2021, <a href="https://blog.griddynamics.com/next-best-action-churn-prevention/">https://blog.griddynamics.com/next-best-action-churn-prevention/</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Prince Grover, “Various Implementations of Collaborative Filtering,” Medium, March 31, 2020, <a href="https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0">https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Guilherme Duarte Marmerola, “Thompson Sampling for Contextual Bandits,” Guilherme’s Blog, November 28, 2017, <a href="https://gdmarmerola.github.io//ts-for-contextual-bandits/">https://gdmarmerola.github.io//ts-for-contextual-bandits/</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>James McInerney et al., “Explore, Exploit, and Explain: Personalizing Explainable Recommendations with Bandits,” in Proceedings of the 12th ACM Conference on Recommender Systems, RecSys ’18 (New York, NY, USA: Association for Computing Machinery, 2018), 31–39, <a href="https://doi.org/10.1145/3240323.3240354">https://doi.org/10.1145/3240323.3240354</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Eugene Yan, “Bandits for Recommender Systems,” eugeneyan.com, May 8, 2022, <a href="https://eugeneyan.com/writing/bandits/">https://eugeneyan.com/writing/bandits/</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Steve Roberts, “Multi-Armed Bandits: Part 1,” Medium, December 10, 2020, <a href="https://towardsdatascience.com/multi-armed-bandits-part-1-b8d33ab80697">https://towardsdatascience.com/multi-armed-bandits-part-1-b8d33ab80697</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>“Beta Distribution,” in Wikipedia, July 27, 2023, <a href="https://en.wikipedia.org/w/index.php?title=Beta_distribution&amp;oldid=1167451431">https://en.wikipedia.org/w/index.php?title=Beta_distribution&amp;oldid=1167451431</a>.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Originally published on <a href="https://blog.griddynamics.com/multi-armed-bandit-recommendations-system/">Grid Dynamics Blog</a></p>
<!-- /wp:paragraph -->