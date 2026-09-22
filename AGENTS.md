# AGENTS.md

## Purpose

This repository is an evidence corpus about the project owner's real use of AI models and agentic tools.

Do not turn it into a generic AI-news, benchmark, or model-ranking repository.

## Required skill

Before adding, revising, auditing, or comparing substantive lessons, read and follow `.agents/skills/lessons-learned-recorder/SKILL.md`.

That skill governs evidence reconstruction, prompt lineage, public-prior comparison, dataset updates, privacy, and the quality gate.

## Primary question

For a real task the project owner performs:

> Which model/tool/workflow has produced the strongest result under comparable conditions, and what tasking pattern made that result more or less successful?

## Required evidence chain

When adding a substantive lesson, look for this chain:

1. prompt/task/instructions before execution
2. model/tool and effort label if known
3. source-of-truth context and tool access
4. artifact produced
5. verification performed
6. project owner's reaction after seeing/using the result
7. later corrections or downstream consequences
8. narrow lesson supported by the evidence

Do not infer a universal model ranking from one project.

## Repository organization

Primary organization is model/tool first:

- `models/chatgpt/`
- `models/codex/`
- `models/claude/`
- `models/claude-code/`
- `models/tripo-3d/`

Use task tags inside cases.

Cross-model conclusions belong in `cross-model/`.

Project coverage belongs in `projects/`.

Owner-observed machine-readable cases belong in `datasets/cases.jsonl`.

Researched public priors belong in `baselines/` and `datasets/model_baselines.jsonl`; they must never be presented as owner-observed cases.

## Evidence levels

- **A:** prompt/context + artifact + verification + direct human signal, ideally with downstream consequence
- **B:** concrete artifact plus strong verification or human signal, but incomplete chain
- **C:** anecdotal/incomplete; useful to preserve but not strong enough for routing claims

## Update rules

- Preserve exact dates and repository links when known.
- Preserve model labels as observed in the session; do not normalize them into current vendor branding.
- Record negative outcomes and rejected prompts/assets.
- A merged PR is not automatically a successful case.
- A green test suite is not a substitute for product playtesting.
- If later evidence weakens an earlier conclusion, update the case rather than protecting the old conclusion.
- Do not invent token cost, elapsed time, model configuration, verification, or user reaction.
- Do not expose private personal information unrelated to the AI task.
- Prefer links to public GitHub artifacts over copying large code diffs.

## Prompt-lineage rule

When the project owner says a prompt was too verbose, too prescriptive, too vague, or otherwise wrong, preserve both:

- the rejected tasking pattern
- the corrected pattern
- the downstream outcome after correction

Prompt evolution is first-class training evidence.

## External tools

Claude Code and Tripo transcripts may not be available. It is acceptable to reconstruct a case from:

- ChatGPT-authored input prompt
- public repository output
- project-owner post-run report
- later review/playtest

Label evidence confidence accordingly.

## Writing style

Be concise, factual, and causal.

Prefer:

> In project X, under conditions Y, model Z produced outcome A; review found B; the owner changed workflow C.

Avoid:

> Model Z is the best model for coding.
