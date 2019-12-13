---
title: ""
layout: archive
permalink: /blog/
classes: wide
author_profile: true
related_img: "/images/fort point.png" 
header:
  image: "/images/fort point.png"
sort_by: date
sort_order: reverse 
og_image: "/images/fort point.png"
sidebar: true
---

{% assign posts = site.posts %} 
{% for post in posts %} 
  {% include archive-single.html type="grid" %} 
{% endfor %}