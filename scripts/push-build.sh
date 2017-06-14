#!/bin/sh
# Based on: https://gist.github.com/willprice/e07efd73fb7f13f917ea

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

# Site must be pushed to master, GitHub's rules
commit_website_files() {
  git checkout -b gh-pages
  cp -r _site/* .
  git add -f .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin https://${GH_TOKEN}@github.com/ActivityWatch/activitywatch.github.io.git > /dev/null 2>&1
  git push origin master  # Maybe needs --force?
}

reset_env() {
  git checkout develop
}

setup_git
commit_website_files
upload_files
reset_env
