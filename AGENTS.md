# AGENTS.md

Root route card for `Dionysus`.

## Purpose

`Dionysus` is the seed garden and dispatch layer for AoA / ToS.
It keeps early forms, wave manifests, seed files, closure notes, prep packs, registry overlays, and planting trace legible until stronger owner repositories can receive them.

## Owner lane

This repository owns:

- seed sources before or between plantings
- wave manifests, closure notes, prep packs, archive surfaces, and seed registry overlays
- planting protocol, replay route, and durable lineage trace when target-repo history is not enough

It does not own:

- final AoA doctrine, final ToS meaning, runtime behavior, SDK helper behavior, or target-repo implementation law
- a shadow backlog disguised as seed canon
- quest or continuity language that hides missing owner routes

## Start here

1. the relevant `*_wave.manifest.json` or current live gated seed surface
2. the exact source seed file
3. the matching closure note when one exists
4. `seed-registry.yaml`
5. `ROADMAP.md`
6. `docs/SEED_SURFACE_MAP.md`
7. `docs/codex/planting-protocol.md`
8. the target repository ownership docs
9. `docs/AGENTS_ROOT_REFERENCE.md` for preserved full root guidance


## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Route away when

- the seed has landed and the owner repository is clear
- source-linked knowledge belongs in `Tree-of-Sophia`
- ecosystem doctrine belongs in `Agents-of-Abyss`
- runtime belongs in `abyss-stack`
- typed helper behavior belongs in `aoa-sdk`
- operator companion behavior belongs in `ATM10-Agent`

## Verify

Default seed-surface check:

```bash
python scripts/validate_seed_surfaces.py
```

When the compact seed route capsule changes:

```bash
python scripts/build_seed_route_map.py --check
python scripts/validate_seed_route_map.py
```

For repo-local reinforcement, also run:

```bash
python -m pytest -q tests
```

## Report

State which seed surface changed, whether meaning or only staging/routing changed, whether lineage or replay posture changed, and whether follow-up now belongs in a stronger owner repo.

## Full reference

`docs/AGENTS_ROOT_REFERENCE.md` preserves the former detailed root guidance for source-of-truth order, prep-pack posture, MCP route details, and planting trace review.
