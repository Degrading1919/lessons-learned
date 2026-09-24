---
name: lessons-learned-recorder
description: Repository workflow for auditing and documenting real AI/model/agent performance in lessons-learned. Use whenever adding or revising a model/tool lesson, correlating a ChatGPT prompt with Codex/Claude/Claude Code/Tripo output, reviewing project history for training evidence, comparing personal results with public benchmarks/opinion, or updating the machine-readable cases dataset. Do not use to write generic model rankings, copy benchmark leaderboards without project evidence, or invent missing preference pairs.
---

# Lessons Learned Recorder

Maintain this repository as an evidence-based record of how AI systems actually perform for the project owner.

The goal is not to crown a universal "best model." The goal is to preserve enough evidence that future agents can answer:

> For this kind of real task, under these conditions, what model/tool/workflow worked, what failed, and how should the next task be routed?

## 1. Start with the real evidence, not a public model prior

Before reading benchmark rankings, reconstruct the project event.

Find as much of this chain as possible:

1. original prompt/task/instructions;
2. exact model/tool and effort label, if known;
3. repository/source-of-truth context available at execution time;
4. tools, MCP servers, IDE/runtime access, and relevant hardware/runtime constraints;
5. artifact produced;
6. tests, build, runtime, playtest, review, or downstream integration;
7. the project owner's reaction after seeing or using the result;
8. later corrections, regressions, follow-up PRs, or workflow changes;
9. a narrow lesson supported by that chain.

Do not begin with "Model X is known to be good at coding" and force the case into that belief.

## 2. Decide whether this is a case, an update, or only a note

Create or update a substantive case when there is an identifiable task/outcome pair.

### New case

Use when the task has a distinct objective, output, and user/verification signal.

### Update an existing case

Use when later evidence changes the interpretation:

- a playtest finds a defect;
- a later review finds architecture drift;
- a merged feature breaks downstream composition;
- the user changes their opinion after extended use;
- a later model run provides a matched comparison.

Prefer revising the original conclusion over creating contradictory duplicate cases.

### Coverage note only

Use when evidence is incomplete.

Do not promote sparse anecdote into a routing rule merely to fill the repository.

## 3. Classify evidence strength

Follow `METHODOLOGY.md`.

- **A:** prompt/context + named model/tool + artifact + verification + direct human signal, preferably with downstream consequence.
- **B:** concrete artifact plus strong verification or human signal, but part of the chain is missing.
- **C:** useful anecdote or partial evidence; not enough for strong routing conclusions.

State uncertainty explicitly.

## 4. Preserve prompt lineage when tasking changed

Prompt evolution is first-class evidence.

When the owner rejects a prompt as too verbose, too prescriptive, too vague, too cautious, too autonomous, or otherwise wrong:

1. preserve the rejected tasking pattern;
2. preserve the corrected pattern;
3. record why the owner preferred the correction;
4. record whether each version was actually executed;
5. record downstream outcome differences only when evidenced.

Store substantial prompt evolution under:

`evidence/prompt-lineage/`

A preferred prompt is not automatically evidence that its downstream output is better unless both were executed or a later artifact demonstrates the effect.

## 5. Correlate external AI platforms carefully

For Claude, Claude Code, Tripo, or another platform whose full transcript is unavailable, reconstruct from:

- the input prompt/task authored in ChatGPT or the repository;
- public commit/PR/asset evidence;
- model attribution in commit metadata when present;
- user post-run report;
- reviewer/playtest findings.

Do not invent what the external model "thought" or did between prompt and artifact.

## 6. Treat the harness as part of the system

Always distinguish:

- base model;
- reasoning/effort setting;
- agent harness (Codex, Claude Code, ChatGPT Work, etc.);
- available tools/MCP;
- repository context;
- task autonomy;
- verification loop.

A coding-agent result is evidence about the complete setup, not the model weights alone.

For environment-heavy tasks, explicitly record whether the model could inspect or manipulate:

