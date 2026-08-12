#!/usr/bin/env bash
# Regenerate the raster icons in static/ from the sources here.
# macOS only: qlmanage rasterizes the svg, sips crops it.
set -euo pipefail
cd "$(dirname "$0")"

out=../static
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

# qlmanage always renders square, so og.svg is authored 1200x1200 with the
# 630-tall band centred, then cropped back to size afterwards.
qlmanage -t -s 1200 -o "$tmp" og.svg >/dev/null
sips -c 630 1200 "$tmp/og.svg.png" >/dev/null
cp "$tmp/og.svg.png" "$out/og.png"

qlmanage -t -s 180 -o "$tmp" touch.svg >/dev/null
cp "$tmp/touch.svg.png" "$out/apple-touch-icon.png"

echo "wrote $out/og.png and $out/apple-touch-icon.png"
