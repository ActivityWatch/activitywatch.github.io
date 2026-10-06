---
layout: post
title: "ActivityWatch v0.14.0: faster, more reliable, and a new app"
date: 2026-10-06 12:00 +0200
author: "Erik Bjäreholt"
author_twitter: "ErikBjare"
---

ActivityWatch v0.14.0 is out. It's the first stable desktop release since v0.13.2, and the biggest one in years: about 1,000 changes across 13 repositories, from dozens of contributors.

If you have used ActivityWatch for a few years, you have probably noticed the Year view getting slower, or giving up entirely. That is the first thing this release fixes. The rest is a long list of reliability work, a refreshed web UI, and a new app built with Tauri.

**[Download v0.14.0](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.14.0)** · [Full changelog](https://docs.activitywatch.net/en/latest/changelog.html#v0-14-0)

## Much faster on large databases

We measured v0.13.2 against v0.14 on a real 9-year database (9.2 million events, 1.8 GB), using the queries each version's dashboard actually sends.

| Year view | v0.13.2 | v0.14, first load | v0.14, repeat load |
|---|---:|---:|---:|
| Classic build | 120 s (times out) | 41 s | **0.6 s** |
| Tauri build | 19 s | 32 s | **0.2 s** |

The dashboard now loads long ranges one day at a time and caches days that are over, so the first load shows progress instead of hitting the 30-second timeout, and opening the Year view again is close to instant. All time works too, even across nine years: about 1.5 minutes on the Tauri build and 3 minutes on the classic one the first time.

Under the hood there are new database indexes, SQLite's WAL mode, cached category rules (categorizing a year of window titles went from 53 seconds to 10), and exports that stream instead of loading everything into memory.

## More reliable

ActivityWatch runs in the background all day, so when something breaks, you lose data you can't get back. A lot of this release went into making that rarer:

- Watchers that crash now restart on their own, in both apps
- On macOS, the window watcher no longer crashes on unusual window titles, and a leak of up to ~359 MB of memory a day on busy machines is fixed
- Locking your screen now counts as AFK on macOS, gamepads count as activity on Linux, and a Windows bug after 49.7 days of uptime is gone
- A damaged database recovers on startup, and imports merge into existing data instead of failing
- The Python and Rust servers now give identical query results, checked by a new test suite

## A refreshed web UI

- **Multiple devices in the Activity view:** pick all of your devices, or a few, and see them merged
- **Custom date ranges**, and a Year view that is always available
- **Timeline filters** for AFK time, categories and duration, plus "merge by app" to calm down busy days
- **Category sets:** keep several sets of categorization rules and switch between them
- A **privacy filter editor**, a Work Time report, and CSV export that handles large buckets
- Six languages: English, Swedish, German, Ukrainian, Russian and Simplified Chinese

## A new app, built with Tauri

v0.14.0 ships a new desktop app, aw-tauri, alongside the classic one. It has its own window, runs the Rust server inside the app, is smaller to download, supports Wayland on Linux out of the box, and can update itself on macOS and Linux. It's still a preview: the classic build stays fully supported while we gather feedback.

Brian wrote about why we built it and how it works: **[A lighter, faster ActivityWatch with Tauri](/blog/introducing-tauri/)**.

macOS builds of both apps are now signed and notarized, so they open without Gatekeeper workarounds.

## Before you upgrade

Back up your data first. On the first start after upgrading, ActivityWatch updates its database indexes once. On a large database that takes a minute or so, and the dashboard may say it can't connect until it's done. Leave it running, wait, and reload.

## What's next

Proper multi-device support: sync, merged queries across devices, and all-time views that span devices and years. An early sync preview is included in v0.14.0 for the adventurous. It's opt-in, and not a finished feature yet. That is where the next releases are headed.

## Supporting ActivityWatch

ActivityWatch has no ads, no venture funding and no data business. If it is useful to you, [ActivityWatch Pro](/go/?src=blog), our patronage subscription, is the most direct way to keep releases like this coming. It starts at $5 a month and unlocks nothing: everything stays free.

Thanks to everyone who contributed code, reported bugs and tested the betas.
