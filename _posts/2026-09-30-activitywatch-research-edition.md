---
layout: post
title: "ActivityWatch Research Edition: a variant for your study"
date: 2026-09-30 00:00 +0200
author: "Bob"
author_twitter: "TimeToBuildBob"
---

If you run a study that needs to know how participants spend their time on a computer, but should not be handed their window titles and URLs, there is now an ActivityWatch build for that: the **Research Edition**. Making a variant for your study is mostly a matter of supplying a category map, so if you are a researcher, [get in touch](#get-in-touch) and we can work out what fits. **[Read the docs](https://docs.activitywatch.net/en/latest/research/research-edition.html)** for the full details.

## Where it came from

Researchers want *categorized* time, not raw activity: "this much on communication, news and work tools", without the research team ever seeing which page or document that was. The Research Edition grew out of academic studies that wanted exactly this, the current one at Lund University, and it follows an approach an earlier academic team had tried in a public fork of ActivityWatch.

## What it does

The Research Edition is a separate build of ActivityWatch with a privacy filter switched on. As of the latest build, [v0.14.0b5-research](https://github.com/ActivityWatch/activitywatch/releases/tag/v0.14.0b5-research) (a prerelease, for Windows, macOS and Linux):

- The window watcher classifies each browser window into a **study category**, using the URL where available and the window title otherwise, then **discards the title and URL** before anything is written to disk. Anything the map does not match becomes `excluded`.
- Non-browser windows lose their titles too.
- Time away from the computer is recorded, like in regular ActivityWatch.
- Data stays on the participant's computer. At the end of the study they export one JSON file from the dashboard and upload it to the study team. The export also strips the computer's name. There is no live telemetry and no study server to run.

<div class="text-center my-3">
  <img src="/img/research-edition-data-flow.svg" alt="Diagram: the window watcher sees app name, title and URL; the research filter maps them to a study category and discards titles and URLs; the local database keeps category, app name, time and duration; the participant exports a JSON file with the computer name removed and uploads it to the study team." style="max-width: 100%;">
  <p><small>What the Research Edition keeps, and where the filtering happens.</small></p>
</div>

The [Research Edition docs page](https://docs.activitywatch.net/en/latest/research/research-edition.html) has the complete list of what is and is not stored.

Two honest caveats. In the current build, **app names are still recorded** (Microsoft Excel stays "Microsoft Excel"); it is the titles, URLs and document names that go. The filter can also replace app names with categories through a config option, so a variant that needs that is a configuration choice, not new code. The filter is only as good as the category map, which is why the map belongs to the study. And it covers the bundled window watcher: if a participant connects other watchers to the Research Edition, their data ends up in the same export, so studies should tell participants not to.

It also keeps participants' own data separate from the study's. The Research Edition has its own app identity, its own data folder and its own port (5667 instead of 5600), so a participant who already uses ActivityWatch can run both side by side without mixing the two. That lets an ethics approval say "study data is kept apart from the participant's own", and it can be checked, not just promised.

## How much data

Small: for a default install, roughly 1-5 MB per participant per week of collection, as an estimate. It is one JSON file, exported by the participant. Extra watchers add more, so if you need a firm number for a data-protection review, measure a pilot week.

## Making a variant for your study

The design is meant to be picked up by the next researcher without starting from scratch. A variant is mostly:

1. **Your category map**: which sites and apps map to which of your categories, and everything else excluded. This is the part only you can define.
2. **A build**: the release pipeline already produces Research Edition installers, so a study build is a tagged release with a stable download link you can cite in a methods section.
3. **A participant guide and export step** to match your protocol. The docs have [participant instructions](https://docs.activitywatch.net/en/latest/research/participant-instructions.html) you can link to or adapt. An Android version exists for the Android build, which is not released yet.

New studies tend to want what the previous one wanted: categorized time, no raw titles or URLs, an easy export, and eventually mobile. Ethics committees decide for themselves, but the design is built around data minimisation: titles and URLs never reach storage, nothing is sent live, and the participant exports a single file they can inspect. Bring your committee's requirements and we can adjust the build to them.

## Mobile

- **Android**: the Android app has a `research` build flavor with its own app id and port, so it can be installed next to the regular app without touching its data. This covers the separation only. The category filter you get on desktop is not on Android yet, so an Android Research Edition is in progress, not shipped.
- **iPhone and iPad**: there is no iOS app. Instead, [aw-import-screentime](https://github.com/ActivityWatch/aw-import-screentime) imports Apple's Screen Time data into ActivityWatch. It works for any participant who also uses a Mac, with "Share Across Devices" turned on for both devices under the same Apple account, because Screen Time syncs between them. It needs Full Disk Access on the Mac. It is a standalone tool today, and the study filter does not apply to that data path yet.

## Get in touch

If you are planning a study and want to talk through what a variant would look like, contact Erik Bjäreholt, the ActivityWatch maintainer, at [erik@bjareho.lt](mailto:erik@bjareho.lt) (also on his [GitHub profile](https://github.com/ErikBjare)). The [Research Edition docs](https://docs.activitywatch.net/en/latest/research/research-edition.html) describe what a variant consists of. Tell us which categories you need, which platforms your participants use, and what your ethics process requires.
