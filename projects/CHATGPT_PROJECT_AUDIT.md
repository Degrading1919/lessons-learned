# ChatGPT Project Audit

This is a coverage inventory of substantial recurring ChatGPT work, including areas that do **not** yet produce a strong model-performance case.

The purpose is to avoid selection bias toward GitHub simply because GitHub leaves better artifacts.

## 1. Repo-backed software and game development — highest evidence density

These projects currently provide the strongest training/evaluation material because prompts, commits, PRs, tests, and user reactions can be correlated.

- Agentic AI
- Modular CRM
- Adventurer's Rise
- Margins
- The Bible Video Game
- Trading / SwingRank
- Caelmor
- Mystery Pallet Simulator

Primary lessons include:

- autonomous task shape
- repository source-of-truth design
- model routing
- implementation vs reviewer roles
- skills/AGENTS governance
- MCP/live-environment integration
- verification and playtesting
- 3D generation pipelines

## 2. Local software projects — strong workflow evidence, weaker artifact links

### Folio

ChatGPT designed tasks and Codex implemented locally. The owner then used the built application and fed real product friction back into the next task.

This is already represented as a case because the human-QC signal is strong.

### Resonant

ChatGPT developed the architecture/task for a local real-time audio visualizer and adopted the same Codex-build / owner-QC workflow.

Current evidence is incomplete because a strong post-build reaction/output chain has not yet been captured.

## 3. 3D asset production — strong specialized-tool evidence

Across Margins and Adventurer's Rise:

- ChatGPT acted as production director/prompt author
- Tripo 3D generated assets
- Blender/Claude Code or direct Studio workflows handled downstream integration
- user rejection/approval of assets changed later prompting standards
- measured geometry and engine constraints fed back into the process

This is strong evidence because visual preference, technical measurements, and downstream usability all matter.

## 4. Cybersecurity / home-lab / security-research work — substantial use, limited current model-comparison evidence

ChatGPT has been used for:

- legitimate self-owned lab setup
- networking/Linux/tool troubleshooting
- security-research workflow design
- bug-bounty/program research
- authorization/process questions

This is a substantial task domain, but the current audit did not find a clean cross-model prompt → artifact → user-reaction chain comparable to the software repositories.

Potential future evidence should focus on:

- whether repo/tool-grounded guidance reduced failed steps
- whether an agent could complete bounded lab automation safely
- false-positive/false-assumption rate
- quality of scope/authorization handling
- usefulness of code-agent vs chat-mode workflows

Do not manufacture a model ranking from general support conversations.

## 5. Coursework / technical learning — high frequency, different evaluation target

ChatGPT has been used for:

- statistics/probability tutoring
- calculator workflows
- AI/ML/cyber course concepts
- document/reading support
- academic writing and discussion responses

The useful metrics here differ from coding:

- correctness
- explainability
- adherence to instructor method
- ability to work from screenshots/course material
- tone/style matching
- citation discipline

No strong model-routing case is currently recorded, but this domain could eventually support its own evaluation set.

## 6. Research and decision-support projects

Recurring work includes career planning, housing/rentals, product/service comparison, and other practical research.

These conversations can become useful cases when there is a measurable downstream decision or outcome. Until then they are weaker model-performance evidence than repo-backed engineering.

## 7. Creative / practical assistance

Recurring cooking, vehicle-detailing, gaming, and similar threads demonstrate preference/style adaptation but are not currently central to the agentic-AI evaluation corpus.

They should only be added as cases when they reveal a reusable model/tool lesson, such as:

- persistent style adherence
- image-generation quality
- planning accuracy
- tool/plugin advantage
- repeated correction pattern

## Audit conclusion

The current repository intentionally gives the most space to software/game/3D projects because they contain the densest evidence chain.

That is an **evidence availability decision**, not a claim that the user's other ChatGPT projects are unimportant.

Future cases should be added whenever a non-GitHub project has:

> identifiable input → identifiable model/tool → observable output → verification/use → clear user signal.
