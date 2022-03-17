.PHONY: build dev

build: assets
	# compass compile
	bundle exec bliss build
	touch .nojekyll

dev: assets
	bundle exec bliss serve

assets: _includes/tables img/stats img/*.png

push-github:
	./scripts/push-build.sh

update-downloads:
	python3 scripts/update-downloads.py

install-deps:
	-sudo npm install -g jekyll-bliss
	bundle config set path 'vendor/bundle'
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
	cd stats && mkdir -p out && poetry run python analyze_stats.py --since 2017-07-01 --column downloads --save ../img/stats/downloads.png
