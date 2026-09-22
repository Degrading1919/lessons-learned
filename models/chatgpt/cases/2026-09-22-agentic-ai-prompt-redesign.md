# Case: ChatGPT — Redesigning the Agentic AI Codex Task

- **Date:** 2026-09-22
- **Project:** Agentic AI
- **Tool:** ChatGPT
- **Task categories:** prompt design, agent orchestration, repository setup
- **Evidence:** Level A

## First output

ChatGPT initially translated the software concept into a conventional incremental engineering task:

- bootstrap the repo
- define Task 001
- build only the shell
- avoid inference/runtime work
- ask for a short plan
- stop after the bounded task

That was a reasonable software-management pattern, but it did not fit how the project owner wanted to exploit a long-horizon coding agent.

## User rejection

The user explicitly rejected the prompt style as too prescriptive and too prone to repeated stopping.

The user's preferred shape was concept + required features + reusable references + "Begin."

## Correction

ChatGPT changed the repository task so the prompt:

- described the product
- pointed to reusable open-source systems
- preserved hard architectural invariants
- granted routine engineering autonomy
- required an end-to-end MVP
- prohibited artificial stop-and-confirm loops

Prompt lineage:
https://github.com/Degrading1919/lessons-learned/blob/main/evidence/prompt-lineage/2026-09-22-agentic-ai.md

## Outcome

The downstream Sol Max Codex run produced the MVP in one prompt and became the template for Modular CRM tasking.

## Supported lesson

**Prompt authors should optimize for the capabilities and operating mode of the downstream agent, not merely for conventional project-management neatness.**

For a high-capability long-horizon agent with a strong repository, a tightly staged task can waste the very autonomy being paid for.
