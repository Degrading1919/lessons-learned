# Lessons Learned: Applied AI and Agentic AI

This repository is a personal evidence base for deciding which AI model, agent, workflow, and prompting style works best for real tasks.

It is not a generic benchmark repository. The evidence comes from actual projects, prompts, code changes, pull requests, playtests, reviews, 3D-production workflows, and direct user feedback.

## Why this exists

Public benchmarks answer questions such as "which model scores highest on benchmark X?"

This repository answers a different question:

> Given the way I actually work, which model or agent should I use for this kind of task, how should I task it, and what failure modes should I expect?

The corpus currently covers work performed with:

- ChatGPT
- Codex
- Claude
- Claude Code
- Tripo 3D

Model names and effort labels are recorded as they appeared in the session when known. They should not be interpreted as permanent vendor-wide rankings.

## Organization

The primary organization is **by model/tool**, because the main use case is model selection.

```text
models/
  chatgpt/
  codex/
  claude/
  claude-code/
  tripo-3d/
cross-model/
projects/
research/
datasets/
templates/
```

Every case is also tagged by task category such as:

- implementation
- architecture
- code review
- debugging
- prompt/task design
- repository governance
- research
- 3D generation
- Blender/Studio integration
- playtest remediation

This gives model-first browsing without losing task context.

## Evidence standard

A strong case should connect as many of these as possible:

1. **Input** — the actual prompt, task brief, or durable repository instructions.
2. **Execution context** — model, effort level, tools, repo state, and relevant constraints.
3. **Artifact** — commit, PR, code, document, build, asset, or generated output.
4. **Verification** — tests, build, playtest, review, or downstream integration.
5. **Human signal** — acceptance, rejection, correction, surprise, frustration, or preference.
6. **Lesson** — a narrow conclusion supported by the evidence.

GitHub output alone is not enough. A merged PR can still have required follow-up. Likewise, a user's positive reaction without an artifact is useful preference data but weaker engineering evidence.

See [METHODOLOGY.md](METHODOLOGY.md). Future agents must also follow [the lessons-learned recorder skill](.agents/skills/lessons-learned-recorder/SKILL.md).

## Current high-confidence findings

The strongest repeated finding is that **task shape and context architecture materially change model performance**.

A broad but well-bounded mission, backed by a strong repository source of truth, has repeatedly outperformed prompts that restate every implementation detail or stop for owner approval at artificial milestones. The September 22, 2026 Agentic AI run is the clearest example: after an overly prescriptive first task was replaced with a mission-oriented end-to-end prompt, a single Codex/Sol Max run produced the local-first orchestration MVP. That result immediately informed Modular CRM's permanent autonomous-tasking guidance.

Other recurring findings:

- Use expensive/high-reasoning models where judgment, integration, or final review is the bottleneck; do not assume they are the best value for routine implementation.
- Separate **authoring** from **review/gating** when the cost of semantic drift is high.
- Repository-local skills and durable instructions are most valuable when they encode repeatable procedures, authority boundaries, and verification, not when they merely repeat project documentation.
- Human playtesting catches classes of failure that green tests do not.
- For generated 3D assets, prompts should optimize for downstream cleanup and reuse rather than pretending text prompts can guarantee topology, rigging, or production readiness.
- A model's successful output is evidence about the complete system — model + prompt + repository + tools + verification loop — not about the model in isolation.

## Project coverage

The initial corpus reviews the user's major AI-assisted projects with sufficient evidence:

- Agentic AI
- Modular CRM
- Adventurer's Rise
- Margins
- The Bible Video Game
- Trading / SwingRank
- Caelmor
- Folio
- Resonant
- Bitburner
- Mystery Pallet Simulator

Forks/reference repositories such as `awesome-llm-apps`, `build-your-own-x`, and `leaked_sys_prompts` are not treated as authored-project outcomes unless a future case specifically uses them as an input.

See [projects/PROJECT_INDEX.md](projects/PROJECT_INDEX.md) for project-level evidence quality, [projects/CHATGPT_PROJECT_AUDIT.md](projects/CHATGPT_PROJECT_AUDIT.md) for the broader cross-domain ChatGPT audit, and [projects/COVERAGE_GAPS.md](projects/COVERAGE_GAPS.md) for known gaps. 

Prompt changes are preserved separately under [evidence/prompt-lineage](evidence/prompt-lineage/) because rejected prompts and their corrected replacements are first-class training evidence.

## Researched model baselines

Current public-research priors for models the owner has not necessarily tested are maintained separately under [baselines/](baselines/README.md).

Initial providers:

- [OpenAI](baselines/OPENAI.md)
- [Anthropic / Claude](baselines/ANTHROPIC.md)
- [Google / Gemini](baselines/GOOGLE.md)
- [Meta](baselines/META.md)
- [DeepSeek](baselines/DEEPSEEK.md)
- [Moonshot / Kimi](baselines/KIMI.md)

These are dated, source-backed starting assumptions based on independent benchmarks, provider documentation, and forum sentiment. They are designed to be replaced or refined by the owner's own project evidence.

For the current OpenAI family, see the [2026-09-24 OpenAI Reddit/efficiency field guide](research/openai/2026-09-24-reddit-field-guide.md), which separates task fit, failure modes, reasoning-effort economics, subscription/API cost, and early GPT-6 launch confidence.

For Anthropic, see the [2026-09-24 Anthropic Reddit/efficiency field guide](research/anthropic/2026-09-24-reddit-field-guide.md), which covers Opus 5.5, Fable 5.1, Opus 5, Sonnet 5, Opus 4.8, Haiku 4.5, and Mythos 5.1.

## Harness efficiency research

Model choice and harness choice are tracked separately.

See:

- [Harness baseline](baselines/HARNESSES.md)
- [2026-09-24 Harness Efficiency Field Guide](research/harnesses/2026-09-24-token-and-window-efficiency.md)
- [Harness A/B Test Protocol](research/harnesses/HARNESS_AB_TEST_PROTOCOL.md)

The harness research compares native Codex and Claude surfaces with Cline, OpenCode, Cursor, and custom API agents. It treats five-hour allowance, API dollars, prompt caching, tool/MCP overhead, subagents, compaction, wall time, and human correction burden as separate variables.

## Public priors vs. personal evidence

Public benchmarks and community sentiment are tracked separately from personal results. See [benchmarks/PUBLIC_PRIORS_VS_PERSONAL_EVIDENCE.md](benchmarks/PUBLIC_PRIORS_VS_PERSONAL_EVIDENCE.md) and the dated [source registry](benchmarks/SOURCES.md).

The rule is simple: public benchmarks establish a prior; the owner's observed project evidence may confirm, contradict, refine, or remain incomparable to it.

## Machine-readable corpus

`datasets/cases.jsonl` mirrors owner-observed prose cases. `datasets/model_baselines.jsonl` stores researched model priors. `datasets/harness_baselines.jsonl` separately stores researched harness priors. Keeping these datasets separate prevents benchmark/forum expectations from being mistaken for personal evidence.

The dataset intentionally records **observed outcomes and human preference signals** rather than turning them into universal model scores.

## Adding a new lesson

Use [templates/CASE_STUDY_TEMPLATE.md](templates/CASE_STUDY_TEMPLATE.md).

Prefer a new case when there is a meaningful task/outcome pair. Update a prior case when later playtesting, review, or integration changes the conclusion.

## Important interpretation rule

Do not read this repository as:

> Model A is better than Model B.

Read it as:

> Under these task conditions, with this context and tool access, this model/workflow produced this result, and this is how the result held up under verification and human use.
