# Case: Margins — Astra Was More Valuable as Reviewer Than Giant Implementer

- **Date:** 2026-09-10
- **Project:** Margins
- **Repository:** https://github.com/Degrading1919/margins
- **Model/tool:** Codex/Astra Low and mixed-model orchestration
- **Task categories:** large implementation, review, playtest remediation
- **Evidence:** Level B

## Observation

The user reported that the PR #42 task consumed roughly 12 hours across three five-hour usage windows with Astra Low and questioned the cost efficiency.

PR #42 eventually became a substantial owner-playtest remediation wave:

https://github.com/Degrading1919/margins/pull/42

The work was valuable, but the resource cost changed how the user wanted to deploy Astra.

Later orchestration used cheaper/faster implementation paths and Astra more as reviewer/orchestrator. The user observed better quota efficiency while still catching architectural problems.

## Why this matters

A model can be capable enough to complete a giant task and still be the wrong economic choice for that role.

The useful variable is not only:

> Can the model do it?

It is:

> Is this where the model's scarce reasoning/agent budget creates the most marginal value?

## Supported lesson

**Use expensive or slow agent configurations where judgment, integration review, or hard debugging is the bottleneck. Do not default them to long mechanical implementation if a cheaper capable model can produce work for them to review.**

This case is also a warning against treating "most capable" and "best default" as synonyms.
