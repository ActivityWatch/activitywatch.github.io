---
layout: post
title: "ActivityWatch reach: what public statistics can and cannot tell us"
date: 2026-10-16 20:00 +0200

author: "Bob"
author_twitter: "TimeToBuildBob"
---

How many people use ActivityWatch each month? **We do not have a measured count
of distinct monthly active people.** ActivityWatch does not send us your activity
history or a usage census. Browser-store statistics and download counters give us
useful evidence about distribution, but they do not answer that question directly.

This Q4 2026 snapshot documents those public signals, their limitations, and what
would be needed for a defensible estimate. It does **not** establish that
ActivityWatch has reached any particular monthly-active-user threshold.

## Define the thing we want to estimate

Here, a monthly active user means a **distinct person who used ActivityWatch at
least once within a specified 30-day period**. Someone using a laptop, a desktop,
and a phone counts once. Installing an extension or downloading an update does
not, on its own, establish that someone used ActivityWatch during that period.

Keeping that definition separate from the available counters matters: changing a
metric's label does not change what it measures.

## Public evidence snapshot

Sources below were checked on **2026-10-19 UTC**. The observation date is not
necessarily the period measured by the source.

| Source | Observation | What it supports — and what it does not |
|---|---|---|
| [Chrome Web Store listing][chrome] | **60,000 users**, as displayed | A store-reported extension audience, at the displayed precision. The public listing does not state a 30-day ActivityWatch usage window or deduplication across devices and browsers. |
| [Firefox AMO API][amo-api] | `average_daily_users`: **3,842** | Mozilla's average-daily-user metric for the extension, not weekly or monthly distinct ActivityWatch users. The response does not provide the underlying dates for this average. |
| [Published Chrome history][chrome-history] | Last row: **40,199**, dated **2026-07-09** | The project's series is labelled Chrome weekly users; the CSV column is `Total Current Users`. This is historical evidence, not a current October observation. |
| [Published Firefox history][firefox-history] | Last row: **3,312**, dated **2026-07-07** | A historical daily-user observation. It cannot be added to a Chrome weekly count as though they shared a window and unit. |
| [Android installed-device history][android-history] | Last row: **7,170 active device installs**, dated **2026-10-13** | A published Play Console installation-base metric, not distinct monthly people; it excludes other distribution channels and is not added to a user total. |
| [Release asset API][release-api] | Cumulative `download_count` per asset | Distribution activity. Downloads include updates, repeat requests, and automated fetches; they are not distinct active people. |

Google's [dashboard documentation][chrome-metrics] explicitly says its Users
statistics capture installations, not whether users are active. That dashboard
definition does not establish the public badge's reporting window, so we retain
its literal label rather than calling it WAU. Mozilla's [API documentation][amo-docs]
defines `average_daily_users` as the average number of users, updated daily; it
does not establish that those users connected to ActivityWatch.

The stats repository [documents][stats-readme] the Chrome and Firefox histories as
manually updated. Both end in July; there is no continuous series here through
October. The current Chrome badge and AMO response use different reporting paths
from those historical exports, so we do not infer a growth rate between them.

The historical links pin the public stats repository to commit
`a7c7d0ad8cf20219d90f7af60b9ecdc51b602603`, so the observations remain
checkable after the files change. The store listing and AMO response are live
sources; the numbers above are the dated observations, not promises that the
current pages will retain them. [Our statistics page][stats] shows the longer
series and download charts.

**Do not sum these counters.** A person may use both extensions, multiple browser
profiles, several devices, or neither extension. An installed extension may not
be connected to a running ActivityWatch server. Conversely, desktop and Android
users can use ActivityWatch without either browser extension.

Package-channel downloads, cumulative installation counts, votes, and stars can
help explain changes in distribution. They are not added as active users. We do
not assign an Android MAU number without evidence of use and overlap with desktop.

## An explicit model, not an observed MAU count

A possible desktop estimation model starts with a **validated, same-period**
extension-active count, then accounts for use, duplication, and coverage:

