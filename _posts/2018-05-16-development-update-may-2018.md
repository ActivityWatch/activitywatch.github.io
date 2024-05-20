---
layout: post
title: "Development Update May 2018"
date: 2018-05-16 11:36:00 +0200
author: "Erik Bjäreholt"
author_twitter: "ErikBjare"
toc: true
---

[On request](https://www.patreon.com/posts/17206179) we've decided to start doing these bimonthly development updates in order to keep you all updated about how development is progressing. It might take a few updates for us to get this going, but we'll get there!

## Milestones

May 7th: We finally released [v0.8.0b1](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b1). It's been our first release since November 2017 and is the first beta release of the upcoming (and amazing) new v0.8 release.

May 15th: We hit 4000 downloads 🌟

## Improvements

 - Implemented our query2 querying language and rewrote much of the visualization code to use it. This is a huge step forward for future visualization work. ([aw-core#46](https://github.com/ActivityWatch/aw-core/pull/46), [aw-server#35](https://github.com/ActivityWatch/aw-server/pull/35), [aw-webui#48](https://github.com/ActivityWatch/aw-webui/pull/48))
 - Added a query explorer in the web UI to help with testing queries. ([aw-webui#64](https://github.com/ActivityWatch/aw-webui/pull/64))
 - Made watchers more resilient by switching to a new type of request queue. ([aw-client#28](https://github.com/ActivityWatch/aw-client/pull/28))
 - Started developing `aw-client-js` ([aw-client-js#2](https://github.com/ActivityWatch/aw-client-js/pull/2)) and switched to using it in `aw-webui` ([aw-webui#62](https://github.com/ActivityWatch/aw-webui/pull/62)).
 - The web UI now has a view for the most-visited domains. ([this commit](https://github.com/ActivityWatch/aw-webui/commit/8f443bc1e258c54f1838994e0f1f79e254d86d6a))
 - The web UI now has a button for removing buckets. ([this commit](https://github.com/ActivityWatch/aw-webui/commit/6410170d3192c9e73bb7957ea7e7b9ce606e25ac#diff-32c6cbf8ae7a966f7e41ec78a6d775cb))
 - We now have [a package on the AUR](https://aur.archlinux.org/packages/activitywatch-bin/) for easy installation on Arch Linux!
 - And a bunch of smaller bugfixes and reliability improvements.

## Going forward

We've been hard at work trying to improve the performance of ActivityWatch ([activitywatch#98](https://github.com/ActivityWatch/activitywatch/issues/98)) using several approaches: 
 - Switching to a pure-SQL implementation of the SQLite datastore. ([aw-core#57](https://github.com/ActivityWatch/aw-core/pull/57))
 - Pre-merging of heartbeat events. ([aw-client#33](https://github.com/ActivityWatch/aw-client/pull/33))

We'll also spend a considerate amount of time developing ActivityWatch this coming summer as we're a team of five people who will be working on our related project [Thankful](https://github.com/ActivityWatch/thankful). Certainly something to look forward to!

**Do you like ActivityWatch and hope to see many updates like this in the future? [Support us on Patreon!](https://www.patreon.com/erikbjare)**

---

> This post was originally published on [the forum](https://forum.activitywatch.net/t/development-update-may-2018/108). It has been reposted here on the blog for archival purposes.
