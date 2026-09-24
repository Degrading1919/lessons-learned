# Claude Code

## Strongest observed roles

Claude Code has been most compelling in this corpus when it can operate through a domain-specific environment rather than only edit files.

Examples:

- Roblox Studio MCP for Adventurer's Rise
- Blender MCP for Margins
- repository + local runtime integration

## Case: Adventurer's Rise PR #19

- **Model:** Claude Opus 4.8 High
- **Tooling:** Claude Code + Roblox Studio MCP
- **PR:** https://github.com/Degrading1919/adventurers-rise/pull/19
- **Task:** connect the existing server-authoritative backend to physical Studio world content without creating duplicate gameplay authority

The output implemented a world-adapter boundary that:

- resolved real physical distance
- mapped physical enemy models to server runtime IDs
- failed closed when world state was unavailable
- avoided a second Humanoid-owned health/combat system
- added bounded Studio diagnostics for verification

The run was evaluated as strong because it crossed repository architecture, Studio hierarchy, runtime IDs, MCP playtesting, and authority boundaries.

## Prompt lesson

The successful prompt was intentionally concise after the user rejected a more verbose version.

It emphasized the invariants that mattered:

- preserve repository authority
- use adapters
- stable IDs
- no duplicate authority
- bounded playtest
- concise evidence report

**Lesson:** when the agent can directly inspect the repository and live environment, prompts should emphasize invariants and acceptance behavior rather than narrating implementation.

## Blender/Margins lesson

Claude Code + Blender MCP was useful for inspecting and manipulating 3D production work, but one session also highlighted a non-model constraint: running Claude Code, Codex, Blender/MCP, VS Code, and Unity concurrently contributed to severe local resource pressure.

**Lesson:** agentic toolchains are bounded by workstation resources. More concurrent agents/tools are not automatically more productive.

## Failure modes to preserve

- Do not invent repository paths; inspect actual paths first.
- Do not let MCP convenience create a second source of gameplay truth.
- Separate exploratory MCP manipulation from deterministic production scripts when repeatability matters.
- Keep playtests bounded and evidence-based rather than turning them into open-ended agent loops.


## Current model-routing prior — 2026-09-24

The strongest owner-observed Claude Code case remains **Opus 4.8 High + Roblox Studio MCP**.

Public research now creates a testable successor hypothesis rather than invalidating that case:

- Opus 5.5 Medium/High may replace 4.8 as the high-end Claude Code default;
- Fable 5.1 is better reserved for planning, orchestration, difficult diagnosis, and final review;
- Sonnet 5 is viable for bounded tasks when effort is controlled;
- Haiku 4.5 is most useful for Explore/search/read/classify subagent work;
- Opus 5 has a poor public prior as a primary implementation author because of mature complaints about readability, overreach, and correction burden.

See [Anthropic Model Field Guide — 2026-09-24](../../research/anthropic/2026-09-24-reddit-field-guide.md).

A priority future comparison is **Opus 5.5 High vs Opus 4.8 High on the same environment-integrated task**, preserving identical repository state, MCP access, acceptance criteria, and verification.
