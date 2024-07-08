---
layout: post
A lighter faster ActivityWatch with Tauri: now available for testing
date: 2024-5-13 16:35 +0300
author: "Brian Vuku"
author_twitter: "subrupt"
---

We're excited to introduce a new initiative [`aw-tauri`](http://github.com/ActivityWatch/aw-tauri), which is a lighter, faster cross-platform repackaging of ActivityWatch. As the name implies the project is built with [Tauri](https://tauri.app), a relatively new Rust-based toolkit that enables easy development of small, fast, and secure applications with a great developer experience.

## Why Tauri

Tauri apps are lightweight, memory efficient and secure by design. Tauri does not ship a renderer but uses the platform native renderer via WebViews. This simple design choice makes the app size compact and memory efficient during runtime, as compared to electron apps. Tauri apps are secure, only interacting with the host systems through Tauri APIs.

## User Experience

`aw-tauri` aims to replace the functionality that is currently implemented in [`aw-qt`](https://github.com/ActivityWatch/aw-qt) and [`aw-notify`](https://github.com/ActivityWatch/aw-notify). Creating a new Rust-powered entrypoint for running ActivityWatch and its modules. With [`aw-server-rust`](https://github.com/ActivityWatch/aw-server-rust) as the default server, it leads to a reliable and highly performant application. Reliability and performance is very important for apps like ActivityWatch, which always run in the background and collect data that is otherwise lost.

`aw-tauri` is designed to be a drop-in replacement for `aw-qt` and `aw-notify`, with the following improvements:

- It houses its own webview, no need to visit `http://localhost:5600` in your browser anymore.
- Watchers can be started and stopped right from the trayicon, just like in `aw-qt`.
- Updates can be pushed seemlessly across platforms provided by tauri's update system!
- [aw-sync](https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync), which is still in active development, will be integrated into the app. Syncing data across devices will be just as seamless.
- Autostart on boot, is built into the app, no need to set up systemd services for linux users.

This is just the beginning, it serves as the baseline for many more improvements to come.

## Developer Experience

`aw-tauri` is built with [aw-server-rust](https://github.com/ActivityWatch/aw-server-rust) serving the backend together with [aw-webui](https://github.com/ActivityWatch/aw-webui). We have taken care to keep the codebase lean and clean, such that it takes very little time to get acquainted with the codebase.

In our current build process for Python modules like `aw-qt`, we rely heavily on PyInstaller for building into binaries. This has been an enduring source of problems, and many developer weeks (if not months) have been spent trying to work out all the issues over the years (especially macOS support, because of the need to codesign a very messy `.app` bundle).

With Tauri, they have handled most of the heavy lifting, and make it easy to produce working binaries for all target platforms. Much of this is simply due to Rust (avoids PyInstaller and its complexity), but also the added tooling for codesigning, and producing suitable bundles for each platform: on Linux you get a lightweight `.AppImage`, on windows a `.msi` installer, and `.app` on macOS.

## Conclusion

`aw-tauri` is still in active development, contributions are welcome and encouraged!

Check out the [README](https://github.com/ActivityWatch/aw-tauri/blob/master/README.md) to see the status of development, and where you can help out.

We are hopeful that it will help solve many of our remaining challenges, and are excited to see it help shape the future of ActivityWatch.
