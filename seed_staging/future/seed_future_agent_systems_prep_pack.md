seed_id: seed.future.agent-systems-prep-pack.v0
title: Future Agent Systems Seed Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: Future agent systems seeds remain parked as staging soil; no owner-repo rollout is verified yet.
reality_checked_at: '2026-04-04'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - memory
  - evals
  - skills
  - documentation
  - mcp
  - a2a
  - governance

# Seed Note: Future Agent Systems Seed Prep Pack

## Purpose

Prepare a non-queued future seed pack from
`dionysus_future_agent_systems_dropin.zip` so strong later seeds can live in
`Dionysus` without pretending to be the next wave, the next live seed, or an
already registered `seed_index` family.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the candidate seeds span multiple owning repositories
- the current posture is staging, not immediate planting
- the current `navigation.next_live_seed` should stay untouched
- the current registry contract does not have a neutral parked state for many `wave: null` candidates

## Bundle contents to preserve

The source artifact is `dionysus_future_agent_systems_dropin.zip`.

It carries:

- `README_DROPIN.md`
- `seed_future_agent_systems_prep_pack.md`
- `seed_future_agent_systems_prep_pack.map.yaml`
- nested `future_agent_systems_seed_pack.zip`
- nested `future_agent_systems_seed_pack/README.md`
- nested applicability, rationale, and origin-notes snippets
- ten seed cards `AOA-SEED-R6` through `AOA-SEED-R15`

## Why these are packed instead of registered now

The current `seed_index` contract is too narrow for a waiting garden:

- if `wave` is `null`, an entry must be `gated_next` or `landed_post_wave`
- these seeds are neither the single live next seed nor already planted post-wave material

So the clean form is:

1. keep them in a prep pack
2. keep the current `next_live_seed` intact
3. append only the prep note to `origin_notes`
4. delay `seed_index` promotion until a later bounded manifest or explicit planting decision

## Readiness buckets

### Direct fit now

- `AOA-SEED-R6` Memory Namespace and Compression Discipline
- `AOA-SEED-R7` Eval Ladder and Judge Discipline
- `AOA-SEED-R8` Skills as Contracted Execution Capsules
- `AOA-SEED-R9` AI-Native Documentation Surface
- `AOA-SEED-R10` Tool Approval and Remote Boundary Policy

### Strong fit after one adjacent bounded planting or baseline

- `AOA-SEED-R11` Online Trace Sentinel
- `AOA-SEED-R12` Skill/Proof Regression Dataset Spine
- `AOA-SEED-R13` MCP Resource and Prompt Surface
- `AOA-SEED-R14` Outward A2A Boundary and Agent Card

### Reserve

- `AOA-SEED-R15` Prompt/Profile Version Spine

## What this pack is not for

- no new wave manifest
- no change to `navigation.next_live_seed`
- no direct downstream planting yet
- no second registry hidden inside a note
- no claim that every seed should be planted

## Final rule

Let this pack wait without pretending to be ordered.
When a later planting begins, choose the smallest bounded seed that strengthens a real owner boundary without forcing three other boundaries to move with it.
