# Claude Projects Playbook: coordinator, threads and subagents

Practical guidance for the owner's next Claude Projects build. It is derived mainly from the [Forge Frenzy case](cases/2026-10-08-forge-frenzy-claude-projects.md) (2026-10-08 to 2026-10-10), so it is one project's evidence, not a general rule. Each practice cites what happened.

## How the pieces fit

- **Coordinator:** watches the project chat, starts threads, routes follow-ups, keeps memory. It cannot interrupt a Remote Control session running on the owner's PC. Only the owner's own message in that thread reaches it immediately.
- **Cloud thread:** a Claude Code session in a cloud container with GitHub. It is good for work that needs only the repository, such as pure Luau modules, docs or manifests.
- **Remote Control thread:** a Claude Code session on the owner's PC with the local checkout and Roblox Studio MCP. Only one should own Studio at a time.
- **Helper subagents:** workers spawned inside a session. They are useful for bounded parallel tasks but draw on the same usage allowance.

## What went well (keep doing)

1. **One Studio owner; parallel workers only off-Studio.** Three cloud threads produced PRs #1–#4 in about 25 minutes, and the Studio thread merged and tested them (106/106 Studio checks). Nobody fought over the live place.
2. **Route follow-up briefs to the thread that already owns the work.** The "PR #5 review fixes" thread took three consecutive briefs (review fixes, reliability pass, consolidation) without re-reading the project from scratch.
3. **"Reproduce or disprove each finding" for cross-model review.** A GPT-6 review followed by Claude remediation reproduced all seven findings, fixed them with regression tests in about 30 minutes, and surfaced an extra bug. Keep pairing an independent reviewer with a remediation brief worded this way.
4. **Treat the previous agent's evidence as claims.** After the GPT continuation, Claude used `git merge-base` to confirm branch state instead of trusting reports, including a stale one from its own coordinator.
5. **Put locked decisions in the repository.** The consolidation pass added "Accepted owner decisions (do not reopen)" to `CLAUDE.md`, so the stolen-weapon ruling survives model and session changes.
6. **Separate evidence types in the report.** `docs/25` splits verified in Studio, mocked, and needs a human. That made the remaining risks (touch input, two live servers, 7–8 s holds for kids) explicit.
7. **Back up before destructive Studio work.** The v2 world rebuild kept the original under `ServerStorage.Backups`.

## Where Claude struggled

1. **Orchestration decided late.** The coordinator started one monolithic session, and the owner had to propose the split. The integrator had already begun the work being split off, and the owner had to paste the stop message manually.
2. **Contract after workers.** The code-layout contract landed about seven minutes after the cloud threads started, so they rewrote code to fit it. One mismatch (numeric vs text forge session ids) would have dropped every hammer click if a worker had not caught it during merge.
3. **Usage burn from fan-out, on the wrong model.** Four sessions plus helpers hit the five-hour limit about 45 minutes after the first brief. All three workers ran on Opus 5.5 although the brief asked for Sonnet 5.5, and the cloud workers alone reported about $23 API-equivalent. Save/rejoin, multi-player and mobile checks were left undone.
4. **Green tests, wrong product.** v1 passed 106 Studio checks and was still judged "developer-facing" and like "AI-generated productivity software" in the owner playtest. GPT's polish pass had touched the same UI.
5. **Green tests, broken input path.** Every real steal failed because ProximityPrompt fires "hold ended" before "triggered". All earlier tests called the server directly. Driving the real prompt from Studio clients found the bug.
6. **Re-litigating a clear owner preference.** The owner said stolen weapons should keep their value. The relay framed it as "rethink the rule", and the thread began designing a compromise, until the owner replied "that is all."
7. **Stale messages after a usage reset.** A thread that woke after the limit posted an old event as news. The coordinator briefed the next session on it and told the owner to send "continue" when nothing was left to continue.
8. **Waiting for permission already given.** The remediation session finished its precondition check and asked whether to start, although the brief said to work autonomously. The coordinator had to nudge it.

## Practices for next time

### Briefing

- **Decide the split in the first brief.** Say which parts are parallel and off-Studio (logic modules, docs, manifests) and which single session owns Studio and integration. Then the coordinator spawns everything at once, before the integrator starts duplicating work.
- **Make the contract the first deliverable.** Ask the integrator to push the layout/API contract (paths, service shape, id types, return conventions) and have workers start only after it exists. Alternatively, put the contract in the repository before the build.
- **State decisions as decisions.** If you already know the answer (for example, "stolen weapons keep full value"), write it as LOCKED. If you want the model to design a rule, mark it OPEN and ask for options before implementation. The review brief asked Claude to constrain stolen-weapon value, which the owner then rejected.
- **Name the real input path in acceptance.** For example: "verify by driving the actual ProximityPrompt/UI from a Studio client, not by calling server functions." Apply this to every player-facing mechanic.
- **Keep the "do not stop at milestones" line, and add "do not ask before starting".** Autonomy language worked for long passes. Add an explicit "start immediately after the precondition checks" for briefs that begin with a verification step.

