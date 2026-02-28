---
layout: post
title: "ActivityWatch vs RescueTime: Why I Built a Free Open-Source Alternative"
date: 2026-02-28 12:00 +0100
author: "Erik Bjäreholt"
author_twitter: "ErikBjare"
toc: true
---

## The Story Behind ActivityWatch

I started building ActivityWatch because I was frustrated with RescueTime. As someone who wanted to understand how I spent my time on the computer, I had been a RescueTime user for years. But over time, the problems kept piling up:

- **My data wasn't mine.** RescueTime stores everything on their servers. I had no way to self-host or keep my data local. For something as personal as a complete log of everything I do on my computer, that felt wrong.
- **It wasn't open source.** When I found bugs — like Xbox controller input being tracked incorrectly — I couldn't fix them myself. I filed reports, but they went nowhere.
- **Linux support was an afterthought.** As a Linux user, I was a second-class citizen. The Linux client was always behind, and eventually RescueTime [dropped Linux support entirely](https://blog.rescuetime.com/linux-update-2024/).
- **"Pay or lose your history."** The free tier only showed the last 3 months. Want to see your all-time data? Pay up. It felt like they were holding my own data hostage.
- **No extensibility.** I couldn't add custom watchers, build integrations, or extend the tracking in any meaningful way. What you got was what you got.

So I built ActivityWatch — a free, open-source, privacy-first time tracker that keeps your data on your device and lets you extend it however you want.

## Feature Comparison

Here's how ActivityWatch compares to RescueTime in 2026:

| Feature | ActivityWatch | RescueTime |
|---------|--------------|------------|
| **Price** | Free and open-source | $12/month (Premium) |
| **Data storage** | Local (your device) | Cloud (their servers) |
| **Linux support** | Full support | Discontinued |
| **Open source** | Yes (MPL-2.0) | No |
| **Custom watchers** | Yes — write your own | No |
| **Browser tracking** | Chrome, Firefox, Edge, Opera | Chrome, Firefox, Edge |
| **Offline tracking** | Yes | Limited |
| **API access** | Full local REST API | Limited API |
| **Self-hosting** | Built-in (it's local-first) | Not available |
| **Data export** | Full export anytime | Limited in free tier |
| **Distraction blocking** | Via third-party tools | Built-in (Premium) |
| **Team features** | Coming soon | Available (Premium) |
| **Mobile tracking** | Android | Android, iOS |

## Where ActivityWatch Wins

### Privacy and Data Ownership

This is the fundamental difference. ActivityWatch stores all your data locally on your device. No cloud accounts, no data uploads, no risk of a company going under and taking your data with it. You own your data, period.

### Extensibility

ActivityWatch has a modular architecture. The core is a local server that stores events from "watchers" — small programs that observe different things. You can write your own watchers for anything: IDE activity, music listening, exercise, or whatever you want to track.

The community has built watchers for:
- VS Code and JetBrains IDEs
- Spotify and media players
- VR headsets
- Custom hardware

### Cross-Platform (Including Linux)

ActivityWatch runs on Windows, macOS, and Linux. When RescueTime dropped Linux in 2024, many users switched to ActivityWatch. We're committed to supporting all major platforms — it's a core part of who we are.

### No Paywalls on Your Own Data

All your data is always accessible. There's no "upgrade to see your history" or "pay to unlock analytics." Every feature is available to every user.

## Where RescueTime Still Has an Edge

To be fair, RescueTime does some things well:

- **Built-in distraction blocking** — FocusTime lets you block distracting websites. ActivityWatch focuses on tracking; for blocking, you can use tools like [Cold Turkey](https://getcoldturkey.com/) or [LeechBlock](https://addons.mozilla.org/en-US/firefox/addon/leechblock-ng/).
- **Team management** — RescueTime has built-in team dashboards and management features. ActivityWatch is primarily designed for individuals (though team features are on our roadmap).
- **iOS support** — RescueTime has an iOS app. ActivityWatch currently only supports Android for mobile.
- **Polished onboarding** — RescueTime has a smoother out-of-box experience for non-technical users. We're actively working on improving our onboarding.

## Migrating from RescueTime

Switching to ActivityWatch is straightforward:

1. **Download ActivityWatch** from [activitywatch.net/downloads](https://activitywatch.net/downloads/)
2. **Install and run** — it starts tracking immediately
3. **Install the browser extension** for [Chrome](https://chrome.google.com/webstore/detail/activitywatch-web-watcher/nglaklhklhcoonedhgnpgddginnjdadi), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/aw-watcher-web/), or [Edge](https://microsoftedge.microsoft.com/addons/detail/activitywatch-web-watcher/nfabjmiphddfnpmmilgjkfnaakceocog)
4. **Check the dashboard** at [localhost:5600](http://localhost:5600) to see your data

Your RescueTime data can be exported and potentially imported — check our [documentation](https://docs.activitywatch.net) for details on data import options.

## What Users Say

People who switched from RescueTime consistently highlight:

> "I switched when RescueTime dropped Linux. ActivityWatch is better in every way — I can actually see all my data without paying."

> "As a developer, the extensibility is what sold me. I wrote a custom watcher for my terminal in an afternoon."

> "The privacy aspect is huge. I don't want a company having a complete log of everything I do on my computer."

## Try ActivityWatch

ActivityWatch is free, open-source, and takes about two minutes to set up. Download it at [activitywatch.net/downloads](https://activitywatch.net/downloads/) and see for yourself.

If you're coming from RescueTime, you'll find that ActivityWatch tracks everything RescueTime did — and more — while keeping your data private and giving you full control.

**Links:**
- [Download ActivityWatch](https://activitywatch.net/downloads/)
- [Documentation](https://docs.activitywatch.net)
- [GitHub](https://github.com/ActivityWatch/activitywatch)
- [General comparison of time trackers](/blog/comparing-time-trackers/)
