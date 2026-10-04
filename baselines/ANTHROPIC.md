# Anthropic / Claude Baseline

_Last researched: 2026-10-04_

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
| **Claude Haiku 4.5** | Utility search/read/classify worker | retrieval/explore | weak modern deep coding | High |
| **Claude Mythos 5.1** | Restricted trusted-access specialist | authorized high-risk workflows | not normal routing tier | Medium |

**Watch:** Anthropic says Haiku 5.5 is coming in the following weeks. It is not yet a current baseline.

## Current API economics

| Model | Input / 1M | Cache read / 1M | Output / 1M |
|---|---:|---:|---:|
| Opus 5.5 | $4.00 | $0.20 | $20.00 |
| Sonnet 5.5 | $2.00 | $0.20 | $10.00 |
| Fable 5.1 | $10.00 | $0.25 | $50.00 |
| Opus 4.8 | $5.00 | $0.50 | $25.00 |
| Haiku 4.5 | $1.00 | $0.10 | $5.00 |

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
- **Haiku 4.5:** search/read/classify/explore until Haiku 5.5 actually releases.

Public evidence does not replace personal cases.
