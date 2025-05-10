---
layout: "post"
title: "Problem-Solving Principles Applied to Data Science"
date: "2025-01-14 17:50:20 +0000"
author: "Vladimir"
wordpress_id: "9498"
status: "publish"
categories:
  - "data-science"
tags:
  - "data-science"
  - "machine-learning"
  - "problem-solving"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center"><em>Auguste Rodin, The Burghers of Calais, The Musée Rodin of Paris, France</em></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Introduction</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The field of Data Science is among the most diverse ones. It's relatively young and still in search for its shapes. It results that many problems require non-standard, out-of-the-box solutions. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Being a data scientist is like being a detective, but you deal with big, flat tables (and sometimes with people). You have an unknown, sometimes unformulated problem, and your goal is to deduce and derive the answer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this post, I will discuss the methods I employ when solving problems, which are not limited to a data science context. I hope that this information can be helpful to someone who is just starting out in the field or&nbsp;an experienced person who wants to explore a slightly different perspective on the topic.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Problem-solving is about creativity</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>And creativity is about generalization.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I've been told once that there are many good problem solvers in the field of data science who can apply very advanced methods and work with complex data—there is no real shortage of good executes in the field. But what is, in fact, a rare find is a strong data scientist with a creative mind. By that, I mean a person who would find a new approach to the problem, a surprising data perspective. At the end of the day, data is just a projection of reality onto our hard drives, and it's easy to get stuck in this projection. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Even though curiosity is natural for a human, it's a skill to systematically apply it to enhance your knowledge of the world and to build connections between seemingly unrelated topics. As one great mathematician once said:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>A mathematician is a person who can find analogies between theorems; a better mathematician&nbsp;is one who can&nbsp;see analogies between proofs, and the best mathematician can notice analogies between theories. One can imagine that the ultimate mathematician&nbsp;is one who can&nbsp;see analogies between analogies.</p>
