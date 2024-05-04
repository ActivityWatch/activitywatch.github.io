---
layout: post
title: Tauri the future of ActivityWatch
date: 2024-5-5 16:35 +0300
author: "Brian Vuku"
author_twitter: "subrupt"
---

We're excited to introduce a new initiative [`aw-tauri`](http://github.com/ActivityWatch/aw-tauri), which is a lighter, faster cross-platform repackaging of ActivityWatch. As the name implies the project is built with [Tauri](https://tauri.app), a relatively new Rust-based toolkit that enables easy development of small, fast, and secure applications with a great developer experience.

## Why Tauri

Tauri apps are lightweight, memory efficient and secure by design. Tauri does not ship a renderer but uses the platform native renderer via webviews. This simple design choice makes the app size compact and memory efficient during runtime, as compared to electron apps. Tauri apps are secure, only interacting with the host systems through tauri apis. Security is a top priority for Tauri, and so it is for ActivityWatch.

## Developer Experience

Aw-tauri is built with the [rust server](https://github.com/ActivityWatch/aw-server-rust) serving the backend and a UI written in Vue. It takes almost no time to get upto speed with the project!

Cross platform development before tauri was a hassle. Binaries had to be built and tested for each target platform separately. Tauri greatly simplifies this.

Tauri enables us to generate releases from the same codebase with a single command. It handles everything platform specific: on Linux you get a lightweight `.AppImage`, on windows a `.msi` installer, and `.app` on macOS. It just works!

## User Experience

Aw-Tauri aims to consolidate most of the functionality that is offered by additional code by other repos. It integrates the window and afk watchers natively. It offers support of notifications by default via [aw-notify](https://github.com/ActivityWatch/aw-notify). It houses its own webview, no need to visit ```http://localhost:5600``` anymore. Watchers can be started and stopped right from the trayicon. Updates can be pushed seemlessly across platforms provided by tauri's update system! [Aw-sync](https://github.com/ActivityWatch/aw-sync) which is still in active development will be integrated into the app. Syncing data across devices will be just as seemless. We will work closely with the user community to make a product that we all love to use.

## Conclusion

`aw-tauri` is still in active development and contributions are welcome and encouraged! More eyes on the code will be beneficial to the project.

We are hopeful that it will help solve many of our outstanding challenges, and are excited to see it shape the future of ActivityWatch.
