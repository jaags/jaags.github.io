---
# layout: single
title: "Node-RED Local Setup"
date: 2018-01-03
permalink: /node-red-local-setup/
tags: [IOT, Internet of things]
header:
  #teaser: "images/node-red-banner-install.png"
  image:  "images/node-red-banner-install.png"
excerpt: "IOT, raspbery pi"
mathjax: "true"
toc: true
toc_icon: "cog"
#categories: self



---

### Node-RED Ready

In the following, let's install Node-RED on Ubuntu 16.04 LTS (Long Term Support) that requires Node.js and npm (node package manager).

### Installing Node.js

Installing Node.js is easy on Ubuntu 16.04 LTS by typing in the below command on the terminal:

`$ sudo apt-get install nodejs`

Once the installation is done, check the version of the node by issue the command:

`$ node -v`
`v8.9.4`


As Nodej.js uses a package manager called npm that allows in install and manage packages. Since Node-RED is an "over-layer graphics" of Node.js, it's manadotary to install it.

`$ sudo apt-get install npm`

When the installation is complete, check the version. If the things are fine, else error would be returned.

`$ npm -v`
`6.8.0`

### Installing Node-RED 

To install Node-RED using npm and admin module which add few tools along, issue the command:

`sudo npm install -g --unsafe-perm node-red node-red-admin`

    Options: 
      -g            - install the Node-RED module in the global directory
      -unsafe-perm  - overrides any errors that may occur during installation


Port:

Node-RED uses port 1880 by default. Hence, it must be enabled using UncomplicatedFirewall (ufw).

`$ sudo ufw allow 1880`


### Runing Node-RED locally:

`$ node-red`

