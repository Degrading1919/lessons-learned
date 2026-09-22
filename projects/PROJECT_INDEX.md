# Project Evidence Index

This index separates authored AI-assisted projects from reference/fork repositories and records how much evidence is currently available for model/task analysis.

| Project | Repository / location | Primary AI usage | Evidence strength | Current use in corpus |
|---|---|---|---|---|
| Agentic AI | https://github.com/Degrading1919/agentic-ai | ChatGPT task design, Codex end-to-end implementation | **A** | Core autonomy/prompt-shape case |
| Modular CRM | https://github.com/Degrading1919/modular-crm | ChatGPT product definition, Codex-oriented task design | **A** | Shows transfer of Agentic AI lesson into durable repo guidance |
| Adventurer's Rise | https://github.com/Degrading1919/adventurers-rise | Codex/Terra implementation, ChatGPT review, Claude Code/Opus + Roblox Studio MCP, Tripo workflow | **A** | Core cross-model implementation/integration cases |
| Margins | https://github.com/Degrading1919/margins | Codex implementation, ChatGPT review/orchestration, Claude Code/Blender MCP, Tripo 3D | **A** | Core cost, playtest, skill, 3D, and reviewer-role cases |
| The Bible Video Game | https://github.com/Degrading1919/The_Bible_Video_Game | Multi-model research, skill/governance design | **A/B** | Core model-judgment and skill-governance case |
| Trading / SwingRank | https://github.com/Degrading1919/trading | ChatGPT review and repo implementation | **B** | Useful architecture/review example |
| Caelmor | https://github.com/Degrading1919/Caelmor-Repo | Extensive Codex-driven design/implementation | **B** | Rich artifact history; prompt/user-response correlation still incomplete |
| Folio | local `C:\Dev\budget-app\` | Autonomous Codex implementation + human playtest | **B** | Strong human-QC lesson; no GitHub artifact currently linked |
| Resonant | local `C:\Dev\resonant\` | Folio-style Codex build workflow | **C** | Task design known; outcome evidence incomplete |
| Bitburner | https://github.com/Degrading1919/bitburner-src | ChatGPT coding grounded against fork API | **B/C** | Useful repo-grounding lesson; fork itself is not authored product evidence |
| Mystery Pallet Simulator | https://github.com/Degrading1919/Mystery-Pallet-Simulator-Repo | Early AI-assisted game planning | **C** | Insufficient prompt-to-output evidence for strong model conclusions |

## Reference/fork repositories

The following are not counted as authored project outcomes by default:

- https://github.com/Degrading1919/awesome-llm-apps
- https://github.com/Degrading1919/build-your-own-x
- https://github.com/Degrading1919/leaked_sys_prompts

They may be cited as research inputs when a case documents how they influenced an authored task.

## Notable repository evidence

### Agentic AI

- Initial constrained bootstrap/task: commit `017ab02f862a3c1cd53deaf4ef977929ed8235d4`
- Prompt/task expanded toward end-to-end autonomy: commits `89e0816`, `455dc97`, `b82fa59`
- End-to-end MVP implementation: commit `c62c9c210c1908a1f5aa4800ea61f62d329ab052`

### Modular CRM

The Agentic AI result was explicitly converted into project doctrine:

- `438b960` — simplified autonomous Codex build task
- `fabb6d4` — durable autonomous-tasking guidance
- `84e911a` — decision log records mission-oriented build prompts

### Adventurer's Rise

Useful model-linked evidence includes:

- PR #3 — reusable Skill/XP foundation; 23 existing + 8 new checks
- PR #18 — server composition required review/fix for clock/reward/settlement/integration issues
- PR #19 — Studio world-adapter integration with physical enemy binding
- PR #24 — Adventurer's Rise Tripo prompting skill
- PR #33 — living-world enemy behavior

### Margins

Useful evidence includes:

- PR #24 — repository-local Tripo prompting skill
- PR #27 — procurement; 122 EditMode + 48 PlayMode checks and Windows build
- PR #42 — owner-playtest remediation; strong example of automated checks not replacing human use
- PR #43 — 3D asset budget catalog built from measured/production-informed evidence
- PR #44 — production asset intake validation; 190 EditMode checks and Windows build
