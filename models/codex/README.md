# Codex

## Observed strengths

Across the current projects, Codex has been strongest when given:

- an authoritative repository
- durable `AGENTS.md` / project rules
- a coherent end goal
- permission to inspect, implement, test, and correct without artificial owner checkpoints
- explicit hard boundaries rather than step-by-step implementation instructions
- a real verification surface: tests, build, app runtime, or playtest

## Model/effort observations

These are personal project observations, not universal rankings.

### GPT-5.6 Sol Max

The strongest current end-to-end success is Agentic AI on September 22, 2026.

After the task was rewritten from a narrow shell/scaffold into a mission-oriented end-to-end MVP, one Sol Max run created the local-first orchestration MVP. The user reported being highly impressed and noted that the run used about 92% of one five-hour usage window.

This is strong evidence that a capable model can use almost an entire long context window productively when the repository already defines the product and the prompt does not force artificial pauses.

### GPT-5.6 Terra High

Adventurer's Rise provided a strong cost/quality signal.

The user explicitly praised Terra High's output cost versus accuracy/content creation. PR #3 added the Skill/XP foundation and passed 23 existing checks plus 8 focused checks. Terra also handled multiple subsequent bounded foundations well.

A later run exhausted available usage while repairing PR #10, showing that even a strong value model still needs quota-aware task sizing.

### Astra Low

Margins PR #42 is the counterexample to "use the biggest/longest agent run for everything."

The user reported that an Astra Low end-to-end task consumed roughly 12 hours across three five-hour windows. Later, Astra was more attractive as a reviewer/orchestrator: it caught architectural issues while consuming substantially less quota.

**Lesson:** use high-cost, long-running agents where their additional integration ability is actually the bottleneck. Reviewer/orchestrator roles can produce better value than asking the same model to own an enormous implementation.

## Prompting pattern that currently wins

When the repository is mature:

1. state the mission
2. name the source of truth
3. give hard architectural/product guardrails
4. identify useful reference implementations
5. explicitly authorize routine engineering judgment
6. prohibit artificial stop-and-confirm loops
7. define what "done" must prove
8. begin

Avoid copying the entire specification into the prompt.

The Modular CRM repository permanently adopted this after the Agentic AI result.

## Verification lessons

Codex output must be judged by what survived:

- tests
- builds
- code review
- runtime integration
- playtesting
- later feature composition

Margins PR #42 is especially important: substantial automated verification existed, yet owner playtesting still surfaced zero-sale deadlocks, closing/customer lifecycle issues, developer-facing setup UX, prompt verbosity, checkout problems, and unsaved-progress concerns.

**Lesson:** green tests are necessary evidence, not product acceptance.


## Current public model prior — 2026-09-24

The owner-observed cases above remain the primary evidence for this repository.

For the newly released GPT-6 family and current OpenAI model economics, use the [2026-09-24 OpenAI model field guide](../../research/openai/2026-09-24-reddit-field-guide.md) as a **public prior only**.

The current research hypothesis is:

- Astra for scarce architectural/integration judgment;
- GPT-6 Sol Medium/High as the serious-work candidate, pending personal validation;
- GPT-6 Luna High/XHigh for bounded bulk execution with cheap verification;
- GPT-5.6 Sol and Terra retained as behavioral fallbacks until matched tests justify replacing them.

Do not rewrite historical GPT-5.6 cases as GPT-6 conclusions.
