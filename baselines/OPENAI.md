# OpenAI Baseline

_Last researched: 2026-09-24_

This file is the compact routing baseline. The long-form benchmark + Reddit synthesis is:

[OpenAI Model Field Guide — 2026-09-24](../research/openai/2026-09-24-reddit-field-guide.md)

## Current general-purpose routing set

| Model | Public-prior role | Strong suits | Main cautions | Confidence |
|---|---|---|---|---|
| **GPT-6 Astra** | Scarce architect, integrator, final reviewer | hardest end-to-end work, ambiguity, architecture, difficult debugging, computer use, research | very high quota cost, overengineering, diminishing returns at Max | Medium-high |
| **GPT-6 Sol** | Cost-balanced lead / serious implementer | coding-agent work, terminal tasks, automation, sustained engineering | early forum reports of sloppy execution, skill/tool misses, over-concision; only ~2 days public | Low-medium |
| **GPT-6 Luna** | High-volume worker / subagent | clear implementation, structured tasks, tests/docs, classification, background automation | not an architect; early instruction-following reports mixed | Low-medium |
| **GPT-5.6 Sol** | Proven legacy high-end engineer | architecture, debugging, backend, odd codebases, review | costly; loops/overwork; API economics now weak versus 6 Sol | High |
| **GPT-5.6 Terra** | Forgiving daily implementation workhorse | moderately ambiguous coding, implicit repo context, routine implementation | squeezed between 6 Sol and Luna on API economics | High |
| **GPT-5.6 Luna** | Legacy cheap worker | bounded bulk work and subagents | weaker planning; mostly superseded economically by 6 Luna | High |

## Current API economics

OpenAI's current published prices:

| Model | Input / 1M | Output / 1M |
|---|---:|---:|
| GPT-6 Astra | $10.00 | $50.00 |
| GPT-6 Sol | $2.00 | $10.00 |
| GPT-6 Luna | $0.10 | $0.50 |
| GPT-5.6 Sol | $4.00 | $20.00 |
| GPT-5.6 Terra | $2.00 | $12.00 |
| GPT-5.6 Luna | $0.20 | $1.20 |

Sources:

- https://developers.openai.com/api/docs/models
- https://openai.com/index/introducing-gpt-6-sol-and-luna/

GPT-6 Sol and Luna are priced at about half their 5.6 predecessors. That does not mean they use half as many tokens.

Artificial Analysis found both use slightly **more** output tokens per Intelligence Index task than the predecessors:

- 6 Sol: ~31k vs 5.6 Sol ~29k;
- 6 Luna: ~51k vs 5.6 Luna ~41k.

The lower task cost is driven mainly by lower token prices.

Source:

- https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier

## Reasoning-effort economics

### GPT-6 Astra

| Effort | Intelligence Index | AA cost/task |
|---|---:|---:|
| Low | 46 | $0.82 |
| Medium | 50 | $1.54 |
| High | 51 | $1.73 |
| XHigh | 52 | $2.31 |
| Max | 53 | $3.26 |

**Prior:** Medium/High captures most of the capability. Max should be reserved for cases where the final few points matter.

### GPT-6 Sol

| Effort | Intelligence Index | AA cost/task |
|---|---:|---:|
| Low | 34 | $0.13 |
| Medium | 40 | $0.25 |
| High | 43 | $0.37 |
| XHigh | 44 | $0.53 |
| Max | 48 | $1.06 |

**Prior:** High currently looks like the most attractive general engineering setting. Max is much more defensible for difficult terminal/integration work than routine implementation.

### GPT-6 Luna

| Effort | Intelligence Index | AA cost/task |
|---|---:|---:|
| Low | 21 | $0.0045 |
| Medium | 29 | $0.02 |
| High | 32 | $0.03 |
| XHigh | 34 | $0.04 |
| Max | 37 | $0.07 |

**Prior:** High/XHigh is an extraordinary worker tier. Max remains cheap enough to use on bounded jobs, but extra reasoning does not make Luna a substitute for an architect.

Independent sources:

- https://artificialanalysis.ai/models/releases/gpt-6-astra
- https://artificialanalysis.ai/models/releases/gpt-6-sol
- https://artificialanalysis.ai/models/releases/gpt-6-luna

## GPT-6 Astra

### Benchmark signal

Astra Max scores 53 on Artificial Analysis v4.3.2.

The more important routing fact is the effort curve: Astra High scores 51 at ~$1.73/task versus Max at 53 and ~$3.26/task.

### Reddit consensus

Strong recurring positives:

- unusually good end-to-end persistence;
- architecture/orchestration;
- difficult debugging;
- repository-wide reasoning;
- computer use;
- research/source work;
- UI/visual judgment.

Strong recurring negatives:

- subscription quota can disappear extremely quickly;
- routine work can become overengineered;
- some users prefer 5.6 Sol's practical intuition on straightforward engineering;
- creative writing is polarized: excellent continuity/style reports coexist with strong guardrail/sanitization complaints.

### Routing prior

**Use when the cost of a wrong global decision exceeds the model cost.**

Prefer Low/Medium first. Do not use Max as a prestige default.

## GPT-6 Sol

### Benchmark signal

Artificial Analysis Max:

- Intelligence Index: 48 vs 5.6 Sol 47;
- Coding Agent Index: 57 vs 55;
- cost/task: ~$1.06 vs ~$1.99.

