#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

Run:  python3 draw.py            # writes entry.png next to this file

The hero illustration (hero.png, generated at build time) is cropped to a
wide band under the masthead; the six stories below it were each verified
against at least two independent news sources reporting 19 November 2026.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/noto"

W, H = 1024, 1024
PAPER = (248, 244, 233)
INK = (22, 22, 22)
RED = (176, 32, 32)
GREY = (96, 90, 80)
RULE = (180, 172, 155)
CHIP_BG = (28, 58, 112)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_MAST = font("NotoSerif-Bold.ttf", 76)
F_DATE = font("NotoSans-Bold.ttf", 36)
F_SUB = font("NotoSans-Regular.ttf", 24)
F_HEAD = font("NotoSerif-Bold.ttf", 26)
F_SUM = font("NotoSans-Regular.ttf", 18)
F_TAG = font("NotoSans-Bold.ttf", 16)
F_CAP = font("NotoSans-Regular.ttf", 19)
F_FOOT = font("NotoSans-Regular.ttf", 16)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
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


STORIES = [
    ("DIPLOMACY  |  SHENZHEN",
     "First-ever Trump-Xi-Putin summit",
     "Xi hosts Trump and Putin for a first three-way meeting on the APEC "
     "sidelines; nuclear arms and Iran on the agenda."),
    ("UKRAINE  |  WAR",
     "Crimean Bridge hit a third time",
     "Traffic halts after another strike just after midnight, the third "
     "attack on the bridge this week, days after its road span collapsed."),
    ("CULTURE  |  GAMES",
     "GTA VI begins global rollout",
     "Rockstar's game unlocks at midnight local time from New Zealand "
     "onward after 13 years; pre-orders top $1.5bn, per Sensor Tower."),
    ("MARKETS  |  TECH",
     "Anthropic debuts on Nasdaq",
     "Claude-maker prices its IPO at $83 a share, a record $81.3bn "
     "offering, and starts trading as ANT at about a $1.5tn valuation."),
    ("CULTURE  |  ART",
     "Van Gogh sells for record $190.4m",
     "Sotheby's sells 'Chataigniers en fleurs' in New York, a record for "
     "the artist, after a Nazi-era ownership dispute is settled."),
    ("POLITICS  |  USA",
     "Jeffries nominated for Speaker",
     "House Democrats back Hakeem Jeffries 251-11; he is on track to "
     "become the first Black Speaker when Congress votes in January."),
]

CAPTION = ("Trump, Xi and Putin meet in Shenzhen - the first three-way summit "
           "of the world's nuclear powers.")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 48

    # --- masthead ---
    d.text((M, 24), "THE WORLD TODAY", font=F_MAST, fill=INK)
    d.rectangle([M, 118, W - M, 124], fill=INK)
    d.text((M, 134), "Thursday, 19 November 2026", font=F_DATE, fill=RED)
    d.text((M, 182), "One day's world news, summed up in a single page.",
           font=F_SUB, fill=GREY)
    d.rectangle([M, 218, W - M, 224], fill=INK)

    # --- hero image band ---
    hero = Image.open(os.path.join(HERE, "hero.png")).convert("RGB")
    hw, hh = hero.size
    target_w, target_h = W - 2 * M, 180
    # centre-crop to the band's aspect ratio, then resize
    scale = max(target_w / hw, target_h / hh)
    hero = hero.resize((round(hw * scale), round(hh * scale)),
                       Image.LANCZOS)
    x0 = (hero.width - target_w) // 2
    y0 = (hero.height - target_h) // 2
    hero = hero.crop((x0, y0, x0 + target_w, y0 + target_h))
    img.paste(hero, (M, 236))
    d.text((M, 422), CAPTION, font=F_CAP, fill=GREY)
    d.rectangle([M, 452, W - M, 458], fill=INK)

    # --- 2 columns x 3 rows ---
    top = 474
    col_w = (W - 2 * M - 36) // 2
    row_h = 165
    xs = [M, M + col_w + 36]
    for i, (tag, head, summ) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = xs[col]
        y = top + row * row_h
        # tag chip
        tw = d.textlength(tag, font=F_TAG)
        d.rounded_rectangle([x, y, x + tw + 14, y + 25], radius=4, fill=CHIP_BG)
        d.text((x + 7, y + 4), tag, font=F_TAG, fill=(255, 255, 255))
        y += 32
        for line in wrap(d, head, F_HEAD, col_w)[:2]:
            d.text((x, y), line, font=F_HEAD, fill=INK)
            y += F_HEAD.size + 3
        y += 2
        for line in wrap(d, summ, F_SUM, col_w)[:3]:
            d.text((x, y), line, font=F_SUM, fill=(58, 54, 48))
            y += F_SUM.size + 4
        # row rule (not after last row)
        if row < 2:
            ry = top + (row + 1) * row_h - 12
            d.line([x, ry, x + col_w, ry], fill=RULE, width=1)

    # --- footer ---
    d.rectangle([M, H - 40, W - M, H - 34], fill=INK)
    d.text((M, H - 26),
           "Sources: NYT, Reuters, AP, BBC, CNN, Kyiv Independent, "
           "Sotheby's via Artnet.",
           font=F_FOOT, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
