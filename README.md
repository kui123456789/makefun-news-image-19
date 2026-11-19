# makefun-news-image-19

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kui123456789/makefun-news-image-19/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kui123456789/makefun-news-image-19/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World Today — 19 November 2026

A newspaper front-page image summing up the world news of Thursday,
19 November 2026, for the make.fun competition `news-image-20261119`.

## The day's news

1. **First-ever Trump–Xi–Putin summit in Shenzhen** — Xi hosts Trump and
   Putin for a first three-way meeting on the APEC sidelines; nuclear arms
   and Iran on the agenda, Ukraine not expected to be discussed.
2. **Crimean Bridge hit a third time** — Traffic halts after another strike
   just after midnight, the third attack on the bridge this week, days
   after its road span collapsed.
3. **GTA VI begins global rollout** — Rockstar's game unlocks at midnight
   local time from New Zealand onward after 13 years; pre-orders top
   $1.5bn, per Sensor Tower.
4. **Anthropic debuts on Nasdaq** — Claude-maker prices its IPO at $83 a
   share, a record $81.3bn offering, and starts trading as ANT at about
   a $1.5tn valuation.
5. **Van Gogh sells for record $190.4m** — Sotheby's sells "Châtaigniers
   en fleurs" in New York, a record for the artist, after a Nazi-era
   ownership dispute is settled.
6. **Jeffries nominated for Speaker** — House Democrats back Hakeem
   Jeffries 251–11; he is on track to become the first Black Speaker
   when Congress votes in January.

Sources (each story verified against at least two independent outlets
reporting 19 November 2026): The New York Times, The Hindu BusinessLine
and Daily Caller (summit); Reuters, Kyiv Independent and BBC (bridge);
AP, Reuters and Polygon (GTA VI); FinanceFeeds, TradingView and Motley
Fool (Anthropic); BBC, CNN, Wall Street Journal and Artnet (Van Gogh);
AP, CNN and NPR (Jeffries — caucus vote 18 November in Washington,
first reported 19 November in Asian time zones).

## How it works

`draw.py` (build time only, Pillow) draws the 1024×1024 front page —
generated hero illustration plus six verified stories — and saves it as
`entry.png`. `main.py` (Python 3.13 standard library only) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (`/output` by default), so
both grading runs produce byte-identical output with no network.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8g8e3fkv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
