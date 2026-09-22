# Meta Baseline

_Last researched: 2026-09-22_

Meta currently has two very different model stories:

1. **Muse Spark 1.3** — a competitive proprietary reasoning/coding model.
2. **Llama 4 Scout/Maverick** — older open-weight multimodal models whose intelligence has fallen far behind the 2026 frontier.

Do not conflate them.

## Current routing summary

| Model | Baseline role | Strong suits | Main weaknesses / cautions |
|---|---|---|---|
| Muse Spark 1.3 | Fast lower-cost coding/agent model | Strong broad benchmarks, fast output, 1M multimodal context, competitive coding/knowledge work | Human trust lags benchmarks; reports of hallucination/forgetting and extra handholding; weights still not generally available |
| Llama 4 Maverick | Open-weight multimodal deployment where control matters more than frontier intelligence | Open weights, inexpensive inference, image/text, 1M context | Far behind current reasoning frontier; weak coding reputation |
| Llama 4 Scout | Extreme-context/open-weight niche | 10M context, multimodal, comparatively efficient deployment for size | Very weak current intelligence/coding baseline; context length does not imply context quality |

## Muse Spark 1.3

### Independent benchmark signal

Artificial Analysis v4.3 reports Muse Spark 1.3 Max at **48**, behind Astra/Fable 5.1 (53) and Opus 5 (51) but ahead of GPT-5.6 Sol (47).

Model-page data also reports:

- around 241 t/s output speed;
- 1M context;
- text/image/video input;
- roughly $1.60 per Intelligence Index task at max effort.

Sources:

- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3
- https://artificialanalysis.ai/models/muse-spark-1-3

### Provider signal

Meta describes Spark 1.3 as trained for:

- long-horizon agentic workflows;
- context tracking across prior results;
- coding with fewer unnecessary turns;
- native multimodal perception.

Source:

- https://ai.meta.com/llama

### Human-review signal

This is currently one of the strongest **benchmark-vs-forum caution cases**.

Positive themes:

- fast;
- inexpensive buffer model when frontier subscriptions run out;
- good simple implementation with a strong prompt;
- some users report near-Opus usefulness inside a capable harness.

Negative themes:

- surprisingly little organic discussion relative to benchmark position;
- reports of needing multiple follow-up prompts to finish reports;
- hallucination/forgetfulness complaints;
- some users call it "benchmaxxed" and poor as the primary agent while still useful as a subagent;
- frustration that promised open weights have not materialized on the expected cadence.

Representative threads:

- https://www.reddit.com/r/MetaAI/comments/1vlfm2x/muse_code_and_spark_is_pretty_crap/
- https://www.reddit.com/r/MetaAI/comments/1wjiq69/how_good_is_muse_spark/
- https://www.reddit.com/r/LocalLLaMA/comments/1whqm2c/hey_meta_wheres_those_muse_spark_weights/
- https://www.reddit.com/r/opencodeCLI/comments/1w48fbk/meta_introduced_coding_plans_for_muse_spark_12/

### Baseline prior

**Worth testing, but do not trust the leaderboard alone.**

Best provisional role:

- implementation/subagent buffer;
- high-throughput review/classification;
- lower-cost tool-using work.

Require strong verification before giving it sole ownership of a complex repo.

This model should be a priority for a controlled personal A/B test because public benchmark rank and forum confidence diverge significantly.

---

## Llama 4 Maverick

### Independent benchmark signal

Current Artificial Analysis places Maverick at only **10** on its Intelligence Index, below the current frontier by a very large margin.

It retains:

- open weights;
- native text/image input;
- 1M context;
- relatively low inference cost.

Source:

- https://artificialanalysis.ai/models/llama-4-maverick

### Human-review signal

Early LocalLLaMA coding reviews were heavily negative, with users comparing its coding ability unfavorably to much smaller models.

Some later testing showed that inference implementation bugs materially hurt early evaluations, and corrected inference improved particular benchmark results.

Representative threads:

- https://www.reddit.com/r/LocalLLaMA/comments/1jsl37d/im_incredibly_disappointed_with_llama4/
- https://www.reddit.com/r/LocalLLaMA/comments/1jy0zjw/gave_maverick_another_shot_much_better/

### Baseline prior

Use for **open-weight control, multimodal deployment, or cost/privacy needs**, not because it is a frontier coding/reasoning model in 2026.

---

## Llama 4 Scout

### Independent benchmark signal

Artificial Analysis currently reports Scout at **8**.

Its differentiator is not intelligence; it is architecture/deployment:

- 109B total / 17B active parameters;
- text + image;
- **10M context window**;
- designed for comparatively efficient deployment.

Sources:

- https://artificialanalysis.ai/models/llama-4-scout/
- https://ai.meta.com/llama/get-started/

### Human-review signal

Coding reception was weak at launch.

The open-model community still values Scout as an experiment in extreme context and efficient MoE deployment, but those are different strengths from instruction-following or software-engineering quality.

### Baseline prior

Scout is a **specialized open-weight context/deployment option**, not a default agent model.

Do not confuse "10M context" with "can reason reliably over 10M tokens."
