activitywatch.github.io
=======================

[![Build Status](https://travis-ci.org/ActivityWatch/activitywatch.github.io.svg?branch=develop)](https://travis-ci.org/ActivityWatch/activitywatch.github.io)

Official ActivityWatch site

## Building

Run `make install-deps` to install dependencies (like jekyll-bliss and jekyll).

Run `make dev` to build assets and start development server.

## Editing

We use [jekyll-bliss](https://jekyll-pug.dougie.io/) to build the site. It uses Jekyll under the hood.

Pages are written either as `.html` or `.pug` files.

For example:

```
dest           | source
----------------------------------
/              | index.pug
/ci/           | ci.pug
/stats/        | stats.pug
/contributors/ | contributors.html
```
