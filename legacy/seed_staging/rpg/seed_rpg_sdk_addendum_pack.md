seed_id: seed.rpg.sdk-addendum.v0
title: RPG SDK Addendum Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: landed_upstream_retained_for_lineage
lifecycle_note: RPG SDK addendum surfaces are landed upstream in aoa-sdk; keep this pack as lineage and transport only.
reality_checked_at: '2026-04-04'
status: pending_archive
priority: later
parent_seed: seed.rpg.bridge-wave-pack.v0
tags:
  - rpg
  - sdk
  - typed-consumer
  - compatibility
  - surfaces

# Seed Note: RPG SDK Addendum Pack

## Purpose

Prepare the narrow RPG SDK consumer addendum as a named prep pack without opening a fresh numbered wave.

This pack stages typed readers, compatibility helpers, explicit surface paths, and fixture-staged future transport files so later agents, tooling, and UI readers can consume the RPG contour without moving meaning or runtime ownership into `aoa-sdk`.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.

This prep pack belongs here because:

- the transport bundle is narrower than a new wave but still needs durable lineage
- the rollout should stay seed-shaped until `aoa-sdk` accepts the addendum
- the addendum depends on earlier RPG law and bridge work while remaining consumer-only
- the package is better treated as staging and transport than as new doctrine authority

## Bundle contents to preserve

The source artifact is `archive/seed_pack_exports/rpg_sdk_addendum_seed.zip`.

It carries:

- `rpg_sdk_addendum_seed/README.md`
- `rpg_sdk_addendum_seed/APPLY_ORDER.md`
- `rpg_sdk_addendum_seed/CODEX_NOTES.md`
- `rpg_sdk_addendum_seed/SEED_MANIFEST.yaml`
- `rpg_sdk_addendum_seed/COVERAGE_MAP.md`
- `rpg_sdk_addendum_seed/TOUCHPOINTS_NOT_INCLUDED.md`
- repo-local typed-consumer surfaces for `aoa-sdk`
- this `Dionysus` prep-pack note, map, and quest object

The landed adaptation keeps the slice API-only and updates the staged
`abyss-stack` fixture transport root to `tests/fixtures/workspace/src/abyss-stack/`
so `aoa-sdk` exercises its real workspace-discovery posture instead of a flatter
seed-only layout.

## Ownership posture

Read the later plantings under these repo-home boundaries:

- `Agents-of-Abyss` and `abyss-stack` remain the owners of RPG meaning and runtime contracts
- `aoa-sdk` owns only the typed consumer hand, compatibility helpers, and surface-path registry
- `Dionysus` owns only seed-garden staging and transport lineage

This pack does not make `aoa-sdk` the source of RPG doctrine, runtime state, or hidden orchestration policy.

## Scope exclusions

This pack explicitly excludes:

- `Agents-of-Abyss`
- `abyss-stack`
- `aoa-agents`
- `aoa-evals`
- `aoa-playbooks`
- `aoa-memo`
- `aoa-routing`
- `aoa-skills`
- `aoa-techniques`
- `8Dionysus`
- `Tree-of-Sophia`
- `aoa-kag`
- `ATM10-Agent`

## Suggested planting order

Keep the default order flexible but bias toward:

1. `aoa-sdk`
2. `Dionysus`

## Final rule

Land the typed hand before the runtime body.
The honest win here is that future consumers can read one cited RPG surface family without turning the SDK into a hidden owner or service brain.
