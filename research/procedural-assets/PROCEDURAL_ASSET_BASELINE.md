# Procedural Asset Work Baseline

_Last updated: 2026-11-02_

Reusable tasking and validation baseline for procedural architecture, terrain, vegetation, equipment, and props. This is a workflow prior, not a claim that any model or harness is generally best. For the Caelmor procedural architecture evidence, see [the case record](../../models/codex/cases/2026-11-02-caelmor-procedural-architecture.md) and the [generator source pinned at `c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e`](https://github.com/Degrading1919/Caelmor-Repo/tree/c5772d6a5cdf3721a5599e03aefcf3e9728a7c9e/CODE/Scripts/architectural_generator).

## Acceptance has two independent layers

**Machine validity** answers whether generated data obeys declared contracts: finite coordinates, closed required solids, valid indices and winding, deterministic replay, no forbidden overlap or envelope penetration, valid attachment/support, export structure, and safe regeneration behavior. Tests should encode measurable constraints and fail with useful diagnostics.

**Art acceptance** answers whether the asset reads correctly and is useful: silhouette, scale, function, regional identity, material response, repair/age cues, visual hierarchy, and consistency with approved art direction. A valid mesh, a matching hash, or a successful package/export does not prove these qualities. Keep the final human art review as a separate gate.

## Author constraints before implementation

Give the implementer the authoritative style/canon references, target use and engine, supported input ranges, units/coordinate conventions, required outputs, existing generator interfaces, and scope boundaries. Distinguish locked canon from visual inference. Define constraints for:

- **Structure and assembly:** foundations/support, load paths, access, attachment points, clearance, openings, collision intent, and which pieces may overhang.
- **Semantic function:** what the asset must do and which forms communicate that function (for example, a usable opening, supported platform, process volume, or traversal surface). Decorative labels do not substitute for geometry.
- **Analytic envelopes:** ground, canopy, roof, water/flood, terrain, or equipment-clearance surfaces. State where contact is allowed, required offsets, bounds, and deliberate exceptions. Validate the complete member/body envelope where feasible, not only its centerline.
- **Inputs and variants:** parameter limits, supported categories, detail modes, wealth/condition/age/context behavior, and legacy/manual overrides. Detail levels may change small geometry and surface treatment; they should not erase fundamental identity.
- **Edit and regeneration contract:** stable semantic IDs per generated piece; preserve/manual-protect controls; source settings and geometry snapshots; scoped/full regeneration behavior; duplicate policy; and how missing or edited IDs are handled.
- **Packaging:** native editable project/add-on, dependencies and license notices, version/manifest, export format(s), sidecars/settings, collision separation, texture/UV requirements, and installation/reopen verification.

Prefer named deterministic RNG streams keyed by seed and semantic purpose (for example, `plant.cluster`, `roof.courses`, `repair.panel.03`). Do not rely on global random call order. Hash canonical geometry/settings and record tool/source revision so a saved configuration can be replayed and compared.

## Adaptive validation ladder

Use the cheapest layer that can falsify an assumption first. Do not treat earlier levels as substitutes for later ones.

1. **Cheap Python fail-fast.** Validate parameter schemas/ranges, units, deterministic repeat hashes, bounds, topology roles, semantic IDs, analytic constraints, support/clearance, overlap, and representative edge cases. Use seeded tables and stress inputs after focused regressions. Keep tests fast and isolate the broken rule in failure output.
2. **Targeted Blender actual-mesh checks.** Convert the riskiest analytic claims into actual mesh checks: triangle/BVH intersections, complete body-to-envelope clearance, openings through cladding and glazing, attachment support, normals/topology, and collision proxies. Sampled vertices/edge midpoints/face centroids are useful diagnostics, but they can miss narrow intersections; use triangle-level checks for important collision classes. Cover extremes and adversarial junctions, not just attractive defaults.
3. **Neutral comparative renders.** Render matched settings, seeds, cameras, lighting, and material treatment. Use enough views to expose silhouette, back/side behavior, footprints, intersections, and functional access; a hero angle alone can hide failures. Include neutral clay views for structural identity and labeled/blind comparison where identity is a requirement. Record exact inputs, source hashes, software version, and image hashes. Treat internal blind reads as signals, not user studies.
4. **PBR, material, and repair review.** Check roughness/normal/albedo response, scale, surface repetition, weathering, wear, patches, replacement parts, and whether condition/wealth changes read at expected distance. Confirm texture and color data survive native export/import; clay renders cannot validate these.
5. **Human final art gate.** A reviewer with the actual art brief decides whether the result is readable, attractive, appropriate, and worth shipping. Record accepted/rejected examples and concrete corrections. A green technical suite cannot stand in for this gate.
6. **Native package/export gate.** Build from the deliverable package, install/enable in an isolated clean profile where practical, generate through user-facing operators, export/reimport, reopen the editable project, and verify sidecar/settings, IDs, protected manual edits, collisions, textures, and deterministic source equivalence. Report target-engine/game validation separately; do not imply it from Blender/GLB success.

Scale effort adaptively: run Python tests after each meaningful geometry change; run only relevant Blender fixtures during iteration; run full matrices, comparative galleries, PBR review, packaging, and human review at integration/release points. If a failure reveals a missing invariant, add a focused permanent gate and then a bounded stress case.

Freeze source formatting and bundled documentation before the final package/evidence pass. Record the exact source/archive hash once; if it changes later, classify whether geometry, materials, UI or only packaging changed and rerun the dependent gates. A geometry-hash match alone cannot certify unchanged materials or rendering inputs. For running jobs, use bounded meaningful waits and compact status results instead of repeated short polls with no new output.

## Detail and geometry cost

Avoid arbitrary polygon budgets or uniform decimation targets. First determine which geometry is visible, functional, structural, or hidden. A low-cost mode may replace hidden backs, buried surfaces, and decorative thickness with explicit surface topology while preserving continuous structural cores, contact surfaces, collision intent, and functional edges. Declare topology role per buffer and test required solids separately from decorative surfaces. Compare actual vertex/triangle counts and export sizes for matched settings; describe them as authoring-data measurements unless target runtime performance was measured. Detail modes must retain core silhouette and semantic behavior.

## Construction-first procedural material authoring — observed Caelmor lesson

[Brookoak case and visual evidence](../../models/codex/cases/2026-11-14-caelmor-brookoak-material-bake.md) · [Prompt and feedback lineage](../../evidence/prompt-lineage/2026-11-14-caelmor-brookoak-material-bake.md) · [Blender source/bake commit](https://github.com/Degrading1919/Caelmor-Repo/commit/3c30aedce2f1763ded1562981a2d303df22d92fa)

**Observed result (2026-11-14):** Material Maker graph revisions generated valid, repeatable maps and steadily better wood fibers, but the owner repeatedly rejected their smooth, dark-bordered shingle laps. A later Sol pass procedurally modeled actual split shingles in Blender—taper, cup/twist, thick exposed butts, damaged corners, sidewalls and overlapping lower boards—then baked a repeatable 2K PBR tile. The owner described the new output as **"much better."** Artistic final approval, production texture registration, and Unity runtime checks remain open.

**When this approach may help:** assembled materials where recognition depends on physically constructed volume, joinery or broken silhouettes—roof shingles, masonry blocks, tiles, cladding, scales, armor plates. This is *not* a rule to high-poly model every dirt, plaster, painted or roughness-driven material.

**Reuse this practical, falsifiable sequence:**

1. Define the physical object, its manufacture, support/contact, exposure and wear. Name the visible macro/meso/micro features; freeze intended tile scale and integration coordinates.
2. Model a **small repeating patch in neutral clay** first. Illuminate from opposite directions. Insist that cross-section, contact, overlap, corner fracture and material thickness read **without** albedo, grain or painted dark seams.
3. If the clay looks like flat panels, **change the representation** before adding color, surface noise, nodes, or resolution. Establish geometry for actual end faces, undercuts and missing silhouettes. Avoid asking a flat height ramp to stand in for an end face.
4. Add a shared wood/stone/metal substrate: grain, cracks and wear from common physically motivated feature fields. Feed color, roughness, height and tangent normals consistently. Fine detail belongs in material maps; silhouette and undercut detail remains geometry.
5. Bake from the constructed source at a documented real-world physical repeat. Check selected-to-active rays, cover gaps, the height sign/scale, tangent convention, albedo with no directional shading, roughness causality, 2×2 seamless repeat and deterministic output digests.
6. **Compare high-detail source versus baked tile** at matched scale, normal and grazing light, opposite-light clay tests and player viewing distance. Record what does not survive baking. Use this evidence to select flat, hybrid or modeled detail/LOD variants.
7. Honor integration contracts—shingle joints, UV frame, seed, material hash, texture packing and physical gauge—without preserving an artistically wrong height-construction method. Coordinate changed registration explicitly, and avoid **double normal/lap shading** where geometry already supplies the relief.
8. Keep **machine verification and owner visual acceptance distinct**. A plausible review from an agent is not human approval. Preserve rejected outputs and direct owner criticism as learning evidence.

**Agent-tasking correction:** Use a causal brief ("show a distinct cut butt/end face with the lower board visibly continuing underneath") and a **cheap neutral-form falsification test**, not generic "AAA realism" or an ever-growing stack of fine-grain nodes. Ask the model to predict the visible effect, render it, compare with the reference and reject unhelpful branches. Source research and reusable skills can improve the hypothesis, but the observed step-change here was the **modeled-then-baked construction change**. The solo final pass does not establish that single-agent execution is generally more efficient.

## Transfer beyond buildings

| Family | Construction/semantic invariant | Visual comparison to demand |
|---|---|---|
| Architecture | Weather shell, opening clearance, supported access, coherent repair/load paths | Same function across cultures; matched wealth/condition tiers |
| Terrain | Watertight required domains, continuous tile borders, slope/drainage constraints | Biomes/landforms with neutral lighting; scale and erosion readability |
| Vegetation | Branch continuity, supported attachments, root/ground contact, stable wind/leaf groups | Species/age/season silhouettes; repeated clumps and canopy density |
| Equipment | Fit/contact/clearance, articulation and assembly axes, thickness and grip dimensions | Purpose/status recognition; wear where handled or loaded |
| Props | Intended use, stable support, construction joints, reusable bounds | Families at actual viewing scale; repairs versus arbitrary surface noise |

These are proposed transferable contracts, not features demonstrated by the architecture project. Add domain-specific gates before treating them as validated production recipes.

## Work-order template

Assign one integration owner and bounded workers with explicit file ownership, interfaces, allowed contacts and acceptance fixtures. Give workers only the relevant references and contract rather than repeatedly loading the entire project transcript. Return inspectable code, exact commands/results and unresolved failures, not just a completion assertion. Reuse workers for narrow corrections when their context remains useful; parallelize dependency-ready work, not competing edits to the same builder. Escalate shared constraints, contradictory canon and actual irreversible blockers. A failed local check should normally trigger correction, not another broad research phase.

Copy and fill this for each task:

```text
Goal and asset family:
Authoritative references / canon status:
Target application, engine, scale, units, coordinate system:
Input parameters, supported ranges, categories, seed behavior:
Required silhouette, function, structure, access, and semantic cues:
Analytic envelopes / support / collision rules / allowed contacts:
Material, condition, repair, wealth, context, and detail behavior:
Manual editing, stable IDs, snapshots, protection, regeneration policy:
Native deliverables, package/install path, exports, sidecars, textures/UVs:
Out of scope / prohibited assumptions:
Machine acceptance (named tests and thresholds):
Visual acceptance (views, comparisons, reviewer, target distance):
Validation ladder and run order:
Evidence to preserve (settings, seed, hashes, counts, versions, failures):
Known limitations and unvalidated target environments:
```

## Provisional routing and controlled learning

Working hypothesis only: Luna High may be useful for bounded utility implementation, research, or test-writing when a stronger integrator owns architecture, integration, and final review. Luna Medium is a hypothesis, not demonstrated by the cited procedural-asset evidence. Use deterministic scripts for bookkeeping, hash comparison, manifests, parameter sweeps, and mechanical checks where an LLM adds no judgment. Do not infer a model ranking from a single PR or successful artifact.

To test routing, run matched experiments that vary one factor at a time: reasoning effort; architecture ownership (worker vs lead); validation timing (early targeted gates vs late broad pass); and tool surface (minimal shell/Blender vs richer desktop/MCP access). Freeze repository commit, task definition, model, effort when not under test, instructions, skill/tool set, acceptance tests, starting state, and machine. Use at least three comparable real tasks before changing a durable routing rule; preserve unmatched capability differences explicitly.

| Proposed experiment | Controlled change | Primary decision measure |
|---|---|---|
| Bounded worker effort | Luna Medium versus High on equivalent held-out utilities/fixtures, same acceptance contract | Accepted task after independent review, including correction/reviewer cost |
| Architecture ownership | Worker-led construction versus lead-authored constraints plus workers; equal intended-use brief | Escaped integration defects and total rework, with blind art ratings; a workflow comparison, not isolated model ability |
| Validation scheduling | Targeted early checks/small neutral gallery versus late broad suite; identical final gates | Time/usage until first semantic/art rejection and until final acceptance |
| Harness/tool surface | Same task/model/effort with sufficient minimal versus rich tools | Input/cache overhead and accepted work per allowance/time, retaining capability differences |

Use held-out seeds and randomized task order to reduce learning/carryover effects. Count incomplete/usage-exhausted runs and failed reviews, not only winners. Define pass thresholds before inspecting results; report small-sample uncertainty and separate machine pass from owner art acceptance. Do not remove essential checks just to make an arm look cheaper.

Measure accepted work and quality alongside cost: first-pass and final acceptance, correction/rework turns, reviewer findings/cost, later regressions, human interventions, wall time, and whether Blender/native install/export/human art review were actually performed. Separately record subscription/quota change, token counts and categories, cache reads/writes, API dollars, starting context, tools/MCP schemas, tool calls/results, retries, compactions, and subagents. These are different resource measures; never convert quota to dollars or invent missing measurements. Optimize accepted work per scarce resource, not token price alone. Follow [Harness A/B Test Protocol](../harnesses/HARNESS_AB_TEST_PROTOCOL.md) and account for fixed harness context/tool overhead described in [Harness Baseline](../../baselines/HARNESSES.md).
