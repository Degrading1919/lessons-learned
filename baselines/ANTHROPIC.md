# Anthropic / Claude Baseline

_Last researched: 2026-11-11_

For the September family baseline, see the [2026-09-24 Anthropic field guide](../research/anthropic/2026-09-24-reddit-field-guide.md).  
For the latest release delta, see [2026-10-04 model release update](../research/models/2026-10-04-new-model-release-update.md).

## Current routing summary

| Model | Public-prior role | Strong suits | Main cautions | Confidence |
|---|---|---|---|---|
| **Claude Opus 5.5** | High-judgment architect / reviewer / premium daily model | ambiguous coding, architecture, UI judgment, collaboration | expensive, still premium quota | Medium-high |
| **Claude Sonnet 5.5** | Implementation worker / well-scoped daily model | coding, bug fixing, terminal work, design, fast iteration | Max is extraordinarily token-heavy | Medium-high |
| **Claude Fable 5.2** | New hardest-problem advisor/orchestrator | top independent v5.0.1 technical score, difficult engineering, deep analysis | extremely expensive at XHigh/Max; launch quota complaints; no canon-writing verdict | Medium benchmark / Low community |
| **Claude Fable 5.1** | Previous-generation reference | historical deep planning/review, constrained storytelling | higher list prices; v4.3 benchmark not directly comparable | High historical |
| **Claude Opus 4.8** | Behavioral fallback | practical Claude Code judgment, environment integration | older, expensive | High owner/community |
| **Claude Sonnet 5** | Superseded mid-tier | historical bounded work | substantially weaker than 5.5; Max was token-heavy | Historical |
| **Claude Opus 5** | Adversarial-QA niche | skeptical reasoning | poor collaboration reputation | High negative prior |
| **Claude Haiku 5.5** | Current cheap utility/subagent tier | 1M context, extraction, classification, retrieval, compaction, focused code | low-cost work does not establish lore prose or quest quality | Medium-high |
| **Claude Haiku 4.5** | Older utility reference | historical search/read/classify behavior | removed from some Claude selectors on October 29; old chats now run 5.5 | High historical |
| **Claude Mythos 5.2** | Restricted trusted-access counterpart of Fable 5.2 | approved cybersecurity/life-science research | not a consumer general model | Medium |
| **Claude Mythos 5.1** | Previous restricted reference | historical approved workflows | replaced by Mythos 5.2 | Medium historical |

**Current-model correction (Nov 8):** Haiku 5.5 **released October 7**; Sonnet 5.5 cached-input reads also dropped from $0.20 to $0.10/M that day. Anthropic removed Haiku 4.5 from several Claude chat model selectors October 29, and continuing an old Haiku conversation may use 5.5. See [November 8 Opus behavior and narrative review](../research/writing/2026-11-08-opus-5-5-regression-and-caelmor-options.md). These are confirmed service/model-option changes, not proof of a broad quality nerf.

## Current API economics

| Model | Input / 1M | Cache read / 1M | Output / 1M |
|---|---:|---:|---:|
| Opus 5.5 | $4.00 | $0.20 | $20.00 |
| Sonnet 5.5 | $2.00 | $0.10 | $10.00 |
| **Fable 5.2** | **$8.00** | **$0.20** | **$40.00** |
| Fable 5.1 | $10.00 | $0.25 | $50.00 |
| Opus 4.8 | $5.00 | $0.50 | $25.00 |
| Haiku 5.5 (prompts ≤100K tokens) | $0.10 | $0.01 | $0.50 |
| Haiku 5.5 (prompts >100K tokens) | $0.50 | $0.05 | $2.50 |
| Haiku 4.5 | $1.00 | $0.10 | $5.00 |

## November 11: Claude Fable 5.2 release baseline

Released **November 9, 2026**; model ID `claude-fable-5-2`, 1M input context and 128K max output, always-on adaptive reasoning. Its **API default effort is High**; confirm actual effort in the Claude app/Code. List API prices are $8/M fresh input, $0.20/M cached read and $40/M output. Optional fast mode ($16/$80) is a throughput premium, not an economy setting.

### Independent benchmark v5.0.1

| Effort | Intelligence Index | AA estimated cost/task |
|---|---:|---:|
| Low | 54 | $3.10 |
| Medium | 56 | $3.80 |
| High | 62 | $9.08 |
| XHigh | 62 | $14.83 |
| Max | **65 (#1)** | **$26.54** |

**Do not compare v5 index numbers directly with the historical Fable 5.1 v4.3 score of 53.** High is the strongest first choice for *difficult* work; Medium often has better marginal economics; XHigh/Max require task-specific evidence. Independent Max output was approximately **274K tokens per benchmark task**, so the 20% list-price reduction from 5.1 does not imply lower completed-task cost.

### Forum consensus (only two days; provisional)

Some users report better speed, reasoning and hard-task handling than 5.1. Others describe **whole five-hour limits exhausted within minutes**, unhelpful compaction, over-delegation, confident errors or no practical advantage over Opus 5.5. Anthropic also acknowledged **fixing some issues that over-consumed limits** and issued an additional all-model reset on November 10, confounding launch-day quotas.

### Caelmor / creative writing

One privately run **ToneBench script-writing** study placed Fable 5.2 XHigh at 2676 Elo vs High 2520 and Max 2651, but **did not find improved tone adherence** over 5.1. Its author still favored Opus 5.5 XHigh for similar quality at less than half the measured cost. This is model-judged and partially judge-sensitive, not an owner or blind human canon test. Route **Fable 5.2 Medium/High** to unusually tangled quest logic or source conflict; keep Opus/Gemini as initial prose authors.

**Subscription limit:** Fable is normally pay-as-you-go on Claude Pro (temporarily included until November 16); on Max/Ultra it draws from the shared weekly pool, with a Fable usage cap of up to 50% of that pool, not an extra allowance. See [official Fable plan and launch offer](https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers).

**Evidence, full citations, pros/cons and operating recommendations:** [November 11 Fable 5.2 release research](../research/models/2026-11-11-claude-fable-5-2-release-baseline.md).

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

## Claude Fable 5.1 (historical)

Previous-generation scarce planning/review resource, especially for low-level work and deep research. It is not the default implementation model.

## Current Anthropic routing

- **Opus 5.5 Medium/High:** architecture, ambiguous work, final review.
- **Sonnet 5.5 Medium/High:** well-scoped implementation and bug fixing.
- **Fable 5.2 Medium/High:** hardest planning, research, low-level diagnosis, canon/quest consistency review; only escalate after measurable need. Keep Fable 5.1 as historical comparator.
- **Opus 4.8:** owner-proven behavioral fallback.
- **Haiku 5.5:** high-volume source extraction, triage, classification and explore; not final fantasy authorship.

Public evidence does not replace personal cases.
