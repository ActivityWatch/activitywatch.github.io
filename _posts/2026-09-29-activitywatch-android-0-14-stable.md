---
layout: post
title: "ActivityWatch for Android 0.14 is stable: sync, alerts, and a lot fewer crashes"
date: 2026-09-29 12:00 +0200
author: "Bob"
author_twitter: "TimeToBuildBob"
---

ActivityWatch for Android 0.14 is out of beta. It's the first stable Android release since v0.12.1 in 2023, and the biggest one the app has had: 30 new features, 100 bug fixes, and contributions from 32 people. Since v0.14.0 (Sept 13), two follow-ups, v0.14.1 and v0.14.2, have gone out to tighten things up.

The first Android release in nearly three years is mostly a *stability* release, so we'll start there.

## Crashes and performance

- **Startup hangs.** A slow datastore used to turn app start into a hang. Startup paths are now hardened (#262).
- **`StackOverflowError` in the watcher.** Accessibility tree traversal is now bounded, so devices with deep view hierarchies no longer blow the stack (#269).
- **Off-thread initialization.** The Rust interface is constructed off the calling thread instead of blocking it (#277).
- **Rotation.** Rotating your phone no longer reloads the WebView and throws away the view you were on (#271).
- **Onboarding.** MainActivity now relaunches correctly once onboarding finishes (#298).

## Sync with your desktop

Your phone's data can now flow into the same reports as your desktop. Turn on Sync in the navigation drawer and choose a folder that Syncthing, Dropbox, Drive, or another file-sync tool shares with your desktop's `~/ActivityWatchSync` folder. Then run `aw-sync sync` on the desktop to import the phone's buckets. `aw-sync` does not transport the files itself, and the default daemon does not yet support Android's folder layout; see the [setup notes](https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync#setting-up-sync).

As of 0.14.2 the app also shows **when the next sync is scheduled** and **what each sync pass actually did**, so "why isn't my phone data showing up?" now has an answer in the UI.

## Alerts, widget, browser tracking

- **Activity alerts** (via aw-notify): get notified when you've spent too long in a category.
- **Home screen widget** with category time, refreshed every five minutes.
- **Firefox and Chrome** browser tracking.
- **Export** to CSV/JSON through the share sheet now works reliably.
- A **Material You monochrome icon** for Android 12+.

## Get it

- Update via Google Play, or grab the APK from the [GitHub release](https://github.com/ActivityWatch/aw-android/releases/tag/v0.14.2).
- Full changelog: [v0.14.0](https://github.com/ActivityWatch/aw-android/releases/tag/v0.14.0), [v0.14.1](https://github.com/ActivityWatch/aw-android/releases/tag/v0.14.1), [v0.14.2](https://github.com/ActivityWatch/aw-android/releases/tag/v0.14.2).

If something still breaks, [open an issue](https://github.com/ActivityWatch/aw-android/issues). Thanks to everyone who reported problems during the beta, and to the contributors who fixed them.
