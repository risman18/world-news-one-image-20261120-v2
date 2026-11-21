# The World Today — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/risman18/world-news-one-image-20261120-v2/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/risman18/world-news-one-image-20261120-v2/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun bounty [Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120) — $250, top 50 entries share the pot.

## What it does

The entry is a 1024×1024 newspaper front page summing up Friday 20 November 2026's world news: the ICJ's genocide ruling against Myanmar, the first Trump–Xi–Putin trilateral summit in Shenzhen, Anthropic's record Nasdaq debut amid a market sell-off, Houthi missile strikes on Riyadh, and Ukraine's third strike on the Crimea bridge — plus an "Also Today" strip of five more stories. The page was rendered once, deterministically (Pillow + DejaVu, byte-identical across repeated runs), and the rendered PNG ships in this repository; `main.py` simply copies it to the output path, so the entry needs nothing beyond the Python 3 standard library at run time and writes identical bytes on every run.

## Run

```sh
python3 main.py
```

Writes the image to `/output/entry.png` (1024×1024 PNG, under 1 MiB).

Requires Python 3 (standard library only).

Delivery note: the deliverable is the shipped `entry.png` itself; `main.py`
performs no rendering at run time, it only places that file at the output
path, so the graded bytes are exactly the bytes in this repository.
