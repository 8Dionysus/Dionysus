# Seed Decision Rationale Lane

## Index Metadata

- Decision ID: DION-SEED-D-0001
- Original date: 2026-06-04
- Surface classes: docs/decisions, scripts/validation, tests/decision-indexes
- Seed surfaces: decision lane, generated indexes, seed registry, planting trace
- Owner lanes: Dionysus, target repositories, sibling decision lanes
- Guard families: canonical ID, generated index parity, seed-garden boundary, owner-repo handoff
- Posture: accepted

## Context

`Dionysus` did not have a durable generated-indexed decision lane. Its strongest
surfaces already named the source-of-truth order for seed work: wave manifests,
source seed files, closure notes, `seed-registry.yaml`, planting protocol, and
target-repo ownership.

That is good for operating the garden, but weak for future rationale lookup.
When a boundary changes around seed registry policy, planting trace, prep-pack
lifecycle, generated seed capsules, or owner-repo handoff, a future agent needs
one compact place to recover why the route was chosen.

The repo already uses `DION-SEED-Q-####` for quest IDs, so the decision lane
should use the same local seed namespace rather than importing an AoA or sibling
prefix.

## Decision

`Dionysus` will carry durable seed-garden rationale as canonical
`DION-SEED-D-####` decision records under `docs/decisions/`, with generated
lookup indexes under `docs/decisions/indexes/`.

The lane indexes surface classes, seed surfaces, owner lanes, guard families,
date, posture, and canonical path. It explains why routes were chosen, but it
does not become seed source, queue control, target-repo doctrine, or generated
seed authority.

## Options Considered

- Leave decisions implicit in `AGENTS.md`, `README.md`, PRs, and git history.
- Copy a sibling decision lane literally, including non-seed metadata.
- Adopt the sibling generated-index pattern with a Dionysus-local seed prefix
  and seed-garden metadata.

## Rationale

The generated-index pattern makes rationale lookup deterministic without
weakening the existing source-of-truth order. `DION-SEED-D` keeps decision IDs
aligned with `DION-SEED-Q` while separate from seed IDs, registry IDs, and target
repo object IDs.

Seed-specific metadata keeps the lane honest: decisions are about seed surfaces,
owner lanes, planting trace, registry policy, and boundary guards, not about
becoming final AoA or ToS meaning.

## Consequences

Good consequences:

- future agents can find seed-garden rationale by number, date, seed surface,
  owner lane, or guard family;
- stale generated decision indexes become testable;
- the lane can explain route choices without bloating `README.md`;
- target repositories keep stronger planted meaning.

Tradeoffs:

- new route-changing seed work needs metadata discipline;
- generated decision indexes must be refreshed when decision metadata changes;
- this lane must stay smaller than seed files, manifests, registry entries, and
  owner-repo truth.

## Source Surfaces

- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `seed-registry.yaml`
- `docs/codex/planting-protocol.md`
- `docs/SEED_SURFACE_MAP.md`
- `scripts/generate_decision_indexes.py`
- `scripts/validate_decision_records.py`
- `tests/test_decision_indexes.py`

## Validation

Run:

```bash
python scripts/generate_decision_indexes.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_decision_records.py
python -m pytest -q tests/test_decision_indexes.py
```
