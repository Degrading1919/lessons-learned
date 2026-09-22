# Prompt Lineage: Modular CRM Adopts the Agentic AI Tasking Pattern

- **Project:** Modular CRM
- **Repository:** https://github.com/Degrading1919/modular-crm
- **Date:** 2026-09-22
- **Trigger:** successful Agentic AI single-prompt Codex run

## Before

The initial end-to-end task was already broad, but it was long and repeated much of the repository specification inside the prompt:

- implementation architecture
- reference implementations
- exhaustive feature checklist
- local usability rules
- quality checklist
- final handoff steps

That created duplicated authority: the same product detail lived in both the repository docs and the task prompt.

## User reaction / requested correction

The user asked that the tasking logic be re-evaluated against the recent Agentic AI result.

The goal was not to reduce scope. It was to reduce **prompt micromanagement**.

## After

Commit:

https://github.com/Degrading1919/modular-crm/commit/438b9602e30e916496dc50647af2afff2280a236

The revised `.agents/tasks/INITIAL_END_TO_END_BUILD.md` became much shorter.

It now centers on:

- **Mission:** build the documented V1 end to end
- **Autonomy:** make implementation decisions; do not stop for routine approval
- **Hard guardrails:** tenant isolation, auditability, provider boundaries, real required behavior, no scope narrowing
- **Completion standard:** keep implementing/testing until the V1 acceptance intent is satisfied
- **Stop condition:** genuine blocker only
- `Begin.`

## Durable project rule

Commit:

https://github.com/Degrading1919/modular-crm/commit/fabb6d4532c2834a66bbec03d581e04d3583f510

`AGENTS.md` was changed to say that detailed product requirements belong in repository docs and major autonomous prompts should stay compact.

Decision log:

https://github.com/Degrading1919/modular-crm/commit/84e911a71ba93e325d40a61943a2eba7c13fe06d

The repository explicitly records the Agentic AI result as the rationale.

## Lesson

This is stronger than a one-off prompt preference because the lesson propagated into permanent project governance:

> durable specification in repo + compact mission prompt + explicit autonomy + evidence-based completion.
