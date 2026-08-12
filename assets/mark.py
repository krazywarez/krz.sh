#!/usr/bin/env python3
"""Render the krz frame mark to RGBA PNG at exact integer pixel boundaries."""
import struct, zlib, sys

GRID = 32
# (x, y, w, h) in grid units
FRAME = [(4, 4, 24, 4), (4, 24, 24, 4), (4, 8, 4, 16), (24, 8, 4, 16)]
BLOCK = (12, 12, 8, 8)

INKS = {
    "dark":  ("#17171a", "#2f6bd6"),   # for light backgrounds
    "light": ("#f1f1ef", "#6f9dff"),   # for dark backgrounds
}


def rgba(hexstr):
    h = hexstr.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)


def chunk(tag, data):
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))


def render(size, fg_hex, ac_hex, path):
    if size % GRID:
        sys.exit(f"size {size} must be a multiple of {GRID}")
    s = size // GRID
    fg, ac = rgba(fg_hex), rgba(ac_hex)
    # transparent canvas
    px = bytearray(size * size * 4)

    def fill(rect, color):
        x, y, w, h = (v * s for v in rect)
        row = bytes(color) * w
        for yy in range(y, y + h):
            off = (yy * size + x) * 4
            px[off:off + w * 4] = row

    for r in FRAME:
        fill(r, fg)
    fill(BLOCK, ac)

    # filter byte 0 per scanline
    raw = b"".join(b"\x00" + bytes(px[r * size * 4:(r + 1) * size * 4])
                   for r in range(size))
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)
    return len(png)


if __name__ == "__main__":
    for name, (fg, ac) in INKS.items():
        for size in (1024, 512):
            p = f"krz-mark-{size}-{name}.png"
            n = render(size, fg, ac, p)
            print(f"{p:28} {size}x{size}  {n:,}b")
