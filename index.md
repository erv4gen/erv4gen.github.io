---
layout: default
title: Home
---

## Navigation
- [About Me](/about/)
- [All Posts](/posts/)
- [Privacy Policy](/privacy-policy/)

## Recent posts
<ul>
  {% for post in site.posts limit:10 %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
    </li>
  {% endfor %}
</ul>
