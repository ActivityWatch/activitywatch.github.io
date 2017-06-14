---
layout: page
title: About
permalink: /about/
---

ActivityWatch is about recording our digital lives, an evergrowing part of out lives in general, and the new opportunities enabled by such a record.

You can find the source code for all ActivityWatch projects at
{% include icon-github.html username="activitywatch" %}


## ActivityWatch

By running ActivityWatch on your devices you can collect data about what you do which you can use for a variety of use cases:

 - Record what you do in life.
 - Learn about what you do, and how much you do it. Such as seeing which applications you use, websites you visit, videos you watch, music you listen to and games you play.
 - Estimate productivity by measuring how much time you spend actually getting stuff done.
 - Figure out who actually creates the content you consume and the software you use, so you can reward them accordingly so they are incentivized to continue. (The mission of the [*Thankful*](#thankful) project)

ActivityWatch is a collection of programs meant to work together on the same machine (and in the future across machines).

The project is divided into parts:

 - **aw-server**: provides storage and retrieval of data using a REST API with a variety of storage methods, nimble enough to run locally.
 - **watchers**: clients to the server which collect and send data to the server.
   A few examples include:
   - [aw-watcher-window](https://github.com/ActivityWatch/aw-watcher-window): Logs active window under macOS and Linux (X11), support for Windows planned. 
   - [aw-watcher-afk](https://github.com/ActivityWatch/aw-watcher-afk): Detects user activity using mouse and keyboard, creates AFK events if AFK and non-AFK events if not.
   - (Planned) [aw-watcher-chrome](https://github.com/ActivityWatch/aw-watcher-chrome), logs active tab(s) in Chrome/Chromium.
   - (Planned) [aw-watcher-firefox](https://github.com/ActivityWatch/aw-watcher-firefox): logs active tab(s) in Firefox.
 - importers, used to fetch data from external sources, transform it to the activitywatch dataformat and send it off to the server.

These parts used together form a cohesive system which protects the integrity of the data and provides confidentiality.
**You can be in full control of your data if you want to without losing features**, there is no requirement that a third party will store your data.

The easiest way to get started using ActivityWatch is to use the [aw-bundle](https://github.com/ActivityWatch/aw-bundle) project which provides the standard set of components at versions which are compatible.


## Thankful

*Reward the creators of content and software according to your preferences. Be thankful.*

**Note:** This is at present no more than a dream, we make no guarrantees that it'll ever get built.

Thankful is a program that takes data about which websites you visit, which music you listen to, which videos you watch,
which applications you use (such as Thankful itself), and then presents it to you and allows you to distribute a charitable
sum of your choice to those creators you think are deserving.

For more, check out [Thankful on GitHub](https://github.com/ActivityWatch/thankful).
