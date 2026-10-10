# Prompt Lineage: Forge Frenzy Claude Projects briefs

- **Project:** Forge Frenzy
- **Repository:** https://github.com/Degrading1919/forge-frenzy
- **Dates:** 2026-10-08 to 2026-10-10
- **Case:** [models/claude-code/cases/2026-10-08-forge-frenzy-claude-projects.md](../../models/claude-code/cases/2026-10-08-forge-frenzy-claude-projects.md)

Three tasking corrections happened during the run. Each one was executed, so its downstream effect is observable.

## 1. Single orchestrator → coordinator split

**Before (executed):** one long build brief addressed to "the lead development orchestrator". It asked for subagents with suggested routing (Opus 5.5 for orchestration, Sonnet 5.5 for bounded work, Haiku for search) and a single Studio owner. The coordinator started one Remote Control session for all of it.

**Owner correction:** "would it not help to separate that task into multiple threads with you as the lead to expedite the build process?" The coordinator agreed and split off three cloud threads. The owner then had to paste a stop/ownership message into the running Studio thread manually: "Stop the Tripo manifest work and don't write the core logic, pets, rebirth or monetization modules…"

**After / downstream:**
- Four PRs landed in about 25 minutes.
- Workers rewrote code to fit the contract that the integrator published after they had started.
- All threads ran on Opus 5.5 medium; the brief's Sonnet/Haiku routing never took effect.
- The whole system hit the five-hour limit about 45 minutes after the brief.

**Lesson:** decide the split, the contract and each thread's model in the brief itself. Routing advice addressed to an orchestrator did not change the models the platform started.

## 2. Brief-requested stolen-weapon cap → owner override

**Before (executed):** the PR #5 review brief listed "P1: High-tier stealing bypasses progression" and asked for the stolen weapon's "usable economic value" to be "appropriately constrained". Claude implemented a cash-out cap and backed it with simulations (40.8 h → ~486 h).

**Owner correction (project chat):** "I do not like the idea of stolen weapons being capped to that persons highest tier, that takes away the incentive to steal". The coordinator relayed this as "please rethink that rule", keeping the anti-skip protections. The thread began simulating a compromise "jackpot" rule.

**Owner correction (thread):** "stolen weapons shoudl retain their value. that is all."

**After / downstream:**
- The cap was removed within about two minutes, re-tested and pushed (`970bb6e`).
- The trade-off was stated once: about 86 h for a constant top-weapon thief.
- The rule is now LOCKED in forge-frenzy `CLAUDE.md` under "Accepted owner decisions (do not reopen)".

**Lesson:** a brief that frames an owner preference as an open design problem gets a design answer. State known decisions as decisions. A relay through another agent can soften a direct preference, so write overrides in the owning thread.

## 3. "Treat previous-agent evidence as claims" (kept)

**Pattern (executed):** the remediation brief after the GPT continuation listed GPT's reported results and said: "Treat those as previous-agent evidence, not a substitute for your own inspection or validation."

**Downstream:** the session verified branch state with `git merge-base` instead of trusting reports. That check also neutralized a stale coordinator instruction. Later briefs kept the same pattern for the GPT-6 review ("independently reproduce or disprove each finding"), and all seven findings were reproduced and fixed.

**Lesson:** keep this wording for any handoff between models or sessions.
