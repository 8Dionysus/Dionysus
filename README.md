# Dionysus Seed Garden

`Dionysus` is the seed-source repository for the current AoA/ToS planting wave.

It stores candidate seeds, compressed bundles, rootline documents, and witness-oriented follow-up seeds.
It is not the final owning home of AoA or ToS layer meaning.

## Canonical first-wave start

The first planting wave now follows **trunk-first** order:

1. `seed_rootline/seed.8dionysus.aoa-tos.rootline.md`
2. `seed_bundle/seed_bundle.md`
3. repo-line translations:
   - `seed_rootline/seed.8dionysus.aoa.kernel-line.md`
   - `seed_rootline/seed.8dionysus.tos.genealogical-memory.md`
   - `seed_rootline/seed.8dionysus.aoa-shared.bridges.md`

Use the rootline as the parent axis.
Use the bundle as the priority map.
Use the repo-line seeds as planting guides for actual layer repositories.

Validation:

```bash
python scripts/validate_manifest.py
```

## First-wave order

The current first-wave sequence is:

1. AoA x ToS rootline
2. AOA-SEED-01 - Ontology Spine of Action
3. AOA-SEED-03 - Narrative-Core Memory
4. TOS-SEED-01 - Layered Node Contract
5. TOS-SEED-02 - Lineage Before Archive
6. AOA-SEED-02 - Self-Agent Checkpoint Stack
7. TOS-SEED-04 - Interpretation Ladder
8. AoA-ToS Bridge Contracts

The Witness / Compost pair remains important, but belongs **after** this structural wave:

- `seed_witness/seed.aoa.protocol-witness.v0.md`
- `seed_witness/seed.tos.context-compost.v0.md`

## Origin notes, not first-wave canon

These files remain useful as origin commentary and fertile soil, but they are not the canonical first-wave start:

- `seed_expat.md`
- `seed_self-agent.md`
- `seed_trio.md`
- `0ld/`

## Working rule

When in doubt:

- plant structure before protocols
- plant explicit boundaries before bridges
- plant authored/core memory before derived retrieval surfaces
- plant ToS node law before archive growth
