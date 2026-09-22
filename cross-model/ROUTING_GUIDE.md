# Cross-Model Routing Guide

This is a current routing heuristic derived from the user's own project evidence. It is not a permanent ranking.

## Route by bottleneck

| Task bottleneck | Current best-supported role |
|---|---|
| Product definition / task shaping | ChatGPT |
| Large end-to-end repo implementation with mature specs | Codex with a high-capability configuration when the integration burden justifies it |
| Routine bounded implementation | Codex with a cost-efficient capable configuration such as the observed Terra High workflow |
| Architecture/governance judgment | High-reasoning ChatGPT/Claude reviewer |
| Live Studio/Blender integration | Claude Code or another code agent with the relevant MCP/environment access |
| 3D base generation | Tripo 3D |
| Repeatable 3D cleanup/validation | Blender scripts/tools + human/agent review |
| Deterministic formatting/validation | Code/scripts, not an LLM |
| Final product acceptance | Human playtest/use |

## The routing pattern that appears most efficient

### Build

Use a capable implementation model with:

- repository source of truth
- clear mission
- hard guardrails
- enough autonomy to finish

### Review

Use an independent strong reasoning model to inspect:

- architecture
- edge cases
- cross-system integration
- silent assumptions
- test gaps

### Correct

Send the implementer a **narrow correction task** grounded in specific review findings.

### Playtest

Use the product as a user.

Convert real friction into the next task.

This loop repeatedly appears more useful than trying to make one giant prompt eliminate all future defects.

## Do not route by prestige

The corpus contains multiple warnings against "always use the biggest model":

- Terra High produced strong bounded implementation at attractive cost.
- Astra Low appeared more economically useful in reviewer/orchestrator roles than as the owner of an enormous implementation wave.
- deterministic transformations should be scripts.
- Tripo is useful for raw geometry but cannot guarantee production readiness.
- live environment access can matter more than raw reasoning score.

## Prompt-size rule

If the repository already contains the details, the task prompt should usually get **shorter**, not longer.

A strong autonomous prompt typically needs:

- mission
- source of truth
- non-negotiable boundaries
- useful external references
- permission to use engineering judgment
- completion evidence standard

Detailed behavior should remain in durable project docs where every future agent can inspect it.

## When to use more prescriptive prompts

Prescriptive prompts are still useful when:

- fixing a known defect list
- performing a migration with exact invariants
- changing only a bounded surface
- preserving an approved architecture
- reviewing a specific PR
- executing a high-risk operation where freedom is undesirable

The Agentic AI lesson is not "always be vague." It is "match task freedom to task maturity."