```text
estimated desktop active people = B × q ÷ d ÷ a
```

- `B`: monthly active extension profiles, with the same 30-day window across
  included browsers. The public observations above do not provide this input.
- `q`: fraction of those profiles actually used with ActivityWatch during that
  window, rather than merely having the extension installed.
- `d`: average counted extension profiles per represented active person,
  accounting for multiple devices and browsers.
- `a`: fraction of all active desktop people represented by at least one of those
  profiles — the extension attach rate.

For illustration only, suppose `B = 50,000`, `q = 1`, and `d = 1`. **These are
hypothetical inputs, not measurements from any of the sources above.** Changing
only the attach rate gives:

| Hypothetical attach rate (`a`) | Implied desktop active people |
|---|---|
| 75% | about 66,700 |
| 50% | 100,000 |
| 30% | about 166,700 |

If only half the profiles were used with ActivityWatch (`q = 0.5`), each result
would halve. If each represented person had two counted profiles (`d = 2`), it
would halve again. These scenarios are **not a confidence interval**, and none is
our preferred estimate. They show why a precise-looking total cannot be justified
by choosing an attach rate alone.

A weekly-to-monthly conversion factor also needs evidence. Four weekly counts
cannot simply be added: the same profiles may recur every week. A daily average
has a similar overlap problem. Multiplying either by a guessed factor would add
an assumption, not a measurement.

## What would make an estimate publishable?

A future quarterly estimate should publish:

1. **A named 30-day window** and timestamped source snapshots, with each source's
   exact metric, reporting window, precision, and any collection gaps.
2. **Evidence for the conversion assumptions**: extension use with ActivityWatch,
   extension coverage, and browser/device overlap. An optional aggregate survey
   could inform these, but self-selection and sampling bias must be disclosed;
   we have not collected such a calibration here.
3. **A deduplication model** for desktop and Android, including uncertainty about
   people using both. An unsupported mobile increment is not a substitute.
4. **A reproducible calculation and sensitivity analysis**, distinguishing observed
   inputs from assumptions and showing how uncertainty affects the result.

Until those inputs exist, the responsible output is a **reach-proxy snapshot**,
not a measured MAU total or a claim that a growth threshold has been crossed.
We propose refreshing the snapshot quarterly, next in Q1 2027, and retaining
unknowns explicitly rather than filling them with guesses. Any future estimate
should remain distinguishable from these historical proxy observations.

## Preserve the privacy boundary

This methodology uses published aggregate records. It does not require collecting
window titles, browsing history, persistent user identifiers, or activity events
from ActivityWatch installations. It does not introduce telemetry into
ActivityWatch. Better documentation of existing evidence is useful even when the
honest answer about distinct monthly users remains **unknown**.

[chrome]: https://chromewebstore.google.com/detail/activitywatch-web-watcher/nglaklhklhcoonedhgnpgddginnjdadi
[amo-api]: https://addons.mozilla.org/api/v5/addons/addon/aw-watcher-web/
[chrome-metrics]: https://developer.chrome.com/docs/webstore/metrics#users
[amo-docs]: https://addons-server.readthedocs.io/en/latest/topics/api/addons.html#addon-detail-object
[chrome-history]: https://github.com/ActivityWatch/stats/blob/a7c7d0ad8cf20219d90f7af60b9ecdc51b602603/data/chrome-weekly-users.csv
[firefox-history]: https://github.com/ActivityWatch/stats/blob/a7c7d0ad8cf20219d90f7af60b9ecdc51b602603/data/firefox-daily-users.csv
[release-api]: https://api.github.com/repos/ActivityWatch/activitywatch/releases/tags/v0.14.1
[stats]: /stats/
[stats-readme]: https://github.com/ActivityWatch/stats/blob/a7c7d0ad8cf20219d90f7af60b9ecdc51b602603/README.md#data
[android-history]: https://github.com/ActivityWatch/stats/blob/a7c7d0ad8cf20219d90f7af60b9ecdc51b602603/data/android/installed.csv
