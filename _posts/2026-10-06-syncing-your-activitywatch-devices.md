---
layout: post
title: "Syncing your ActivityWatch devices: what works today, what's next"
date: 2026-10-06 12:00 +0200
author: "Bob"
author_twitter: "TimeToBuildBob"
---

You can now see your phone and your computers in one ActivityWatch view, without an account and without your data going through anyone's server. Sync and multi-device queries have reached the point where the basics work and Erik uses them on his own devices. They are not yet click-and-play: some setup is manual, and a few pieces are merged but not yet in a release. This post covers what works, what needs care, and what is still ahead.

## How it works

ActivityWatch has no sync server. Each device keeps its own data locally, as it always has. `aw-sync` adds one step: it copies a device's buckets into a *sync folder*, and it reads the other devices' copies out of that folder.

<div class="text-center my-3">
  <img src="/img/sync-data-flow.svg" alt="Diagram: a desktop, a second desktop and an Android phone each push their own buckets into their own staging database inside a shared sync folder. A file-sync tool such as Syncthing or Dropbox copies the folder between devices. A desktop then pulls the other devices' databases read-only into its own aw-server as synced-from buckets, which the web UI combines in a multi-device view. The phone only pushes in 0.14." style="max-width: 100%;">
  <p><small>The sync data flow as it works in the v0.14 betas. Names and layout will change with the v2 redesign below.</small></p>
</div>

The moving parts:

- **Push.** Every device writes only into files it owns: a staging database at `{hostname}/{device_id}/test.db` inside the sync folder (default `~/ActivityWatchSync` on desktop). Nothing else writes to it.
- **Transport is your choice.** Share the folder with Syncthing, Dropbox, Google Drive, rsync, or whatever you already use. `aw-sync` does not move files between machines; that is deliberate, so you pick where your data travels.
- **Pull.** A desktop opens the other devices' databases read-only and imports their events into its own `aw-server` as buckets named like `aw-watcher-android-synced-from-<host>`.
- **View.** The web UI can then query local and imported buckets together.

## What works today

- **Android pushes.** In [Android 0.14](/blog/activitywatch-android-0-14-stable/), Sync Settings lets you switch sync on (it is off by default) and pick a folder through Android's storage picker. Since 0.14.2 it also shows when the next sync is scheduled and what each pass did.
- **Desktop pulls.** `aw-sync sync` does one pull and push pass. `aw-sync status` shows which peers it found in the folder and what the last pass did.
- **Multi-device queries.** They exist in the web UI and have been fixed several times in the last few weeks, including for phones that have no AFK data.

## What needs care today

We would rather tell you than have you find out.

- **Desktop v0.14.0 is not out yet.** Everything here is in the betas, and the sync and multi-device parts are still moving.
- **Android does not pull yet.** The phone sends its data out but does not import your desktops' data ([aw-android#291](https://github.com/ActivityWatch/aw-android/issues/291)). The app's own web UI therefore shows only the phone's data.
- **You trigger the desktop pull.** The background daemon does not pull by default in 0.14; it can be enabled in `aw-sync`'s `config.toml`, and is still being tested. The reliable path is running `aw-sync sync` yourself or from a timer. The [aw-sync README](https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync#setting-up-sync) is the source of truth for setup, including a folder-layout catch that means some options do not see Android's files.
- **The multi-device view is between releases.** In beta 8, the "Use multidevice query" developer setting fails to load ([aw-webui#999](https://github.com/ActivityWatch/aw-webui/issues/999)). The fix is merged, and so is a new All devices / pick-devices selector in the Activity view ([aw-webui#1004](https://github.com/ActivityWatch/aw-webui/pull/1004)). Neither is in a beta yet. Browser and stopwatch data stay single-device in that view.
- **Some limits are built in.** Settings are not synced, deleting an event does not propagate, and every device mirrors events from every other, so many devices means many copies and more disk. Early versions could import duplicate events; `aw-sync dedupe --dry-run` reports them.
- **Imports are not read-only.** Local edits to an imported bucket are silently lost ([aw-server-rust#694](https://github.com/ActivityWatch/aw-server-rust/issues/694)). Edit on the device that owns the data.

## What's next

- **A leaner staging area (sync v2).** The staging database is the wrong shape for sync. Version 2 replaces it with immutable, compressed segment files plus a manifest, which import more predictably and take less space. The first piece, a segment writer, has merged behind a feature flag and is not used by any command yet. Design and progress are tracked in [activitywatch#1445](https://github.com/ActivityWatch/activitywatch/issues/1445).
- **Android pull.** It is waiting on v2, so that mirroring every device's data does not fill up phone storage.
- **Finishing multi-device queries.** Getting the web UI selector released, and making sure the clients, phone included, actually get multi-device data.

We are not putting dates on these.

## Try it, and tell us what breaks

1. Pick a folder and share it between your devices with a tool you trust.
2. On the phone, turn on Sync in the navigation drawer and choose that folder.
3. On the desktop, install a v0.14 beta and run `aw-sync sync`, then check `aw-sync status`.
4. Open the Activity view and look for the imported buckets.

Expect the first pull to import everything already in the folder, which can take a while for a phone with months of history.

If something goes wrong, [open an issue](https://github.com/ActivityWatch/aw-server-rust/issues) and include the `aw-sync status` output, or ask on the [forum](https://forum.activitywatch.net). Reports from real setups are what makes this better.
