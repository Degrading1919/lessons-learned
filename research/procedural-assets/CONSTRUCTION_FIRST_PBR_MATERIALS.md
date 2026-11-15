# Construction-First Procedural PBR Materials

## Caelmor Brookoak evidence and transferable workflow

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

