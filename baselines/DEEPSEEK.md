# DeepSeek Baseline

_Last researched: 2026-09-22_

## Current routing summary

| Model | Baseline role | Strong suits | Main weaknesses / cautions |
|---|---|---|---|
| DeepSeek V4.1 Flash | Cheap/fast coding and agentic execution; open-weight workhorse | Very high throughput, excellent cost, 1M context, strong DeepSWE/automation, MIT weights, multimodal | Very verbose reasoning; scope creep/side quests; mixed tutoring/creative quality; needs strict boundaries |
| DeepSeek V4 Pro | Reference/premium V4 tier | Stronger than older Flash on some reasoning/knowledge tasks | V4.1 Flash now challenges/surpasses it on many practical metrics; product tier is in transition |

## DeepSeek V4.1 Flash

### Independent benchmark signal

Artificial Analysis currently reports:

- Intelligence Index: **39**
- AutomationBench-AA: **69%**
- Terminal-Bench 4.0: **27%**
- SciCode: **52%**
- AA-LCR: **84%**
- output speed: roughly **226–239 t/s**
- context: **1M**
- open weights, MIT license

It is not at the Astra/Fable broad-intelligence frontier, but it is exceptionally competitive for an open model at its price and speed.

Sources:

- https://artificialanalysis.ai/models/deepseek-v4-1-flash
- https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-deepseek-v4-flash

### Provider signal

DeepSeek reports:

- 552B total MoE;
- 8B active for input / 16B for output;
- native vision;
- DeepSWE v1.1: 74.2;
- Terminal-Bench 2.1: 90.6;
- Automation-Bench: 54.8;
- materially smaller KV cache than prior generation.

DeepSeek initially said V4.1 Flash would replace V4 Pro routing; its API changelog later states V4 Pro remains available in response to user demand.

Sources:

- https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- https://api-docs.deepseek.com/updates/

### Human-review signal

Positive themes are unusually strong around **speed and coding value**:

- difficult debugging solved cheaply;
- strong Python/low-level technical work;
- much faster and lower-token than earlier Flash in informal comparisons;
- attractive open/local ecosystem.

Negative themes:

- cheap per token does not always mean cheap per completed task;
- can chase side quests and make more calls than frontier models;
- tendency toward nested branches, one-off fixes, or patching symptoms rather than abstractions in some user reports;
- study/tutoring and creative-writing users report shallower responses;
- state/repetition behavior changed enough that some existing applications regressed.

Representative threads:

- https://www.reddit.com/r/DeepSeek/comments/1wcbz1z/im_in_love_with_v41_for_coding/
- https://www.reddit.com/r/DeepSeek/comments/1watjcl/deepseek_v41_flash_vs_v4_flash_vision_exp_38/
- https://www.reddit.com/r/DeepSeek/comments/1wdd9hh/deepseek_v41_flash_is_cheap_per_tokenbut_is_it/
- https://www.reddit.com/r/DeepSeek/comments/1wcht7m/deepseek_flash_41_the_worst_version_of_deepseek/
- https://www.reddit.com/r/DeepSeek/comments/1wgvgm5/deepseek_v41_flash_is_a_downgrade_on_creativity/

### Baseline prior

Very strong candidate for:

- coding worker/subagent;
- bulk implementation;
- cheap second opinion;
- long-context technical synthesis;
- open-weight research/deployment where infrastructure exists.

Use stricter task boundaries than with a frontier planner.

A promising role split is:

> stronger model defines architecture and invariants → DeepSeek V4.1 Flash implements/tests → independent reviewer checks abstraction quality.

---

## DeepSeek V4 Pro

V4 Pro remains available, but V4.1 Flash has complicated its role.

DeepSeek says V4.1 Flash beats V4 Pro on several practical dimensions and originally planned to route Pro requests to Flash temporarily. The September 10 changelog later says Pro remains because of demand.

Current Artificial Analysis v4.3 lists DeepSeek V4 Pro 0813 Max at **36**, while V4.1 Flash's current model page reports 39.

Sources:

- https://api-docs.deepseek.com/updates/
- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3

### Baseline prior

Treat V4 Pro as a **transition/reference model**, not the default DeepSeek recommendation.

Re-evaluate when V4.1 Pro arrives.
