# Methodology

## Goal

This repository is a personal empirical record of AI performance on real work. It is designed to answer model-routing and tasking questions using project evidence rather than generic benchmark scores.

The unit of analysis is a **case**, not a model.

A case is a task/outcome pair with enough context to explain why the result should or should not influence future model choice.

## Evidence hierarchy

### Level A — strongest

Contains all or nearly all of:

- prompt/task or durable task instructions
- named model/tool
- repository or artifact output
- automated verification and/or real playtest
- direct user reaction
- downstream consequence, such as merge, correction, reuse, or workflow change

### Level B — useful

Contains a concrete artifact and either strong verification or clear human feedback, but not the complete chain.

### Level C — anecdotal / incomplete

Contains a useful observation but lacks enough prompt, artifact, verification, or user-response evidence to support a strong model-selection conclusion.

Do not silently promote Level C evidence into a model recommendation.

## What gets recorded

Each case should capture:

- date
- project
- model/tool
- exact model/effort label when known
- task categories
- source-of-truth context available to the model
- prompt/tasking pattern
- autonomy level
- tools/connectors/MCP available
- artifact links
- tests/build/playtest/review evidence
- direct human preference signal
- failures or corrections
- supported lesson
- confidence/evidence level

## Causal discipline

Do not write "Model X is good at coding" because one PR succeeded.

Prefer:

> Under a repository-grounded, end-to-end implementation task with explicit hard boundaries and permission to continue without milestone approval, Model X produced a coherent implementation that passed these checks and received this user reaction.

A result may be caused by:

- model capability
- effort/reasoning setting
- repository quality
- prompt structure
- task decomposition
- tool access
- existing tests
- MCP/IDE/runtime access
- reviewer quality
- human playtesting
- luck or unobserved state

The repository should preserve these variables instead of collapsing them into a single score.

## Human preference signals

User reactions are first-class evidence.

Examples:

- accepted without revision
- "surprisingly good"
- "actually incredible"
- rejected as too verbose
- rejected as too prescriptive
- rejected visual output as unusable
- required architectural correction
- preferred one model's judgment over another
- judged a workflow too expensive for the result
- changed future workflow because of the result

Paraphrase when exact transcript preservation is unnecessary. Preserve short exact wording only when it materially captures the preference signal.

## Merge status is not correctness

A merged PR proves adoption, not perfection.

Record later discoveries against the original case:

- runtime bugs
- playtest friction
- architecture drift
- hidden scope gaps
- test blind spots
- token/quota cost
- manual cleanup

This allows a case conclusion to evolve.

## Negative evidence matters

Failures are not noise.

Examples from the current corpus include:

- a task prompt that was too prescriptive and encouraged artificial stopping
- a long-running end-to-end agent run with poor quota efficiency
- green tests that still left playtest failures
- 3D prompting that produced an unacceptable visual result
- invented repository paths in downstream prompting
- concurrent AI/Blender/Unity workloads causing local resource pressure

Record the failure and the correction that followed.

## Model labels

Store model labels exactly as observed in the session when possible, for example:

- GPT-5.6 Sol Max
- GPT-5.6 Terra High
- Astra Low
- Claude Opus 4.8 High

These labels are historical observations. Vendor naming, availability, and behavior may change.

## External AI tools

For tools whose full conversation history is unavailable, such as Claude Code or Tripo 3D, build the chain from:

1. the prompt/task authored in ChatGPT
2. the downstream repository artifact, PR, commit, or asset metadata
3. the user's report/reaction after execution
4. later review/playtest evidence

This is sufficient to create a useful case even without the external platform transcript.

## Dataset policy

`datasets/cases.jsonl` is derived evaluation/preference data.

It is not presented as a statistically balanced benchmark or production-ready RLHF dataset. It is a structured personal corpus suitable for:

- retrieval
- qualitative preference analysis
- routing heuristics
- future pairwise-preference construction
- prompt-pattern analysis
- longitudinal model comparisons

Do not invent missing ratings. Use null/unknown fields or lower evidence confidence.
