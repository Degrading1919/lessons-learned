# ChatGPT

## Best-supported roles in this corpus

ChatGPT has been most useful as:

- product/design discussion partner
- task and prompt author for downstream agents
- repository reviewer
- cross-model evaluator
- architecture critic
- decision recorder
- GitHub-aware integrator for bounded changes

The strongest pattern is not "ChatGPT writes the most code." It is that ChatGPT often improves the **task environment** in which Codex, Claude Code, or another tool will work.

## High-confidence lessons

### 1. Prompt design should leave implementation intelligence to the implementation agent

In Agentic AI, the first Codex bootstrap prompt was too narrow and procedural. It explicitly constrained Task 001, prohibited major runtime work, and told the agent to stop after a focused shell.

The user rejected that pattern and asked for a prompt closer to:

> here is the software concept, here are required features, here are existing implementations worth studying, begin

The revised task moved detailed truth into the repository and authorized end-to-end execution. The subsequent Codex/Sol Max run produced the working MVP.

**Lesson:** when the repository already carries the specification, ChatGPT should write a mission, boundaries, useful references, and a completion standard rather than micromanaging implementation steps.

See: [Agentic AI case](../codex/cases/2026-09-22-agentic-ai-sol-max-end-to-end.md).

### 2. Review should preserve good architecture while finding integration errors

Adventurer's Rise repeatedly used ChatGPT as the reviewer after implementation. PR #18 is a useful example: review identified mismatched clock semantics, fabricated begin rewards, missing periodic settlement, startup ordering, and silent reward-credit failure.

The fix prompt was narrow because the implementation already existed.

**Lesson:** broad prompts are valuable for greenfield/end-to-end construction; narrow prompts are valuable when correcting a known defect set.

### 3. Human product feedback should be converted into the next agent task

Folio Phase 1 worked, but user playtesting exposed issues that technical completion did not: pay-date logic, due-date UX, category selection, zero-balance handling, precomputed interest, backup/restore, naming, and graph behavior.

ChatGPT converted that feedback into a targeted correction prompt.

**Lesson:** after a usable build exists, stop theorizing and use real product friction as the highest-value next context.

### 4. Repository grounding beats generic advice

The Bitburner workflow explicitly separated generic strategy knowledge from fork-specific API/syntax/RAM/runtime questions. For the latter, the repository was the authority.

**Lesson:** use general model knowledge for stable concepts; use the actual repository for interfaces, constraints, and current behavior.

## Failure modes observed

- Overly prescriptive implementation prompts can artificially limit strong coding agents.
- Verbose prompts often restate information already available in the repository.
- Prompt writers can invent paths or assumptions unless told to inspect the real repository first.
- Review conclusions should distinguish verified defects from stylistic preference.

## Evidence limits

Some ChatGPT project work is conversational and has no standalone GitHub artifact. Those cases should be treated as preference/process evidence until an artifact or downstream result is linked.
