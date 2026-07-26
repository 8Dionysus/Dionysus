seed_id: seed.aoa.surface-detection-first-wave-pack.v0
title: AoA Surface Detection First-Wave Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: Surface-detection first-wave seed remains staged in Dionysus; no additive aoa-sdk multi-surface detection seam or surface-detection CLI/report path is verified upstream yet.
reality_checked_at: '2026-04-07'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - surface-detection
  - aoa-sdk
  - control-plane
  - closeout
  - heuristics
  - schemas
  - cli

# Seed Note: AoA Surface Detection First-Wave Prep Pack

## Purpose

Prepare the `aoa-surface-detection-first-wave-seed` bundle as one bounded prep
pack inside `Dionysus`.

This pack preserves an additive first-wave seam for noticing AoA surfaces in
live work without pretending that `Dionysus` or `aoa-sdk` should become the
semantic owner of sibling repositories.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source artifact is a seed package, not a repo-ready patch
- the package centers on `aoa-sdk`, but it proposes behavior that touches
  several AoA owner layers at once
- the bundle carries docs, schemas, examples, and snippets that should be
  adapted to live repo structure rather than copied unchanged
- the owner-repo reality check shows that the named first-wave seam is not yet
  verified upstream
- the package includes a second-wave follow-on note that should stay lineage
  only until the first-wave owner seam is real

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-surface-detection-first-wave-seed.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-surface-detection-first-wave-seed-summary.md`.

The package carries:

- `README.md`
- `TO_CODEX.md`
- `seed_manifest.json`
- `aoa-sdk/patch_map.yaml`
- `aoa-sdk/AGENTS.insert.md`
- docs for first-wave architecture, heuristics, and closeout handoff
- typed schemas and examples for the surface-detection report and closeout
  handoff
- additive snippets for models, detector flow, CLI shape, and acceptance tests
- one deferred follow-on note for a later cross-repo second wave

## Boundary posture to preserve

Read this pack under these boundaries:

- keep `aoa-sdk` on the control plane
- keep canonical meaning in sibling owner repositories
- preserve `activated`, `manual-equivalent`, `candidate-now`, and
  `candidate-later` as honest labels
- keep only executable, host-visible skills in immediate activation lanes
- keep playbook, eval, memo, technique, and agent signals as inspect, hint, or
  closeout objects rather than hidden runtime authority
- keep promotion-shaped notes in reviewed closeout rather than in active-route
  mutation

## Ownership posture

Read later landings under these owner boundaries:

- `aoa-sdk` is the first honest owner for the additive detection seam
- `aoa-skills` remains the executable runtime truth that first-wave detection
  may reference but must not widen
- `aoa-playbooks`, `aoa-evals`, `aoa-memo`, `aoa-agents`, and
  `aoa-techniques` keep their own canonical meaning and should only appear as
  explicit surface candidates or closeout handoffs
- `Dionysus` only preserves the pack and its planting posture; it does not
  turn surface detection into a seed-garden doctrine

## Application posture

Treat this pack as a bounded first-wave prep source.

The honest first landing, if chosen later, is:

1. add a standing surface-detection reflex to `aoa-sdk/AGENTS.md`
2. add one additive detection report and CLI path in `aoa-sdk`
3. preserve the existing `aoa skills ...` contract instead of widening it into
   hidden non-skill activation
4. hand surviving non-skill notes to the reviewed closeout path

The follow-on second-wave sketch should stay deferred until recurring real
first-wave reports justify tighter cross-repo support.

When planted later, regenerate docs, schemas, examples, and tests from
repo-native surfaces rather than copying seed snippets verbatim into the live
repo.

## What this pack is not for

- no immediate owner-repo rollout from `Dionysus`
- no move of canonical meaning out of sibling repositories
- no auto-activation of playbooks, evals, memo, techniques, or agents
- no renaming or breaking of existing `aoa skills ...` commands
- no treatment of `manual-equivalent` as `activated`
- no use of the session-growth closeout kernel inside an active route

## Final rule

Keep this pack because it names one useful additive control-plane seam around
AoA surface detection.

But preserve the difference between:

- executable skills and non-skill surfaces
- immediate activation and reviewed closeout
- one staged pack in `Dionysus` and the later owner-repo landing in `aoa-sdk`
