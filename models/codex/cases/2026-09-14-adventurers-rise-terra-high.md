# Case: Adventurer's Rise — Terra High as a Cost/Quality Implementation Model

- **Date:** 2026-09-14 onward
- **Project:** Adventurer's Rise
- **Repository:** https://github.com/Degrading1919/adventurers-rise
- **Model/tool:** Codex, GPT-5.6 Terra High
- **Task categories:** Roblox/Luau implementation, server authority, progression systems
- **Evidence:** Level A/B

## Evidence

The user explicitly praised Terra High's balance of output cost, accuracy, and content creation.

A concrete early example is PR #3:

https://github.com/Degrading1919/adventurers-rise/pull/3

It added a reusable server-authoritative Skill/XP foundation and reported:

- 23 existing PlayerData checks passed
- 8 focused Skill/XP checks passed
- whole-source Luau compile/analysis checks
- no premature Studio/client scope

Subsequent PRs built combat, enemy runtime, gathering, offline training, and composition on top of the same repository discipline.

## Important counterevidence

PR #18 later required review corrections for integration issues including:

- clock-domain mismatch
- fabricated begin rewards
- missing periodic settlement
- startup ordering
- silent reward-credit failure

This prevents the conclusion from becoming "Terra High output can be merged without review."

Another run exhausted available usage while repairing PR #10, showing that quota still constrains sustained autonomous work.

## Supported lesson

**Terra High is a strong default implementation tier for bounded, well-specified repository work when cost/quality matters, but integration-heavy composition still benefits from an independent reviewer.**

The project also supports a broader workflow:

> lower-cost capable implementer → independent architectural review → narrow correction task

That often beats paying the highest-capability model to author every line.
