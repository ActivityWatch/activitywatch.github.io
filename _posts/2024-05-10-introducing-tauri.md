---
layout: post
title: Tauri the future of ActivityWatch
date: 2024-5-10 16:35 +0300
author: "Brian Vuku"
author_twitter: "subrupt"
---

We're excited to introduce a new initiative [`aw-tauri`](http://github.com/ActivityWatch/aw-tauri), which is a lighter, faster cross-platform repackaging of ActivityWatch. As the name implies the project is built with [Tauri](https://tauri.app), a relatively new Rust-based toolkit that enables easy development of small, fast, and secure applications with a great developer experience.

## Why Tauri

Tauri apps are lightweight, memory efficient and secure by design. Tauri does not ship a renderer but uses the platform native renderer via webviews. This simple design choice makes the app size compact and memory efficient during runtime, as compared to electron apps. Tauri apps are secure, only interacting with the host systems through tauri apis. Security is a top priority for Tauri, and so it is for ActivityWatch.

## Developer Experience

`aw-tauri` is built with [aw-server-rust](https://github.com/ActivityWatch/aw-server-rust) serving the backend together with [aw-webui](https://github.com/ActivityWatch/aw-webui). We have taken care to keep the codebase lean and clean, such that it takes very little time to get acquainted with the codebase.

In our current build process, we rely heavily on PyInstaller for building the modules written in Python. This has been an enduring source of problems, and many developer weeks (if not months) have been spent trying to work out all the issues over the years (especially macOS support, because of the need to codesign a very messy `.app` bundle).

With Tauri, they have handled most of the heavy lifting, and make it easy to produce working binaries for all target platforms. Much of this is simply due to Rust (avoids PyInstaller), but the added tooling for codesigning and producing suitable bundles for each platform: on Linux you get a lightweight `.AppImage`, on windows a `.msi` installer, and `.app` on macOS.

## User Experience

`aw-tauri` aims to consolidate much of the functionality that is currently implemented in [`aw-qt`](https://github.com/ActivityWatch/aw-qt), [`aw-server-rust`](https://github.com/ActivityWatch/aw-server-rust), and [`aw-notify`](https://github.com/ActivityWatch/aw-notify).

- It houses its own webview, no need to visit `http://localhost:5600` in your browser anymore.
- Watchers can be started and stopped right from the trayicon, just like in `aw-qt`.
- Updates can be pushed seemlessly across platforms provided by tauri's update system!
- [aw-sync](https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync), which is still in active development, will be integrated into the app. Syncing data across devices will be just as seamless.

These are only the first steps to getting aw-tauri usable, but most of all it serves as a stable foundation enabling many improvements down the line.

## Conclusion

`aw-tauri` is still in active development, contributions are welcome and encouraged!

Check out the [README](https://github.com/ActivityWatch/aw-tauri/blob/master/README.md) to see the status of development, and where you can help out.

We are hopeful that it will help solve many of our remaining challenges, and are excited to see it help shape the future of ActivityWatch.
