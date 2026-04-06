seed_id: seed.aoa.stats-telemetry-pack.v0
title: AoA Stats Telemetry Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: partially_landed_retained_for_lineage
lifecycle_note: The first owner-local receipt wave is now landed in aoa-skills and aoa-evals, while the derived stats layer remains intentionally deferred; Dionysus keeps the seed for lineage and later adjunct planning.
reality_checked_at: '2026-04-05'
status: pending_archive
priority: medium
parent_seed: seed.aoa.automation-opportunity-scan-pack.v0
tags:
  - stats
  - telemetry
  - observability
  - session-harvest
  - automation
  - aoa-skills
  - aoa-evals
  - schemas

# Seed Note: AoA Stats Telemetry Prep Pack

## Purpose

Prepare the `aoa-stats-telemetry` seed as a bounded future prep surface inside
`Dionysus`.

This pack preserves one shared receipt and derived-summary posture around the
now-live session-harvest and automation family without pretending that
federated statistics is already an owner-repo truth surface.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source artifact is a seed package, not a repo-ready patch
- the pack spans several owner layers at once rather than one honest source
  owner
- the package proposes shared schemas and derived views, but no live
  observatory-style repo exists yet
- the first useful landing is split across owner-local receipt surfaces, not
  one monolithic repo
- the bundle includes `.seed` schemas and examples that should be adapted from
  live repo truth, not copied into owner repos unchanged

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-stats-telemetry-seed.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-stats-telemetry-seed-summary.md`.

The package carries:

- `README.md`
- `CODEX_HANDOFF.md`
- `seed/family_manifest.yaml`
- docs for architecture, layer boundaries, metric families, and agent
  writeback rules
- shared schemas for:
  - `stats-event-envelope`
  - `skill-run-receipt`
  - `eval-result`
  - `progression-delta`
  - `decision-fork`
  - `automation-candidate`
  - `object-window-summary`
- receipt examples for the first-wave event kinds
- one integration note for session-harvest and automation bridging

## Boundary posture to preserve

Read this pack under these boundaries:

- keep source-owned meaning in current owner repos
- keep counts separate from verdicts, progression, and raw evidence
- keep every aggregate linked back to inspectable evidence refs
- keep progression multi-axis and route-scoped rather than collapsing into one
  total score
- keep receipts append-only and correction-friendly with `supersedes`
- keep cross-repo summaries derived rather than sovereign
- keep UI and dashboard ambition out of the first planting wave

## Ownership posture

Read later landings under these owner boundaries:

- `aoa-skills` owns bounded workflow meaning and the first instrumented family
- `aoa-evals` owns bounded proof meaning and any honest eval-result receipt
  surface
- `aoa-playbooks` may later consume automation or repeated-window summaries,
  but not as the first source of meaning
- `aoa-agents` may later harden actor or checkpoint refs, but not as a
  shortcut around workflow or proof ownership
- `aoa-memo` may later mirror provenance-thread or correction posture, but not
  as the truth source for receipts
- `aoa-techniques` may later extract reusable telemetry practices only after
  live instrumentation stabilizes
- a later derived stats or observatory-style adjunct may own cross-repo read
  models, but it must stay downstream from owner receipts and verdicts
- `Dionysus` only preserves the pack and its planting posture; it does not
  become the federated stats owner

## Application posture

Treat this pack as a partially landed lineage pack.

The honest first planting is now live as:

1. bounded finish receipts across the live session-harvest and automation
   family in `aoa-skills`
2. one bounded `eval_result_receipt` seam in `aoa-evals`
3. a shared receipt-envelope contract that stays weaker than owner-local
   workflow or proof meaning

The wider downstream path remains deferred on purpose:

1. add derived read models in a dedicated stats or observatory-style adjunct
2. let `aoa-playbooks` consume automation-pipeline or repeated-window signals
   only as downstream hints
3. extract reusable telemetry practice into `aoa-techniques`

When planted later, regenerate schemas, validators, and builders from
repo-native surfaces rather than copying seed files directly into live repos.

## What this pack is not for

- no new sovereign stats repo implied by this note alone
- no one-number score for quality or progression
- no replacement of eval verdicts with counters
- no duplication of raw logs when evidence refs are enough
- no silent multi-repo writeback from a central telemetry layer
- no immediate federation-wide rollout directly from `Dionysus`
- no first-authoring into `aoa-routing` or `aoa-kag`

## Final rule

Keep this pack because it names a useful machine-first receipt spine around the
live session-harvest and automation family.

But preserve the difference between:

- source-owned receipts in owner repos
- bounded proof verdicts in `aoa-evals`
- derived summaries in a later downstream stats layer
- one staged transport pack in `Dionysus`
