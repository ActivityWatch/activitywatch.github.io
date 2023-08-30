.PHONY: build dev

build: assets
	# compass compile
	bundle exec jekyll build

dev:
	bundle exec jekyll serve

assets: _includes/tables img/stats img/*.png

update-downloads:
	python3 scripts/update-downloads.py

install-deps:
	# This shouldn't be set in CI, but it's maybe (?) useful for local development
	#bundle config set path 'vendor/bundle'
	# we also need `pug`: npm install -g pug
	bundle install

precommit:

# Used to optimize png filesizes (which need to be <128K due to https://github.com/DougBeney/Jekyll-Bliss/issues/4)
# If files are still >128K, then you might want reduce the number of colors and remove metadata to reduce size:
#   convert $INPUT $OUTPUT -colors 256 -strip -define png:exclude-chunk=all
#   optipng $INPUT $OUTPUT
img/%.png:
	optipng -o5 $@

clean:
	-rm -r _site
	-rm -r _build
	-rm -r _includes/tables
	-git restore _includes/tables/github-stats.html
	-make --directory=contributor-stats clean


#
# Build dependencies, not to be run manually
#

stats:
	git clone --recurse-submodules https://github.com/ActivityWatch/stats.git || true

contributor-stats:
	git clone --recurse-submodules https://github.com/ActivityWatch/contributor-stats.git || true

_includes/tables: contributor-stats
	make --directory=contributor-stats build-aw
	cp -r contributor-stats/tables _includes/

img/stats: stats
	cd stats && poetry install
	mkdir -p img/stats
	mkdir -p stats/out
	cd stats && poetry run python analyze_stats.py --since 2017-07-01 --column downloads --per-day --save ../img/stats/downloads.png
	cd stats && poetry run python analyze_stats.py --since 2017-07-01 --column 'Chrome WAU' --title 'Chrome Weekly Active Users' --save ../img/stats/chrome-wau.png
	cd stats && poetry run python analyze_stats.py --since 2017-07-01 --column 'Firefox DAU' --resample 7D --title 'Firefox Daily Active Users (7D mean)' --save ../img/stats/firefox-dau-7d.png
