# Prompt Lineage: Agentic AI End-to-End Build

- **Project:** Agentic AI
- **Repository:** https://github.com/Degrading1919/agentic-ai
- **Date:** 2026-09-22
- **Why this lineage matters:** the user's correction to the prompt materially changed the scope and was followed by a highly successful Codex run.

## Version 1 — narrow Task 001

Bootstrap commit:

https://github.com/Degrading1919/agentic-ai/commit/017ab02f862a3c1cd53deaf4ef977929ed8235d4

The original `CODEX_START_PROMPT.md` instructed Codex to:

- implement Task 001 exactly as scoped
- build the Configure + Work shell
- avoid model inference
- avoid runtime/scheduler/MCP/A2A implementation
- keep the work tightly scoped
- provide a plan first
- stop after the focused task

This was internally coherent, but it optimized for controlled incremental delivery rather than the owner's desired use of a long-horizon agent.

## User reaction

The user rejected the prompt because it was too prescriptive and encouraged repeated stopping.

The desired pattern was substantially closer to:

> Here is the concept of the software I want to build, these are the features it needs to have, here is a place you can find examples of preexisting code to integrate into the tool so you do not have to build it all. Begin.

The user explicitly wanted end-to-end completion instead of five-minute milestones.

## Version 2 — mission-oriented autonomous prompt

Current prompt:

https://github.com/Degrading1919/agentic-ai/blob/main/CODEX_START_PROMPT.md

The revised prompt:

- describes the concept in product language
- defines the Configure graph as capability/permission topology
- explains agent/model separation and structured work orders
- describes hardware/resource behavior
- names open-source systems to study
- tells Codex that repo docs are context, not a reason to stop at a scaffold
- authorizes reasonable engineering decisions
- instructs the agent to continue through logical work
- allows interruption only for a genuine blocker
- ends with `Begin.`

Relevant prompt-expansion commit:

https://github.com/Degrading1919/agentic-ai/commit/b82fa59958d6ec9b84dc0f7e4feb8c68cce47b6a

## Downstream output

Implementation commit:

https://github.com/Degrading1919/agentic-ai/commit/c62c9c210c1908a1f5aa4800ea61f62d329ab052

The resulting MVP included the graph editor, Work console, topology-bound execution, structured work orders, model lifecycle logic, persistence, observability, provider/tool boundaries, docs, and tests.

## Post-run user signal

The user reported being impressed by the result and emphasized that:

- it came from one prompt
- it used about 92% of a five-hour usage window
- the result was strong enough to become the reference for how another complicated project should task Codex

## Transfer

Modular CRM then codified the lesson in its own repository.

See:
[Modular CRM prompt lineage](2026-09-22-modular-crm.md)

## Lesson

The improvement was not "remove all constraints."

The improvement was:

> move durable detail into the repository, keep the task prompt mission-oriented, preserve hard guardrails, and let the agent decide implementation steps.
