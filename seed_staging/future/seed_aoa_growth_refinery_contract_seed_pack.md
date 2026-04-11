seed_id: seed.aoa.growth-refinery-contract-seed-pack.v0
title: AoA Growth Refinery Contract Companion Seed Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: The growth-refinery contract companion remains staged in Dionysus as the v1 contract substrate for the wider docket route; no owner-layer slice from this companion pack is landed yet.
reality_checked_at: '2026-04-11'
status: pending_archive
priority: high
parent_seed: seed.aoa.growth-refinery-docket-pack.v0
tags:
  - growth-refinery
  - lineage
  - contracts
  - acceptance
  - dionysus
  - agents-of-abyss
  - aoa-sdk
  - aoa-skills
  - aoa-stats
  - aoa-evals
  - aoa-playbooks
  - aoa-memo

# Seed Note: AoA Growth Refinery Contract Companion Seed Pack

## Purpose

Prepare the growth-refinery contract companion as one bounded future prep
surface inside `Dionysus`.

This pack supplies the v1 contract substrate for the already staged
growth-refinery docket:

- contract text
- examples
- acceptance gates
- one tiny structural validator

It does not replace the docket pack that already names the route order, owner
sequence, and stop-lines.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This companion pack belongs here because:

- the source artifact is a cross-repo contract seed, not one owner-repo patch
- it sharpens the staged growth-refinery docket without becoming a separate
  owner-repo queue
- it mixes doctrine notes, proposed-targets, examples, and a validator that
  should be adapted into owner repos, not copied into them unchanged
- it provides merge gates for later owner PRs while staying weaker than live
  owner-repo truth

## Companion posture

Read this pack beside
`seed_staging/future/seed_aoa_growth_refinery_docket_pack.md`.

Keep the difference explicit:

- the docket pack defines route order, owner boundaries, and stop-lines
- this contract pack defines the v1 contract substrate and acceptance gates
- neither pack is owner truth
- neither pack authorizes blind file-tree import into live repos

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-growth-refinery-contract-seed-pack-2026-04-11.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-growth-refinery-contract-seed-pack-2026-04-11-summary.md`.

The package carries:

- top-level guidance: `README.md`, `WHY_NOW.md`, `TARGET_MAP.md`,
  `ACCEPTANCE_MATRIX.md`, `CODEX_EXECUTION_PROMPT.md`,
  `CODEX_REVIEW_PROMPT.md`, `REVIEW_CHECKLIST.md`
- contract notes:
  - `contracts/candidate_lineage_contract_v1.md`
  - `contracts/growth_funnel_contract_v1.md`
  - `contracts/memory_writeback_contract_v1.md`
- a tiny structural validator:
  - `tools/validate_lineage_examples.py`
- a cross-stage example bundle:
  - `examples/lineage_bundle_v1/checkpoint_lineage_hint.json`
  - `examples/lineage_bundle_v1/harvest_packet_candidate.json`
  - `examples/lineage_bundle_v1/seed_lineage_entry.json`
  - `examples/lineage_bundle_v1/candidate_lineage_summary.json`
- proposed target files for:
  - `Agents-of-Abyss`
  - `aoa-sdk`
  - `aoa-skills`
  - `Dionysus`
  - `aoa-stats`
  - `aoa-evals`
  - `aoa-playbooks`
  - `aoa-memo`

## Boundary posture to preserve

Read this pack under these boundaries:

- keep the canonical chain explicit as
  `cluster_ref -> candidate_ref -> seed_ref -> object_ref`
- keep `aoa-sdk` on provisional carry only
- keep `aoa-skills` as the first honest home of reviewed `candidate_ref`
- keep `Dionysus` as the only home of `seed_ref`
- keep `aoa-stats` derived-only
- keep `aoa-evals` proof-only
- keep `aoa-playbooks` scenario-only
- keep `aoa-memo` memory-only
- keep `aoa-routing` and `aoa-kag` derivative

## Ownership posture

Read later landings under these owner boundaries:

- `Agents-of-Abyss` owns the doctrine anchor and crosswalk
- `aoa-sdk` owns checkpoint and closeout carry
- `aoa-skills` owns reviewed candidate identity
- `Dionysus` owns seed identity and planting trace
- `aoa-stats` owns the derived funnel summary
- `aoa-evals` owns the proof bundles
- `aoa-playbooks` owns the recurring session-growth cycle
- `aoa-memo` owns lineage-aware memory writeback

## Application posture

Treat this pack as the contract companion for the staged route.

The honest landing order stays:

1. `Agents-of-Abyss`
2. `aoa-sdk`
3. `aoa-skills`
4. `Dionysus`
5. `aoa-stats`
6. `aoa-evals`
7. `aoa-playbooks`
8. `aoa-memo`

When planted later:

- adapt contracts and examples to live repo conventions
- regenerate repo-owned generated surfaces from local builders
- use the acceptance matrix as merge gates, not as a claim of landed reality

## What this pack is not for

- no replacement of the staged docket pack
- no new numbered wave manifest
- no change to `navigation.next_live_seed`
- no direct import of `proposed-targets/` into live repos unchanged
- no new sovereign lineage layer
- no first-authoring into `aoa-routing` or `aoa-kag`

## Final rule

Keep this pack because the staged docket route now needs concrete v1 contracts,
examples, and acceptance gates.

But preserve the difference between:

- one staged docket pack that sets the route
- one staged contract companion that sharpens the route
- and later owner-repo truth that must still be landed slice by slice
