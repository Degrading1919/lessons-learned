# Tripo 3D

## Core production lesson

Tripo should be treated as a **geometry-generation stage**, not as a production-readiness oracle.

The strongest workflow that emerged from Margins was:

> task-specific prompt/reference → Tripo generation → inspect → Blender cleanup/normalization → downstream material/engine validation → record measured production data

For Margins the broader pipeline became:

> Tripo 3D → Blender cleanup → Substance Painter → Unity

For Adventurer's Rise:

> Tripo 3D → Blender cleanup/optimization → Roblox Studio

## Prompting rules that survived use

The repository-local Margins skill (PR #24) encoded several rules that repeatedly proved useful:

- choose text-to-3D vs image-to-3D vs multiview based on the asset
- keep reference images clean and production-oriented
- for characters, use symmetrical T/A poses, full uncropped body, separated limbs, readable joints, even lighting, and minimal occlusion
- prefer orthographic/front/side information when using references
- describe silhouette, construction, proportions, and material identity before decorative detail
- optimize for reusable asset families, not one-off hero meshes
- do not promise exact topology, exact polygon counts, rigging success, cleanup time, or production readiness from a prompt

PR:
https://github.com/Degrading1919/margins/pull/24

## Negative visual feedback matters

One early Margins door/reference attempt was rejected by the user as "garbage."

That is important evidence. The failure was not solved by adding more adjectives. The accepted direction emphasized:

- believable real thickness
- chunky/softened forms
- restrained wear
- subtle faceting
- neutral studio presentation
- stylization without collapsing into cartoon proportions or CAD realism

**Lesson:** visual prompting should be corrected from concrete rejected/accepted examples, not from generic style words alone.

## Measured budgets beat speculative budgets

Margins PR #43 rebuilt the asset budget around measured/production-informed data rather than carrying forward guessed triangle ceilings.

https://github.com/Degrading1919/margins/pull/43

The catalog records:

- raw source triangle count
- measured vs ceiling LOD counts
- source/provenance
- normalization state
- materials/textures
- collision
- expected instance count
- viewing distance
- production status

Later work derived Tripo quad-face input limits from approved LOD0 triangle ceilings.

**Lesson:** use Tripo output as empirical input to pipeline standards. Do not invent technical budgets before seeing representative generated assets.

## Transfer to Adventurer's Rise

The same prompting discipline was adapted in Adventurer's Rise PR #24:

https://github.com/Degrading1919/adventurers-rise/pull/24

What transferred:

- evidence discipline
- prompt anatomy
- method selection
- cleanup assumptions
- family reuse
- failure-driven iteration

What did not transfer blindly:

- Unity-specific budgets
- Margins visual assumptions
- unsupported polygon/texture/collision/LOD/rig limits

**Lesson:** a good AI skill captures process, not project-specific numbers masquerading as universal truth.