### Usage budget

- **On a limited plan, default to one strong session plus few helpers.** Fan out to parallel threads only when the five-hour window is fresh and the work is truly independent. Tell the sessions the budget; later briefs that said "use helpers sparingly" ran a full review, reliability and consolidation pass in one evening without hitting the limit.
- **Front-load what needs the session that is about to run out.** In v1, save/rejoin, two-player and mobile checks were last and got cut. Ask for persistence and multi-client checks before polish.
- **Name the model for every thread yourself, in your own words.** The first brief said "prefer Sonnet 5.5 for bounded work", but every thread still started on Opus 5.5, including a docs-only manifest that cost about $3.78 in API-equivalent terms. Say it per thread when you approve a split, for example "start the manifest and both logic threads on Sonnet 5.5, medium effort". The platform only switches models when you ask explicitly.
- **Keep worker sessions short.** The core-economy worker read 20.7M cached tokens to write 126k. Re-reads cost the same on Sonnet and Opus, so one PR per thread, closed when merged, saves more than switching models alone. Don't keep using a finished worker for follow-ups.
- **Watch the weekly allowance, not just the five-hour window.** The weekly warning appeared about 28 hours before Claude work stopped for the week. When it shows, finish and merge in-flight work rather than starting new passes.

### Steering mid-flight

- **Write overrides directly in the owning thread, in one line.** "Stolen weapons should retain their value. That is all." worked immediately. A project-chat message relayed through the coordinator was softened into a design question.
- **Talk to a Remote Control session yourself when it must change course now.** The coordinator's notes wait until the session's turn ends.
- **After a usage reset, verify state from git and the PR before acting on any thread's status.** Messages posted on wake can describe old events.

### Environment (Roblox Studio via Remote Control)

- **Serve the forge-frenzy folder from the Claude desktop app** so approval cards offer the right folder. Today the PC serves only `modular-crm`, and sessions must be briefed to `cd`.
- **Keep the Studio window un-minimized** during sessions that take screenshots, and **enable Studio API access** before persistence testing.
- **Grant the GitHub `workflow` scope up front** (`gh auth refresh -s workflow`) if the agent should create CI workflows.

### Verification and acceptance

- **Schedule an owner playtest after the first playable loop**, not after the full feature list. The v1 UX direction was wrong in ways no test measured.
- **Keep an independent reviewer from another model before merge.** The GPT review found seven real issues that Claude's own suites had passed.
- **Require the verified / mocked / needs-a-human split** in every completion report.

## Ready-to-paste brief skeleton

Use this shape for the next big Claude Projects build. Keep it short and let the repository carry the detail.

```markdown
Mission: <one sentence, the finished outcome>.
Source of truth: <repo path>; read README/CLAUDE.md/docs first. LOCKED decisions there are final.

Owner decisions (do not reopen):
- <decision 1>
- <decision 2>

Open for you to decide (give options before building): <list, or "none">

Split (decide now, before any session starts):
- Studio/integration owner: one Remote Control session in <path>, model Opus 5.5 high.
- Parallel cloud threads, model Sonnet 5.5 medium, one PR each, then close:
  - <thread A: files it owns>
  - <thread B: files it owns>
- Integrator's first push: the code contract (layout, service API, id types). Workers start after it lands.

Acceptance:
- Drive every player-facing mechanic through the real client input path in Studio, not server calls.
- Persistence and multi-client checks before polish.
- Report verified in Studio / mocked / needs a human separately.

Autonomy: work without asking after the precondition checks; stop only for purchases, publishing, paid generation, credentials or irreversible changes.
Budget: my plan is limited; use helpers sparingly and say which model each helper ran on.
```

## Open questions to test

- Opus 5.5 vs Sonnet 5.5 as a bounded cloud worker on the same kind of thread (no Sonnet thread ran here), measured by accepted PRs and cache-read tokens per PR.
- Opus 5.5 vs Sonnet 5.5 as the Studio integrator on a bounded remediation, with identical brief and verification (quota per accepted fix).
- One session with sparse helpers vs coordinator fan-out on the same build, measured by accepted features per five-hour window.
- Whether a pre-written contract in the repo removes the rework seen in episode 1.
