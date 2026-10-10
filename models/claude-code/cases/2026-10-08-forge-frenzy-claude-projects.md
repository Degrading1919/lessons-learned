# Case: Forge Frenzy — Claude Projects coordinator, parallel threads and a single Studio owner

- **Date:** 2026-10-08 to 2026-10-10
- **Project:** Forge Frenzy (Roblox blacksmithing incremental)
- **Repository/artifact:** https://github.com/Degrading1919/forge-frenzy — PRs [#1](https://github.com/Degrading1919/forge-frenzy/pull/1)–[#5](https://github.com/Degrading1919/forge-frenzy/pull/5), merge commit `eec062a`
- **Model/tool:** Claude Projects (claude.ai) with a coordinator session, cloud thread sessions and Claude Code Remote Control sessions on the owner's PC; Roblox Studio MCP; in-session helper subagents
- **Exact model/effort label:** commits carry `Co-Authored-By: Claude Opus 5.5 (1M context)` (25 commits on `main`). Effort level not recorded. The models used by in-session helper subagents were not recorded; the first brief asked for Sonnet 5.5 workers and Haiku-class exploration, but that routing is not confirmed.
- **Other models in the chain:** GPT-6.1 Sol High continuation between Claude passes (label from the owner's brief); an independent GPT-6 review of PR #5.
- **Task categories:** end-to-end implementation, agent orchestration, Blender/Studio integration (Roblox Studio), playtest remediation, code review remediation, repository governance
- **Evidence:** Level A for episodes 3–4 (prompt, artifact, Studio verification, direct owner signal, downstream rule change); Level B for episodes 1–2 (the owner's playtest judged the combined Claude + GPT 1.0, so the signal is not Claude-only).

## Objective

Build the design-only Forge Frenzy repository into a complete, playable Roblox game in the existing published Studio place, then iterate through owner playtest remediation, an independent-review remediation and a repository consolidation. Real purchases, publishing and paid Tripo generation stayed off throughout.

## Starting context

- A mature design repository (docs 01–14, `design/balance-v0.json`, LOCKED/PLANNED/OPEN decision labels, a Claude build-mission doc).
- Roblox Studio MCP running on the owner's Windows PC; the Studio place was an empty baseplate.
- Remote Control on that PC served only the `modular-crm` folder, so every machine session started there and had to `cd` to the forge-frenzy checkout.
- A Claude plan that regularly hits its five-hour usage limit.

## Prompt/tasking pattern

All four major briefs were long, mission-oriented and pasted by the owner into the project chat:

1. **Build** (2026-10-08 00:16 UTC): "complete playable game, not an MVP"; read the repo source of truth; single Studio owner; model routing suggestion (Opus 5.5 for orchestration, Sonnet 5.5 for bounded work, Haiku for search); do not stop at milestones; no purchases/publishing/paid generation.
2. **Owner playtest remediation** (03:26 UTC): resume after a GPT continuation; treat the GPT agent's reported evidence as claims to re-verify; `docs/21` supersedes earlier design; do not regenerate the world; work autonomously until ready for another owner playtest.
3. **PR #5 review remediation** (21:40 UTC): "independently reproduce or disprove" seven GPT-6 review findings; redesign steal duration on a log curve; constrain the economic value of stolen high-tier weapons.
4. **Consolidation** (23:02 UTC): merge PR #5, delete integrated branches, rewrite README/CLAUDE/AGENTS, optional Lune CI.

Follow-up briefs 3 and 4 and a mid-pass correction were routed by the coordinator into the thread that already owned Studio and PR #5, so one session carried context across three briefs.

## Episodes, output and verification

### 1. Parallel first build (00:16–01:03 UTC)

- The coordinator first started one Remote Control session for the whole brief. The **owner** proposed splitting it ("would it not help to separate that task into multiple threads…?"). The coordinator agreed and split three cloud threads off: Tripo manifest, core forging/economy Luau, companions/eggs/rebirth Luau. The Studio thread stayed the single integrator.
- The Studio session did not act on the coordinator's split note immediately (a coordinator cannot interrupt a session running on the user's machine); the owner had to paste the stop/ownership message into the Studio thread. The Studio session had already started the Tripo manifest "in parallel".
- The Studio thread published the module layout/API contract (`docs/16_CODE_LAYOUT_AND_CONTRACTS.md`) about seven minutes *after* the cloud threads started, so both had to move code they had already written into the contract's layout.
- Output within ~25 minutes: PR #1 (Tripo manifest, 101 assets, prompts validated by script), PR #2 (companions/evolution/leaderboards/monetization, 64 Lune tests), PR #3 (32 tiers, click-luck forging, rolls, production, ProfileStore saves; 44 → 110 tests), PR #4 (evolution reset fix found while aligning PR #2 with PR #3). PR #3's worker merged the integration branch and found a contract mismatch on its own: session ids were numbers in one service and strings in the Studio glue, so "every hammer click would have been ignored".
- Studio thread: built hub, six plots and HUD; merged all four PRs; 106/106 Studio checks; played the loop in Studio; opened draft PR #5.
- **Resource signal:** all sessions hit the five-hour usage limit at 00:58–01:03 UTC, about 45 minutes after the brief. Whether the window was fresh at the start is not recorded. Save/rejoin, multi-player and mobile checks were left undone.
- Environment friction: Studio screenshots came back blank while the window was minimized; the agent asked the owner to bring it to the front. DataStore testing needed the owner to enable Studio API access.

### 2. GPT continuation, owner playtest, Claude remediation (03:26–15:29 UTC)

- GPT-6.1 Sol High continued on the same branch (4 commits `41ed8b1`..`9d4f3ba`, reported 149 Studio / 153 local checks).
- **Owner playtest of that 1.0:** "technically functional" but it "reads too much like AI-generated productivity software", with clipped buttons, text-heavy panels, remote-management menus and a several-hour endgame instead of the intended long curve (`docs/21_OWNER_PLAYTEST_REMEDIATION.md`). This is a judgment on the combined Claude + GPT build.
- The coordinator briefed the new machine session to check a "PR #3 merged at 05:22" report. That report was a stale message posted by a cloud thread when its usage window reset; the session verified with `git merge-base` that the merge was really at 00:57 and an ancestor of all GPT commits, and changed nothing. The session then reported and waited for a go-ahead the owner had already given in the brief; the coordinator had to nudge it to start.
- The first Remote Control card for this pass opened the wrong folder; the owner declined it and had to approve a second one.
- Remediation output: v2 economy (simulated ~494–496 h free to final metal, premium ~162 h), station-local world and chunky mobile-first UI, build pads, booth selling, display income, stealing, laser Forge Lock, pet merging; 221 Lune / 212 Studio checks; real two-client steal/lock test; persistence test; desktop and phone-landscape inspection. The live world was backed up to `ServerStorage.Backups` before rebuilding. Work paused once for the usage limit and resumed on its own.

### 3. Independent GPT review → Claude reproduce-and-fix (21:40–23:00 UTC)

- All seven GPT-6 findings reproduced in code; none were disproven. Fixes landed in ~30 minutes with regression tests (Lune 233, Studio 222), a two-client Studio acceptance (15 checks) and 14–15 economy simulations including stealing strategies. Testing also found an extra bug: swapping the podium weapon mid-hold stole the new weapon.
- The brief asked that stolen high-tier weapons be economically constrained, so Claude added a cash-out cap. **The owner rejected it:** "I do not like the idea of stolen weapons being capped… that takes away the incentive to steal." The coordinator relayed this as "rethink that rule" while keeping the anti-skip protections, and the thread started simulating a compromise ("jackpot") rule. The owner cut that off in the thread: "stolen weapons shoudl retain their value. that is all." Claude removed the cap within two minutes, re-ran the two-client test, and reported the trade-off once (a player who steals a top weapon every 15 minutes finishes in ~86 h instead of ~500 h).
- Final reliability brief: Claude added thief-side steal recovery and a real-DataStore recovery test (4 cases). **Driving the real ProximityPrompt from Studio clients exposed that every real steal had been failing:** the prompt fires "hold ended" just before "triggered", and the server treated it as a cancel. Every earlier test had called the server directly. After the fix: 20/20 two-client checks, Lune 238/238, Studio 229/229.

### 4. Consolidation (23:02–23:06 UTC)

- Verified that the feature branches were contained in PR #5, merged PR #5 as `eec062a`, deleted four integrated branches, rewrote README/CLAUDE.md/AGENTS.md around the current game with an "Accepted owner decisions (do not reopen)" list, and added `docs/README.md` to separate current documents from historical ones.
- The Lune CI workflow could not go live: the GitHub token lacked the `workflow` scope. It is staged at `tools/ci/lune.yml`.
- Weekly Claude usage ran out on 2026-10-10 ~03:00 UTC; ChatGPT took over the project.

## Human signal

- The owner proposed parallelization, then accepted the coordinator's single-Studio-owner split.
- Owner playtest rejected the 1.0 player experience while accepting its backend.
- Owner's next brief opened with "Your previous remediation substantially resolved the GPT review findings… meaningful improvements."
- Owner rejected the stolen-weapon cap twice, the second time tersely, after the system turned the preference into a design exercise.
- Owner returned to Claude for each successive brief and moved the project to ChatGPT only because the weekly limit was exhausted.

## Failures / corrections

- Orchestration was decided after the integrator had already started, and the code contract was published after the parallel workers had started, which cost rework and needed a manual paste from the owner.
- Parallel fan-out burned the five-hour window in about 45 minutes and left save/multi-player/mobile checks undone.
- Green suites (106 Studio checks in v1; 222 in the review pass) did not catch either the "developer-facing" UX or the broken real steal input path.
- Stale cross-session messages after a usage reset caused one wasted verification task and one outdated "send continue" instruction to the owner.
- A direct owner preference was relayed as an open design question and briefly re-litigated.
- Remote Control's folder restriction produced one wrong-folder approval card.

## Downstream consequence

- `CLAUDE.md` in forge-frenzy now carries "Accepted owner decisions (do not reopen)", including full resale value for stolen weapons.
- Later briefs told sessions to use helpers sparingly because of usage limits.
- `docs/25` records evidence as verified in Studio / mocked / still needs a human, and `CLAUDE.md` makes that the standard.
- The practices are collected in [the Claude Projects playbook](../CLAUDE_PROJECTS_PLAYBOOK.md).

## Supported lesson

With a mature design repository, a single machine session that owns Studio and integration, plus a few cloud threads that write pure Luau or docs against a published contract, produced a large playable build quickly. It also burned a five-hour window in under an hour. A strong model on a review-remediation brief reliably reproduced and fixed an independent reviewer's findings. The two failures that mattered got past green unit and spec suites: the player experience, and the real input path. Each was found only by a human playtest or by driving real client input.

## What this does not prove

- That Opus 5.5 is better than GPT-6.1 Sol: the two worked on different phases with different briefs, so this is not a matched comparison.
- That parallel threads are generally worth it: here the speed came at a heavy quota cost on a limited plan.
- That helper subagents were Sonnet or Haiku: their models were not recorded.
- That the v1 UX problems were Claude's alone: GPT polished the same UI before the playtest.

## Dataset tags

```yaml
task_types: [end-to-end implementation, agent orchestration, Roblox Studio integration, playtest remediation, code review remediation, repository governance]
model_family: Anthropic/Claude
model_label: Claude Opus 5.5 (1M context) per commit trailers; helper models unknown
tooling: [Claude Projects coordinator, cloud thread sessions, Claude Code Remote Control, Roblox Studio MCP, Lune, GitHub]
artifact_type: PRs #1-#5, merge eec062a
verification: [Lune suites, Studio spec runner, two-client Studio acceptance, real-DataStore recovery test, economy simulations, owner playtest]
human_signal: v1 UX rejected; review remediation praised; stolen-weapon cap rejected
outcome: merged to main; ready for next owner playtest
evidence_level: A/B
```
