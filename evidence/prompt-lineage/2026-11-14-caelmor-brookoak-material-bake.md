# Prompt lineage: Caelmor Brookoak procedural material breakthrough

- **Period:** 2026-11-14, one evolving MMS/Sol session and owner review; sequential attempts, not controlled model A/B tests.
- **Case:** [Brookoak material construction retrospective](../../models/codex/cases/2026-11-14-caelmor-brookoak-material-bake.md)
- **Source artifacts:** [registered base](https://github.com/Degrading1919/Caelmor-Repo/commit/51f3f1542275bb96d131e2e1f03baf735e971f64), [first Timber Study](https://github.com/Degrading1919/Caelmor-Repo/commit/430ef659553bea64063b02193fa745652e515e53), [graph refinement](https://github.com/Degrading1919/Caelmor-Repo/commit/a5749a0123464ced2882362d90750d7f4a83c11d), [modeled/baked result](https://github.com/Degrading1919/Caelmor-Repo/commit/3c30aedce2f1763ded1562981a2d303df22d92fa).
- **Provenance:** Prompt drafts and direct owner/MMS responses preserved in the contemporary conversation; the full external agent transcript and resource counters were not independently exported for this record.

## P0 — “make it significantly more realistic” through the material graph

**Executed, per owner-reported result.** The owner provided Pierre Fleau's professional timber reference and requested more believable fibers, knots, splits, edges, wear and coordinated PBR channels. A lengthy revised research-grounded task asked for height-first primary/secondary/tertiary forms, matched lighting and reference critique, MaterialPilot tools, and approval gates. Sol High orchestrated the effort; earlier passes employed Terra/Luna and independent reviewer feedback.

**Consequence:** Material Maker produced the first 2K Timber Study and a subsequent refinement. Export/normal/tiling checks passed. The owner's response was **not approved**: at roof scale the output remained predominantly smoother board faces and cleaner butts; more grain was not solving the underlying form problem.

## P1 — Socratic visual comparison and explanation of the failure

**Executed as direct owner dialogue before the next implementation.** The owner supplied the old result and the Fleau reference and asked, in order, **“Do you see a difference in these images?”**, **“Why does photo 2 contain the level of detail that it does?”**, and **“What has prevented you from doing that thus far?”**. The owner also supplied material-construction skills:

- https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-wood-material/SKILL.md
- https://github.com/linegel/threejs-complete-set-of-skill/blob/main/skills/threejs-procedural-materials/SKILL.md

Sol admitted that its previous construction treated overlap as a lap ramp and a dark groove, keeping boards fundamentally flat while improving fibers and shallow checks.

**Consequence:** The diagnosis shifted from **"surface-detail deficit"** to **"missing distinct timber pieces, end faces and believable overlap"**. This was a hypothesis update supported by the reference and review, not yet a new successful artifact.

## P2 — research the physical workflow, then narrow to available tools

The owner asked Sol to research how experienced material artists and LLM-assisted workflows build realistic PBR. Sol reported distilling seven relevant sources (artist breakdowns, wood-roof physics, Adobe PBR and procedural-material research). The owner challenged the adequacy of that effort and constrained implementation to **Blender + Material Maker**, allowing a hybrid bake pipeline.

Sol proposed a falsifying comparison: a small patch of modeled overlapping shingles versus flat baked counterparts, with neutral clay and reversed lights. Full roof assembly and UV registration would be tested after the patch.

**Consequence:** The task changed from "keep polishing the current material graph" to "prove or reject the physical board cross-section and baking method first". Seven sources were an agent-reported interim scope, not a controlled finding that more browsing necessarily improves quality.

## P3 — authorize solo end-to-end physical construction and baking

**Executed owner instruction:** **“Begin on your next attempt. Do not use subagents for this. You have resources explaining the process artists take, your current working product, and the end goal. Continue implementing until you have a material that is just as realistic as your reference image.”**

**Consequence:** Sol produced [`build_brookoak.py`](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/build_brookoak.py) and four 2K bake maps. The new source generated actual shaped, overlapping wood shingles, then projected height/normals/color/roughness onto the registered flat tile. The owner said **“This is much better”**, and asked why it worked. Sol attributed the change to modeling thickness, exposed ends, overlapping undercourses, chips and growth-following surface damage **before** baking.

## Interpretation and next-use rule

The visible preference is for the **changed representation and resulting image**, not proven superiority of a particular model, skill, effort level, use of subagents, or exact wording. The owner did not yet certify reference parity or Unity readiness.

For similarly stuck 3D material tasks, preserve the full sequence: failed outputs and user objections; physically specific diagnosis; small neutral-form test; conversion from graph-only shading to procedural high-poly source where needed; matched baked/rendered evidence; final owner sign-off. A generic "AAA realism" phrase alone would miss the actual causal change.
