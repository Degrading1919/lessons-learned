# Case: Adventurer's Rise — Opus 4.8 High + Roblox Studio MCP

- **Date:** 2026-09-16
- **Project:** Adventurer's Rise
- **Repository:** https://github.com/Degrading1919/adventurers-rise
- **Model/tool:** Claude Code, Claude Opus 4.8 High, Roblox Studio MCP
- **PR:** https://github.com/Degrading1919/adventurers-rise/pull/19
- **Evidence:** Level A/B

## Task shape

The repository backend already had server-authoritative services. The missing problem was physical Studio integration.

The prompt was deliberately reduced to a compact set of invariants after the user rejected a verbose version.

Core requirements:

- build the adapter, not a second authority system
- preserve stable runtime IDs
- fail closed
- use Studio/MCP for bounded verification
- keep the report concise

## Output

PR #19 implemented the Studio world-adapter boundary and physical enemy binding.

Notable design choices:

- physical models carried no second Humanoid health authority
- CombatDistanceProvider reported real world distance while Combat retained eligibility authority
- GatheringNodeResolver mapped stable node IDs to physical nodes
- physical enemy model ↔ runtime ID binding preserved backend ownership
- missing/off-world state failed closed
- Studio-only diagnostic access was guarded from live server use

## Human/reviewer signal

The run was judged a strong Opus 4.8 High result because it successfully crossed:

- repository contracts
- Studio hierarchy
- MCP verification
- runtime identity
- gameplay authority boundaries

Only small follow-up fixes were needed before merge.

## Supported lesson

**Claude Code becomes substantially more valuable when it can inspect and manipulate the real target environment through MCP, provided the prompt clearly protects authority boundaries.**

The important capability was not "write more code." It was closing the gap between repository abstractions and the live Studio world.
