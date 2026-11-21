#!/usr/bin/env python3
"""make.fun entry: world news of Friday 20 November 2026, one image (v2, full-day edition).

Deterministic, standard library only: copies the pre-rendered entry.png
held in this repository to /output/entry.png. No network, no clock, no
randomness. The front page itself was rendered once, deterministically,
with Pillow and DejaVu fonts (byte-identical across repeated runs);
shipping the rendered PNG plus this copier keeps the entry independent
of the grading sandbox's font set.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY_NAME = "entry.png"


def copy_entry(src, dst):
    """Copy the pre-rendered front page byte for byte; return its size."""
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    return len(data)


def main():
    src = os.path.join(HERE, ENTRY_NAME)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, ENTRY_NAME)
    size = copy_entry(src, dst)
    print("wrote %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