<!-- /wp:paragraph --><cite>Stefan Banach</cite></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>My understanding of this quote is that "analogies between analogies" is a rephrased&nbsp;<em>generalization</em>.&nbsp;<br>Generalized knowledge forms a broad outlook, is the highest-quality knowledge that can exist, and is a key to any new discovery! <em>Liberal arts</em> facilitates the generalization of knowledge; it teaches you creativity and active thinking. If force, you create a habit of idea fusion and examples of how the same underlying principle (model) can work in very different contexts.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I remember several times I found an inspiration or cross-reference to the data science problem while reading through a fiction book. Our world is filled with different models: some of them based on big enough dataset, some aren't, but these models can still be useful.  <br>So don't descriminate fiction and liberal arts in general, it's not a waste of time for techy, it's a practice in creativity, practice in problem-solving.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Analytics is like debugging</h2>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>Analysis is like debugging</p>
<!-- /wp:paragraph --><cite>-Edward Schwalb</cite></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>With a background in computer science, this is quite intuitive for me. You have a complex system you want to understand, tweak, and eventually affect. You want to find, isolate, and control most factors affecting the outcome. The nature is quite ironical, and usually, you don't have direct access to the most important factors, at most to some proxy metrics of them. It's not necessarily a bad thing per se, but you must be aware of what limitations it brings to your model.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Start Simple</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As a data scientist, you'll often approach an open-ended, loosely defined problem that may&nbsp;not&nbsp;be firmly formulated.&nbsp;There'll be many possible paths to proceed with the exploration, and it's so easy to get lost in the woods of theories that look so appealing and attractive that it's hard to resist following them. Leave that alone, and you'll quickly find yourself completely lost and overwhelmed with theories that can explain every possible outcome. To avoid that, data scientists should think of themselves as "detectives" and follow the rigorous rules:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li><em>Ask the most simple question</em></li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>First, find out the most simple question you can find a reliable answer to. It may be something as trivial as "What data do we have?" or&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true,"start":2} -->
<ol start="2"><!-- wp:list-item -->
<li><em>Start with the situation when you have the most information.</em></li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>When you get answers to your questions, identify the area where you have the most information.&nbsp;This&nbsp;would be your starting point in the analysis. By testing your hypotheses, there'll be fewer chances for confusion and messing with facts&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true,"start":3} -->
<ol start="3"><!-- wp:list-item -->
<li><em>Find something that you can prove working and then reduce the search space</em></li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>This&nbsp;means paying precise attention to the feedback of your tests. Even the most simple model whose effect size is higher than the variance can tell a lot about the environment that you study and can give a hint about where to move next.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true,"start":4} -->
<ol start="4"><!-- wp:list-item -->
<li><em>Use Occam's razor to illuminate sophisticated questions/explanations.</em></li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>This&nbsp;is&nbsp;practically&nbsp;the return to&nbsp;point&nbsp;#1 - stick with the&nbsp;simplest&nbsp;explanation.&nbsp;With more data available and more experiments conducted, you'll&nbsp;be tempted&nbsp;to find a more "elegant," more "sophisticated" explanation for your subject. Be cautious: in two competitive hypotheses, cut off the one that has more assumptions or parameters...&nbsp;Unless you can find more data to justify it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Optimizing data brings more benefits than optimizing the model</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Most of the time, data scientists would spend unproductive trying to optimize the model.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Part of&nbsp;the reason&nbsp;why using cleverer algorithms has a smaller payoff than you might expect is that,&nbsp;<em>to a first approximation, they all do the same.</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I like this quote from the "A Few Useful Things to Know About Machine Learning"&nbsp;<sup><a href="//obsidian.md/index.html#fn-1-1efb5d87b261c04c" target="_blank" rel="noreferrer noopener">[1]</a></sup>&nbsp;article:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>All learners essentially work by grouping nearby examples into the same class; the key difference is&nbsp;in&nbsp;the meaning of "nearby".</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>With nonuniformly distributed data, learners can produce widely different frontiers while still making the&nbsp;same&nbsp;predictions in the regions that matter (those with a substantial number of training examples and, therefore, also where most test examples are likely to appear).&nbsp;This&nbsp;also helps explain why powerful learners can be unstable but still accurate.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Easily, the most crucial factor is the features used.&nbsp;Learning is easy if many independent features correlate&nbsp;well with the class. On the other hand, if the class is a very complex function of the features, you may not be able to learn it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">All models are wrong, but some are useful</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This&nbsp;is at the core of our business. You will never get a perfect model, but you don't&nbsp;even&nbsp;need one.&nbsp;What you need is&nbsp;an understanding of what imperfect model can&nbsp;be applied&nbsp;in a particular situation.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A simple example is Linear Regression. It is quite a&nbsp;strong&nbsp;tool for analysis despite its simplicity.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9502,"width":"627px","height":"auto","sizeSlug":"full","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-full is-resized"><img src="/media/2024/04/lr-1.png" alt="" class="wp-image-9502" style="width:627px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The important part is that if you know that residuals of your model are&nbsp;normal&nbsp;(i.e., your estimator is unbiased), you can be sure that if applied at scale, errors of your model would&nbsp;tend to&nbsp;cancel each other out.&nbsp;This&nbsp;is a&nbsp;special&nbsp;case of&nbsp;the realization of&nbsp;the&nbsp;Central Limit Theorem&nbsp;and its power.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":9509,"width":"726px","height":"auto","sizeSlug":"full","linkDestination":"none","align":"center","className":"is-style-default"} -->
<figure class="wp-block-image aligncenter size-full is-resized is-style-default"><img src="/media/2024/04/lr2-1.png" alt="" class="wp-image-9509" style="width:726px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Modeling key principle</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>You must know when the model&nbsp;works&nbsp;and&nbsp;doesn't and what <em>limitations</em>.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>Make sure your model's metric&nbsp;is represented&nbsp;in the online data.&nbsp;Whatever metric you use,&nbsp;make sure to&nbsp;evaluate it during the model serving.&nbsp;</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>This is, at the same time, the most simple and the most complicated principle in machine learning. When you train the model, you have full control over the data you feed to it, and the model learns the corresponding distribution. But when the model is deployed to production, it is left on the mercy of what data will be passes to it. If it significantly different from what has been seen, and the model has some non-linear components, it can produce unstable and unexpected prediction. This is known as <em>data drift.</em> I can re-state this principle as "if something goes wrong, checking the data, it's probably the cause, and only then check the model". </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">The sophistication of the algorithm is rarely the limiting factor</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In AI applications, the sophistication of the algorithm is rarely the limiting factor. The quality of the design, the data, and the people that make up the system all matter more.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Data scientists should be a good speaker</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I've proven many times that an unsophisticated project with a convincing story and well-crafted deck will outgrow advanced projects that you have trouble pitching. Even a simple visualization can go a long way.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In other words, prepare presentations for all your projects and keep these decks organized. Even if you fail to sell your project at first, there will certainly be another opportunity with better circumstances, and having a deck ready can be paramount.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In this article, I outlined some of the key principles I developed as a data scientist. Not all of them are strict rules or necessary checkmarks, but rather guidance that I follow on a daily basis. This post wasn't filled with technical details, as one may expect. Even though tech details are the actual material components of machine learning, the approach and strategy of applying them define the quality of the resulting effect.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By adopting these principles in your data science work, you can streamline your process, avoid common mistakes, and ultimately create more effective, robust models.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you have any questions, thoughts, or principles of your own to share, please leave a comment below. I'd love to hear from you and learn from your experiences as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For those interested in diving deeper into these principles and other data science topics, I invite you to check out my upcoming meetup called "AI/ML Conversations" where we'll explore these concepts in greater depth. It happens in-peson in NYC and online via Zoom.<br>It's a fantastic opportunity to connect with other data science enthusiasts, learn from expert speakers, and share your own insights. Looking forward to seeing you there! We are open to speakers, so feel free to reach out to me on LinkedIn, or use this form to submit your proposal.</p>
<!-- /wp:paragraph -->