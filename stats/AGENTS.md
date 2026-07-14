# AGENTS.md

Route card for owner-local statistical questions in `Dionysus`.
Read the root `AGENTS.md` first.

## Applies to

Everything under `stats/`.

## Role

This directory owns statistical questions over seed-garden objects whose
meaning belongs to `Dionysus`. Shared measurement grammar and cross-owner
composition remain owned by `aoa-stats`.

## Read before editing

1. Root `AGENTS.md`, `README.md`, and `ROADMAP.md`.
2. `seed-registry.yaml`, `schema/seed-registry.contract.yaml`, and
   `scripts/validate_seed_registry.py`.
3. `docs/SEED_SURFACE_MAP.md` and `docs/codex/planting-protocol.md`.
4. `stats/README.md` and `stats/port.manifest.json`.
5. The central measurement and packet contracts under `aoa-stats/stats/`.

## Boundaries

- The validated registry v2 `seed_index` is the exact population. Wave rows,
  origin notes, staging files, archives, reports, and target-repository state
  do not enter the denominator.
- Only the literal owner-authored label `landed_post_wave` enters the
  numerator. Do not reinterpret other lifecycle labels as ordinal progress.
- A complete population with no `landed_post_wave` rows is an observed zero.
- An unsupported registry version or a malformed, empty, or duplicate
  population is unknown, not zero.
- The reference packet is weaker than `seed-registry.yaml`, the exact seed
  sources, wave manifests, closure notes, and target-repository reality.
- The ratio does not prove that a target landing exists, remains current, was
  accepted, is complete, or carries canonical meaning.

## Validation

Inspect the registry and packet first. The port validator requires a compatible
`aoa-stats` checkout through `AOA_STATS_ROOT`, `.deps/aoa-stats`, or the sibling
`../aoa-stats` path; CI supplies its pinned checkout explicitly, and an
unavailable central validator is a failed check. Then run:

```bash
python scripts/validate_local_stats_port.py
python -m pytest -q tests/test_local_stats_port.py
```

Use the root route for repository-wide validation.

## Closeout

Report the seed-garden question, exact registry population, manual positive and
negative cases, packet posture, central validation, and repository validation.
