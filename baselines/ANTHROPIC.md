# Anthropic / Claude Baseline

_Last researched: 2026-11-08_

For the September family baseline, see the [2026-09-24 Anthropic field guide](../research/anthropic/2026-09-24-reddit-field-guide.md).  
For the latest release delta, see [2026-10-04 model release update](../research/models/2026-10-04-new-model-release-update.md).

## Current routing summary

| Model | Public-prior role | Strong suits | Main cautions | Confidence |
|---|---|---|---|---|
| **Claude Opus 5.5** | High-judgment architect / reviewer / premium daily model | ambiguous coding, architecture, UI judgment, collaboration | expensive, still premium quota | Medium-high |
| **Claude Sonnet 5.5** | Implementation worker / well-scoped daily model | coding, bug fixing, terminal work, design, fast iteration | Max is extraordinarily token-heavy | Medium-high |
| **Claude Fable 5.1** | Scarce deep planner/reviewer | low-level code, orchestration, research | very expensive | High |
| **Claude Opus 4.8** | Behavioral fallback | practical Claude Code judgment, environment integration | older, expensive | High owner/community |
| **Claude Sonnet 5** | Superseded mid-tier | historical bounded work | substantially weaker than 5.5; Max was token-heavy | Historical |
| **Claude Opus 5** | Adversarial-QA niche | skeptical reasoning | poor collaboration reputation | High negative prior |
| **Claude Haiku 5.5** | Current cheap utility/subagent tier | 1M context, extraction, classification, retrieval, compaction, focused code | low-cost work does not establish lore prose or quest quality | Medium-high |
| **Claude Haiku 4.5** | Older utility reference | historical search/read/classify behavior | removed from some Claude selectors on October 29; old chats now run 5.5 | High historical |
| **Claude Mythos 5.1** | Restricted trusted-access specialist | authorized high-risk workflows | not normal routing tier | Medium |

**Current-model correction (Nov 8):** Haiku 5.5 **released October 7**; Sonnet 5.5 cached-input reads also dropped from $0.20 to $0.10/M that day. Anthropic removed Haiku 4.5 from several Claude chat model selectors October 29, and continuing an old Haiku conversation may use 5.5. See [November 8 Opus behavior and narrative review](../research/writing/2026-11-08-opus-5-5-regression-and-caelmor-options.md). These are confirmed service/model-option changes, not proof of a broad quality nerf.

## Current API economics

| Model | Input / 1M | Cache read / 1M | Output / 1M |
|---|---:|---:|---:|
| Opus 5.5 | $4.00 | $0.20 | $20.00 |
| Sonnet 5.5 | $2.00 | $0.10 | $10.00 |
| Fable 5.1 | $10.00 | $0.25 | $50.00 |
| Opus 4.8 | $5.00 | $0.50 | $25.00 |
| Haiku 5.5 (prompts ≤100K tokens) | $0.10 | $0.01 | $0.50 |
| Haiku 5.5 (prompts >100K tokens) | $0.50 | $0.05 | $2.50 |
| Haiku 4.5 | $1.00 | $0.10 | $5.00 |

## November 8: disputed Opus 5.5 behavior and narrative routing

Early-November Claude Code users report instruction/reasoning changes, with a Nov 8 observational report identifying a possible Nov 3 shift; a longitudinal pinned-model general-accuracy test provides counterevidence and has not finished the post-November-3 interval. No public evidence proves a weight-level nerf or degraded Caelmor literary performance. Explicitly compare **Opus 5.5 High versus XHigh** in fresh sessions with frozen source packets before changing the incumbent writing model.

For fantasy lore/dialogue, blind human preference currently puts **Gemini 4 Argon High and Opus 5.5 High in the leading overlapping interval**, with Astra and Fable strong on different model-judged short/long creative evaluations. Keep independent canon checks and Creative Director approval.

Sources: [November 8 evidence review](../research/writing/2026-11-08-opus-5-5-regression-and-caelmor-options.md), [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).

## Claude Sonnet 5.5

Released September 28.

Anthropic positions it as the faster/lower-cost complement to Opus 5.5 for well-scoped everyday tasks, bug fixes, polished artifacts, and design. Anthropic says it runs 30%+ faster and can cost up to 30% less for most work than Sonnet 5.

Source:

- https://www.anthropic.com/claude-sonnet-5-5

### Independent benchmark prior

Artificial Analysis:

| Effort | Intelligence Index | Approx. AA cost/task |
|---|---:|---:|
| Low | 36 | $0.42 |
| Medium | 41 | $0.59 |
| High | 47 | $1.12 |
| XHigh | 52 | $2.75 |
| Max | 56 | $7.67 |

At Max, Sonnet 5.5 used roughly **193k output tokens per Intelligence Index task**, the highest Artificial Analysis had measured and about seven times Astra Max.

It reaches frontier-like benchmark quality by spending an extraordinary amount of reasoning/output at Max.

Source:

- https://artificialanalysis.ai/articles/claude-sonnet-5-5/

### Community consensus

The clearest emerging workflow is:

> **Opus 5.5 plans/reviews → Sonnet 5.5 implements.**

Positive themes:

- excellent well-scoped coding;
- strong bug fixing;
- fast iteration;
- strong UI/design/front-end output;
- materially better than Sonnet 5.

One community A/B across repeated real coding tasks reported equal pass rates between Sonnet 5.5 High and Opus 5.5 High on that sample, with Sonnet finishing faster and cheaper. This remains one user's workload, not a universal benchmark.

Negative/caution themes:

- XHigh/Max can fan out or think so much that task cost explodes;
- some noncoding users find it cautious/hedgy;
- harness/subagent behavior can dominate the apparent model cost.

### Routing prior

**Sonnet 5.5 Medium/High is the current Anthropic implementation-worker default prior.**

Use Opus 5.5 where ambiguity, architecture, or final judgment matters more than throughput.

Avoid Max by default.

## Claude Opus 5.5

Retains the premium judgment role.

Use for:

- architecture;
- ambiguous implementation;
- final review;
- UI/product judgment;
- difficult debugging.

The release of Sonnet 5.5 makes it easier to stop wasting Opus quota on mechanical work.

## Claude Fable 5.1

Still a scarce planning/review resource, especially for low-level work and deep research. It is not the default implementation model.

## Current Anthropic routing

- **Opus 5.5 Medium/High:** architecture, ambiguous work, final review.
- **Sonnet 5.5 Medium/High:** well-scoped implementation and bug fixing.
- **Fable 5.1 High/XHigh:** hard planning/research/low-level diagnosis.
- **Opus 4.8:** owner-proven behavioral fallback.
- **Haiku 5.5:** high-volume source extraction, triage, classification and explore; not final fantasy authorship.

Public evidence does not replace personal cases.
