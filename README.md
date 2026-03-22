# Dionysus Seed Garden

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem.

It stores seed sources, wave manifests, and archived planting surfaces. It is not the final owning home of AoA meaning, ToS meaning, or repo-local implementation detail.

## What belongs here

- seed sources before or between plantings
- wave manifests that define order
- archived canonical seed sources kept for lineage
- planting protocol and navigation overlays for humans and Codex

## What does not belong here

- runtime services
- final repo-owned doctrine that should live in a target repo
- derived graph/export/UI inflation
- silent AoA ↔ ToS collapse
- repo-local backlog disguised as seed canon

## Current state

- `first_wave.manifest.json` through `ninth_wave.manifest.json` define the planting waves.
- `scripts/validate_manifest.py` validates those manifests.
- `0ld/` is the historical canonical archive of planted seed sources.
- `0ld/seed_pack_2026-03-22/` is the archived canonical source pack for the closed ninth wave.
- `ninth_wave.closure.md` closes the ninth wave on contract-first terms and records the archive move.
- `seed_expansion/seed.tos.wider-world-thought-expansion.v0.md#tos-expansion-wider-world-thought-expansion` is the next live gated seed surface.
- `seed-registry.yaml` is the navigation overlay for humans and Codex.
- `docs/codex/planting-protocol.md` defines the current planting discipline.

## Source-of-truth order

When there is tension between files, read in this order:

1. wave manifest
2. canonical source seed file
3. closure note or supporting note for the same wave
4. `seed-registry.yaml`
5. target repository structure and ownership

`seed-registry.yaml` is intentionally redundant with the manifests. The manifest defines order. The seed file defines meaning. The registry makes navigation legible.

## Repository map

- `0ld/`
  - historical canonical seed sources
  - previous bundles, rootlines, witness seeds, templates, branch pilots, and soil-prep files
- `0ld/seed_pack_2026-03-22/`
  - archived canonical source pack for the closed ninth wave
- `seed_expansion/`
  - next live surface after the archive move
- `*_wave.manifest.json`
  - machine-readable planting order by wave
- `ninth_wave.closure.md`
  - closure state and landed surfaces for wave nine
- `scripts/validate_manifest.py`
  - manifest reference validator
- `seed-registry.yaml`
  - human/Codex navigation overlay
- `docs/codex/planting-protocol.md`
  - planting rules for Codex and maintainers
- `seed_expat.md`, `seed_self-agent.md`, `seed_trio.md`
  - origin notes and fertile soil, not first-wave canon

## Seed lifecycle

- `archived_canonical`
  - historical seed source still needed for lineage and replay
- `pending_archive`
  - temporary pack or surface still live only until archive move
- `gated_next`
  - next seed surface acknowledged but not yet opened as a full wave

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
7. Leave trace in the PR, commit message, or planting report.

See `docs/codex/planting-protocol.md` for the detailed rules.

## Validation

```bash
python scripts/validate_manifest.py
```

The current validator checks the wave manifests. It does not yet validate `seed-registry.yaml` or planting reports.

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
