---
layout: post
title: "Development Update August 2018"
date: 2018-08-28 19:06:00 +0200
author: "Erik Bjäreholt"
author_twitter: "ErikBjare"
toc: true
---
It's now been 104 days since the last "bimonthly" development update, this means:

 1. It's time for a new one, and this is a unusually good "bimonthly" update. :ok_hand:
 2. Development updates will now be quarterly. 

## Milestones 🏁

2018-05-28: We released [v0.8.0b2](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b2).  🚢
 - Major performance improvement: pre-merging of heartbeats. ([aw-client#33](https://github.com/ActivityWatch/aw-client/pull/33))
 - Query2 now supports a syntax for creating lists, allowing queries to return multiple things. ([aw-core#50](https://github.com/ActivityWatch/aw-core/pull/50))
 - View full diff [on GitHub](https://github.com/ActivityWatch/activitywatch/compare/v0.8.0b1...v0.8.0b2).

2018-05-30: We released [v0.8.0b3](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b3).  🚢
  - Major performance improvements by pre-merging heartbeats on the server and client-side
  - Improved design of the web UI
  - Implemented flooding ([aw-core#58](https://github.com/ActivityWatch/aw-core/pull/58)) which significantly improving the accuracy some types of events (notably window events, [see this issue for numbers](https://github.com/ActivityWatch/activitywatch/issues/124)). 
 - View full diff [on GitHub](https://github.com/ActivityWatch/activitywatch/compare/v0.8.0b2...v0.8.0b3).

2018-06-22: We hit 1000 stars on GitHub 🌟

2018-07-03: We hit 5000 downloads ⬇️ __and__ we released [v0.8.0b4](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b4)!  🚢
 - View full diff [on GitHub](https://github.com/ActivityWatch/activitywatch/compare/v0.8.0b3...v0.8.0b4).

2018-07-09: We released [v0.8.0b5](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b5). 🚢
 - View full diff [on GitHub](https://github.com/ActivityWatch/activitywatch/compare/v0.8.0b4...v0.8.0b5).

2018-07-17: We hit over 200 daily active users for the web watcher. :chart_with_upwards_trend:

2018-08-14: We hit 6000 downloads ⬇️

2018-08-27: We released [v0.8.0b6](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b6). 🚢
 - Added a new timeline visualization to better visualize event history. ([aw-webui#97](https://github.com/ActivityWatch/aw-webui/pull/97))
 - Fixed the highly popular Windows-specific issue where all modules started by aw-qt also opened a terminal window which they ran in. ([activitywatch#212](https://github.com/ActivityWatch/activitywatch/issues/212))
 - View full diff [on GitHub](https://github.com/ActivityWatch/activitywatch/compare/v0.8.0b5...v0.8.0b6).

Unknown date:

 - At some point we implemented support for the text editors Vim and VSCode, probably in v0.8.0b4. This included a visualization in the web UI where you can see the most edited files, most edited languages, and most edited projects!

## Going forward 🏃‍♀️

 - Raw SQL datastore
    - @johan-bjareholt is still working on a raw SQL implementation of the Peewee datastore that is expected to give further performance improvements, among other things. ([aw-core#57](https://github.com/ActivityWatch/aw-core/pull/57))
 - Import bucket API ([aw-server#41](https://github.com/ActivityWatch/aw-server/pull/41))
   - And later web UI button to make export/import cycle possible, enabling the ability to manually move data between instances with a simple export file.
 - Decentralized sync
   - We've started researching the possibility for a very simple type of sync where you choose a folder that is being synced by Syncthing/Dropbox/Google Drive which is then used to exchange data between hosts.  ([aw-server#50](https://github.com/ActivityWatch/aw-server/pull/50))
   - A huge step towards finally implementing a decentralized sync MVP (thanks to Syncthing ❤️).

## What else?

During the summer @ErikBjare, @johan-bjareholt, @Powersource, and three other wonderful people have been developing [Thankful](https://github.com/ActivityWatch/thankful) under the group name [Superuser Labs](https://superuserlabs.github.io/). We think we're onto something kinda amazing, but we have a bit to go before it's an improvement over existing donation methods.

## Support us! ❤️ 💸

Last month we **only received *$13* in donations** (after fees), that means your donation could be extra important to us. **Do you use ActivityWatch and want to see many updates like this in the future? Support us on [Patreon](https://www.patreon.com/erikbjare) or [OpenCollective](https://opencollective.com/activitywatch)!**

---

> This post was originally published on [the forum](https://forum.activitywatch.net/t/development-update-august-2018/136). It has been reposted here on the blog for archival purposes.
