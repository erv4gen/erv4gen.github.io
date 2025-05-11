---
layout: default
title: All Posts
permalink: /posts/
---

<h2>Topics</h2>

{%- if site.tags.size > 0 -%}
  <ul>
    {%- for tag in site.tags -%}
      {%- assign tag_name = tag | first -%}
      {%- assign tag_posts = tag | last -%}
      <li><a href="{{ site.baseurl }}/tag/{{ tag_name | slugify }}/">{{ tag_name }}</a> ({{ tag_posts.size }})</li>
    {%- endfor -%}
  </ul>
{%- else -%}
  <p>No topics found.</p>
{%- endif -%}

<h2>All Posts</h2>

{%- if site.posts.size > 0 -%}
  <ul>
    {%- for post in site.posts -%}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span> - {{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {%- endfor -%}
  </ul>
{%- else -%}
  <p>No posts found yet.</p>
{%- endif -%}
