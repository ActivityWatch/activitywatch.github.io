build:
	compass compile
	jekyll build

install-deps:
	sudo gem install jekyll jekyll-compass compass jekyll-last-modified-at

dev:
	jekyll serve --watch --drafts

clean:
	rm -r _site
