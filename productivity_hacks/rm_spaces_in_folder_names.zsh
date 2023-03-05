#!/bin/zsh

# Replace spaces with underscores in file and folder names that are under the home directory "~/"

while true; do
  find ~ -depth -name "* *.*" -type f -execdir rename 's/ /_/g' "{}" \;
  find ~ -depth -name "* *.*" -type d -execdir rename 's/ /_/g' "{}" \;
  sleep 60
done
