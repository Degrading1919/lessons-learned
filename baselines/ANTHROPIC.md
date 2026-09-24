# Anthropic / Claude Baseline

_Last researched: 2026-09-24_

This is the compact routing baseline.

For the long-form benchmark + Reddit synthesis, see:

[Anthropic Model Field Guide — 2026-09-24](../research/anthropic/2026-09-24-reddit-field-guide.md)

## Current routing summary

| Model | Public-prior role | Strong suits | Main cautions | Confidence |
|---|---|---|---|---|
| **Claude Opus 5.5** | New flagship / high-end daily model | coding, UI/debugging, agentic knowledge work, clearer collaboration | only two days public; still expensive; minor bugs/sloppiness remain | Low-medium |
| **Claude Fable 5.1** | Scarce planner / deep reviewer | architecture, orchestration, low-level code, research, difficult debugging | very expensive; quota burn; production fallback complicates pure-model comparison | Medium-high |
| **Claude Opus 5** | Transition / adversarial-QA niche | benchmark-strong reasoning | mature complaints about verbosity, jargon, overreach, context drift and correction burden | High |
| **Claude Sonnet 5** | Thorough mid-tier agent | bounded coding, knowledge work, tool use, architecture exploration | max effort is a token monster; weaker task economics than sticker price suggests | High |
| **Claude Opus 4.8** | Proven behavioral fallback | practical coding judgment, Claude Code execution, long-context work | older and relatively expensive | High |
| **Claude Haiku 4.5** | Utility worker / subagent | search, read, classify, explore, quick prototypes | weak deep reasoning and modern terminal/automation performance | High |
| **Claude Mythos 5.1** | Restricted trusted-access specialist | authorized high-risk cyber/life-science workflows | not a normal routing tier | Medium |

Anthropic says Sonnet 5.5 and Haiku 5.5 will follow Opus 5.5 in the coming weeks. Do not create routing conclusions for them until they exist.

## Current API economics

| Model | Input / 1M | Output / 1M | Cache read / 1M |
|---|---:|---:|---:|
| Opus 5.5 | $4.00 | $20.00 | $0.20 |
| Fable 5.1 | $10.00 | $50.00 | $0.25 |
| Opus 5 | $5.00 | $25.00 | $0.50 |
| Sonnet 5 | $2.00 | $10.00 | $0.20 |
| Opus 4.8 | $5.00 | $25.00 | $0.50 |
| Haiku 4.5 | $1.00 | $5.00 | $0.10 |

Important: Sonnet 5's lower token price does not automatically mean lower completed-task cost because it can use dramatically more reasoning/output tokens at high/max effort.

## Opus 5.5 effort economics

Artificial Analysis v4.3.2:

| Effort | Intelligence | AA cost/task |
|---|---:|---:|
| Low | 42 | $0.55 |
| Medium | 51 | $1.34 |
| High | 54 | $1.82 |
| XHigh | 56 | $3.46 |
| Max | 58 | $5.98 |

**Prior:** Medium/High is the likely high-value zone. Max is reserved for cases where the final quality margin matters.

## Fable 5.1 effort economics

| Effort | Intelligence | AA cost/task |
|---|---:|---:|
| Low | 47 | $2.37 |
| Medium | 49 | $2.98 |
| High | 51 | $3.91 |
| XHigh | 53 | $5.98 |
| Max | 53 | $7.63 |

**Prior:** XHigh dominates Max on the current broad benchmark. Do not default to Max.

## Sonnet 5 effort economics

| Effort | Intelligence | AA cost/task |
|---|---:|---:|
| Low | 25 | $0.51 |
| Medium | 28 | $1.00 |
| High | 32 | $1.79 |
| Max | 38 | $5.09 |

High→Max roughly triples task cost and reasoning/output-token use for six index points.

**Prior:** Low/Medium/High preserves Sonnet's mid-tier economic role. Max often destroys it.

## Claude Opus 5.5

Early independent results place it at the current frontier:

- Intelligence Index 58
- strong agentic knowledge work
- strong coding/terminal/automation results
- lower list price and much cheaper cache reads than Opus 5

Early Reddit themes:

- much clearer, more natural communication;
- fast coding;
- strong UI bug finding;
- former Opus 5/Codex users considering a return;
- still some bugs and minor sloppiness;
- subscription usage can still burn quickly.

