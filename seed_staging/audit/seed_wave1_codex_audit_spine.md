seed_id: seed.wave1.codex-audit-spine.v0
title: Wave 1 Codex Audit Spine Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: audit-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: Cross-repo audit spine remains staged in Dionysus; no owner-repo rollout is verified as landed.
reality_checked_at: '2026-04-04'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - audit
  - codex
  - review
  - protocol
  - validation
  - routing

# Seed Note: Wave 1 Codex Audit Spine

## Purpose

Prepare the first cross-repo audit update wave for `Agents-of-Abyss`, `ATM10-Agent`, and `abyss-stack` without landing anything there yet.

This pack is meant to install a shared audit spine before wider skill, eval, or deeper nested-instruction growth.
It keeps future Codex audits narrower, more reviewable, and less error-prone without turning `Dionysus` into the owner of downstream runtime or constitutional meaning.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the update spans multiple owning repositories
- the first coherent slice is cross-repo staging, not a single-repo landing
- the target repos should receive bounded plantings later, not speculative partial edits now
- the current wave and `navigation.next_live_seed` should remain untouched

## Bundle contents to preserve

The source artifact is `wave1_codex_audit_update_pack.zip`.

It carries:

- `Agents-of-Abyss/ECOSYSTEM_AUDIT_INDEX.md`
- `Agents-of-Abyss/docs/CODEX_AUDIT_PROTOCOL.md`
- `ATM10-Agent/AUDIT.md`
- `abyss-stack/AUDIT.md`
- `PATCH_SNIPPETS.md` with bounded `AGENTS.md` insertion text

## Ownership posture

Read the later landings under these repo-home boundaries:

- `Agents-of-Abyss` owns the ecosystem center, routing clarity, layer map, and federation rules
- `ATM10-Agent` owns local-first workflow posture, runnable entrypoints, dry-run safety, and operator-facing execution flows
- `abyss-stack` owns runtime substrate, deployment, secrets bootstrap, exposure posture, and infrastructure validation

This pack prepares audit surfaces for those owners.
It does not transfer their meaning into `Dionysus`.

## What this wave is for

Install shared audit contracts before deeper repo-local changes:

- compact audit routing for the ecosystem center
- explicit Codex audit protocol for the center repo
- repo-local `AUDIT.md` surfaces for workflow and runtime repos
- explicit GitHub review severity guidance through small `AGENTS.md` additions

## What this wave is not for

- no direct downstream planting yet
- no repo refactor pass
- no wave 2 work for `aoa-skills` or `aoa-evals`
- no `.codex/config.toml` tightening in this slice
- no change to `navigation.next_live_seed`
- no new `seed_index` entry yet

## Later application order

When the future planting starts, keep the order bounded:

1. add the new files exactly as written in the bundle
2. insert the `AGENTS.md` snippets from `PATCH_SNIPPETS.md`
3. run each target repo's existing validation
4. only then open the next audit-update wave

## Target repo landing intent

### `Agents-of-Abyss`

Primary future surfaces:

- `ECOSYSTEM_AUDIT_INDEX.md`
- `docs/CODEX_AUDIT_PROTOCOL.md`
- small `AGENTS.md` additions for audit routing and review guidelines

Main function:

- keep constitutional and routing audits fast
- make source-of-truth drift and wrong-owner routing review-critical
- keep the center from absorbing layer-owned meaning

### `ATM10-Agent`

Primary future surfaces:

- `AUDIT.md`
- small `AGENTS.md` additions for audit contract and review guidelines

Main function:

- keep dry-run posture review-critical
- make secrets, destructive input paths, service drift, and false verification claims explicit review blockers

### `abyss-stack`

Primary future surfaces:

- `AUDIT.md`
- small `AGENTS.md` additions for audit contract and review guidelines

Main function:

- keep runtime exposure, secrets, bootstrap, render, and substrate-boundary drift explicitly review-critical

## Validation reminders for later planting

### `Agents-of-Abyss`

- `python scripts/validate_ecosystem.py`

### `ATM10-Agent`

- `python -m pytest`
- nearest smoke path for any touched runnable entrypoint

### `abyss-stack`

- `python scripts/validate_stack.py`
- smallest relevant bootstrap / render / profile checks for touched surfaces

## Preserved vocabulary

- audit spine
- constitutional
- runtime
- workflow
- meaning
- proof
- PLAN
- DIFF
- VERIFY
- REPORT
- RESIDUAL RISK

## Final rule

Use this prep pack to stage later bounded audit plantings.
Do not let a cross-repo audit wave become a justification for cross-repo authorship drift.
