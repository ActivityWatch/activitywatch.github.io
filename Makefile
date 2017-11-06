.PHONY: build dev

build: _includes/tables
	# compass compile
	jekyll build

dev: _includes/tables
	jekyll serve --watch --drafts

push-github:
	./scripts/push-build.sh

install-deps:
	gem install jekyll jekyll-compass compass jekyll-last-modified-at

clean:
	rm -rf _site
	rm -rf contributor-stats
	rm -rf _includes/tables


#
# Build dependencies, not to be run manually
#

contributor-stats:
	git clone --recurse-submodules https://github.com/ActivityWatch/contributor-stats.git

_includes/tables: contributor-stats/tables
	cp -r contributor-stats/tables _includes/

contributor-stats/tables: contributor-stats
	make --directory=contributor-stats clone
	make --directory=contributor-stats build
