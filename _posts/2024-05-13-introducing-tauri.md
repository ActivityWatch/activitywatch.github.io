---
layout: post
title: "A lighter faster ActivityWatch with Tauri: now available for testing" 
# HOLD: placeholder date (far future so Jekyll will not publish it by accident).
# Publish only after ActivityWatch v0.14.0 stable is released, then set this to the real publish date/time.
date: 2099-12-31 12:00 +0200
author: "Brian Vuku"
author_twitter: "subrupt"
---

The upcoming ActivityWatch v0.14.0 ships a new desktop app: [`aw-tauri`](https://github.com/ActivityWatch/aw-tauri), a lighter, faster cross-platform repackaging of ActivityWatch. As the name implies the project is built with [Tauri](https://tauri.app), a relatively new Rust-based toolkit that enables easy development of small, fast, and secure applications with a great developer experience.

We first announced this work in 2024, when it was little more than a prototype. Since then it has grown into something you can install on Windows, macOS (Apple Silicon and Intel) and Linux, and the v0.14.0 betas include it for every one of those platforms. This post is the story so far: why we did it, what you get, and how you can try it today.

<div class="text-center my-3">
  <img src="/img/screenshots/screenshot-v0.14.0b8-aw-tauri-welcome.png" alt="The ActivityWatch dashboard (Welcome page, with Activity, Timeline and Stopwatch in the top bar) running inside the aw-tauri application window" style="max-width: 100%;" class="border">
  <p><small>The ActivityWatch dashboard inside aw-tauri's own window (v0.14.0b8, Linux; window decorations not shown). No browser tab needed.</small></p>
</div>

## Why Tauri

Tauri apps are lightweight, memory efficient and secure by design. Tauri does not ship a renderer but uses the platform native renderer via WebViews. This simple design choice makes the app size compact and memory efficient during runtime, as compared to electron apps. Tauri apps are secure, only interacting with the host systems through Tauri APIs.

That last part holds if you build an app the "Tauri way". ActivityWatch also runs an HTTP server (`aw-server-rust`, on `localhost:5600`), so we still have to take precautions to not expose sensitive information to other devices on the network or to websites, just like before.

## What you get

`aw-tauri` aims to replace the functionality that is currently implemented in [`aw-qt`](https://github.com/ActivityWatch/aw-qt) and [`aw-notify`](https://github.com/ActivityWatch/aw-notify). Creating a new Rust-powered entrypoint for running ActivityWatch and its modules. With [`aw-server-rust`](https://github.com/ActivityWatch/aw-server-rust) as the default server, it leads to a reliable and highly performant application. Reliability and performance is very important for apps like ActivityWatch, which always run in the background and collect data that is otherwise lost.

`aw-tauri` is designed to be a drop-in replacement for `aw-qt`, and the main application that appears as a tray icon and manages the server and the watchers:

- It houses its own webview, no need to visit `http://localhost:5600` in your browser anymore.
- Watchers can be started and stopped right from the tray icon, just like in `aw-qt`. Crashed modules are restarted automatically, with a backoff and a limit on retries.
- The server runs inside the app (`aw-server-rust`), so there is no separate server process to manage.
- Autostart on login is built into the app and can be toggled from the tray menu, no need to set up systemd services for Linux users.
- Notifications: [`aw-notify`](https://github.com/ActivityWatch/aw-notify-rs) has since been rewritten in Rust, and `aw-tauri` runs it and shows its output as native desktop notifications, enabling configurable usage notifications (such as goals or alerts).
- [aw-sync](https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync) is included in the bundles, but sync is still in preview: it is opt-in and not switched on by default.
- Tauri also offers an update system, which we are excited to use. It is wired up to GitHub Releases, but we are still verifying it, so for now you update by installing the new version.

The watchers themselves are still mostly the same ones as before: the Python `aw-watcher-afk` and `aw-watcher-window` for cross-platform compatibility. There is no cross-platform Rust watcher, yet. On Linux the bundle also includes [`awatcher`](https://github.com/2e3s/awatcher), a Rust watcher that covers window and AFK tracking on both X11 and Wayland, which is why the v0.14.0 release notes list native Wayland support for the Tauri build.

`aw-tauri` does not replace the classic `aw-qt` build in v0.14.0: both are published side by side, and the release notes still label the Tauri distribution as experimental. We would like to hear how it works for you before that changes.

## Developer Experience

`aw-tauri` is built with [aw-server-rust](https://github.com/ActivityWatch/aw-server-rust) serving the backend together with [aw-webui](https://github.com/ActivityWatch/aw-webui). We have taken care to keep the codebase lean and clean, such that it takes very little time to get acquainted with the codebase.

In our current build process for Python modules like `aw-qt`, we rely heavily on PyInstaller for building into binaries. This has been an enduring source of problems, and many developer weeks (if not months) have been spent trying to work out all the issues over the years (especially macOS support, because of the need to codesign a very messy `.app` bundle).

With Tauri, they have handled most of the heavy lifting, and make it easy to produce working binaries for all target platforms. Much of this is simply due to Rust (avoids PyInstaller and its complexity), but also the added tooling for codesigning, and producing suitable bundles for each platform: on Linux you get a lightweight `.AppImage`, on Windows an installer, and `.app` on macOS.

In the v0.14.0 betas, the Windows installer is an `.exe` setup, macOS gets a `.dmg` for both Apple Silicon and Intel, and Linux gets `.AppImage`, `.deb`, `.rpm` and `.zip` for x86_64 and arm64.

The Tauri bundles are also smaller to download. Here is the size of the installers attached to the v0.14.0b8 release, for the classic build and the Tauri build:

| Installer | Classic (`aw-qt`) | Tauri |
|-----------|------------------:|------:|
| Windows `.exe` | 81 MB | 43 MB |
| macOS Apple Silicon `.dmg` | 64 MB | 53 MB |
| macOS Intel `.dmg` | 70 MB | 56 MB |

These are download sizes read from the release assets, not a measurement of runtime memory use. We have not benchmarked memory yet.

## Try it today

The v0.14.0 betas include `aw-tauri` builds for all platforms. Find them under "Tauri distribution" in the [release notes](https://github.com/ActivityWatch/activitywatch/releases), or on the [downloads page](https://activitywatch.net/downloads/) (once v0.14.0 is out, look for the Tauri builds next to the classic ones).

- **Windows:** the `.exe` installer.
- **macOS:** the `.dmg`, for either Apple Silicon or Intel.
- **Linux:** the `.zip` has everything (`aw-tauri` as `.AppImage`, `.deb` and `.rpm`, plus the watchers): run `move-to-aw-modules.sh` from it to copy the modules to `~/aw-modules/`, which is where `aw-tauri` looks for them. The standalone `.AppImage`, `.deb` and `.rpm` on the release page contain only the `aw-tauri` app itself.

A few caveats, since this is still testing:

- **Back up your data before upgrading.** The v0.14 server performs a one-time database index migration on first start. It does not intentionally change or delete events, but on a large database it can take a while, so leave ActivityWatch running until the dashboard shows up.
- Don't run `aw-qt` and `aw-tauri` at the same time: they both want port 5600.
- Found a bug? Please [open an issue](https://github.com/ActivityWatch/aw-tauri/issues) or tell us in the [release discussion](https://github.com/ActivityWatch/activitywatch/discussions).

## Who this is for

ActivityWatch [has passed 1 million downloads]({% post_url 2026-09-29-one-million-downloads %}), and the desktop app is where most of our users start. Making it simpler to build, sign and ship is how we get fixes and improvements out to them faster.

<div class="text-center my-3">
  <img src="/img/stats/downloads.png" alt="Cumulative ActivityWatch downloads passing 1 million, and weekly downloads rising to over 10,000" style="max-width: 100%;">
  <p><small>Cumulative and weekly desktop downloads from GitHub Releases. Live chart on the <a href="/stats/">stats page</a>.</small></p>
</div>

## Help us finish it

`aw-tauri` is still in active development and contributions are welcome and encouraged! More eyes on the code will be beneficial to the project.

Check out the [README](https://github.com/ActivityWatch/aw-tauri/blob/master/README.md) to see the status of development, and where you can help out. Open items include a settings UI, downloading watchers on demand, the updater, and code signing ([see the issues](https://github.com/ActivityWatch/aw-tauri/issues)).

We are hopeful that it will help solve many of our remaining challenges, and are excited to see it help shape the future of ActivityWatch.

Thanks to [Brian Vuku (0xbrayo)](https://github.com/0xbrayo), the main author of `aw-tauri`, who wrote the original version of this post.
