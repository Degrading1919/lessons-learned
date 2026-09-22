# Case: Agentic AI — Sol Max End-to-End MVP

- **Date:** 2026-09-22
- **Project:** Agentic AI
- **Repository:** https://github.com/Degrading1919/agentic-ai
- **Model/tool:** Codex, GPT-5.6 Sol Max
- **Task categories:** implementation, architecture, local AI runtime, UI, orchestration
- **Evidence:** Level A

## Starting condition

The repository began with a well-defined concept:

- local-first visual agent orchestration IDE
- Work and Configure views
- capability topology rather than workflow DAG
- models and agents as separate concepts
- structured work orders
- local model lifecycle/resource constraints

The first Codex task was intentionally narrow. Commit `017ab02f862a3c1cd53deaf4ef977929ed8235d4` told Codex to build only the Configure + Work shell, avoid inference, and stop after a focused Task 001.

## User correction

The user rejected that tasking style as too prescriptive and too likely to make the agent stop repeatedly.

The preferred tasking model was:

- explain the product concept
- list the capabilities the finished software needs
- point to relevant existing projects/code patterns to study
- let the agent work end to end
- interrupt the owner only for a genuine blocker

Commits `89e0816`, `455dc97`, and `b82fa59` changed the repository/task accordingly.

The revised task explicitly told the agent not to stop at a UI mockup or architecture scaffold and named Langflow, XYFlow/React Flow, llama.cpp, llama-swap, Open WebUI, MCP, and A2A as references.

## Output

Commit:

https://github.com/Degrading1919/agentic-ai/commit/c62c9c210c1908a1f5aa4800ea61f62d329ab052

Commit title:

> Build local-first agent orchestration MVP

The implementation included:

- Configure graph editor
- Work console
- topology-bound runtime
- structured work orders
- model lifecycle scheduling
- local persistence
- provider/tool boundaries
- runtime observability
- documentation
- tests

The implementation also documented deliberate MVP limits instead of pretending unfinished capabilities existed.

## Human signal

The user described the result as impressive and specifically noted that it came from a **single prompt** and used about **92% of one five-hour usage window**.

The user then used this result as the benchmark for how another large project, Modular CRM, should task Codex.

## Downstream consequence

Modular CRM commit `84e911a71ba93e325d40a61943a2eba7c13fe06d` records the explicit decision:

> Major Codex implementation prompts should define the mission, hard guardrails, autonomy, and completion standard without restating the entire specification or requiring staged approvals.

That is unusually strong evidence because the lesson changed durable behavior in another repository.

## Supported lesson

**For a mature repository with strong source-of-truth documentation, a broad mission-oriented prompt can outperform a highly prescriptive milestone prompt.**

The winning prompt did not remove constraints. It moved constraints into durable repository context and gave the implementation agent freedom to solve the engineering problem.

## What this case does not prove

It does not prove that Sol Max is always the best coding model.

The result depended on:

- strong prior product definition
- an unusually coherent repository bootstrap
- current reference implementations
- a task that rewarded long-horizon integration
- enough usage budget to let one run consume almost a full window

The transferable lesson is primarily about **task construction and repository context**, with Sol Max providing the capability to capitalize on it.