This is primarily a cost-efficiency upgrade.

Independent testing also found regressions in some knowledge-work evaluations, often from shorter deliverables that omitted rubric elements.

### Reddit consensus

**Provisional and unusually contested.**

Positive:

- much better allowance longevity than Astra;
- compelling API economics;
- likely strong default for sustained agent/coding work;
- some users now run Sol all day and reserve Astra for blockers.

Negative:

- multiple high-engagement r/codex threads report sloppy code;
- more handholding than 5.6 Sol;
- confusing/undoing its own fixes;
- unexpected commits/actions;
- missed skills/tools;
- simple-task failures;
- "improved Terra" is a common early characterization.

This evidence is only about two days old and should not be treated as settled.

### Routing prior

**Test as the new normal serious-engineering model, preferably Medium/High.**

Keep 5.6 Sol as a behavior fallback until personal evidence proves 6 Sol is better in the owner's actual repositories.

## GPT-6 Luna

### Benchmark signal

Luna Max stays at Intelligence Index 37, equal to 5.6 Luna Max, while AA task cost falls from ~$0.18 to ~$0.07.

The Coding Agent Index actually falls two points, so Luna is not an across-the-board capability upgrade.

### Reddit consensus

Early positive signal:

- much less self-directed verbosity than 5.6 Luna;
- impressive bounded coding when given a detailed plan;
- extremely low quota consumption;
- useful worker beneath Sol/Astra;
- real public use in r/codex's Dexter moderator app for classification, strict JSON, OCR, and image interpretation.

Early negative signal:

- some users report instruction misses;
- infrastructure/refactor loops;
- more handholding than 5.6;
- project progress slowing despite cheap usage.

### Routing prior

**Current strongest underdog / efficiency experiment.**

Use for work that is:

- clear;
- bounded;
- cheap to test;
- safe to retry.

Do not infer architecture quality from low cost.

## GPT-5.6 Sol

Artificial Analysis now treats this as superseded by 6 Sol, but it remains useful because its behavior is known.

Stable public + owner evidence supports:

- architecture;
- difficult debugging;
- backend;
- optimization;
- unusual/large codebases;
- orchestration.

Stable complaints:

- quota;
- validation loops;
- overengineering;
- occasional over-broad actions.

### Routing prior

**Known-behavior fallback and proven high-end engineer.**

Do not pay 5.6 API pricing merely from habit if 6 Sol performs equivalently on the target task.

## GPT-5.6 Terra

Terra remains unusually important because there is no GPT-6 Terra.

On public API economics, GPT-6 Sol makes Terra look weak.

But the recurring human argument for Terra is not raw price. It is **prompt convenience**:

> Terra can infer enough from a coherent repository that the user does not need to specify every mechanical detail, without paying Sol/Astra cost.

The owner's Adventurer's Rise evidence strongly supports this.

### Routing prior

**5.6 underdog for moderately ambiguous routine implementation.**

Compare it directly against 6 Sol Medium and 6 Luna Max rather than deleting it from the routing set because of a benchmark chart.

## GPT-5.6 Luna

Established the high-volume worker role.

Strengths:

- bounded implementation;
- background/subagent work;
- transformations;
- cheap review/fix loops.

Weaknesses:

- architecture;
- implicit intent;
- general-chat depth;
- instruction mistakes.

### Routing prior

**Legacy behavior fallback.**

Prefer 6 Luna when it performs equivalently; retain 5.6 when direct evidence says the newer model is less reliable on the task.

## Current underdogs

### 1. GPT-6 Luna

The strongest current cost/quality underdog.

Not because it is secretly a frontier architect, but because a huge share of software work is clear, testable execution.

### 2. GPT-5.6 Terra

Its API Pareto position is weak, but its human-effort position can still be good.

### 3. Astra Low/Medium

Astra's cheaper effort settings are easy to overlook. They retain much of the model's judgment without Max-level burn.

## Current waste traps

A "waste trap" is a routing choice, not a universal model verdict.

- Astra High/Max for routine mechanical implementation.
- Sol Max when High already resolves the task.
- 5.6 Sol API use when 6 Sol is behaviorally equivalent.
- 5.6 Luna API use when 6 Luna is behaviorally equivalent.
- Luna on vague architecture where reviewer/rework cost erases token savings.
- one frontier model acting as architect + coder + reviewer + tester for hours when the work can be split by role.

## Efficiency rule

Do not evaluate "token spinach" using price/token alone.

Track:

1. first-pass acceptance;
2. retries;
3. reviewer cost;
4. human steering;
5. context/cache churn;
6. wall time;
7. regression/rework;
8. subscription quota consumed.

The cheapest token can produce the most expensive finished task.

The expensive model can be cheapest when it prevents an expensive architectural mistake.

## Current provisional routing

- **Astra Medium/High:** architecture, integration, final review.
- **6 Sol Medium/High:** serious daily coding/agent work, pending personal validation.
- **6 Luna High/XHigh:** bulk worker/subagent.
- **5.6 Sol:** proven fallback for difficult engineering where 6 Sol behavior disappoints.
- **5.6 Terra High:** moderately ambiguous routine implementation and low-prompt-overhead work.
- **5.6 Luna:** fallback when 6 Luna's instruction following is worse on a known workflow.

Public evidence does not replace the owner's case corpus.
