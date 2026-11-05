#!/usr/bin/env bash
# Build the site into public/ with orgo, then do what orgo does not: version asset
# URLs by content hash, set the footer year, and list directory URLs in the sitemap.
set -euo pipefail
cd "$(dirname "$0")"

rm -rf public
orgo build content -o public --strict

# Cloudflare caches assets for a year, so each URL changes when its file does.
for f in main.css favicon.svg apple-touch-icon.png og.png; do
  h=$(shasum -a 256 "public/$f" | cut -c1-20)
  find public -name '*.html' -exec perl -pi -e "s{/\\Q$f\\E\"}{/$f?h=$h\"}g" {} +
  if ! grep -rqF "$f?h=$h" public --include='*.html'; then
    echo "build.sh: no links to $f found; templates/base.html changed?" >&2
    exit 1
  fi
done

year=$(date +%Y)
find public -name '*.html' -exec perl -pi -e "s{&copy; \\d{4} ·}{&copy; $year ·}g" {} +

# orgo lists directory indexes by file; the site links them as /dir/.
perl -pi -e 's{/index\.html</loc>}{/</loc>}g' public/sitemap.xml

# The incremental cache is a build input, not part of the site.
rm public/.orgo-cache.json
