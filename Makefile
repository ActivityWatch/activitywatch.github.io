.PHONY: build dev

build: assets
	# compass compile
	bundle exec bliss build

dev: assets
	bundle exec bliss serve

assets: _includes/tables img/stats

push-github:
	./scripts/push-build.sh

update-downloads:
	python3 scripts/update-downloads.py

install-deps:
	-sudo npm install -g jekyll-bliss
	bundle config set path 'vendor/bundle'
	bundle install

clean:
	-rm -r _site
	-rm -r _includes/tables
	-make --directory=contributor-stats clean


#
# Build dependencies, not to be run manually
#

stats:
	git clone --recurse-submodules https://github.com/ActivityWatch/stats.git || true

contributor-stats:
	git clone --recurse-submodules https://github.com/ActivityWatch/contributor-stats.git || true

_includes/tables: contributor-stats/tables
	cp -r contributor-stats/tables _includes/

img/stats: stats
	pip show poetry || pip install poetry
	cd stats && poetry install
	mkdir -p img/stats
	cd stats && mkdir -p out && poetry run python analyze_stats.py --since 2017-07-01 --column downloads --save ../img/stats/downloads.png

contributor-stats/tables: contributor-stats
	make --directory=contributor-stats build-aw
