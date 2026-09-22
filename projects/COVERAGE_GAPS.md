# Coverage Gaps

This file prevents the repository from pretending the current audit is more complete than the available evidence.

## Repositories visible but not yet strongly correlated to ChatGPT prompt → AI output → user reaction

### Caelmor

Repository:
https://github.com/Degrading1919/Caelmor-Repo

There is extensive Codex/AI-shaped commit and PR history, including recent economy architecture work and older runtime/combat changes.

The current audit has enough artifact evidence to know it is relevant, but the retrieved ChatGPT history does not yet provide a clean prompt-before / reaction-after chain for the most important PRs. Treat model conclusions as provisional until those conversations are correlated.

### Mystery Pallet Simulator

Repository:
https://github.com/Degrading1919/Mystery-Pallet-Simulator-Repo

The game appears in older project discussions and was identified as a good fit for AI-assisted repeatable systems/content, but the current repository history is too sparse to support a strong model-performance case.

### transfertoVM

Repository:
https://github.com/Degrading1919/transfertoVM

The repository is visible to the connected GitHub account, but this audit did not retrieve enough ChatGPT project history tying it to an AI task/outcome. Do not classify it further without evidence.

## Reference/fork repositories

These are visible but should not be treated as authored outcome evidence unless a specific case shows how they were used:

- https://github.com/Degrading1919/awesome-llm-apps
- https://github.com/Degrading1919/build-your-own-x
- https://github.com/Degrading1919/leaked_sys_prompts
- https://github.com/Degrading1919/bitburner-src — the fork is reference/runtime authority; the AI-authored scripts built against it are the actual output evidence

## Local projects

### Resonant

Known tasking pattern: autonomous Folio-style Codex build for a Rust/wgpu audio visualizer.

The build prompt is known, but no strong post-build quality signal was retrieved. Keep as Level C until an output/reaction pair is captured.

### Folio

Strong human-QC evidence exists, but the source of truth is a local folder rather than GitHub. Preserve the case while noting that artifact links are unavailable.

## Future audit rule

When new evidence becomes available, prefer closing these gaps by linking:

1. original prompt/task
2. model/tool label
3. repository commit/PR or local artifact
4. verification
5. user's post-run reaction
