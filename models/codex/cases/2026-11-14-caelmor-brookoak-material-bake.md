# Case: Caelmor — modeling the shingle before baking finally improved its material

- **Date:** 2026-11-14 (one evolving development/review sequence; not separate matched trials)
- **Project:** Caelmor / Lowmark Brookoak roof shingles
- **Repository:** [Caelmor-Repo](https://github.com/Degrading1919/Caelmor-Repo)
- **Agent/tool attribution:** Owner referred to the material agent as **MMS / Sol**, later set to **High** effort. Earlier study used Terra High graph work and Luna Low checks; a subsequent study had Astra High critique. The decisive final bake pass was explicitly assigned to Sol **without subagents**. Exact underlying Sol release, harness and per-pass effort telemetry were not independently recovered; do not infer a controlled solo-versus-team result.
- **Execution environment:** Local Blender 5.0.1 and Python/NumPy/Cycles; Material Maker 1.7 and MaterialPilot MCP for earlier editable graph studies; GitHub repository; same-wall/UV-scale visual comparisons.
- **Task categories:** procedural 3D, PBR, material authoring, high-poly-to-texture baking, artistic feedback, agent task design, tool selection, Blender integration.
- **Evidence:** **A** for linked prompts/artifacts, iterative owner feedback and documented build/verification; the runtime checks below are agent-reported and captured in source/notes, not independently rerun for this retrospective. Final art approval and Unity runtime validation remain open.

## Objective and starting context

Build a convincing, reusable, game-ready roof material for a grounded medieval RPG, using professional weathered split-timber shingles as a visual quality benchmark: [Pierre Fleau, *Wood Temples Texturing*](https://pfleau.artstation.com/projects/6KW0W). The artist reference informed desired **construction and fidelity**, not a license to reproduce pixels or source graphs.

The production target was a tiling physical repeat **1.28 m across × 2.40 m down/up the roof**: **eight courses, each exposing 0.30 m**. A separate [Roof AutoComplete implementation](https://github.com/Degrading1919/Caelmor-Repo/commit/0169d9643155e49410f15245530589c18c8719f3) already switched between mapped and modeled shingles and registered the albedo's exact hash, joint layout, UV orientation and physical scale. Material improvement therefore had to preserve integration invariants or coordinate registration changes.

## Prompt and feedback lineage

See the [prompt-lineage record](../../../evidence/prompt-lineage/2026-11-14-caelmor-brookoak-material-bake.md). The owner initially asked for dramatically higher-quality procedural PBR textures and supplied the Fleau reference. A research-grounded prompt called for causal wood construction, height-first form hierarchy, reference decomposition, visual tests and independent review. The model implemented that framing mostly **inside the existing 2D material graph** and repeatedly delivered legitimate but insufficient improvements.

After seeing a weak result next to the reference, the owner directly questioned the visual difference, why the professional material had its detail, which underlying construction was missing, and what prevented the agent from addressing it. The agent acknowledged that it had retained the old **lap ramp and perimeter** and spent too much effort on fibers, color and surface marks. Subsequent research narrowed to **Blender + Material Maker**, then the owner explicitly authorized implementation **without subagents** until the material approached the reference.

These were sequential revisions of one real task, **not a test of prompt slogans, model effort settings, or number of research sources**.

## What was built and how it changed

| Stage and evidence | Observed method | Result / feedback |
| --- | --- | --- |
| [Original registered Brookoak](https://github.com/Degrading1919/Caelmor-Repo/commit/51f3f1542275bb96d131e2e1f03baf735e971f64) | Native Material Maker graph with registered staggered courses, noise-driven wood fiber, edge/lap relief and four PBR outputs | Reproducible and aligned, but in-house roof views read flat and uniform. Owner wanted much more depth/character. |
| [Timber Study](https://github.com/Degrading1919/Caelmor-Repo/commit/430ef659553bea64063b02193fa745652e515e53) | 2K graph study added board-local fibers, knot influence, splits and warmer albedo | Technically verified but owner explicitly declined artistic approval; at building distance much of the improvement read as recoloring. |
| [Graph refinement](https://github.com/Degrading1919/Caelmor-Repo/commit/a5749a0123464ced2882362d90750d7f4a83c11d) | Broader riven grain and end checks; knot attempts rejected when they produced artificial contours | Better fiber detail, but doubled dark lap lines, smooth/rounded boards and weak exposed ends persisted. Reviewer criticism and user comparison showed the underlying representation remained wrong. |
| [Riven Bake construction](https://github.com/Degrading1919/Caelmor-Repo/commit/3c30aedce2f1763ded1562981a2d303df22d92fa) | [Editable Blender Python source](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/build_brookoak.py) creates separate overlapping shingles with taper, cupping, twisting, sidewalls, end faces, irregular corners, split/growth fields and damage. Cycles bakes a four-channel 2K tile from the modeled source. | Owner's direct reaction: **“This is much better.”** The high-poly construction and neutral-light tests resolved much of the missing thickness and overlap. Agent still reported weaker torn fibers, abrasion and fracture relative to the reference. |

**Decisive mechanism:** A texture-level gradient representing a seam is not a timber board. The final procedure represented **each shingle as an actual object first**—including its exposed end and relationship to the board beneath it—then projected that construction into height, normal, albedo and roughness. The improvement is plausibly attributable to changing the representation **and** to the earlier critique/research/iteration, not to an isolated wording trick.

## Technical artifact and verification

The final commit contains [the builder](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/build_brookoak.py), [bake instructions](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/README.md), [modeled/baked comparison](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/Lowmark_Brookoak_RoofShingles_RivenBake_review.jpg), [2×2 repeat](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/Lowmark_Brookoak_RoofShingles_RivenBake_repeat.jpg), and [generator integration preview](https://github.com/Degrading1919/Caelmor-Repo/blob/3c30aedce2f1763ded1562981a2d303df22d92fa/MEDIA/Materials/procedurally_generated/Lowmark_Brookoak_RoofShingles_RivenBake_integration.jpg).

The agent reported and its checked-in builder/README support the following **local authoring checks**:

- Deterministic regeneration of **2048 × 2048** albedo, tangent-space normal, roughness and height; byte-for-byte matching four-map rebake in the reported run.
- Physically scaled repeating tile with registered joint centers. Neutral clay tests under reversed lighting separated structural volume from painted effects; paired modeled-versus-baked views expose projection loss.
- Cycles selected-to-active projection from modeled shingles to a UV plane. Height uses a declared **50 mm** normalization range. Seam/repeat review was performed.
- Isolated Blender binding at Roof AutoComplete **0%, 50% and 100%** detail by temporarily supplying the candidate hash. **Production registration was left unchanged**; this is not a verified installed add-on or Unity result.

A modeled board and a flat baked surface cannot share silhouette fidelity. Missing corners, undercuts and lifted splinters require real geometry. Applying full lap normals over already-dimensional shingles can double the relief; modeled shingles need an appropriate **wood-only** material or residual detail branch.

## Human signal, failed approaches and costs

The owner consistently rejected the graph-only material as short of the professional reference, including after it passed graph validators and deterministic exports. The owner preferred the later high-poly-derived bake, explicitly describing it as **much better** and asking why. The agent's own explanation matches the visual change: modeled taper, thick butts, true end faces, overlapping undercourses, chips and grain-aligned checks produced depth that face streaks alone could not.

Recorded failure modes:

- Iterating more fibers, noise, roughness and palette after reviewers had already identified an incorrect board cross-section.
- Treating knots as isolated pits/closed rings rather than growth fields redirecting fibers.
- Conflating deterministic PBR export, higher texture resolution or attractive grazing-light previews with actual material realism.
- Letting generator compatibility with the previous shingle registration discourage architectural revision of the high-poly source.
- An early review/research cycle summarized only seven retained sources; the larger lesson is **relevant physical diagnosis and executable tests**, not a mandatory source count.
- The final pass used no subagents by owner request, but there are **no controlled resource or quality measurements** proving solo execution beats multi-agent execution.

Time, token consumption, subscription quota and dollar cost were not provided; record as **unknown**.

## Transferable workflow for future projects

Use this **construction-first procedural material protocol** where identity depends on assembly, thickness or visible wear (shingles, bricks, masonry, armor plates, bark, roof tiles):

1. **Define the physical object and manufacturing/exposure history.** State what the viewer must read at full object, medium form and microdetail scales.
2. **Freeze integration contracts first:** units, tile footprint, orientation, course gauge, joint/ID layout, seeds, UV phase, map packing and target engine. Distinguish changeable visual style from required interfaces.
3. **Prototype a small assembled patch in neutral clay** with opposite light directions. Require readable cross-sections, contact, overlap and fractures **before** color or fine fibers.
4. **Use geometry for macro/meso forms**, including true sides, warped boards and altered silhouettes. Use Material Maker or native shaders for subordinate wood fibers, color, fine cracks and condition, each driven by common physical feature fields.
5. **Bake the reusable representation** at declared real-world scale; verify albedo contains no baked directional shading, normals/height agree, roughness responds to the same causes, and seams tile.
6. **Compare modeled and baked versions** with matched cameras, lighting and scale, then test at target in-game distance. Determine which missing forms must remain dimensional geometry at LODs.
7. **Preserve and check the baseline**: fixed seed, export hashes, registration/UV contract, mixed flat+modeled tests and target-runtime import. Do not promote a candidate merely because a bake reproduces.
8. **Keep human art acceptance separate** from code/test/export success; document rejected examples and the visual cause of each correction.

An AI agent should be asked to **predict what a construction change will make visible and test that prediction**. If the grayscale board patch still reads like flat panels, do not compensate with stronger albedo or extra scratches. Use a narrow falsifying prototype instead of another large undirected graph pass.

## Supported lesson

**For assembled materials whose perceived realism comes from thickness, contacts and broken silhouettes, it can be more effective to procedurally construct the high-detail object and bake it than to keep refining a flat graph.** In this case, that representation change—combined with the owner's reference-grounded critique and native clay/PBR tests—produced the first explicitly preferred material.

This is an observed **workflow/tool-selection** lesson, not a causal claim that Sol High, Blender, a particular skill or a longer research prompt is universally best.

## What this does not prove

- No controlled comparison of Material Maker graph capability versus all possible procedural graph methods, nor of Sol versus Terra/Luna or single-agent versus subagent execution.
- No final owner production-art approval, game-camera playtest, shipped Unity import, runtime performance measurement, or production texture hash swap.
- No claim that the 2K baked atlas reproduces every feature of the artist's professional source. It was an original study using a reference, not reverse engineering of that artist's private node graph.
- No guarantee that modeled-and-baked is appropriate for materials whose appearance derives predominantly from surface chemistry or roughness rather than physical assembly.

## Dataset tags

```yaml
task_types: [procedural 3D, PBR, material authoring, Blender baking, human art review, prompting]
model_family: OpenAI/Sol (exact release unverified)
model_label: Sol High (owner-visible label)
tooling: [Blender 5.0.1, Python, NumPy, Cycles, Material Maker 1.7, MaterialPilot MCP, GitHub]
artifact_type: Blender procedural source + four-channel baked tile + comparison renders
verification: [agent-reported deterministic rebake, clay render, matched comparisons, isolated Roof AutoComplete material binding]
human_signal: original graph rejected; later Riven Bake explicitly preferred as "much better"
outcome: viable reviewed candidate, not production-approved or Unity-verified
evidence_level: A (task/artifact/human signal), constrained technical claims
```
