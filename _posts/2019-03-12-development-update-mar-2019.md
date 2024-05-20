---
layout: post
title: "Development Update March 2019"
date: 2019-03-12 13:06:00 +0200
author: "Erik Bjäreholt"
author_twitter: "ErikBjare"
toc: true
---

It's time for another development update!

We are sorry for the long delay in our development updates, but infrequent updates also mean ***larger*** updates. [The last development update](https://forum.activitywatch.net/t/development-update-august-2018/136) was written about half a year ago, so we have a lot of things to share!

If you don't want to read all these notes and just want to experience the new beta of ActivityWatch right away, [you can download it here](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b8)!

# 🏁 Milestones

- **2019-03-09:** 🚢 [0.8.0 beta 8](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b8) was released

- **2019-01-14:** 🤖 First [aw-android](https://github.com/ActivityWatch/aw-android/) release

 - **2019-01-05:** ⬇️ We passed 10,000 downloads!

- **2018-12-08:** ⚙️ [aw-server-rust](https://github.com/ActivityWatch/aw-server-rust/) reached feature parity

- **2018-11-03:** 🚢 [0.8.0 beta 7](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.8.0b7) was released

[Changelog can be found here](https://activitywatch.readthedocs.io/en/latest/changelog.html#v0-8-0b8)

# 📯 Major News

## 🤖 ActivityWatch is now in early beta on Android!

We have been working on getting ActivityWatch to Android for a long time (see [this issue](https://github.com/ActivityWatch/activitywatch/issues/6)). There's a good reason why we think it's important: in my own analysis, it accounts for almost half of my screen time!

So now we finally have something that you can try out! While not great (yet) there's a lot to be excited about.

By being backed by our new high-performance implementation of the aw-server written in Rust (see below) it will have the same underlying features and APIs of the desktop version of ActivityWatch, making it a great foundation that will make development easy going forward. The web UI is currently available in the app (but is notably broken in a lot of ways), but we hope to be able to build some native UI elements in the future!

Now we just need to find the time to keep building, but we hope we might be able to find some contributors to help us out with doing so now that we have a solid foundation built on the same APIs already available in ActivityWatch elsewhere!

Get it on the [Play Store](https://play.google.com/store/apps/details?id=net.activitywatch.android), or [check out the code on GitHub](https://github.com/ActivityWatch/aw-android)!

## ⚙️ New high-performance implementation of aw-server written in Rust

While Python is a great language to quickly build new features in, it's not great for performance or deploying to multiple platforms (especially Android). So @johan-bjareholt took on the tremendous task of reimplementing aw-server in the highly performant and secure programming language Rust. 

This is big news for several reasons:

 - Since Rust compiles to Android we have built a library for use on Android, letting us avoid reimplement all of ActivityWatch to Android devices specifically (and vastly decreases the time to port future features like sync to Android).
 - The high-performance improves battery life on devices like laptops, phones, and tablets.
 - The high-performance will make it easier for us to implement weekly summaries
 - Having two implementations gives us better testing and encourages work towards common specifications and standards.

The Python implementation will still be used for experimenting with new features, but expect the Rust implementation to be shipped with the normal desktop releases sometime in the future!

## ✏️ More editor watchers

The community has contributed with many new editor watchers the past few months which we appreciate a lot! They have done some awesome work and most of them are even in a better state than the vim watcher we have written ourselves. Thanks everyone for the awesome work!

* [aw-watcher-vscode](https://github.com/ActivityWatch/aw-watcher-vscode) - Visual Studio Code extension, by [@Otto-AA](https://github.com/Otto-AA).
* [activity-watch-mode](https://github.com/pauldub/activity-watch-mode) - emacs mode forked from wakatime-mode, by [@pauldub](https://github.com/pauldub).
* [aw-watcher-jetbrains](https://github.com/OlivierMary/aw-watcher-jetbrains) - JetBrains IntelliJ plugin, by [@OlivierMary](https://github.com/OlivierMary).
* (Alpha) [ActivityWatchVS](https://github.com/LaggAt/ActivityWatchVS) - Visual Studio plugin, by [@LaggAt](https://github.com/LaggAt)

## 🔧  Windows and macOS builds now work again
In v0.8 beta 7 we had issues with the windows bundle due to breaking updates of our dependencies PyInstaller and jsonschema. This is now fixed and our windows builds should now work properly again in v0.8 beta 8.

Back in 0.8 beta 6 macOS support was also broken, but that has been working for a while now since beta 7 which has been around for a few months already.

 ## 📦 Import and export
The import and export APIs now work consistently ([aw-server#41](https://github.com/ActivityWatch/aw-server/pull/41)). We have added a UI to export all buckets and to import buckets. Migrating your activitywatch data to another computer is now as easy as using one export button on one computer, moving the file to your new computer and upload it in with the import button! Import and export can also be used if you want to try out the new aw-server-rust and want to move over all your previously logged aw-server data.


# 🏃‍♀️ Going forward

 - 🛰️ Raw SQL datastore
    - @johan-bjareholt has merged a raw SQLite implementation of the datastore that has performance improvements compared to the current Peewee SQLite datastore. Automatic migration from the old datastore to the new one is supported. The new datastore is however not the default yet, we need more user-testing before doing that. ([aw-core#57](https://github.com/ActivityWatch/aw-core/pull/57))
 - 🔄 Decentralized sync
   - Still being worked on, see last developer update for more info and the [latest comments in the issue]().
 - ⏱️ Stopwatch beta
   - The web-ui now has a stopwatch watcher where you can manually set timers with different tags to track for example how long you have been at work, how long you have been working on a specific project or whatever else you can come up with it being useful for.
   - It's is very limited and lacks some important features, such as manually editing start/stop times. There is also a lack of visualization, it currently only shows a list of the individual entries.
  - 🖥️ Wayland support
    - @johan-bjareholt has had discussions with a few wayland compositor devs and have tried to convince the xdg-desktop-portal API bundle to add a protocol for exposing focused windows appname and title, [but it's a hard sell unfortunately...](https://github.com/flatpak/xdg-desktop-portal/issues/304)
  - 🗓️ Weekly summary view
    - Weekly/monthly/yearly summaries is a highly requested feature and a high priority for us. We have acceptable performance in aw-server to support weekly summaries, and when we switch over to aw-server-rust we hope to be able to support monthly summaries without issues. Summaries longer than a month will need more work though and won't be supported in the near future.
  - 🤖 Better Android version
    - The Android app, while technically released, isn't "production ready" yet. We would ❤️ contributions from people with some Android development experience!

# Support us! ❤️ 💸

Last month we **only received *$26* in donations**, that means your donation could be extra important to us. **Do you use ActivityWatch and want to see many updates like this in the future?  Please support us with donations, it really does make a difference!**
All donation methods are listed on our [donations page](https://activitywatch.net/donate/).

# 📧 Stay up to date

Want to get notified when we have more amazing news to share? Sign up on the forum, [subscribe to the newsletter](http://eepurl.com/cTU6QX), and [follow us on Twitter](https://twitter.com/ActivityWatchIt)!

---

> This post was originally published on [the forum](https://forum.activitywatch.net/t/development-update-march-2019/189). It has been reposted here on the blog for archival purposes.
