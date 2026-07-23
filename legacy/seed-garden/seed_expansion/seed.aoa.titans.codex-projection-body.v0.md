# AOA-TITAN-SEED-02: Codex Projection Body

## Purpose

Bind the Titan names to the existing Codex role projection without making the installed `.codex/agents/` files the source of truth.

## Contract

`aoa-agents` owns role meaning. Codex TOML files are generated projection bodies. Workspace `.codex/agents/` is an install surface, not a sovereign role authoring surface.

## Required mapping

```text
Atlas    -> architect       -> read-only
Sentinel -> reviewer        -> read-only
Mneme    -> memory-keeper   -> read-only
Forge    -> coder           -> workspace-write
Delta    -> evaluator       -> read-only
```

## First landing

Target repos: `aoa-agents`, then `8Dionysus`

Required surfaces:

```text
aoa-agents/docs/TITAN_SERVICE_COHORT.md
aoa-agents/generated/titan_service_cohort_index.min.json
8Dionysus/docs/TITAN_FIRST_APPEARANCE_RUNBOOK.md
```

## Validation

Run the Codex subagent projection builder and validator in `aoa-agents`. Then validate the Codex plane in `8Dionysus`.

## Non-goals

This seed does not hand-edit installed `.codex/agents/*.toml` and does not duplicate MCP server declarations inside every agent file.
