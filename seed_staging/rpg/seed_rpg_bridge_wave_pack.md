seed_id: seed.rpg.bridge-wave-pack.v0
title: RPG Bridge Wave Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: landed_upstream_retained_for_lineage
lifecycle_note: RPG bridge-wave surfaces are landed upstream across owner repos; keep this pack as lineage and transport only.
reality_checked_at: '2026-04-04'
status: pending_archive
priority: next
parent_seed: seed.rpg.architecture-rfc.v0
tags:
  - rpg
  - bridge-wave
  - unlock-proof
  - party-template
  - navigation

# Seed Note: RPG Bridge Wave Pack

## Purpose

Prepare the next adjunct RPG bridge rollout as a named prep pack without opening a fresh numbered wave.

This pack stages the bridge between proof, composition, and navigation so later runtime/frontend work can read honest source-owned contours instead of inventing them.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.

This prep pack belongs here because:

- the rollout spans multiple owning repositories
- it should stay transport-shaped until the owner repos accept the landings
- prior RPG lineage should remain visible instead of being flattened into one giant wave
- the package is better treated as staging and transport than as new doctrine authority

## Bundle contents to preserve

The source artifact is `archive/seed_pack_exports/rpg_bridge_wave_seed.zip`.

It carries:

- `rpg_bridge_wave_seed/README.md`
- `rpg_bridge_wave_seed/APPLY_ORDER.md`
- `rpg_bridge_wave_seed/CODEX_NOTES.md`
- `rpg_bridge_wave_seed/SEED_MANIFEST.yaml`
- `rpg_bridge_wave_seed/COVERAGE_MAP.md`
- `rpg_bridge_wave_seed/TOUCHPOINTS_NOT_INCLUDED.md`
- `rpg_bridge_wave_seed/later-wave-targets.md`
- repo-local bridge-wave surfaces for `Agents-of-Abyss`, `aoa-evals`, `aoa-playbooks`, and `aoa-routing`
- this `Dionysus` prep-pack note, map, and quest object

## Ownership posture

Read the later plantings under these repo-home boundaries:

- `Agents-of-Abyss` owns the common bridge-wave model and anti-collapse law
- `aoa-evals` owns unlock-proof meaning
- `aoa-playbooks` owns party-template and build-synergy meaning
- `aoa-routing` owns derived navigation cards and nothing stronger
- `Dionysus` owns only seed-garden staging and transport lineage

## Scope exclusions

This pack explicitly excludes:

- `abyss-stack`
- `aoa-sdk`
- `8Dionysus`
- `aoa-agents`
- `aoa-memo`
- `aoa-skills`
- `aoa-techniques`
- `Tree-of-Sophia`
- `aoa-kag`
- `ATM10-Agent`

## Suggested planting order

Keep the default order flexible but bias toward:

1. `Agents-of-Abyss`
2. `aoa-evals`
3. `aoa-playbooks`
4. `aoa-routing`
5. `Dionysus`

## Final rule

Land the bridge surfaces before any live runtime or frontend promotion.
The honest win here is that unlocks, party builds, and navigation can finally talk to each other without erasing who owns their meaning.
