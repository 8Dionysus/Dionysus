# Dionysus Seed Garden

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem.

It stores seed sources, wave manifests, archived planting surfaces, and the minimal protocol needed to move seeds into owning repositories. It is not the final owning home of AoA meaning, ToS meaning, or repo-local implementation detail.

## What belongs here

- seed sources before or between plantings
- wave manifests that define order
- archived canonical seed surfaces kept for lineage
- live gated future-work seeds that are not yet open waves
- planting protocol, registry overlays, and validation surfaces
- planting trace only when the trace would otherwise be lost

## What does not belong here

- runtime services
- final repo-owned doctrine that should live in a target repo
- derived graph/export/UI inflation
- silent AoA ↔ ToS collapse
- repo-local backlog disguised as seed canon

## Current state

- `first_wave.manifest.json` through `ninth_wave.manifest.json` define the planting waves.
- `scripts/validate_manifest.py` validates manifest refs.
- `scripts/validate_seed_registry.py` validates `seed-registry.yaml`, wave linkage, and closure-note status alignment.
- `scripts/validate_nested_agents.py` validates the required root and local `AGENTS.md` coverage for the wave 1.3 operating surfaces.
- `scripts/validate_seed_surfaces.py` runs all three validators as one entrypoint.
- `archive/` is the canonical archive root.
- `archive/seed_pack_2026-03-22/` is the archived canonical source pack for the closed ninth wave.
- `archive/seed_post_wave/seed.aoa.agents-runtime-pack.v0.md#aoa-seed-r1-agents-runtime-seam` is the archived source pack for the landed post-wave runtime slice.
- `seed_expansion/seed.tos.wider-world-thought-expansion.v0.md#tos-expansion-wider-world-thought-expansion` is the next live gated seed surface.
- `seed-registry.yaml` is the navigation overlay for humans and Codex.
- `schema/seed-registry.contract.yaml` defines the registry field contract.
- `docs/codex/planting-protocol.md` defines the planting discipline.
- `templates/planting-report.template.md` and `reports/planting/` define how planting trace should be stored when Dionysus keeps the report.

## Source-of-truth order

When there is tension between files, read in this order:

1. wave manifest
2. canonical source seed file
3. closure note for the same wave
4. `seed-registry.yaml`
5. planting protocol and contract files
6. target repository structure and ownership
7. `README.md`

The manifest defines order. The seed file defines meaning. The closure note defines the finished state of a closed wave. The registry makes navigation legible. The README should explain, not overrule.

## Repository map

- `archive/`
  - historical canonical seed sources
  - previous bundles, rootlines, witness seeds, templates, branch pilots, soil-prep files, archived packs, and archived post-wave seed-packs
- `seed_expansion/`
  - next gated future-work surface only
- `*_wave.manifest.json`
  - machine-readable planting order by wave
- `ninth_wave.closure.md`
  - closure state and landed surfaces for wave nine
- `seed-registry.yaml`
  - human/Codex navigation overlay
- `schema/seed-registry.contract.yaml`
  - registry field contract and cross-link expectations
- `AGENTS.md` and local `AGENTS.md` files
  - repo and directory-level operating guidance for Codex and maintainers
- `docs/codex/planting-protocol.md`
  - planting rules for Codex and maintainers
- `templates/planting-report.template.md`
  - reusable planting report template
- `reports/planting/`
  - durable planting trace when Dionysus is the right place to hold the report
- `scripts/validate_manifest.py`
  - manifest reference validator
- `scripts/validate_seed_registry.py`
  - registry and closure-alignment validator
- `scripts/validate_nested_agents.py`
  - required `AGENTS.md` coverage validator
- `scripts/validate_seed_surfaces.py`
  - single validation entrypoint for CI and local runs
- `seed_expat.md`, `seed_self-agent.md`, `seed_trio.md`
  - origin notes and fertile soil, not first-wave canon

## Seed lifecycle

- `archived_canonical`
  - historical seed source still needed for lineage and replay
- `pending_archive`
  - temporary source surface still live only until archive move
- `gated_next`
  - acknowledged next seed surface, not yet an opened wave
- `landed_post_wave`
  - planted and merged post-wave seed kept live in the registry even after archive cleanup, until a later lifecycle-model pass changes that status

## Wave map

- `first_wave`: trunk-first structure and parent axis
- `second_wave`: method spine
- `third_wave`: counterpart bridge
- `fourth_wave`: witness and compost pilot pair
- `fifth_wave`: ToS growth law trio
- `sixth_wave`: ToS corpus scaffold
- `seventh_wave`: bounded lineage pilot
- `eighth_wave`: soil prep before manual Zarathustra entry
- `ninth_wave`: AoA contract growth, now closed and archived on canonical terms

## Using Dionysus to plant with Codex

1. Pick the wave manifest.
2. Read the exact source seed referenced by the manifest.
3. Open the matching entry in `seed-registry.yaml`.
4. Read the target repository before writing anything.
5. Plant the smallest linked slice that leaves:
   - one human-readable explanation
   - one structural artifact
   - preserved seed vocabulary
   - explicit boundaries
6. Stop at contracts/docs when a seed would cross red-risk zones.
7. Leave trace in the PR, commit message, or a report based on `templates/planting-report.template.md`.

Operational editing guidance lives in `AGENTS.md` and the nearest nested `AGENTS.md`.

See `docs/codex/planting-protocol.md` for the detailed rules.

## Validation

```bash
python scripts/validate_seed_surfaces.py
```

This runs:

- `python scripts/validate_manifest.py`
- `python scripts/validate_seed_registry.py`
- `python scripts/validate_nested_agents.py`

The registry validator checks field shape, path validity, anchor validity, wave linkage, next-live-seed coherence, and closure-note status alignment. The nested-agents validator checks that the required root and wave-local `AGENTS.md` files are present and non-empty.

A GitHub Actions workflow lives at `.github/workflows/validate-seed-surfaces.yml`.

## Working rule

When in doubt:

- plant structure before expansion
- plant authored and source-linked surfaces before derived projections
- plant lineage before archive
- plant bridges as derived contracts, not identity collapse
- plant witness and compost as public contracts before heavier runtime instrumentation
- plant templates before branch multiplication
- plant one bounded pilot before plurality
- keep Dionysus small, legible, and transplant-focused
