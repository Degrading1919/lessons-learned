# Case: Caelmor — procedural architecture passed tests before it met the art brief

- **Development:** 2026-11-02–03 UTC; commits are dated November 2 in the owner's local timezone.
- **Project/artifact:** [Caelmor PR #85](https://github.com/Degrading1919/Caelmor-Repo/pull/85), reviewed through `c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e`. Open, unmerged at retrospective capture.
- **Observed configuration:** Codex desktop/local shell and Blender 5.0.1; root `gpt-6.1-sol`, `high`; requested worker routing `gpt-6-luna`, `high`. See the [session evidence](../../../evidence/measurements/2026-11-02-caelmor-development.md) for actual calls, outcomes and counter limitations.
- **Task categories:** procedural 3D, architecture, orchestration, debugging, technical art, Blender integration, testing, source-control recovery.
- **Evidence:** **A for the development/feedback chain**; weaker for causal model comparisons and final artistic acceptance. This is one evolving, mixed-agent project, not a controlled model benchmark.

## Objective and starting context

The owner requested an installable standalone Blender add-on producing detailed medieval exteriors through procedural geometry rather than prefab assembly. Initial scope was Lowmark, irregular orthogonal footprints, coherent intersecting roofs, timber, masonry, openings, chimneys, materials and deterministic variation. A supplied research brief, live Caelmor canon/dossiers, repository rules and open-source examples were available. Later assignments broadened purpose, region, wealth and construction context while explicitly excluding Unity integration, runtime profiling and interiors.

The implementation had local Python, headless Blender, actual renders, editable scenes, Git and GitHub access. This environment mattered: neither a text-only code review nor model capability alone could establish whether the generated asset worked in Blender. There was no verified target-engine acceptance or production art sign-off.

The owner explicitly asked for Luna High workers, independent verification, autonomous routine decisions, and progress per usage allowance rather than minimum calls. See [prompt lineage and direct feedback](../../../evidence/prompt-lineage/2026-11-02-caelmor-procedural-architecture.md). That preference is not evidence that this routing was cheaper than alternatives.

## Iterations and what each actually established

| Stage | Durable evidence | Outcome and unresolved gap |
|---|---|---|
| Prototype | [Isolated prototype `ecb1090`](https://github.com/Degrading1919/Caelmor-Repo/commit/ecb109013c7723ec920feb9f04161b7df66bf9dc), copied from local mixed `9eaaf1d` | Five functions; 14 Python tests, 80 stress inputs, Blender integration, 40 views of ten buildings, native install/export. Functioning geometry; owner still saw repetition, implausible braces, clean surfaces and roof lines. |
| Exterior correction / v0.2 | [`e3643f5`](https://github.com/Degrading1919/Caelmor-Repo/commit/e3643f54c61483af527ad3a6316f50d6193be8c5) | Construction schedule, full-section roof clearance, shingle courses/repairs, material/export corrections, 20 Python tests and 17 roof fixtures. Corrected a real envelope failure; did not establish cultural variety. |
| Regional expansion / v0.3 | [`bb3349a`](https://github.com/Degrading1919/Caelmor-Repo/commit/bb3349a69669708919207abcfb6b666ceb0df692); [`eda657c` main integration](https://github.com/Degrading1919/Caelmor-Repo/commit/eda657c738b668d11cbcefa960a7f1d94d62d6a9) | Twenty function profiles, four regions, 17 local contexts, wealth/upkeep controls, hip roofs and efficient topology. 37 Python tests and 96 stress inputs. Broader geometry and green checks still left regional cottages and socioeconomic tiers too similar in the gallery. |
| World construction / v0.4 | [`c5772d6`](https://github.com/Degrading1919/Caelmor-Repo/commit/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e) | Separate regional mass/roof/support systems, access rules, working ranges, wheels/slipways and forge volumes. 44 Python tests; 240 region/function/wealth cases; 80 context cases; final 388-record geometry replay. Neutral silhouettes improved; wealth readability and authenticity remained incompletely solved. |

Counts describe different scopes and revisions; do not add them into a unique-test or unique-building total. Historical reports are retained in [VALIDATION.md](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/VALIDATION.md); the [prototype report](https://github.com/Degrading1919/Caelmor-Repo/blob/ecb109013c7723ec920feb9f04161b7df66bf9dc/CODE/Scripts/architectural_generator/tests/VALIDATION.md) is separately pinned. These are executed-run records, inspected retrospectively; this documentation mission did not rerun Blender or benchmark the generator.

## Failure mechanisms, detection and corrections

### Roof lines were geometry, not a color problem

The owner identified the brown lines directly: “The tops of the walls are still poking through the roofs, that is what the brown lines on the roof is”. Initial mesh closure, roof coverage and deterministic hash checks could all pass while facade members breached the weather shell. The later diagnostic measured a facade timber post **139 mm above the roof plane at the outer eave**. That measured post is a concrete instance of the owner's broader wall-top diagnosis, not evidence every line was the same primitive.

The correction accounted for section width, outward projection, roof slope and deck thickness. Frame datums and fascia placement were lowered against their actual supporting planes; openings/headers under low steep eaves were constrained. The validator sampled vertices, edge midpoints and face centroids, requiring structural timber/details to remain at or below the nominal underside of the 120 mm roof deck (roof envelope minus 0.12 m). Walls could meet the deck, with a separate small interpolation tolerance. A regression deliberately inserts the former unsafe post and expects rejection. [Contract](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/ENGINE_CONTRACT.md), [roof fixtures](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/test_roof_clearance.py).

**Lesson:** independent generators need a shared envelope contract. Closed meshes and plausible centerlines do not prove assembled clearance. Sampled clearance remains a bounded diagnostic, not a continuous proof for arbitrary polygons. Intentional stepped stone gable parapets must be distinguished from accidental roof penetration.

### Windows, frames and access needed assembly-level rules

Openings could be legal as wall rectangles while casing, shutters or diagonal timber still occupied the same space. The expanded assignment explicitly identified window-to-beam clearance. The revised semantic frame schedule exposed principal posts, plates, braces and gable members; tests checked the full assembly bounds, including shutters. Actual triangle BVH tests checked glass/timber intersections, and aperture rays checked that cladding did not conceal the intended holes. Aesthetic placement and engineering collision are related but separate checks. [Facade/raycast tests](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/test_facade_raycast.py), [BVH tests](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/test_glass_timber_bvh.py).

World construction introduced further cross-module risks: actual upper doors had to land on supported decks, linked volumes needed sufficient separation, attachment faces needed blind openings, and gate passages had to remain open even in an industrial context. World tests inspect actual deck polygons and nearest aperture hits rather than only checking that a feature flag is present. Root integration also corrected a context rule that could put a forge annex across a gate exit. These are reasons to retain a single owner for global massing/access contracts, even when regional builders are delegated. [World tests](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/test_world.py), [world Blender checks](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/test_world_blender.py).

### Regional names and parameter differences did not establish architecture

V0.3 genuinely changed geometry and passed tests; calling it only a palette swap would erase real work. But much of its vocabulary remained shared: pitched roofs, rectangular openings, repeated bays and cottage-like bodies. The owner asked why farming Lowmark and industrial Emberholt should look alike, describing Emberholt as brutalist-inspired iron/volcanic-stone civilization rather than wooden houses. The subsequent prompt required geography/material culture/industry/history to drive construction and demanded texture-neutral comparisons.

V0.4 changed the production rules themselves: Lowmark broad halls/open shed ranges; Thornfell heavy steep stone halls/stepped foundations and gables; Mire braced raised floors/bowed roofs/decks; Emberholt thick angular blocks/terraces/vents/ironwalks. During integration, initial Lowmark/Thornfell views were rejected as too interchangeable and revised; 24 affected frames were refreshed. A later Luna blind reviewer identified all four regional cottages with varying confidence. This is useful internal evidence of improvement, **not owner approval or a controlled human recognition study**. [World validation/review](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/WORLD_VALIDATION.md).

The later ChatGPT art assessment praised texture-neutral recognizability but criticized minimal wealth differentiation, ceremonial/jagged Thornfell gables and modern-block-like Emberholt. Those are **assistant judgments**, preserved separately from the owner's direct art direction. The owner then requested this retrospective, not another development cycle. Production authenticity was not established.

### Socioeconomic differentiation remained a partially satisfied requirement

Tests established wealth-dependent dimensions, cover/material choices and differing buffers in selected fixtures; upkeep could change wear independently of massing. That is weaker than demonstrating that viewers can distinguish modest, established and affluent homes across every region. A 240-case validity matrix cannot measure cultural or status readability. The twelve-cottage wealth sheet exists, but the blind region test did not test wealth classification. Future acceptance should compare capacity, privacy, entry hierarchy, work space, construction phases and repair quality at matched seeds and viewing distance, with explicit human decisions. More named settings or assertions that hashes differ are insufficient.

### The mixed Git commit was a workflow failure with an instruction-level cause

The initial repository instructions mandated `git add -A`, commit and push without a prepublication audit. In a shared dirty checkout, this captured 32 unrelated files along with the generator into local `9eaaf1d`; `git push origin main` then failed non-fast-forward. The agent stopped and reported the exact failure, consistent with the stop rule. This explains the mechanism without excusing the polluted scope or treating the concurrent work as expendable.

The owner subsequently authorized inspection and isolation. Only the generator directory was restored onto a branch based on remote main; the original mixed commit/checkout and preservation ref were retained. Main was incorporated without overwriting concurrent work, and publication proceeded through PR #85. The final PR's 125 paths were all under the generator prefix. [Preservation record and excluded-path inventory](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/PUBLICATION.md).

**Transfer:** isolate the workspace before generating changes or establish a scoped staging boundary. A blanket staging rule and a prohibition on scope inspection are unsafe together in a concurrently edited checkout. This is a repository/harness policy lesson, not evidence that Luna caused a Git failure.

## Engineering methods worth retaining

The pure geometry layer produced mesh buffers without importing Blender eagerly. A stable interface between settings/plan, geometry, facade, roof, backend and tests made bounded delegation and cheap checks possible. Named seed streams isolated random decisions; stable semantic IDs and settings snapshots enabled deterministic replay and targeted regeneration. Native tests deliberately edited/protected geometry, regenerated selected/all layers, preserved untagged manual work and a second building, then exported/reimported and reopened the file. Protection preserves work; it does not guarantee that a manual edit remains compatible after a grammar change.

The roof implementation used **convex planar patches and an analytic upper envelope with support domains**, clipped tile courses, split T-junctions and welded seams. Hips partitioned their own supported slope domains; world builders supplied shed, piecewise bowed and terrace roof sources. This bounded orthogonal solution avoided introducing an arbitrary-polygon skeleton dependency. It was not a general straight-skeleton implementation. The code studied Building Tools and polyskel for concepts; the [provenance record](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/THIRD_PARTY.md) says no upstream code/assets were copied. The add-on carries GPL-3.0-or-later and its full license. This retrospective did not conduct an independent legal audit.

World construction reused these geometry primitives while adding zone-qualified identities, local weather envelopes, occupied masses, attachment/access logic and legacy dispatch. New UI scenes enabled world construction; old snapshots/API defaults preserved legacy behavior. This compatibility split prevented an art-system replacement from silently changing saved settings.

Research became more useful when it supplied **construction principles**, not ornamental references: Historic England farmstead relationships, Highland stone/recessed-opening precedent, UNESCO raised water-connected settlements, and industrial process hierarchy at Völklingen. The [regional research document](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/WORLD_ARCHITECTURAL_LANGUAGES.md) distinguishes lore anchors from reversible art inference. A source-check correction of Ashspire to the dossier's wealthy ward illustrates why research summaries still require verification. Historical/industrial references do not approve modern machinery or new Caelmor canon.

Repair logic improved from conspicuous rectangular/color cohorts toward bounded course replacements and sistered real posts. It remained heuristic; final surface repetition and subtle condition differences were documented limitations. Meaningful repair should explain a construction event, exposure or load problem, not simply add random blemishes.

## Geometry efficiency: measured savings, not a runtime claim

`EFFICIENT` retained closed structural cores and the roof deck while omitting concealed layering, veneer backs and selected buried faces; decorative buffers explicitly used `SURFACE` topology. Thus “all buffers must be manifold solids” was replaced by a role-aware contract, rather than silently weakening validation. LOW/MEDIUM/HIGH controls retained configurable detail. [Measurement script](https://github.com/Degrading1919/Caelmor-Repo/blob/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator/tests/measure_geometry_modes.py).

| V0.4 HIGH cottage, same seed/settings except mode | SOLID triangles | EFFICIENT triangles | Reduction |
|---|---:|---:|---:|
| Lowmark | 31,492 | 16,179 | 48.63% |
| Thornfell | 36,768 | 20,670 | 43.78% |
| Mire | 57,868 | 20,500 | 64.57% |
| Emberholt | 19,872 | 18,057 | 9.13% |

The older v0.3 HIGH examples had 42.77–61.73% savings on different buildings. Do not read that as a performance trend between releases. Emberholt's compact terrace geometry left less redundant roofing to remove. Neither set measures FPS, memory in a target engine, silhouette equivalence at every distance, or a justified universal polygon limit.

## Which verification paid for itself?

| Layer | Evidence/value in this case | Limits / efficient schedule |
|---|---|---|
| Python topology, seed and parameter checks | Fast repeatable foundation; real invalid settings and coverage/overlap regressions | Different hashes are not meaningful art differences. Run focused checks during edits, broader matrices at integration. |
| Shared semantic/envelope constraints | Added after roof/frame and access defects; reject unsafe assemblies before Blender | Only cover encoded roles/domains/tolerances; deliberately test a bad fixture. |
| Blender actual mesh rays/BVH | Independently checked glass/timber and apertures after backend conversion | Keep adversarial windows, slopes and linked-volume fixtures; avoid running every expensive scene for every doc edit. |
| Clay matched-function/wealth galleries | Exposed cosmetic regional similarity and supported rejection/revision | Blind agent classification has no human-study validity. Use consistent cameras and enough views, not one showcase seed. |
| PBR/closeups | Exposed tile patches, weathering/repetition, joinery and export tint issues | Clay cannot replace it; full galleries need not be rerendered for unrelated code changes. |
| Native ZIP install/operator/export/reopen | Found packaging/application issues source tests cannot; verified real deliverable and manual protection | Perform after source/package freeze; check ZIP/source byte identity. Blender success is not target-engine acceptance. |
| Source/geometry evidence replay | 388/388 settings reproduced; saved inputs/manifests make later comparisons auditable | Geometry hashes do not prove unchanged materials/cameras. Earlier image source bytes differed; snapshots were preserved instead of claiming all images used final source. |

Recorded examples of execution cost: v0.2 roof sweep **85.153 s / 17 builds**; v0.3 **135.986 s / 21 fixtures**; final combined Blender batch **150.5 s / 7 methods across 5 modules**; v0.4 context sweep **36.501 s / 80 inputs**. These are different workloads and cannot rank model speed or be summed as total project time. No measured ablation proves a particular test redundant. Likely avoidable work includes repeated broad evidence refreshes after late changes and model-driven bookkeeping; these are scheduling hypotheses, not quantified savings.

A concrete late churn example is recorded at root lines 4680–4687: trimming trailing blank lines in three regional source files was followed by rebuilding the ZIP, both native install checks and another 388-setting geometry replay. The changed archive justified refreshing package identity, but freezing formatting before the final evidence pass would have avoided that extra release cycle. Repeated short polls of the still-running replay also returned no new evidence. Prefer bounded longer waits and deterministic result summaries. This identifies avoidable scheduling/context work; it does not establish that the final install/replay gates themselves should be removed or quantify model/token savings.

Permanent gates should retain the original unsafe eave/post regression; full window/shutter-to-frame clearance; actual aperture/BVH checks; domain-aware roof/volume/access validation; repeat-seed isolation and unique IDs; protected/scoped regeneration and legacy snapshots; topology-role tests; and final native package install/export. Permanent **art** gates should retain matched neutral region/function/status sets, PBR repair views and recorded human decisions. See the reusable [procedural asset baseline](../../../research/procedural-assets/PROCEDURAL_ASSET_BASELINE.md).

## Model roles, orchestration and efficiency conclusions

The observed configuration made bounded facade, backend/UI, geometry, research and QA tasks delegable. Explicit contracts/file ownership limited collisions; follow-ups reused workers for corrections. The lead owned difficult roof geometry, cross-volume/access integration and final visual judgment. Independent review mattered, but workers and the lead also required correction: successful local modules did not establish assembled construction or art direction.

The session evidence supports **role fit under this workflow**, not a worker-versus-lead accuracy or price ranking. Initial author-written tests missed roof penetration; later integration and owner feedback expanded what “correct” meant. The owner supplied indispensable semantic direction, particularly Emberholt's industrial identity. A stronger root configuration did not automatically infer all that direction or solve socioeconomic authenticity.

Use the [resource evidence](../../../evidence/measurements/2026-11-02-caelmor-development.md) for measured counters and unknowns. Subscription allowance, repeated/cached input tokens, elapsed time, runtime test seconds, API dollars and human attention are separate variables. No dollar price, allowance-to-token conversion, active-work duration, or counterfactual cost saving is established by this case. Token volume must include context/cache/compaction and reviewer overhead before it is used to judge a model.

Recovered measurements are substantial: **2,809 unique responses**, **365,672,329 logged processed tokens**, including **360,243,584 cached input tokens** across the lead and 15 workers. The lead accounts for 514 responses/110,351,373 tokens; workers for 2,295/255,320,956. This is repeated-context processing, not 365 million tokens of new code or a bill. Two compactions, 36 follow-up task calls and 109 inter-agent messages are visible. Heavy QA workers also implemented fixtures, rendered evidence and diagnosed failures; their token volume cannot be labeled pure overhead or compared fairly with a small geometry helper.

One continuation actually terminated with **`usage_limit_exceeded`** at 19:51 UTC, after the initial exterior correction work; the owner later resumed it. A later 50% allowance reading therefore cannot support a claim that the entire project used half a window. The end-to-end timestamp envelope is about 9 h 28 m including idle time/interruption; neither it nor test-runtime seconds measures model speed. There was no controlled cheaper-model or leaner-harness alternative. Efficiency is consequently an unresolved measurement question despite successful delivery.

The narrow routing recommendation is to trial Luna High for bounded tasks with cheap acceptance tests and a technically competent integrator. Prefer scripts for manifest/hash comparisons, seeded matrix construction, dataset/link checking and gallery composition. Route global geometry contracts, ambiguous construction, canon interpretation and final integration to stronger judgment. Whether Luna Medium suffices for simpler work, or stronger early architecture reduces total rework, requires matched trials rather than intuition. The baseline supplies those experiments.

### Public-prior reconciliation

Against the repository's **dated 2026-10-04** [model prior](../../../research/models/2026-10-04-new-model-release-update.md), this case **adds operational nuance** to Sol engineering plus Luna workers: it demonstrates the combined setup on a real Blender artifact, including expensive review and corrections. It is **not comparable** to a benchmark claim about independent model capability, token-price efficiency or quota superiority. Against the [harness prior](../../../baselines/HARNESSES.md), repeated context, cache, tools and coordination are relevant observed mechanisms; CLI-versus-Desktop or API-versus-subscription savings were not tested. No new public model baseline or leaderboard is created here.

## Supported lesson and unresolved limits

AI coding agents can build an editable procedural construction system with strong technical evidence while repeatedly missing the intended visual standard. The most useful correction was to move from object validity to assembly constraints, then from parameter variety to culturally motivated construction rules, and to judge those rules in actual controlled renders. Keep the failed images, owner diagnosis and rejected intermediate approach alongside the successful artifact.

This case does not prove production readiness, complete socioeconomic readability, realistic structural engineering, general polygon support, automatic terrain fitting, target-engine fitness, universal model superiority or minimal cost. PR adoption and artistic acceptance remain separate. The next efficiency improvement to test is earlier semantic/art falsification with bounded workers and targeted checks—not simply fewer tests or a cheaper model name.
