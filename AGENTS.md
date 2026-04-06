# AGENTS.md

## Purpose

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem. It stores wave manifests, source seed files, archived canonical surfaces, planting protocol, registry overlays, and durable planting trace when that trace would otherwise be lost.

## Nearest-file precedence

Follow the nearest `AGENTS.md` first when working inside:

- `archive/AGENTS.md`
- `docs/codex/AGENTS.md`
- `reports/planting/AGENTS.md`
- `seed_expansion/AGENTS.md`

## Source-of-truth order

When files pull in different directions, treat these as authoritative in this order:

1. relevant `*_wave.manifest.json`
2. exact canonical source seed file
3. matching closure note for the same wave
4. `seed-registry.yaml`
5. planting protocol and contract files
6. target repository structure and ownership
7. `README.md`

This file explains how to work in the repo. It does not overrule the seed surfaces above.

When work starts from a named prep pack with no manifest, read the pack note and matching `.map.yaml` after checking the stronger live surfaces above. Named prep packs do not overrule an opened wave, `navigation.next_live_seed`, or canonical seed meaning.

## Local contract

- keep `Dionysus` small, legible, lineage-preserving, and transplant-focused
- prefer the smallest source-linked change that makes planting, replay, or navigation clearer
- prefer named prep packs over new numbered waves when multi-repo future work should stay flexible and need-driven
- preserve filenames, anchors, and referenced paths whenever possible
- keep AoA and ToS boundaries explicit
- keep public surfaces public-safe
- treat already-landed repositories as live homes rather than deferred future seeds

## Hard no

- do not turn `Dionysus` into a shadow owner of runtime behavior or target-repo doctrine
- do not let bridge language become identity collapse
- do not treat derived zip exports as seed canon
- do not open a new numbered wave just to store planting priority
- do not leave manifest, registry, closure, archive, and seed-expansion linkage out of sync when one of them changes

## Workflow

`PLAN -> DIFF -> VERIFY -> REPORT`

## Validation

Run the repository entrypoint:

```bash
python scripts/validate_seed_surfaces.py
```

That gate should remain the single seed-surface validation entrypoint.
For repo-local and workflow reinforcement, also run:

```bash
python -m pytest -q tests
```

Use `reports/planting/` only when the target-repo PR or commit trail would not preserve the lineage well enough on its own.
