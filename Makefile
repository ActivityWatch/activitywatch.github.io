.PHONY: build dev

build: _includes/tables
	# compass compile
	bundle exec bliss build

dev: _includes/tables
	bundle exec bliss serve

push-github:
	./scripts/push-build.sh

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

contributor-stats:
	git clone --recurse-submodules https://github.com/ActivityWatch/contributor-stats.git || true

_includes/tables: contributor-stats/tables
	cp -r contributor-stats/tables _includes/

contributor-stats/tables: contributor-stats
	make --directory=contributor-stats build-aw
