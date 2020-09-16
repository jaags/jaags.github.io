---
#layout: single
title: "Serverless Framework Patterns"
date: 2019-01-02
permalink: /serverless-framework-patterns/
tags: [Serverless Architecture]
header:
  #teaser: "/images/perceptron/percept.jpg"
excerpt: "Serverless. Microservices"
mathjax: "true"
toc: true
toc_icon: "cog"
#categories: self
---

Serverless framework can be summarized into four patterns and are as follows:

* Microservices Pattern

* Services Pattern

* Monolithic Pattern

* Graph Pattern


Each on of the mentioned patterns will be explored below with their benefits and drawbacks. 

## Microservices Pattern

In the Microservices Pattern each job or functionality is isolated within a separate Lambda function. In the case of our example app, each Lambda function would also have a single http endpoint that serves as the entry point for that function.

```
service: serverless-social-network
provider: aws
functions:
  usersCreate:
    handler: handlers.usersCreate
    events:
      - http: post users/create
  commentsCreate:
    handler: handlers.commentsCreate
    events:
      - http: post comments/create
```







  