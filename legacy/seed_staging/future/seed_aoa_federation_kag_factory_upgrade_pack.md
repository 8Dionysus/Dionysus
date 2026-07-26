seed_id: seed.aoa.federation-kag-factory-upgrade-pack.v0
title: AoA Federation KAG Factory Upgrade Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: Federation KAG factory upgrade seed is staged in Dionysus; no owner-repo landing is verified yet, and the donor-registry plus live-spine split still needs repo-native adaptation in aoa-kag before any routing or SDK follow-through should move.
reality_checked_at: '2026-04-09'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - kag
  - federation
  - donor-registry
  - activation-gates
  - routing
  - sdk
  - memo
  - source-first

# Seed Note: AoA Federation KAG Factory Upgrade Prep Pack

## Purpose

Prepare the `aoa-federation-kag-factory-upgrade-seed-2026-04-06` bundle as
one bounded future prep surface inside `Dionysus`.

This pack preserves the next manifest-driven federation-KAG upgrade without
pretending the bundle is already an owner-repo patch or a live widening of the
current public spine.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source artifact is a seed package, not an owner-repo patch
- the bundle is precise enough to guide landing, but it still spans multiple
  owner layers and must be adapted to repo-native builders, validators, and
  docs
- the package separates mandatory `aoa-kag` work from optional
  `aoa-routing`, `aoa-sdk`, and `aoa-evals` follow-through, so staging should
  preserve that order explicitly
- the donor boundary matters as much as the code delta: `aoa-techniques`,
  `Tree-of-Sophia`, and `aoa-memo` must stay stronger than the bundle's own
  transport surfaces
- the package explicitly tries to widen generic ingress without widening live
  exposure by accident, so owner-repo reality must stay stronger than the zip

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-federation-kag-factory-upgrade-seed-2026-04-06.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-federation-kag-factory-upgrade-seed-2026-04-06-summary.md`.

The package carries:

- `README.md`
- `codex/REPO_GROUNDING.md`
- `codex/CODEX_BRIEF.md`
- `codex/WORK_ITEMS.yaml`
- `codex/ACCEPTANCE.md`
- `codex/FILE_TOUCHPOINTS.json`
- `codex/RISK_NOTES.md`
- `machine/upgrade_manifest.json`
- `machine/test_matrix.yaml`
- one proposed donor-registry manifest and example for `aoa-kag`
- one optional routing ABI delta for `aoa-routing`
- one optional control-plane delta for `aoa-sdk`

## Boundary posture to preserve

Read this pack under these boundaries:

- keep source repos authoritative for authored meaning
- keep `aoa-kag` as derived substrate, not federation sovereignty
- keep donor publication, registry visibility, spine visibility, and routing
  visibility as separate gates
- keep `aoa-routing` navigation-only, not donor authority
- keep `aoa-sdk` on the control plane, not as a semantic duplicate of KAG or
  routing
- keep `aoa-memo` registry-visible by default without inflating memory into
  proof or graph truth
- keep the live spine and routing contour two-donor by default until explicit
  activation says otherwise
- keep `AOA-K-0008` unactivated in this tranche

## Ownership posture

Read later landings under these owner boundaries:

- `aoa-kag` is the first honest owner for generic federation ingress, donor
  activation metadata, live spine regeneration, and the derived registry output
- `aoa-routing` is only the later home for additive routing compatibility if
  the new KAG registry needs bounded consumption there
- `aoa-sdk` is only the later home for a small typed read helper after the KAG
  owner seam is stable
- `aoa-evals` is optional and should receive proof only if one durable
  portable contract is genuinely needed
- `aoa-techniques`, `Tree-of-Sophia`, and `aoa-memo` stay donor and validation
  context for this bundle, not first-authoring homes
- `Dionysus` only preserves the pack, order, and lineage; it does not move
  owner truth here

## Application posture

Treat this pack as a bounded future prep source.

The honest first landing, if chosen later, is:

1. land generic federation export validation, donor activation registry, live
   spine iteration, and regression tests in `aoa-kag`
2. only after that, decide whether `aoa-routing` needs one small compatibility
   update to consume donor visibility additively
3. only after the KAG registry is stable, decide whether `aoa-sdk` deserves
   one typed helper for donor enumeration
4. keep `aoa-evals` optional unless a portable proof gap remains after
   repo-local tests are real

When planted later, regenerate repo-native manifests, generated outputs, and
tests from live owner surfaces instead of copying the package outputs
unchanged.

## What this pack is not for

- no new wave manifest
- no change to `navigation.next_live_seed`
- no `seed_index` promotion yet
- no direct owner-repo writeback from `Dionysus`
- no silent widening of live routing from a staging pack
- no turning `aoa-kag` into authority for source meaning
- no turning `aoa-sdk` into routing or donor-sovereignty logic
- no memo truth inflation
- no `AOA-K-0008` activation

## Final rule

Keep this pack because it names the next bounded step out of the current
two-donor federation bottleneck.

But preserve the difference between:

- one staged bundle in `Dionysus`
- one repo-native owner landing in `aoa-kag`
- one optional routing follow-through in `aoa-routing`
- one optional control-plane helper in `aoa-sdk`
- donor context that remains stronger in `aoa-techniques`,
  `Tree-of-Sophia`, and `aoa-memo`
