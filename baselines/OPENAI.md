# OpenAI Baseline

_Last researched: 2026-10-04_

For historical launch-week detail, see the [2026-09-24 OpenAI field guide](../research/openai/2026-09-24-reddit-field-guide.md).  
For the latest release delta, see [2026-10-04 model release update](../research/models/2026-10-04-new-model-release-update.md).

## Current general-purpose routing set

| Model | Public-prior role | Strong suits | Main cautions | Confidence |
|---|---|---|---|---|
| **GPT-6 Astra** | Scarce architect / integrator / final reviewer | highest judgment, ambiguous end-to-end work, computer use, research | expensive, quota-heavy, can overbuild | High |
| **GPT-6.1 Sol** | Serious daily engineering default candidate | near-Astra intelligence, coding agents, terminal work, strong cost/quality | materially slower than 6.0 Sol; some under-execution/tool complaints | Medium-high |
| **GPT-6 Luna** | High-volume worker / subagent | bounded implementation, tests, docs, transforms, classification | not an architect; instruction following remains task-dependent | Medium-high |
| **GPT-6 Sol** | Superseded transition model | historically strong cost-balanced coding | replaced after seven days by 6.1 Sol | Historical |
| **GPT-5.6 Sol** | Known-behavior fallback | difficult debugging, architecture, backend | costly versus 6.1 | High historical |
| **GPT-5.6 Terra** | Forgiving implementation underdog | moderately ambiguous repo work, lower prompting burden | weak current API Pareto position | High owner evidence |
| **GPT-5.6 Luna** | Legacy worker fallback | bounded cheap work | economically superseded by 6 Luna | High historical |

## Current API economics

| Model | Input / 1M | Cached input / 1M | Output / 1M |
|---|---:|---:|---:|
| GPT-6 Astra | $10.00 | $1.00 | $50.00 |
| GPT-6.1 Sol | $2.00 | $0.10 | $10.00 |
| GPT-6 Sol | $2.00 | $0.20 | $10.00 |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |

OpenAI now explicitly recommends Astra for the most demanding work, GPT-6.1 Sol for near-Astra complex work at lower cost, and Luna for focused high-volume work.

Sources:

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/changelog

## GPT-6.1 Sol

Released September 29, only seven days after GPT-6 Sol.

### Independent benchmark prior

Artificial Analysis currently reports:

| Effort | Intelligence Index | Approx. AA cost/task |
|---|---:|---:|
| Low | 42 | $0.13 |
| Medium | 48 | $0.21 |
| High | 50 | $0.32 |
| XHigh | 51 | $0.39 |
| Max | 52 | $0.72 |

Astra Max is 53 at about $3.26/task.

**Interpretation:** 6.1 Sol is now the strongest OpenAI price/performance candidate for serious work. High/XHigh look more rational than reflexive Max.

Artificial Analysis also found 6.1 Sol using roughly 10–30% more output tokens than 6 Sol, so the improvement is not simply "less spinach." It buys more useful capability per dollar/task.

Source:

- https://artificialanalysis.ai/articles/gpt-6-1-sol-replaces-gpt-6-sol-after-just-7-days-with-near-astra-intelligence/

### Community consensus

Positive themes:

- much better than GPT-6 Sol;
- extremely light subscription usage;
- feels like a real successor to 5.6 Sol;
- strong backend/workhorse behavior;
- users report hours of work where Astra would exhaust a window quickly.

Negative themes:

- the dominant complaint is **speed**;
- multiple users report 2–3x slower visible generation than older Sol variants;
- some reports of under-execution, over-investigation, weak frontend output, or questionable verification;
- launch-week service capacity may be confounding model latency.

The strongest consensus is roughly:

> very good work per quota, but potentially poor work per wall-clock hour.

### Routing prior

**GPT-6.1 Sol High** is the current OpenAI default candidate for serious daily engineering.

Use XHigh for hard coding/integration when the extra depth is useful. Keep Astra for the hardest judgment/architecture. Use Luna for cheap bounded workers.

Do not discard 5.6 Sol/Terra personal evidence until matched owner tests establish the replacement.

## GPT-6 Astra

Astra remains the high-judgment tier.

Use it where:

- ambiguity is extreme;
- the task crosses many systems;
- a wrong architecture decision is expensive;
- final independent review has high leverage.

Medium/High remains the public efficiency prior; Max is not a prestige default.

## GPT-6 Luna

Luna remains the best OpenAI high-volume worker prior.

Use for:

- clear implementation;
- tests;
- docs;
- extraction/transformation;
- classification;
- background/subagent work.

Cheap verification is the condition that makes Luna cheap completed work.

## Superseded model note

GPT-6 Sol remains in the corpus because its September launch evidence matters historically, but OpenAI's own model page now directs users to GPT-6.1 Sol.

Historical cases must keep their original model label.

## Current owner-oriented OpenAI routing

- **Astra Medium/High:** architecture, extreme ambiguity, final review.
- **GPT-6.1 Sol High/XHigh:** serious daily coding and agent work.
- **GPT-6 Luna High/XHigh:** bounded worker/subagent work.
- **GPT-5.6 Sol/Terra:** known-behavior fallbacks until owner A/B evidence says otherwise.

Public evidence does not replace personal project evidence.
