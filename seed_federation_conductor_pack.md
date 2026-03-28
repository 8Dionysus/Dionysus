seed_id: seed.aoa.federation-conductor-pack.v0
title: AoA Federation Conductor Pack Prep Note
profile_anchor: 8Dionysus
projects:
  - AoA
kind: prep-pack-note
status: pending_archive
priority: high
parent_seed: null
tags:
  - conductor
  - orchestration
  - runtime
  - run-activation
  - worker-leases
  - capability-capsules

# Seed Note: AoA Federation Conductor Pack

## Purpose

Prepare the federation conductor import pack from
`dionysus_federation_conductor_seed_pack_2026-03-24.zip` as a bounded future
prep surface inside `Dionysus`.

This pack preserves the runtime-body follow-on seeds from the Symphony dialogue
without turning `Dionysus` into a shadow runtime repo and without changing the
current live ToS gate.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the pack spans several AoA owning repositories
- the current registry already has a different live next seed
- the included `seed_expansion/` recommendation is too strong for the present local contract
- the right current posture is staging cross-repo runtime invariants before any outward planting

## Bundle contents to preserve

The source artifact is `dionysus_federation_conductor_seed_pack_2026-03-24.zip`.

It carries:

- `dionysus_federation_conductor_seed_pack_2026-03-24/README.md`
- `dionysus_federation_conductor_seed_pack_2026-03-24/seed_expansion/seed.aoa.federation-conductor-pack.v0.md`
- `dionysus_federation_conductor_seed_pack_2026-03-24/seed_expansion/notes/symphony-import-boundaries.md`
- `dionysus_federation_conductor_seed_pack_2026-03-24/seed_expansion/notes/suggested-seed-registry-append.yaml`

## Ownership posture

Read later plantings under these repo-home boundaries:

- `abyss-stack` owns conductor runtime state, work units, leases, and operator surfaces
- `aoa-routing` owns route hints and entrypoints
- `aoa-playbooks` owns activation meaning and scenario law
- `aoa-agents` owns role, tier, and tool-family posture
- `aoa-memo` owns writeback and recall boundaries
- `aoa-evals` owns trace-to-verdict and proof posture
- `Tree-of-Sophia` remains outside runtime authorship

This pack stages later runtime-body plantings for those owners.
It does not transfer their meaning into `Dionysus`.

## Pack contents to preserve

The bounded seed set is:

- `AOA-SEED-C1` Federation Conductor
- `AOA-SEED-C2` Derived Run Activation Pack
- `AOA-SEED-C3` Deterministic Work Units and Worker Leases
- `AOA-SEED-C4` Capability Capsules and Session-Scoped Grants

## Suggested planting order

Keep the order from the source pack:

1. `AOA-SEED-C1`
2. `AOA-SEED-C3`
3. `AOA-SEED-C2`
4. `AOA-SEED-C4`

## What this pack is not for

- no replacement of `navigation.next_live_seed`
- no direct insertion into `seed_expansion/`
- no new wave manifest
- no monolithic `WORKFLOW.md` sovereign prompt law
- no runtime dashboards as source of truth
- no direct ToS authorship from runtime convenience

## Final guardrail

Import the discipline of the orchestrator, not the orchestrator as a new religion.
Use this prep pack to preserve bounded runtime-body follow-on seeds until one later planting intentionally chooses them.
