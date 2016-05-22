---
layout: page
title: About
permalink: /about/
---

ActivityWatch is about recording what you do, so you can become aware of what you do, and choose to do better.
The ActivityWatch team currently works on two related projects:

 - [ActivityWatch](#activitywatch)
 - [Thankful](#thankful)

You can find the source code for all ActivityWatch projects at
{% include icon-github.html username="activitywatch" %}


# ActivityWatch

By running ActivityWatch on your devices you can collect data about what you do which you can use for a variety of use cases:

 - Learn about what you do.
 - Estimate productivity.
 - See which programs you use, websites you visit and games you play the most.
 - Figure out who actually creates the content you absorb and the software you use, so you can reward them. With [*Thankful*](#thankful).

ActivityWatch is a collection of programs meant to work together either on the same system across systems.

The project is divided into parts:

 - aw-server, which provides storage and retreival of data.</li>
 - watchers, clients to the server which collect and send data to the server.
   A few examples include:
   - [aw-watcher-afk](https://github.com/ActivityWatch/aw-watcher-afk), detects user activity using mouse and keyboard.
   - [aw-watcher-firefox](https://github.com/ActivityWatch/aw-watcher-firefox), logs active tab(s) in Firefox.
   - [aw-watcher-x11](https://github.com/ActivityWatch/aw-watcher-x11), logs active window under X11/Linux.
   - (Planned) [aw-watcher-chrome](https://github.com/ActivityWatch/aw-watcher-chrome), logs active tab(s) in Chrome and Chromium.
   - (Planned) [aw-watcher-chrome](https://github.com/ActivityWatch/aw-watcher-osx), logs active window in OS X.
   - (Planned) [aw-watcher-chrome](https://github.com/ActivityWatch/aw-watcher-windows), logs active window under Windows.
 - importers, used to fetch data from external sources, transform it to the activitywatch dataformat and send it off to the server.

These parts used together form a cohesive system which protects the integrity of the data and provides confidentiality. 
**You can be in full control of your data if you want to without losing features**, there is no requirement that a third party will store your data.

The easiest way to get started using ActivityWatch is to use the [aw-bundle](https://github.com/ActivityWatch/aw-bundle) project which provides the standard set of components at versions which are compatible.


# Thankful

*Reward the creators of content and software according to your preferences. Be thankful.*

Thankful is a program that takes data about which websites you visit, which music you listen to, which videos you watch,
which applications you use (such as Thankful itself), and then presents it to you and allows you to distribute a charitable
sum of your choice to those creators you think are deserving.

For more, check out [Thankful on GitHub](https://github.com/ActivityWatch/thankful).

