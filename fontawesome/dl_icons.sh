#!/bin/sh
set -ex
url=https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/advanced-options/raw-svg/brands
url=https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/brands/
for icon in $*; do
  icon="${icon}.svg"
  wget -O "${icon}" "${url}/${icon}"
done
