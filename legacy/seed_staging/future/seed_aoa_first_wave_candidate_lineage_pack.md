seed_id: seed.aoa.first-wave-candidate-lineage-pack.v0
title: AoA First Wave Candidate Lineage Hardening Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: landed_upstream_retained_for_lineage
lifecycle_note: 'The Growth Refinery first-wave lineage hardening is now landed upstream across Agents-of-Abyss, aoa-sdk, aoa-skills, and Dionysus; keep this pack as lineage evidence for the aligned cluster_ref -> candidate_ref -> seed_ref chain, the center validator, and the closed schema/example/doc seams.'
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

Treat this pack as landed upstream and retained for lineage.

The current owner-repo slices now exist:

1. `Agents-of-Abyss` owns the center cross-repo validator
2. `aoa-sdk` owns the closeout candidate-lineage map and provisional
   checkpoint example alignment
3. `aoa-skills` owns the candidate-ref bridge note and reviewed receipt
   schema hardening
4. `Dionysus` owns the seed lineage example alignment
5. the cross-repo validator passes for the live example chain

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
