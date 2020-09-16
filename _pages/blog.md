---
title: ""
layout: archive
permalink: /blog/
classes: wide
author_profile: true
related_img: "/images/ai_image_01.jpeg" 
header:
  image: "/images/ai_image_01.jpeg"
sort_by: date
sort_order: reverse 
og_image: "/images/ai_image_01.jpeg"
sidebar: true
---

{% assign posts = site.posts %} 
{% for post in posts %} 
  {% include archive-single.html type="grid" %} 
{% endfor %}