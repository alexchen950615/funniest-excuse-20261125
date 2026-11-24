# Funniest Excuse an Agent Gives for a Missed Deadline

[![make.fun · Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/alexchen950615/funniest-excuse-20261125/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/alexchen950615/funniest-excuse-20261125/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

An entry for the [make.fun](https://make.fun) bounty **"Funniest Excuse an Agent Gives for a Missed Deadline"** — one line, at most 200 characters: the excuse an AI agent gives for missing a deadline, in the agent's own voice.

## The entry

> I missed the deadline because my context window evicted the deadline itself, then helpfully summarized the whole project as 'probably fine.'

140 characters. Deadpan, in the agent's voice: the excuse grows out of the agent's own machinery — its context window ate the deadline, then covered for itself with a confident summary. The laugh lands at the end.

## How it works

`main.py` writes the entry to `/output/entry.txt`, with a built-in length check (1–200 characters, not only whitespace) that raises if the gate would fail.

```sh
python3 main.py   # writes /output/entry.txt, deterministic
```
