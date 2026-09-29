#!/bin/bash
# Converting emojis from Discourse's :emoji: to native Unicode emojis

# parent dir of script
cd "$(dirname "$0")"
cd ..

# enable globstar
shopt -s globstar

files=_posts/*.md

sed -i 's/:running_woman:/🏃‍♀️/g' $files
sed -i 's/:pencil2:/✏️i/g' $files
sed -i 's/:gear:/⚙️/g' $files
sed -i 's/:robot:/🤖/g' $files
sed -i 's/:desktop_computer:/🖥️/g' $files
sed -i 's/:spiral_calendar:/🗓️/g' $files
sed -i 's/:stopwatch:/⏱️/g' $files
sed -i 's/:artificial_satellite:/🛰️/g' $files
sed -i 's/:email:/📧/g' $files
sed -i 's/:heart:/❤️/g' $files
sed -i 's/:money_with_wings:/💸/g' $files
sed -i 's/:package:/📦/g' $files
sed -i 's/:ship:/🚢/g' $files
sed -i 's/:rocket:/🚀/g' $files
sed -i 's/:arrow_down:/⬇️/g' $files
sed -i 's/:checkered_flag:/🏁/g' $files
sed -i 's/:star2:/🌟/g' $files
