# Moonshot / Kimi Baseline

_Last researched: 2026-09-22_

## Current routing summary

| Model | Baseline role | Strong suits | Main weaknesses / cautions |
|---|---|---|---|
| Kimi K3 | Frontier-adjacent open-weight planner/agent/knowledge model | Excellent open-weight intelligence, strong agentic knowledge work, 1M context, vision, coding, open weights | Huge model, slow/expensive to self-host, expensive/slow per task, harness-sensitive thinking history, can be excessively proactive |
| Kimi K2.7 Code | Coding-focused open-weight implementer | Strong long-horizon coding, MCP/agent improvements, more concise than prior K2 generation | General intelligence well below K3/frontier closed models; slower than average; community reports mixed execution consistency |

## Kimi K3

### Independent benchmark signal

Artificial Analysis's current v4.3-era model page reports:

- Intelligence Index: **44**
- among the strongest open-weight models;
- 1M context;
- 2.8T total parameters / about 104B active;
- output speed roughly 40 t/s;
- estimated task cost around $2 in its evaluation.

Earlier in July, K3 was second only to Claude Fable 5 on AA-Briefcase, Artificial Analysis's private agentic knowledge-work benchmark.

Sources:

- https://artificialanalysis.ai/models/kimi-k3
- https://artificialanalysis.ai/articles/kimi-k3-agentic-knowledge-benchmark

### Provider signal

Moonshot describes K3 as:

- 2.8T-parameter open model;
- native vision;
- 1M context;
- designed for long-horizon coding, knowledge work, and reasoning.

Unusually, Moonshot also publishes three explicit limitations:

1. **thinking-history sensitivity** — switching into K3 mid-session or using an incompatible harness can destabilize quality;
2. **excessive proactiveness** — it may make unexpected decisions on ambiguous/minor issues;
3. **UX gap** — Moonshot itself says user experience remains behind Claude Fable 5 and GPT-5.6 Sol.

Source:

- https://www.kimi.ai/blog/kimi-k3

### Human-review signal

Positive themes:

- strong frontend/visual coding;
- some users report Sol/Fable-class performance on real code;
- unusually strong open model for one-shot code generation;
- attractive as a local/open planner if hardware exists.

Negative themes:

- massive local hardware/storage demands;
- self-host speed can be impractical without very large clusters;
- cloud/API long-horizon tasks can burn a lot of tokens/credits;
- some users do not see consistent parity with Fable/Sol;
- planning/delegation may be a better role than direct high-volume local execution.

Representative threads:

- https://www.reddit.com/r/LocalLLaMA/comments/1uymonq/does_k3_really_live_up_to_the_hype_real_world/
- https://www.reddit.com/r/LocalLLaMA/comments/1vrupyu/whats_the_verdict_on_kimi_k3_qwen3824t/
- https://www.reddit.com/r/LocalLLaMA/comments/1va0rce/first_kimi_k3_results_on_home_lab_4ts/
- https://www.reddit.com/r/LocalLLaMA/comments/1vatzo6/whats_the_cheapest_way_to_get_kimi_k3_not/
- https://www.reddit.com/r/LocalLLaMA/comments/1v8364f/kimi_k3_weights_now_released/

### Baseline prior

K3 is one of the most interesting models for this repository because it combines:

- open weights;
- frontier-adjacent intelligence;
- agentic knowledge work;
- long context;
- native multimodality.

Use it with a **verified compatible harness** and explicit authority boundaries.

Potential best role:

> planner / researcher / high-level coding agent feeding cheaper/faster implementation workers.

For local use, the model's enormous footprint may make cloud access more practical than ownership despite the open weights.

---

## Kimi K2.7 Code

### Independent benchmark signal

Artificial Analysis currently reports:

- Intelligence Index: **26**
- 256K context
- around 62 t/s
- relatively concise compared with many reasoning models
- roughly $0.54 per Intelligence Index task

This broad index undersells its purpose: it is a specialized coding model, not Kimi's general frontier model.

Source:

- https://artificialanalysis.ai/models/kimi-k2-7-code/

### Provider/model-card signal

Moonshot reports substantial gains from K2.6 on coding/agent benchmarks while using about 30% fewer thinking tokens.

Published model-card comparisons include:

- Kimi Code Bench v2: 62.0 vs GPT-5.5 69.0 and Opus 4.8 67.4
- Program Bench: 53.6 vs 69.1 / 63.8
- MCP Atlas: 76.0 vs 79.4 / 81.3
- MCP Mark Verified: 81.1 vs 92.9 / 76.4

These are provider-published comparisons and harness choices differ.

Sources:

- https://www.kimi.ai/resources/kimi-k2-7-code
- https://huggingface.co/moonshotai/Kimi-K2.7-Code

### Human-review signal

Community reports are mixed but suggest a useful niche:

Positive themes:

- strong implementation worker in established codebases;
- good value when a stronger model supplies the plan;
- capable of long coding sessions.

Negative themes:

- some users report hesitation or "advice instead of execute" behavior;
- overscanning/token waste;
- usage limits or practical token burn can be worse than expected;
- some prefer K2.6 or DeepSeek for reliability/value.

### Baseline prior

Use K2.7 Code as an **implementation specialist**, not a general strategist.

Promising workflow:

> Opus/Fable/Sol/K3 plans and reviews → K2.7 Code executes.
