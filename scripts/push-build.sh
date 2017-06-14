#!/bin/bash
# Based on: https://gist.github.com/willprice/e07efd73fb7f13f917ea

EMAIL="$(git config user.email)"
NAME="$(git config user.name)"

setup_git() {
  git config user.email "travis@travis-ci.org"
  git config user.name "Travis CI"
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
  git config user.email $EMAIL
  git config user.name $NAME
}

if [ -z ${TRAVIS+""} ]; then
    echo "WARNING: Not running under Travis, exiting."
    exit 1;
fi

setup_git
commit_website_files
upload_files
reset_env
