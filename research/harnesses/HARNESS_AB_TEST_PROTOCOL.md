
# Harness A/B Test Protocol

_Last updated: 2026-09-24_

## Goal

Measure which harness produces the most accepted work per:

- five-hour allowance;
- weekly allowance;
- API dollar;
- wall-clock hour;
- unit of human attention.

## 1. Freeze the comparison

Hold constant where possible:

- repository commit;
- task prompt;
- model;
- effort;
- repository instructions;
- skill set;
- MCP/tool set;
- acceptance tests;
- machine/environment;
- task start state.

If surfaces cannot provide identical capabilities, record the difference rather than pretending they are equivalent.

## 2. Measure fixed harness overhead

Start a fresh session and issue:

> Reply exactly OK. Do not inspect files or use tools.

Run at least three times per harness/model/effort.

Record:

- starting context tokens;
- total input tokens;
- cached input;
- output/reasoning;
- five-hour percentage change;
- latency.

This estimates fixed system/tool/context overhead.

## 3. Run a bounded real task

Prefer an objectively verifiable task:

- one defined defect;
- one API endpoint plus tests;
- one bounded refactor;
- one fixed PR review;
- one repository-grounded report.

Use at least three comparable real tasks before making a strong routing change.

## 4. Record

### Identity

- date/time
- harness/version
- provider
- model
- effort
- subscription/API plan
- repository
- commit
- task ID

### Subscription

- five-hour % before/after
- weekly % before/after
- credits before/after

### Tokens

- total input
- uncached input
- cached input
- cache-write
- output
- reasoning
- initial context

### Harness behavior

- tools advertised
- MCPs enabled
- plugins/skills enabled
- tool calls
- subagents and their models/efforts
- compactions
- retries
- rereads after compaction
- overflow events

### Quality/time

- wall time
- human interventions
- correction turns
- tests
- review findings
- first-pass accepted
- final accepted
- later regression

## 5. Derived metrics

### Five-hour cost

window_used_pct = before_pct - after_pct

### Indicative accepted-work yield

accepted_tasks_per_100_pct = accepted_tasks / window_used_pct * 100

Provider accounting may be nonlinear, so do not treat this as a guaranteed full-window extrapolation.

### API cost per accepted task

api_dollars / accepted_tasks

### Cache-read ratio

cached_input / total_input

Anthropic's published production data suggests:

- 90%+: strong
- 80–90%: plausible/healthy
- below 80%: investigate

Do not blindly apply the same numeric threshold to OpenAI. Use OpenAI cache diagnostics.

### Human correction burden

human_interventions + correction_turns

### Rework-adjusted cost

initial run + correction runs + reviewer cost

## 6. Priority experiments

### Codex CLI vs Codex Desktop

Same model/effort/repo/task.

Purpose: reproduce or reject the reported 8k–10k startup-context difference and measure actual five-hour impact.

### Claude Code CLI vs Claude Chat/Desktop/Cowork

Choose a task both surfaces can legitimately execute.

Purpose: compare quota, human turns, wall time, and accepted result.

For real repository implementation, Claude Code remains the natural baseline.

### Native subscription vs Cline direct API

Same model/task/acceptance gate.

Purpose: estimate the subscription subsidy on the owner's actual work.

### Minimal tools vs full tool/MCP catalog

Same harness/model/task.

Purpose: quantify tool-schema tax.

### Single agent vs lead + workers

Same task and quality gate.

Purpose: determine when parallel wall-time savings justify duplicate context/model calls.

### Fresh task vs long continued task

Purpose: identify the crossover between cache/context reuse and context rot/compaction overhead.

## 7. Avoid contaminated comparisons

Do not:

- change model and harness together;
- change effort between arms;
- use different repo commits;
- use different MCP sets;
- compare trivial and hard tasks;
- compare subscription percentage with API dollars without quality normalization;
- declare a winner from one run.

## 8. Promotion rule

A durable harness-routing change should usually require:

- at least three consistent matched runs with quality parity; or
- one very large difference with a known mechanism and successful reproduction.

Otherwise preserve the result as provisional.

## 9. Future personal-run dataset

When real measurements exist, create datasets/harness_runs.jsonl.

Do not fabricate historical usage numbers.
