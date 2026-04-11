seed_id: seed.aoa.first-wave-candidate-lineage-pack.v0
title: AoA First Wave Candidate Lineage Hardening Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: partially_landed_retained_for_lineage
lifecycle_note: The Growth Refinery first-wave lineage surfaces are already partly landed across Agents-of-Abyss, aoa-sdk, aoa-skills, and Dionysus; keep this pack as the hardening guide for one aligned live example chain, one cross-repo validator, and the remaining schema/example/doc seams.
reality_checked_at: '2026-04-11'
status: pending_archive
priority: high
parent_seed: seed.aoa.growth-refinery-contract-seed-pack.v0
tags:
  - growth-refinery
  - candidate-lineage
  - hardening
  - cluster-ref
  - candidate-ref
  - seed-ref
  - agents-of-abyss
  - aoa-sdk
  - aoa-skills
  - dionysus

# Seed Note: AoA First Wave Candidate Lineage Hardening Pack

## Purpose

Preserve the first-wave candidate-lineage hardening packet inside `Dionysus`.

This pack is not a new Growth Refinery route. It tightens the already-landed
first-wave lineage surfaces so one live example chain stays coherent from
`cluster_ref` through `candidate_ref` to `seed_ref`.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This hardening pack belongs here because:

- it spans the center, control plane, skill harvest layer, and seed garden
- it is a cross-repo adaptation guide, not one owner-repo patch
- it preserves a proposed validator and example chain that must be fitted to
  live repo conventions
- it explicitly warns against duplicating doctrine and contract surfaces that
  already landed

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-first-wave-candidate-lineage-pack-2026-04-11.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-first-wave-candidate-lineage-pack-2026-04-11-summary.md`.

The package carries:

- `aoa_first_wave_candidate_lineage_pack/README.md`
- `aoa_first_wave_candidate_lineage_pack/LIVE_STATE_ALIGNMENT.md`
- `aoa_first_wave_candidate_lineage_pack/contracts/candidate_lineage_contract_v1.md`
- `aoa_first_wave_candidate_lineage_pack/CODEX_EXECUTION_PROMPT.md`
- `aoa_first_wave_candidate_lineage_pack/PR_SLICES.md`
- `aoa_first_wave_candidate_lineage_pack/ACCEPTANCE_MATRIX.md`
- `aoa_first_wave_candidate_lineage_pack/proposed-targets/*`

## Boundary posture to preserve

Read this pack under these boundaries:

- `Agents-of-Abyss` owns the cross-repo validator and center pointer, not a
  repo-local candidate ledger
- `aoa-sdk` owns provisional lineage carry and may mint only `cluster_ref`
- `aoa-skills` owns reviewed `candidate_ref` minting after donor harvest
- `Dionysus` owns `seed_ref` minting and seed-lineage examples
- no owner outside `Dionysus` may mint `seed_ref`
- no first-wave hardening patch may introduce a new sovereign lineage repo

## Application posture

Treat this pack as partially landed lineage hardening.

The current owner-repo slices already exist, so later planting must be minimal:

1. add the missing `Agents-of-Abyss` validator
2. add the `aoa-sdk` closeout candidate-lineage map schema and example
3. align the `aoa-sdk` checkpoint hint example with the live chain
4. add an `aoa-skills` candidate-ref bridge note
5. harden the existing harvest-packet receipt schema for lineage entries
6. align the `Dionysus` seed lineage example with the same chain
7. run the cross-repo validator

## What this pack is not for

- no duplicate `REVIEWABLE_GROWTH_REFINERY.md`
- no duplicate `CANDIDATE_LINEAGE_CROSSWALK.md`
- no direct import of `proposed-targets/`
- no `candidate_ref` minting in `aoa-sdk`
- no `seed_ref` minting in `aoa-skills`
- no Wave D automation

## Final rule

Use this pack to close the first-wave seams that make the Growth Refinery
chain reviewable.

Keep the owner split strict:

- `aoa-sdk`: `cluster_ref`
- `aoa-skills`: `candidate_ref`
- `Dionysus`: `seed_ref`