- Roblox Studio;
- Blender;
- Unity;
- browser/runtime;
- local shell;
- databases;
- GitHub;
- other MCP-connected systems.

## 7. Record cost and resource behavior when known

Cost is part of observed performance.

Record only evidence the owner actually supplied or that the platform exposes:

- usage-window percentage;
- token or credit use;
- wall-clock time;
- number of usage windows;
- retries;
- hardware pressure;
- concurrent agent/tool load.

Do not fabricate dollar cost from subscription quota unless a direct conversion exists.

Distinguish:

- API cost;
- subscription quota burn;
- execution time;
- human attention required.

These are different efficiency metrics.

## 8. Compare against public priors only after documenting the personal result

For a model/tool conclusion with enough evidence, perform a benchmark/public-opinion reconciliation.

### Source priority

Use, in order:

1. independent benchmark organizations with clear methodology;
2. benchmark-owner leaderboards;
3. provider-published evals, clearly labeled as provider results;
4. reputable third-party empirical comparisons;
5. community reports such as Reddit/Hacker News for workflow sentiment only.

Do not treat community opinion as a benchmark.

### Community-freshness rule

When using Reddit, Hacker News, forums, or social posts:

- look for repeated themes across multiple independent threads rather than one spectacular anecdote;
- record the age of the model/release when sentiment was sampled;
- treat upvotes as a signal that an experience resonated, not as a scientific vote;
- account for complaint-community, fan-community, launch-day hype, and launch-day backlash bias;
- label community conclusions as **provisional** when the model has less than roughly two weeks of public use unless unusually strong longitudinal evidence already exists;
- preserve meaningful disagreement instead of forcing a fake consensus.

A high-engagement complaint two days after launch is evidence that a failure mode deserves testing. It is not proof that the model is generally bad.

### Completed-task efficiency rule

Do not reduce efficiency to price per token.

When evidence allows, distinguish:

- input/output token price;
- actual output/reasoning token use;
- cache behavior;
- first-pass task success;
- retries and rework;
- reviewer-model cost;
- human steering/attention;
- wall-clock time;
- subscription quota or credit consumption;
- downstream regression cost.

A cheaper model can produce a more expensive completed task if correction cost dominates. An expensive model can be cheaper overall if it prevents a costly architectural error.

### Harness-efficiency rule

When the outcome involves an agent harness, record model and harness separately.

Do not attribute high token/quota use to the model until checking:

- native subscription vs API billing;
- starting/fixed context;
- prompt-cache read/write behavior;
- tool and MCP schema size;
- tool-result accumulation;
- skills/plugins;
- subagent count and actual subagent model/effort;
- compactions;
- retries and rereads;
- provider adapter or proxy route;
- human correction burden.

Use `baselines/HARNESSES.md` and `research/harnesses/2026-09-24-token-and-window-efficiency.md` as the current public harness prior.

For matched owner experiments follow `research/harnesses/HARNESS_AB_TEST_PROTOCOL.md`.

A harness result should optimize **accepted work per scarce resource**, not merely tokens per request.

### Match the comparison

Prefer the same:

- exact model version;
- reasoning effort;
- agent harness;
- benchmark period;
- task type.

If exact matching is impossible, say so.

Do not compare "Astra Low" directly to "Astra Max" as if they were the same configuration.

### Record one of four relationships

- **confirms public prior** — personal evidence points in the same direction;
- **contradicts public prior** — personal result materially differs;
- **adds operational nuance** — benchmark capability is confirmed, but quota, prompt shape, environment access, or human review changes the best routing;
- **not comparable** — public evidence does not measure the observed task/configuration well enough.

Public evidence belongs in `baselines/` for current provider/model priors, in `benchmarks/` for cross-model benchmark reconciliation, or in a case's benchmark-reconciliation section. It should not overwrite the personal observation.

When creating or refreshing a public model baseline, also update `datasets/model_baselines.jsonl` and preserve an `as_of` date.

## 9. Use public benchmarks as priors, not labels

