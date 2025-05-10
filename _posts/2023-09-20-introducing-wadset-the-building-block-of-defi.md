---
layout: "post"
title: "Introducing WadSet&#58; The Building Block of DeFi"
date: "2023-09-20 12:31:33 +0000"
author: "Vladimir"
wordpress_id: "446"
status: "publish"
categories:
  - "crypto"
  - "finance"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<!-- wp:paragraph -->
<p>Anyone with even a passing familiarity with the crypto realm recognizes this: the crypto market largely operates independently from the broader economy. While this independence might present enticing investment opportunities for those looking to diversify their portfolios, it caps the crypto market's growth potential. For it to truly flourish, the crypto market needs to integrate with the wider economy. A promising starting point? The creation and adoption of asset-backed tokens, which offer a direct, peer-to-peer representation of valued assets on-chain.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The concept of formulating an asset-backed token is not novel; it traces its roots all the way back to the practice of securitization. The best-formulated design principles for such a token are highlighted in the vision paper of Lipton, Hardjono, and Pentland [LIPTON et al., 2018], including:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Clear ownership identification</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Transparent shared state</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Mechanisms implementing fiscal policies</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Unambiguous, authenticable identification of entities</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Accurate, unhindered system-wide reporting</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>These principles, which were instrumental in the construction of the internet, are fundamental to the design of the WadSet-based decentralized finance (DeFi) architecture.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what exactly is WadSet? To understand this, we first need to distinguish between traditional finance (TradFi) and DeFi.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Investopedia <a href="https://www.investopedia.com/terms/f/finance.asp">defines</a> finance as a term concerning the management, creation, and study of money and investments. Let's tackle the money aspect first, given its foundational role in finance. Money serves to capture and <a href="https://www.stlouisfed.org/education/economic-lowdown-podcast-series/episode-9-functions-of-money#:~:text=There%20have%20been%20many%20forms,%2C%20limited%20supply%2C%20and%20acceptability.">store</a> value generated in the economy, and participants accept it. But how is money created to begin with?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As highlighted in our previous blog post, in TradFi, money is supplied from the top down. Central banks dictate the amount of liquidity (cash or cash-equivalent assets) available for commercial banks. These commercial banks then determine the liquidity accessible to the broader economy. Broadly speaking, the process can be visualized as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":9493,"width":"507px","height":"auto"} -->
<figure class="wp-block-image aligncenter is-resized"><img src="/media/2024/03/image-4.png" alt="" class="wp-image-9493" style="width:507px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The current financial arrangement has its <a href="https://en.wikipedia.org/wiki/Bretton_Woods_system">roots</a> in the technologies and financial practices of the 20th century. While it was deemed reasonable for its time, its inherent limitations played a role in financial crises, as noted by [<a href="/media/2016/12/swp2016-59.pdf">Bauer &amp; Granziera, 2016</a>]. With the advent of modern financial technologies, it's not a stretch to believe that alternative, possibly more resilient, designs can emerge.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We advocate for a radical transformation in liquidity provision. Instead of banks or ISPs being the primary sources, we envision a world where investors and value creators take the helm. Liquidity managers, collaborating within a cooperative or community framework, should be acknowledged as invaluable assets. For this community-driven approach to thrive and deliver optimal returns, a solid, dependable mechanism is paramount.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":9491,"width":"454px","height":"auto"} -->
<figure class="wp-block-image aligncenter is-resized"><img src="/media/2024/03/image-2.png" alt="" class="wp-image-9491" style="width:454px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>A WadSet serves as a versatile financial instrument pivotal to the world of DeFi. It is essentially a tokenized asset fund, created when an asset owner secures their asset in a segregated DeFi wallet through a decentralized application (dApp). If the asset is a tangible real-world asset, security is generated by the respective institutional service provider (ISP) over the locked asset. This fractional ownership is documented on the blockchain as a collateralized token, available for trade on the open market (DEX/CEX).</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Wadset - is the ownership recorded on the Blockchain&nbsp;</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let's delve into the fabric of (decentralized) finance using the WadSet architecture. We can envision DeFi as a hierarchy of WadSets that interlink and operate seamlessly together</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":9489,"width":"465px","height":"auto"} -->
<figure class="wp-block-image aligncenter is-resized"><img src="/media/2024/03/image.png" alt="" class="wp-image-9489" style="width:465px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Now, let's examine each layer individually. We'll begin with the most fundamental WadSet, representing the basic unit of value - money. This serves as the foundational building block:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":9492,"width":"623px","height":"auto"} -->
<figure class="wp-block-image aligncenter is-resized"><img src="/media/2024/03/image-3.png" alt="" class="wp-image-9492" style="width:623px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The "money" WadSet (which we refer to as a flatcoin) represents liquid funds securely held in a dedicated bank account. This account is directly linked to the flatcoin minted on the network. Through a legal agreement binding the individual, the coin, and the service provider (e.g., a bank), the flatcoin's value is assured. This setup eliminates the need for the community to trust that the network operator maintains sufficient funds to match the circulating tokens, a concern often associated with asset-backed stablecoins like Tether or Circle.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Such a fully-backed flatcoin can be harnessed by the financial system to generate secured loans, inherently designed to be resistant to "bank run" scenarios.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The next layer in the DeFi fabric can be digital with real-world assets. For example, a WadSet that represents ownership of Bitcoin, an Apple share, or a real estate property.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With both the "cash" and "asset" layers combined, we can construct a tokenized <em>investment</em> WadSet fund that would utilize available funds to optimize investors' wealth and liquidity needs.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":9490,"width":"597px","height":"auto"} -->
<figure class="wp-block-image aligncenter is-resized"><img src="/media/2024/03/image-1.png" alt="" class="wp-image-9490" style="width:597px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Consider this a re-envisioned asset-backed fund where all assets are securely stored in a segregated wallet, with transparent ownership by token holders. At first glance, this setup might remind one of a mutual fund (MF) or an exchange-traded fund (ETF). However, the underlying mechanics differ significantly. Both MFs and ETFs pool investors' funds into a <em>aggregated</em> account, purchase assets, and then hold these assets on the investors' behalf. While this structure grants "small" investors access to portfolios they might not otherwise afford, it introduces a specific, often overlooked risk: tracking error.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This WadSet structure stands in stark contrast to the MF/ETF model. WadSet streamlines ownership across every layer of the product's structure. The investors' funds reside in a <em>segregated</em> account, accessible solely by the respective owners. In the event of a market stressor, where numerous investors scramble to liquidate their assets for cash, the price of others' WadSets will remain aligned with its corresponding net asset value (NAV). This design inherently shields investors from the risk of tracking error.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Throughout this exploration, we've touched upon the transformative potential of the WadSet structure in the realm of decentralized finance. We've seen how it stands distinct from traditional financial instruments like MFs and ETFs, offering a more transparent and direct ownership model that mitigates risks like tracking error. As we move forward, there's much more to unpack. In our next article, we'll delve deeper into the intricacies of WadSet mechanics. We'll shed light on the price stability principles of the flatcoin, viewing it through the lens of stablecoin theory and put its resilience to the test with stress-test simulations. Join us as we continue this journey into the future of finance.</p>
<!-- /wp:paragraph -->