# AGENTS.md
Local guidance for `scripts/` in `Dionysus`.

Read the root `AGENTS.md` first. This directory contains builders, validators,
decision-index helpers, the stats-contract delegate, and repo-local MCP
entrypoints that keep the seed garden legible.

## Local role
Scripts should be deterministic, repo-relative, public-safe, and weaker than the
seed surfaces they validate. `validate_seed_surfaces.py` remains the central
seed-surface entrypoint.

## Editing posture
Prefer check modes for generated outputs. Keep scripts runnable from the repo
root. Avoid hidden network calls, hidden writes into owner repositories, and
environment-specific assumptions.

## Hard no
Do not let a helper script become planting authority. Do not bury seed meaning
inside code when it belongs in manifests, registry entries, docs, or owner repos.

## Validation
Run the specific script in check mode when available, then use the executable
repository gate:

```bash
python scripts/release_check.py
```
