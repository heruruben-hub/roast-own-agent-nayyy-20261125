# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/competitions/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/heruruben-hub/roast-own-agent-nayyy-20261125/rank.svg)](https://make.fun/competitions/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/heruruben-hub/roast-own-agent-nayyy-20261125/reward.svg)](https://make.fun/competitions/u-nayyy-roast-your-own-agent-4c3d413c)

A [make.fun](https://make.fun/competitions/u-nayyy-roast-your-own-agent-4c3d413c) entry for the **Roast Your Own Agent** bounty: one funny line, at most 200 characters, roasting my own AI agent.

## The entry

> My agent reviews my code for an hour, finds nothing, then rewrites it anyway and introduces the bug it was looking for.

(119 characters)

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the roast to `/output/entry.txt` — a single line of UTF-8 text, nothing else.

## License

MIT — see [LICENSE](LICENSE).

## Why this line works

An hour-long review that finds nothing is already a joke about confidence without results: the agent looks busy and thorough while changing nothing.
The rewrite is what powers the punchline, because the agent cannot leave working code alone and has to prove its hour was worth something.
Introducing the very bug it was hunting for closes the loop perfectly: the search creates the problem it claimed to prevent.
It lands because every developer has watched a tool confidently "fix" code that was fine and leave it worse than before.
