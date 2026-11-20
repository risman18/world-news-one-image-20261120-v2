#!/usr/bin/env python3
"""THE WORLD TODAY — Friday, 20 November 2026.

Renders one 1024x1024 newspaper front page summarising the full day's
world news. Deterministic: no network, no randomness, no timestamps.
Stdlib + Pillow only. Fonts: DejaVu (installed in this sandbox).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/output/entry.png"

CREAM = (247, 242, 231)
PAPER = (252, 249, 240)
NAVY = (20, 38, 74)
NAVY_LT = (38, 62, 108)
RED = (163, 30, 34)
INK = (26, 26, 26)
GREY = (96, 96, 96)
RULE = (20, 38, 74)
HAIR = (178, 168, 148)

FD = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FD, "DejaVuSerif.ttf")
SERIF_B = os.path.join(FD, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FD, "DejaVuSans.ttf")
SANS_B = os.path.join(FD, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw wrapped paragraph; returns y after last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def story(draw, x, y, w, kicker, headline, body, hsize, bsize, hlead, blead):
    """Draw one story block; returns y after the block."""
    kf = font(SANS_B, 13)
    hf = font(SERIF_B, hsize)
    bf = font(SERIF, bsize)
    # kicker with small red square
    draw.rectangle([x, y + 3, x + 9, y + 12], fill=RED)
    draw.text((x + 15, y), kicker, font=kf, fill=RED)
    y += 22
    y = para(draw, x, y, headline, hf, w, hlead, color=NAVY)
    y += 6
    y = para(draw, x, y, body, bf, w, blead)
    return y


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    M = 34  # margin
    CW = W - 2 * M  # content width

    # ---- outer frame ----
    d.rectangle([10, 10, W - 11, H - 11], outline=NAVY, width=2)
    d.rectangle([16, 16, W - 17, H - 17], outline=HAIR, width=1)

    y = 30
    # ---- masthead ----
    mast = font(SERIF_B, 56)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, y), title, font=mast, fill=NAVY)
    y += 66
    # dateline row
    d.line([M, y, W - M, y], fill=NAVY, width=2)
    y += 8
    dl = font(SANS_B, 14)
    left = "FRIDAY, 20 NOVEMBER 2026"
    right = "FULL-DAY EDITION"
    d.text((M, y), left, font=dl, fill=NAVY)
    rw = d.textlength(right, font=dl)
    d.text((W - M - rw, y), right, font=dl, fill=NAVY)
    center = "FIVE STORIES THAT DEFINED THE DAY"
    cw = d.textlength(center, font=font(SANS, 13))
    d.text(((W - cw) / 2, y + 1), center, font=font(SANS, 13), fill=GREY)
    y += 24
    d.line([M, y, W - M, y], fill=NAVY, width=2)
    y += 14

    # ---- lead story: ICJ (full width) ----
    lead_body = (
        "The International Court of Justice ruled on Thursday that Myanmar committed "
        "genocide against its Rohingya minority, the first time the court has found a "
        "state responsible for genocide. In a 9\u20136 decision, judges found that security "
        "forces carried out mass killings and widespread sexual violence in northern "
        "Rakhine State, aiming to destroy a substantial part of the Rohingya population. "
        "The case was brought by The Gambia in 2019; the court now turns to reparations, "
        "a safe return home and restored citizenship for the Rohingya."
    )
    y = story(d, M, y, CW,
              "THE HAGUE  ·  JUSTICE",
              "WORLD COURT: MYANMAR COMMITTED GENOCIDE",
              lead_body, 30, 15, 34, 20)
    y += 10
    d.line([M, y, W - M, y], fill=NAVY, width=2)
    y += 10

    # ---- middle row: two columns ----
    gap = 28
    col_w = (CW - gap) // 2
    x2 = M + col_w + gap
    y_mid = y

    shenzhen = (
        "The leaders of the United States, China and Russia held their first three-way "
        "summit in Shenzhen on Thursday and signed a four-point joint declaration. The "
        "talks lasted about 70 minutes and produced no breakthrough on Ukraine, Iran or "
        "nuclear-arms limits, according to reports from the meeting. In Berlin the same "
        "day, Ukraine\u2019s allies said Europe was ready to talk with Russia, and US envoy "
        "Jared Kushner said Moscow was \u201ccomfortable\u201d with Article 5-style security "
        "guarantees for Kyiv."
    )
    anthropic = (
        "Anthropic, the maker of the Claude chatbot, closed its first day on the Nasdaq "
        "at $97.17, up 17% from its $83 offer price, after opening at $111.50. The "
        "$81.3 billion offering is the largest IPO on record, briefly valuing the company "
        "above $2 trillion. The debut could not lift the wider market: the S&P 500 fell "
        "about 2% for a fifth straight losing day, and Japan\u2019s Nikkei dropped 4.8% on "
        "Friday, with SoftBank down more than 16%."
    )
    y1 = story(d, M, y_mid, col_w,
               "SHENZHEN  ·  SUMMIT",
               "Trump, Xi and Putin hold first three-way summit",
               shenzhen, 21, 14, 25, 19)
    y2 = story(d, x2, y_mid, col_w,
               "NEW YORK  ·  MARKETS",
               "Anthropic soars in record debut as markets slide",
               anthropic, 21, 14, 25, 19)
    y = max(y1, y2) + 8
    d.line([M, y, W - M, y], fill=HAIR, width=1)
    y += 8

    # ---- lower row: two columns ----
    y_low = y
    houthi = (
        "Houthi missiles struck Riyadh\u2019s financial district, damaging the Public "
        "Investment Fund tower and other buildings in the Saudi capital. Saudi Arabia "
        "said it intercepted another missile and five drones on Friday, after the Houthis "
        "claimed attacks on Saudi airports, military bases and the capital. The strikes "
        "mark a sharp escalation in the region\u2019s widening conflict."
    )
    ukraine = (
        "Ukraine struck the Kerch Bridge to Crimea for the third time in four days, "
        "halting rail traffic across the strait, as President Putin vowed a response. "
        "Overnight, Russia launched a missile-and-drone attack on Kyiv that killed three "
        "people and damaged three bridges across the Dnipro River, the city\u2019s mayor said. "
        "Ukraine\u2019s allies met in Berlin on Thursday to coordinate their position ahead "
        "of possible talks with Moscow."
    )
    y1 = story(d, M, y_low, col_w,
               "RIYADH  ·  CONFLICT",
               "Missiles hit Riyadh\u2019s financial district",
               houthi, 21, 14, 25, 19)
    y2 = story(d, x2, y_low, col_w,
               "KYIV  ·  WAR IN UKRAINE",
               "Ukraine hits Crimea bridge a third time",
               ukraine, 21, 14, 25, 19)
    y = max(y1, y2) + 10

    # ---- ALSO TODAY strip ----
    strip_h = 130
    d.rectangle([M, y, W - M, y + strip_h], fill=NAVY)
    d.text((M + 16, y + 12), "ALSO TODAY", font=font(SANS_B, 15), fill=(247, 242, 231))
    d.line([M + 16, y + 36, W - M - 16, y + 36], fill=(120, 140, 175), width=1)
    items = [
        "IMF warns global public debt is nearing 100% of world GDP, its highest since World War II.",
        "GTA 6 launch tops $2.3 billion in sales.",
        "US Senate passes bipartisan energy-permitting bill, 62\u201333; the bill now goes to the House.",
        "Kenya begins a 42-day countdown to Ebola-free status after discharging its last patient.",
        "Young people in more than 25 European countries strike over living costs and housing.",
    ]
    sf = font(SANS, 13)
    iy = y + 44
    for it in items:
        d.text((M + 16, iy), "\u2022", font=sf, fill=(247, 242, 231))
        iy = para(d, M + 34, iy, it, sf, CW - 50, 17, color=(232, 236, 244))
        iy += 1
    y += strip_h + 8

    # ---- footer ----
    ff = font(SANS, 11)
    foot = "Compiled from public reporting on 20 November 2026  ·  THE WORLD TODAY"
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, y), foot, font=ff, fill=GREY)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
