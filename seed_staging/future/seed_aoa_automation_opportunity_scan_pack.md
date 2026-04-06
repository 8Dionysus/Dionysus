seed_id: seed.aoa.automation-opportunity-scan-pack.v0
title: AoA Automation Opportunity Scan Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: Automation-opportunity scan seed remains staged in Dionysus; the add-on skill is not yet landed in aoa-skills, and no owner-repo rollout is verified yet.
reality_checked_at: '2026-04-05'
status: pending_archive
priority: medium
parent_seed: seed.aoa.session-harvest-family-pack.v0
tags:
  - automation
  - session-harvest
  - aoa-skills
  - aoa-playbooks
  - checkpoint
  - playbook-seeds
  - donor-harvest

# Seed Note: AoA Automation Opportunity Scan Prep Pack

## Purpose

Prepare the `aoa-automation-opportunity-scan` seed as a bounded future prep
surface inside `Dionysus`.

This pack preserves one separate automation-readiness detector around the now
live session-harvest family without pretending the detector is already
canonical `aoa-skills` truth.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source artifact is a seed package, not an owner-repo patch
- the add-on plugs into live session-harvest skills but is not itself landed
- the pack spans several owner layers even though `aoa-skills` is the first
  honest landing surface
- the bundle includes `.seed` files that should be inspected and adapted, not
  copied into live repos unchanged
- the package forecasts later `aoa-playbooks`, `aoa-techniques`,
  `aoa-agents`, and `aoa-evals` consequences that should stay explicit before
  any planting starts

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-automation-opportunity-scan-seed.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-automation-opportunity-scan-seed-summary.md`.

The package carries:

- `README.md`
- `CODEX_HANDOFF.md`
- `PACKAGE_MANIFEST.json`
- `seed/addon_manifest.yaml`
- `seed/SKILL_INDEX.additions.md`
- `seed/PORTABLE_AND_GENERATED_HINTS.md`
- reference notes for automation fit, session-harvest integration,
  playbook-seed bridging, and checkpoint posture
- fixture ideas for `seed_ready`, `not_now`, and `checkpoint_required`
- one seed bundle for:
  - `aoa-automation-opportunity-scan`

## Family posture to preserve

Read this pack under these family boundaries:

- keep `aoa-session-donor-harvest` as the broad post-session refinery nucleus
- keep `aoa-quest-harvest` narrow as the leaf promotion-triage skill
- keep `aoa-automation-opportunity-scan` separate as the detector and
  packager for automation readiness
- allow donor-harvest to emit `automation_candidate` only as an extract kind,
  not as hidden automation authority
- keep route-forks, self-diagnose, self-repair, and progression-lift as
  explicit adjacent family seams rather than silently collapsing them into one
  automation detector
- keep scheduling, self-change, and hidden runtime orchestration out of scope

## Ownership posture

Read later landings under these owner boundaries:

- `aoa-skills` is the first honest owner for the detector skill
- `aoa-playbooks` is the later home for recurring multi-skill or
  schedule-shaped automation seed candidates
- `aoa-techniques` is the later home for extracted automation-fit practice once
  the live skill seam stabilizes
- `aoa-agents` may receive later checkpoint-law or authority-boundary posture,
  but not as a shortcut around `aoa-skills`
- `aoa-evals` may receive later proof hooks or approval-sensitivity evidence,
  but not before skill-level meaning is real
- `aoa-memo` may later mirror readiness or recurrence writeback, but not as a
  substitute for reviewed evidence
- `aoa-routing` and `aoa-kag` remain derivative consumers, not first-authoring
  homes
- `Dionysus` only preserves the pack and its planting posture; it does not move
  owner truth here

## Application posture

Treat this pack as a bounded future prep source.

The honest first landing, if chosen later, is:

1. add `aoa-automation-opportunity-scan` as a separate scaffold core skill in
   `aoa-skills`
2. let `aoa-session-donor-harvest` recognize `automation_candidate` as one
   extract kind
3. add fixture coverage for `seed_ready`, `not_now`, and
   `checkpoint_required`

Only after that first live shape proves stable should the wider downstream path
be considered:

1. route recurring automation-seed candidates toward `aoa-playbooks`
2. extract automation-fit practice into `aoa-techniques`
3. harden checkpoint and proof posture in `aoa-agents` and `aoa-evals`

When planted later, regenerate owner-repo builders, catalogs, portable
exports, policy matrices, and fixtures from live repo surfaces rather than
copying generated files from the seed package.

## What this pack is not for

- no new `seed_expansion` entry
- no change to `navigation.next_live_seed`
- no immediate multi-repo rollout from `Dionysus`
- no live scheduler or background execution authority
- no direct import of `.seed` files as canonical source
- no hidden widening of `aoa-session-donor-harvest` into an automation engine
- no silent self-repair or self-upgrade routes without checkpoint posture
- no first-authoring into `aoa-routing` or `aoa-kag`

## Final rule

Keep this pack because it names a plausible next detector around the live
session-harvest family and the already-existing automation-seed posture in
`aoa-playbooks`.

But preserve the difference between:

- a staged add-on seed in `Dionysus`
- a bounded detector landing in `aoa-skills`
- later automation-seed routing in `aoa-playbooks`
- later canonical extraction into `aoa-techniques` and adjacent owner layers
