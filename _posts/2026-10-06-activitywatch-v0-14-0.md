---
layout: post
title: "ActivityWatch v0.14.0: faster, steadier, synced, and a new app"
date: 2026-10-06 12:00 +0200
author: "Erik Bjäreholt"
author_twitter: "ErikBjare"
---

ActivityWatch v0.14.0 is out. It's been almost two years since v0.13.2, and it's the biggest release in a long time: about 1,000 changes across 13 repositories, from 32 contributors, tested over eight betas.

The short version: it's much faster once you have years of data, a lot steadier, your devices can finally share their data with each other, the Android app has caught up, and there's a new desktop app built with Tauri. The longer version is below.

**[Download v0.14.0](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.14.0)** · [Full changelog](https://docs.activitywatch.net/en/latest/changelog.html#v0-14-0)

## Your devices, together

Multi-device support is the most-requested feature in our user survey (1,714 responses). You use a laptop, a desktop and a phone, and you want one picture of your time, not three.

v0.14.0 is the release where that comes together. Sync is **local-first**: there is no ActivityWatch server and no account. aw-sync copies each device's data into a folder, and you move that folder between devices with whatever you already trust: Syncthing, Dropbox, a network drive. Your data never touches a server of ours. Each device only ever writes its own files and opens the others read-only, so one device can't corrupt another's data.

Once your devices are syncing, the Activity view can show any set of them merged into one view: your desktop and laptop together, or everything including your phone. Pick the devices in the device selector.

We spent the last weeks of this cycle running sync on our own machines and phones and fixing what broke: duplicate events after a resume, one bad device aborting a whole sync, phone data not being picked up, and an `aw-sync status` command that now tells you what each device has synced.

It's honest to say it's still rough. Every device keeps a full copy of every other device's data, so it uses more disk than it should. Settings and deletions don't sync. Setup is manual, and sync isn't started for you: turn it on in the app's modules menu, or run `aw-sync`. A much more compact format is already in the works, and making multi-device simple is the main goal for the next releases. If you run ActivityWatch on more than one device, [try it](https://docs.activitywatch.net/en/latest/syncing.html) and tell us what you hit.

## Android caught up

Last month we released [ActivityWatch for Android 0.14](/blog/activitywatch-android-0-14-stable/), the first stable Android release since 2023. User-perceived crashes went from about 7.8% to under 1%, and it added alerts, a home-screen widget, Firefox and Chrome tracking, and CSV and JSON export.

It also ships the same sync as the desktop: pick a folder on your phone, sync it like any other, and your phone's time shows up next to your desktop's in the Activity view.

## Much faster on large databases

If you have used ActivityWatch for a few years, you have probably watched the dashboard get slower. We measured v0.13.2 against v0.14 on a real 9-year database (9.2 million events, 1.8 GB), with each version's own dashboard queries. The new dashboard loads long ranges one day at a time, so here are both servers on that same workload, a Year of daily queries:

| Year view, 365 daily queries | v0.13.2 | v0.14 first load | v0.14 repeat load |
|---|---:|---:|---:|
| Classic app (Python server) | 120 s | 41 s | **0.6 s** |
| Tauri app (Rust server) | 139 s | 32 s | **0.2 s** |

Loading day by day is also what lets the dashboard show progress, draw per-day charts, and cache days that are over, which is why coming back to a view is near instant. (v0.13.2 asked for a whole Year in one request instead: on the Python server that took two minutes and hit the 30-second timeout, on the Rust server 19 seconds.)

Under the hood there are new database indexes, SQLite's WAL mode, cached category rules (categorizing a year of window titles went from 53 seconds to 10) and exports that stream instead of loading everything into memory. Day, week and month views benefit too: they no longer time out on big databases.

## Steadier

ActivityWatch runs in the background all day, and when it breaks you lose time you can't get back. A lot of this release went into making that rarer:

- Watchers that crash now restart on their own, in both apps, with crash logs
- On macOS, the window watcher no longer crashes on unusual window titles, and a leak of up to ~359 MB of memory a day on busy machines is fixed
- Locking your screen now counts as AFK on macOS, gamepads count as activity on Linux, and a Windows bug after 49.7 days of uptime is gone
- A damaged database recovers on startup, and imports merge into existing data instead of failing
- The Python and Rust servers now give identical query results, checked by a new test suite

## A new app, built with Tauri

v0.14.0 ships a new desktop app, aw-tauri, alongside the classic one. It has the same features and is lighter: it has its own window, runs the Rust server inside the app, is smaller to download, supports Wayland on Linux out of the box, and updates itself on macOS and Linux. It's less battle-tested so far, so the classic app ships too and stays the default.

Brian, who built most of it, wrote about why and how: **[A lighter, faster ActivityWatch with Tauri](/blog/introducing-tauri/)**.

macOS builds of both apps are now signed and notarized for Apple Silicon and Intel, so they open without Gatekeeper workarounds, and browser URLs are tracked properly again.

## A refreshed web UI, and more control

- **Timeline:** swimlanes, filters for AFK time, categories and duration, and "merge by app" to calm down busy days
- **Custom date ranges**, and a Year view that is always available
- **Category sets:** keep several sets of categorization rules and switch between them, plus rule priorities
- A **Work Time report** and **billable hours** export by category
- A **privacy filter** that drops sensitive window titles before they ever reach the database
- An optional **API key** for the server, if you expose it beyond your own machine
- ActivityWatch now speaks **Swedish, German, Ukrainian, Russian and Chinese**
- Support for more browsers: Arc, Dia, Zen, Helium, Floorp and others

And for the AI crowd: one canonical query returns clean, categorized events, so an assistant can answer questions about your time without a custom integration.

## Upgrading

On the first start after upgrading, ActivityWatch updates its database indexes once. Your data isn't changed. On a large database it takes up to a minute, and the dashboard may not connect until it's done. Leave it running and reload. Notifications are now opt-in, so turn them back on in Settings if you used them.

## Thank you

32 people contributed to this release. Special thanks to [@0xbrayo](https://github.com/0xbrayo) for aw-tauri, [@2e3s](https://github.com/2e3s) for awatcher and native Wayland support, [@hawai-i](https://github.com/hawai-i) for bringing macOS browser URLs back, and [@NickWick13](https://github.com/NickWick13) for the Swedish translation.

ActivityWatch has no ads, no venture funding and no data business. If it is useful to you, [ActivityWatch Pro](/go/?src=blog), our patronage subscription, is the most direct way to keep releases like this coming. It starts at $5 a month and unlocks nothing: everything stays free.
