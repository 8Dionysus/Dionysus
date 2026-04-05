seed_id: seed.questbook.source-proof-pack.v0
title: Questbook Source-Proof Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: landed_upstream_retained_for_lineage
lifecycle_note: Questbook source-proof surfaces are landed upstream across owner repos; keep this pack as lineage and transport only.
reality_checked_at: '2026-04-04'
status: pending_archive
priority: next
parent_seed: null
tags:
  - questbook
  - techniques
  - skills
  - evals
  - proof
  - source-owned

# Seed Note: Questbook Source-Proof Pack

## Purpose

Prepare the source/proof questbook rollout from
`archive/seed_pack_exports/questbook_second_wave_seed.zip` as a named prep pack
for the three source-owned AoA layers that should follow the shared foundation.

This pack stages repo-local questbooks for `aoa-techniques`, `aoa-skills`, and
`aoa-evals` after the shared model, delegation, routing, playbook, and memo
seams are already legible.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the rollout spans multiple owning repositories but is not the next live seed
- the source/proof contour should wait for the foundation pack rather than open a fresh numbered wave
- the work is stronger as a named dependency-bound prep pack than as a queue-like wave alias

## Bundle contents to preserve

The source artifact is `archive/seed_pack_exports/questbook_second_wave_seed.zip`.

It carries:

- `questbook_second_wave_seed/README.md`
- `questbook_second_wave_seed/APPLY_ORDER.md`
- `questbook_second_wave_seed/SEED_MANIFEST.yaml`
- `questbook_second_wave_seed/TOUCHPOINTS_NOT_INCLUDED.md`
- `questbook_second_wave_seed/COVERAGE_MAP.md`
- repo-local questbook starter surfaces for `aoa-techniques`, `aoa-skills`, and
  `aoa-evals`

## Ownership posture

Read the later plantings under these repo-home boundaries:

- `aoa-techniques` owns canon hardening, donor refinery, and generated/source alignment
- `aoa-skills` owns bounded workflow and runtime-seam obligations
- `aoa-evals` owns proof, regression, and verdict-bridge obligations

This pack stages repo-local questbook adoption for those owners.
It does not make `Dionysus` or `aoa-routing` the owner of quest meaning there.

## Scope exclusions

This pack explicitly excludes:

- `ATM10-Agent`, which is outside this rollout line
- `aoa-sdk`, which should wait for a later dedicated named seed
- `aoa-kag`, `Tree-of-Sophia`, and `abyss-stack`, which belong in the later boundary/runtime contour
- `Dionysus` and `8Dionysus`, which should reflect planted reality after upstream packs land

## Suggested planting order

Keep the default order flexible but bias toward:

1. `aoa-techniques`
2. `aoa-skills`
3. `aoa-evals`

## Final rule

Do not spread questbook into source/proof repos before the shared foundation is
in place. Source-owned questbooks should harden existing repo boundaries, not
compensate for missing center-level seams.
