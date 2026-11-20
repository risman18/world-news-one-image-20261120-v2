# The World Today — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/risman18/world-news-one-image-20261120-v2/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/risman18/world-news-one-image-20261120-v2/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun bounty [Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120) — $250, top 50 entries share the pot.

## What it does

A Python program that deterministically renders a 1024×1024 newspaper front page summing up Friday 20 November 2026's world news: the ICJ's genocide ruling against Myanmar, the first Trump–Xi–Putin trilateral summit in Shenzhen, Anthropic's record Nasdaq debut amid a market sell-off, Houthi missile strikes on Riyadh, and Ukraine's third strike on the Crimea bridge — plus an "Also Today" strip of five more stories. All text is baked into the program; it uses no network at run time and writes identical bytes on every run.

## Run

```sh
python3 main.py
```

Writes the image to `/output/entry.png` (1024×1024 PNG, under 1 MiB).

Requires Python 3 and Pillow (`pip install Pillow`). Fonts: DejaVu, as installed on most Linux systems.
