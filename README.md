# Dionysus Seed Garden

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem.

It stores seed sources, wave manifests, archived planting surfaces, live gated expansion surfaces, and the minimal protocol needed to move bounded seeds into owning repositories. It is not the final owning home of AoA meaning, ToS meaning, runtime behavior, or repo-local implementation detail.

> Current release: `v0.1.0`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Start here

Read in this order:

1. the relevant `*_wave.manifest.json`
2. the exact source seed named by that manifest
3. the matching closure note for that wave when one exists
4. `seed-registry.yaml`
5. `docs/codex/planting-protocol.md`
6. the target repository structure and ownership
7. `AGENTS.md` and the nearest nested `AGENTS.md`

If work starts from a named prep pack rather than an opened wave, read the pack note and matching `.map.yaml` after checking the stronger live surfaces above. Named prep packs are flexible staging notes. They do not overrule an opened wave or the current live seed.
After reading a prep-pack note, verify the owner repo directly before treating staging guidance as current queue truth.

## What belongs here

- seed sources before or between plantings
- wave manifests that define order
- archived canonical seed surfaces kept for lineage and replay
- live gated future-work seeds that are not yet open waves
- named prep packs for flexible future-work staging when a new numbered wave would be premature
- planting protocol, registry overlays, and validation surfaces
- planting trace when the target-repo trail would not preserve the lineage well enough

## What does not belong here

- runtime services
- final repo-owned doctrine that should live in a target repository
- derived graph, export, or UI inflation
- silent AoA ↔ ToS collapse
- repo-local backlog disguised as seed canon

## Key live surfaces

- `archive/` is the canonical archive root for historical seed sources
- `archive/seed_pack_exports/` holds derived ingress and transport bundles only; never treat them as canonical seed surfaces
- `seed_expansion/` holds the current gated next-work surfaces after the archived ninth wave
- `generated/seed_route_map.min.json` is the compact low-context seed entry capsule; `seed-registry.yaml` remains the canonical seed ledger and navigation overlay
- `seed-registry.yaml` is the human/Codex navigation overlay
- `docs/SEED_SURFACE_MAP.md` explains how to read `seed_staging/` and `seed_notes/exploratory/` without confusing canon, staging, lineage, and exploratory donor notes
- `docs/codex/` holds the planting protocol and provenance rules
- `docs/CODEX_MCP.md` explains the repo-local Codex MCP surface and its stop rules
- `templates/planting-report.template.md` defines the durable planting-report shape when Dionysus needs to hold the trace
- `reports/planting/README.md` explains when Dionysus should keep durable planting trace instead of relying on target-repo PR or commit history alone
- `scripts/validate_seed_surfaces.py` is the single seed-surface validation entrypoint
- `seed_staging/` holds structured transport and staging packs grouped by domain instead of mixing them into the root
- `seed_notes/exploratory/` holds informal exploratory seed texts that should not be mistaken for queue control
- repo-local questbook surfaces in `QUESTBOOK.md`, `quests/`, `schemas/`, and `generated/` are follow-through for the seed garden, not a second sovereignty layer
- `aoa-sdk` has already been seeded into its own live repository and should be treated as a live owning home for SDK work rather than as deferred future separation

## Source-of-truth order

When files pull in different directions, treat these as authoritative in this order:

1. relevant `*_wave.manifest.json`
2. exact canonical source seed file
3. matching closure note for the same wave
4. `seed-registry.yaml`
5. planting protocol and contract files
6. target repository structure and ownership
7. `README.md`

The manifest defines order. The seed file defines meaning. The closure note defines the finished state of a closed wave. The registry makes navigation legible. The README should explain, not overrule.

## Using Dionysus to plant with Codex

1. Pick the wave manifest or the current live gated seed.
2. Read the exact source surface.
3. Open the matching entry in `seed-registry.yaml`.
4. Read the target repository before writing anything.
5. Plant the smallest linked slice that leaves:
   - one human-readable explanation
   - one structural artifact
   - preserved seed vocabulary
   - explicit boundaries
6. Stop at contracts or docs when a seed would cross red-risk zones.
7. Leave trace in the target PR or commit trail, or in `reports/planting/` when the lineage would otherwise be lost.

For donor-shaped or mixed seeds, also record donor repo/ref, transplant policy, redistribution obligations, and explicit `what survives` / `what stays behind` notes.
When an owner-repo landing merges and Dionysus still keeps a linked prep pack or transport note for lineage, update `lifecycle_status` and `lifecycle_note` in the same cleanup pass so staged-only markers do not outlive the merge.

## Validation

The seed-surface validation entrypoint remains:

```bash
python scripts/validate_seed_surfaces.py
```

For the compact seed-entry capsule itself, use:

```bash
python scripts/build_seed_route_map.py --check
python scripts/validate_seed_route_map.py
```

For current repo-local and workflow reinforcement, also run:

```bash
python -m pytest -q tests
```

For the optional repo-local MCP slice, also run:

```bash
python -m pytest -q tests/test_dionysus_mcp_state.py
python scripts/dionysus_mcp_server.py
```

For advisory v3 readiness status only, also use:

```bash
python scripts/check_seed_registry_v3_readiness.py seed-registry.yaml --write-report reports/seed-registry-v3-readiness.md
```

## Working rule

When in doubt:

- plant structure before expansion
- plant authored and source-linked surfaces before derived projections
- plant lineage before archive
- plant bridges as derived contracts, not identity collapse
- plant witness and compost as public contracts before heavier runtime instrumentation
- plant templates before branch multiplication
- use named prep packs when future work needs priority and dependency control without a fresh numbered wave
- keep Dionysus small, legible, and transplant-focused
