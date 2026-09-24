# Public Model Baselines

_Last researched: 2026-09-24_

This directory records **research priors** for model routing before the project owner has enough direct evidence to form a personal conclusion.

These files are intentionally separate from `models/<tool>/cases/`.

A baseline answers:

> Based on current independent benchmarks, provider documentation, and real-user reports, what should we tentatively expect this model to be good or bad at?

A personal case answers:

> What actually happened when the project owner used this model/tool on a real task?

Personal evidence is allowed to override a baseline.

## Providers covered

- [OpenAI](OPENAI.md) — current compact baseline; see also the [2026-09-24 OpenAI Reddit/efficiency field guide](../research/openai/2026-09-24-reddit-field-guide.md)
- [Anthropic / Claude](ANTHROPIC.md)
- [Google / Gemini](GOOGLE.md)
- [Meta](META.md)
- [DeepSeek](DEEPSEEK.md)
- [Moonshot / Kimi](KIMI.md)

## Scope rule

This is not an exhaustive catalog of every historical or Hugging Face model.

The initial baseline includes models that are current enough, distinctive enough, or accessible enough to plausibly affect routing decisions:

| Provider | Models / families covered |
|---|---|
| OpenAI | GPT-6 Astra, Sol, Luna; GPT-5.6 Sol, Terra, Luna |
| Anthropic | Claude Fable 5.1 / Mythos 5.1; Claude Opus 5.5; Claude Sonnet 5 |
| Google | Gemini 3.8 Flash; current Pro-model availability caveat |
| Meta | Muse Spark 1.3; Llama 4 Maverick; Llama 4 Scout |
| DeepSeek | DeepSeek V4.1 Flash; V4 Pro as an outgoing/reference tier |
| Moonshot / Kimi | Kimi K3; Kimi K2.7 Code |

## Evidence labels

Each provider file separates:

- **Independent benchmark signal** — strongest public prior.
- **Provider signal** — useful but self-reported.
- **Human-review signal** — Reddit/forum experience; anecdotal, self-selected, and harness-dependent.
- **Baseline routing prior** — a tentative role assignment, not a verdict.

## Benchmark-version warning

Artificial Analysis changed its Intelligence Index to v4.3 in September 2026. Scores from older v4.1/v4.2 releases are not directly comparable with current v4.3 scores.

Prefer current model pages when comparing models today. Preserve older numbers only when reconstructing what the public prior was at the time of a historical case.

## Harness warning

For coding and agent work, the model is only part of the system.

A result can depend heavily on:

- Codex vs Claude Code vs Kimi Code vs Antigravity vs Muse Code;
- reasoning effort;
- tool access and MCP;
- repository instructions;
- context management;
- subagent behavior;
- browser/computer-use implementation;
- caching and quota policy.

Do not convert a harness-specific complaint into a claim about the base model without qualification.

## How these baselines should evolve

When the owner uses one of these models on a meaningful task:

1. preserve the task and result as a personal case;
2. compare the result to this baseline;
3. classify it as confirming, contradicting, adding operational nuance, or not comparable;
4. update the routing guide only when the personal evidence justifies it.