**Routing prior:** current high-end default candidate for Claude Code, especially Medium/High, but preserve launch-week uncertainty.

## Claude Fable 5.1

Repeated strengths:

- planning;
- architecture;
- orchestration;
- deep debugging;
- low-level systems work;
- difficult research;
- repository-wide review.

Repeated weakness:

- quota and dollar cost.

A measured 22,022-call Reddit comparison found more tokens per prompt than Fable 5 but lower API cost per prompt because cache-read pricing dropped sharply.

**Routing prior:** scarce thinking/review resource, not bulk implementation. Prefer XHigh over Max absent contrary task-specific evidence.

## Claude Opus 5

The benchmark numbers are strong.

The human signal is much worse.

Recurring complaints:

- jargon;
- walls of text;
- unnecessary code comments;
- unrelated refactors;
- assumptions before verification;
- context drift;
- instruction misses;
- expensive correction loops.

There is a possible niche as adversarial QA/reviewer.

**Routing prior:** do not use as the normal author when 5.5/4.8 are available.

## Claude Sonnet 5

Useful for:

- bounded implementation;
- normal web/devops work;
- knowledge work;
- tool use;
- architecture exploration at controlled effort.

Problem:

- Max is extraordinarily verbose/token-hungry.

Artificial Analysis Max:
- ~118k output tokens/task
- ~88k reasoning tokens/task
- ~$5.09/task

High:
- ~44k output
- ~28k reasoning
- ~$1.79/task

**Routing prior:** use controlled effort; do not assume "Sonnet" means cheap.

## Claude Opus 4.8

Still a strong behavioral fallback.

Community + owner evidence supports:

- practical judgment;
- implementation;
- long-context coding;
- environment/MCP integration;
- fewer collaboration problems than Opus 5.

**Routing prior:** keep routable until Opus 5.5 proves equal/better in the owner's own work.

## Claude Haiku 4.5

Best role:

- search;
- read;
- classify;
- retrieve;
- explore;
- quick prototypes;
- repeated rubric-based judgments.

Artificial Analysis reasoning variant:
- index 17
- ~$0.21/task
- ~109 t/s
- 200k context

It is fast, but in 2026 it is not globally cheap/capable compared with newer external worker models.

**Routing prior:** Anthropic-native utility subagent, not serious architecture or difficult implementation.

## Current underdogs

1. **Opus 4.8** — older but trusted behavioral fallback.
2. **Haiku 4.5** — useful retrieval/classification/explore worker inside Claude Code.
3. **Opus 5.5 Medium/High** — much better effort economics than reflexive Max.
4. **Sonnet 5 Low/Medium/High** — can still be useful when Max is avoided.

## Current waste traps

- Opus 5 as the default implementation author.
- Sonnet 5 Max used because Sonnet is assumed to be the economical tier.
- Fable 5.1 Max when XHigh scores the same on the current broad benchmark.
- Opus 5.5 Max by default.
- Haiku on vague architecture or difficult coding.
- one premium Claude performing all search, implementation, test, review and summarization when tasks can be delegated by cognitive difficulty.

## Completed-task efficiency rule

Claude economics should track:

- token price;
- actual reasoning/output tokens;
- cache reads;
- first-pass acceptance;
- user corrections;
- subagent fanout;
- wall time;
- subscription quota;
- reviewer cost;
- regressions.

The family contains examples in both directions:

- **Sonnet 5:** cheaper tokens, expensive task because it thinks a lot.
- **Fable 5.1:** more tokens than predecessor, cheaper API prompt because cache reads are cheaper.
- **Opus 5:** strong benchmark ability, poor human-attention economics because communication/rework is expensive.

## Current provisional routing

- **Opus 5.5 Medium/High:** serious daily Claude Code.
- **Fable 5.1 High/XHigh:** architecture, orchestration, hard research/review.
- **Opus 4.8:** known-behavior implementation fallback.
- **Sonnet 5 Low/Medium/High:** bounded normal work.
- **Haiku 4.5:** search/read/classify/explore.
- **Opus 5:** adversarial-QA niche only unless personal evidence says otherwise.
- **Mythos 5.1:** authorized trusted-access specialist work.

Public evidence does not replace the owner's case corpus.