Examples:

Bad:

> Sol is the best coding model because it ranks first.

Better:

> At the time, public coding-agent benchmarks would have made Sol a strong prior for long-horizon coding. In the owner's Agentic AI case it also performed exceptionally, but the run consumed nearly a full usage window; the personal lesson therefore adds quota/task-shape information the benchmark did not capture.

Bad:

> Terra is worse because a general intelligence index puts it off the Pareto frontier.

Better:

> Terra's public coding-agent results were strong, while the owner's bounded implementation results were unusually cost-effective. That supports Terra specifically for this workflow even if generic intelligence/cost rankings prefer another configuration.

## 10. Separate capability from role fit

A model can be excellent but poorly routed.

Record whether the evidence concerns:

- implementation;
- architecture;
- debugging;
- review;
- governance;
- product design;
- research;
- live environment integration;
- 3D generation;
- deterministic transformation.

Prefer role-specific conclusions.

## 11. Human use is a separate acceptance layer

Automated tests prove contract behavior, not product quality.

When a usable product exists, preserve findings from:

- owner playtest;
- visual review;
- workflow friction;
- UX failure;
- confusing copy;
- performance under normal use;
- integration with later features.

If playtesting finds defects after green tests, update the case. Do not hide the contradiction.

## 12. Update all relevant repository surfaces

For a new substantial case, inspect whether these need changes:

- `models/<tool>/README.md`
- `models/<tool>/cases/<date>-<slug>.md`
- `cross-model/ROUTING_GUIDE.md`
- `projects/PROJECT_INDEX.md`
- `projects/COVERAGE_GAPS.md`
- `evidence/prompt-lineage/`
- `baselines/<PROVIDER>.md`
- `benchmarks/PUBLIC_PRIORS_VS_PERSONAL_EVIDENCE.md`
- `datasets/cases.jsonl`
- `datasets/model_baselines.jsonl` when public-model data changes
- `datasets/harness_baselines.jsonl` when public harness research changes
- `datasets/harness_runs.jsonl` only after real owner measurements exist

Do not mechanically update every file when the case adds nothing to that surface.

## 13. Machine-readable dataset rules

`datasets/cases.jsonl` must remain valid one-object-per-line JSON.

Preserve null/unknown values instead of guessing.

For future records, capture when available:

- `model_family`
- `model_label`
- `reasoning_effort`
- `agent_harness`
- `task_types`
- `autonomy_level`
- `tooling`
- `prompt_pattern`
- `artifact`
- `verification`
- `human_signal`
- `resource_signal`
- `outcome`
- `lesson`
- `public_prior_alignment`
- `evidence_level`

Do not rewrite historical fields solely for schema aesthetics if the evidence is unavailable.

## 14. Preference-pair rule

Do not fabricate RLHF-style chosen/rejected pairs.

Create a pair only when both candidate outputs (or stable references to them) and the actual preference are preserved.

Prompt preference and output preference are different datasets.

## 15. Privacy boundary

This repository is public.

Record only personal information needed to understand the AI task.

Do not publish unrelated:

- addresses;
- account identifiers;
- private financial details;
- credentials;
- sensitive personal information.

Prefer project-role descriptions over identity details.

## 16. Quality gate before commit

Confirm:

- the exact model/tool label is not invented;
- dates are concrete when known;
- artifact links resolve;
- user reactions are faithful and not exaggerated;
- failures are preserved;
- public benchmark claims are sourced and dated;
- provider self-reports are not presented as independent validation;
- the lesson is narrower than the evidence;
- a model is not ranked universally from one case;
- JSONL still parses;
- later evidence has not already invalidated the conclusion.

## 17. Output style

Write concise causal records.

Prefer:

> Terra High implemented the bounded Skill/XP foundation with 31 passing checks. Later composition review still found integration defects in a different PR. The evidence supports Terra as a cost-effective bounded implementer, not as a substitute for independent integration review.

Avoid:

> Terra is objectively the best value model.
