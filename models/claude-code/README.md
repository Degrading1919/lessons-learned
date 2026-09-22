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
