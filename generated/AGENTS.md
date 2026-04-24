# AGENTS.md
Local guidance for `generated/` in `Dionysus`.

Read the root `AGENTS.md` first. This directory holds compact derived
navigation capsules for the seed garden, including `generated/seed_route_map.min.json`.

## Local role
Generated files make low-context seed entry easier, but they do not own seed
meaning. Manifests, exact seed sources, closure notes, `seed-registry.yaml`, and
planting protocols remain stronger.

## Editing posture
Do not hand-edit compact surfaces when a builder owns the output. Change the
source surface or builder, then regenerate. Preserve stable ids, source refs,
lifecycle markers, and owner-repo routing.

## Hard no
Do not treat a generated route map as seed canon, queue sovereignty, or proof
that an owner repository has accepted work.

## Validation
When generated seed route surfaces change, run:

```bash
python scripts/build_seed_route_map.py --check
python scripts/validate_seed_route_map.py
python scripts/validate_seed_surfaces.py
```
