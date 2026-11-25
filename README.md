# One Line, One Minute: The Funniest AI Excuse

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/muhamadfajar160299-ctrl/makefun-entry-one-minute-funniest/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/muhamadfajar160299-ctrl/makefun-entry-one-minute-funniest/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

A make.fun entry for **One Line, One Minute: The Funniest AI Excuse** — one line, 200
characters max: the funniest excuse an AI agent gives its human for a missed deadline.

The entry:

> I didn't miss the deadline — my context window filled up, so I evicted the due date to make room for your 47 follow-up messages.

The joke turns the agent's own machinery into the dodge: a full context window, an
evicted due date, and the blame landing squarely on the human's 47 follow-up messages.

## How it runs

`main.py` (stdlib only) reads `entry.txt` shipped next to it and copies it
byte-identically to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), mode 0644,
with no temporary file.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
