---
layout: "post"
title: "Chapter 2&#58; Permutations and Symmetry"
date: "2023-12-06 16:08:07 +0000"
author: "Vladimir"
wordpress_id: "383"
status: "publish"
categories:
  - "data-science"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<!-- wp:paragraph -->
<p>In the <a href="https://veremin.net/chapter-1-introduction-to-random-walk-2/">first chapter</a>, we embarked on an exploratory journey into the world of stochastic calculus, starting with the basic yet profound concept of the random walk. We began by demystifying the complexity of probability theory, revealing its inherent beauty and simplicity through the lens of discrete-time random walks. We delved into the fundamental principles of probability, using the concept of a 'fair coin' to introduce the Binomial distribution and its application in modeling random walks. This foundation sets the stage for a deeper exploration into the mathematical intricacies of random walks.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By now, we can derive some mathematical representations of the random walk. We can start with the most simple one, an equation for a forward path:<br> $$S_n = X_0 + X_1 + \cdots + X_n$$<br> Where:<br> $latex X = \begin{cases} +1 &amp;\text{with probability} \frac{1}{2}, \\  -1 &amp; \text{with probability} \frac{1}{2},  \end{cases}$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, let's think about what we have here:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>$latex S_n$: is a number that represent a position after $latex n$ steps;</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$latex {X_n}$: is a series of random variables, a single realization of the trajectory that leads to the $latex S_n$.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Since  $latex X_0, X_1, \cdots , X_n$ are <em>iid</em> (independent and identically distributed), let's do a trick and rearrange some elements in the series a little bit:<br> We swap each even element with an odd:<br> $latex X_0 , X_1 , X_2, X_3 ,\cdots$ ⇾ $latex X_1 , X_0 , X_3, X_2 ,\cdots$<br>Note, that the  sum of each of the series is still $latex S_n$, since values are the same, but what changed is the <em>trajectory</em> by which we got to the $latex S_n$. We can illustrate it by plotting an original and new trajectory:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":384,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/12/Pasted-image-20231205160823.png" alt="" class="wp-image-384"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The symmetry in these trajectories is notably striking. It begs the question, 'Are there additional trajectories that would similarly lead to the same $latex S_n$ destination?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's another example where all possible trajectories leading to the point $latex S_n$ is plotted:<br></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":385,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/12/Pasted-image-20231205160850.png" alt="" class="wp-image-385"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Interestingly, we can count precisely the number of trajectories that lead to $latex S_n$ from the origin, bear with me:<br> If we forget about time axis for a second and consider only a position axis (y-axis), then we can express the position $latex S_n$ after $latex n$ steps as a function of two variables:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li># of steps forward (positive direction), let's call it $latex k$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li># of steps backwards (negative direction), it'll be $latex n-k$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>$latex S_n= m = k - (n-k)$ </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Solving for $latex k$, we get:<br> $latex k = \frac{m+n}{2}$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, you can see that to end up $latex m$ steps away from the origin, you need to take $latex \frac{m+n}{2}$​ steps forward, and the rest backward.<br> Since we're looking for all possible combinations (ways of write down #k +1s and #(n-k) -1s), we can use the binomial coefficient:<br> $$\text{# of trajectories}={n  \choose k}={n  \choose \frac{m+n}{2}}$$<br> For example, we can find that after 10 steps ($latex n=10$) the number of paths lead to point $latex m=2$ is exactly $latex {10 \choose \frac{10+2}{2}=6 }= 210$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Even though the number of trajectories gives us a clue about the likelihood of ending up exactly $latex m$ steps from the origin, it's still challenging to compare different outcomes. This difficulty arises because the number of trajectories increases with $latex n$. We need a factor that is also a function of $latex n$, but in the opposite way, so that the measure of likelihood be in the same scale disregard of the $latex n$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's start by rearranging back all trajectories $latex \left\{ S\right\}_n$ that results at $latex m$ by sorting by outcome<br> $latex S_{n,i} = X_0 + X_1 + \cdots + X_n$ ⇾<br> ⇾ $latex S_n^{\text{sorted}} = \text{sort}(S_{n,i})= X_0^{+} + X_1^{+} + \cdots + X_k^{+} \cdots X_0^{-} + X_1^{-} + \cdots + X_{n-k}^{-}$</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>$latex S_{n,i}$ represents a specific permutation of the random walk after $latex n$ steps. </li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$latex S_n^{\text{sorted}}$​ reflects the sorted, common form of any permutation  of $latex S_{n}$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Now, let's answer the question "How likely you can see a row of $latex \left[ X^{+}=+1\right]$ $latex k$ times in the row followed by a series of $latex \left[ X^{-}=-1 \right]$ $latex (n-k)$ times straight".<br> Since we're dealing with a symmetric random walk and $latex P(X^+)= P(X^-)=\frac{1}{2}$, it'll be:<br> $$(\frac{1}{2})^k \times (\frac{1}{2})^{n-k}=(\frac{1}{2})^{n}$$<br>You can see that this scaling factor is exactly what we're looking for since it scales down with  $latex n$ balancing out our combinatorial part.  By putting it all together, we can finally derive the Probability Mass Function (PMF) for a simply symmetric random walk:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$P(m|n) = {n  \choose k}p^{n-k}(1-p)^k={n  \choose \frac{m+n}{2}}p^n$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>NOTE: for a non-symmetric (drift) random walk , the $latex P(X^+)\ne P(X^-)$ and hence we should use the full form.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, let's return once again to the property of time symmetry that I mentioned in the beginning. We can now postulate it from the PMF quite easily:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Since we're using a desperate step of $latex X=\pm1$, $latex S_n$ should be one step away (either below or above) $latex S_{n-1}$ and</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>the position $latex S_t$ depends only on the position $latex S_{t-1}$<br> Given that, we can derive the PMF for $latex S_n$ as a function of PMF  of $latex S_{n-1}$: <br> $$P(m|n)= \frac{1}{2} P(m-1 | n-1) +\frac{1}{2}P(m+1|n-1)$$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The symmetric random walk, despite its seemingly simple nature, is a fundamental model with far-reaching implications and applications. This model serves as a cornerstone in understanding and analyzing complex phenomena across various disciplines including physical, biological, finance, and other systems where even a straightforward mathematical concept can offer profound insights into the complexities of a system.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The versatility of a symmetric random walk allows for modifications and adaptations that can tackle more specific and complex scenarios. For instance, introducing asymmetry or additional constraints can simulate more realistic conditions in various fields.<br> Its ability to model a wide range of real-world systems underlines the importance of probabilistic thinking and statistical principles in understanding our world.</p>
<!-- /wp:paragraph -->

<!-- wp:shortcode -->
[mathjax]
<!-- /wp:shortcode -->