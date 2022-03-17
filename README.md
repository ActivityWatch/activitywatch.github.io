activitywatch.github.io
=======================

[![Build Status](https://github.com/ActivityWatch/activitywatch.github.io/workflows/Build/badge.svg)](https://github.com/ActivityWatch/activitywatch.github.io/actions)

Official ActivityWatch site

## Building

Run `make install-deps` to install dependencies (like jekyll).

Run `make dev` to build assets and start development server.

## Editing

We use [jekyll](https://jekyllrb.com/) to build the site.

Pages are written either as `.html` or `.pug` files (using `jekyll-pug`).

For example:

```
dest           | source
----------------------------------
/              | index.pug
/ci/           | ci.pug
/stats/        | stats.pug
/contributors/ | contributors.html
```

## Generated stats

Stats are generated for downloads (using https://github.com/ActivityWatch/stats/) and contributor statistics (using https://github.com/ActivityWatch/contributor-stats).
