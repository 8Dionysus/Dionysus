seed_id: seed.wave2.codex-skill-proof-audit-bridge.v0
title: Wave 2 Codex Skill and Proof Audit Bridge Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: audit-pack-note
status: pending_archive
priority: medium
parent_seed: null
tags:
  - audit
  - codex
  - skills
  - evals
  - bridge
  - workflow
  - proof

# Seed Note: Wave 2 Codex Skill / Proof Audit Bridge

## Purpose

Prepare the second cross-repo audit update wave for `Agents-of-Abyss`, `aoa-skills`, and `aoa-evals` without planting into those repositories yet.

This pack exists to make the seam between workflow meaning and proof meaning explicit after the constitutional audit spine is in place.
It prepares a bounded later wave so Codex can audit execution and proof surfaces without silently blending them together.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the wave spans three owning repositories
- the first coherent slice is cross-repo staging, not immediate downstream edits
- the seam needs to be source-linked before any repo-local patch wave begins
- the current wave state and `navigation.next_live_seed` should remain untouched

## Bundle contents to preserve

The source artifact is `wave2_codex_audit_update_pack.zip`.

It carries:

- `Agents-of-Abyss/docs/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md`
- `aoa-skills/AUDIT.md`
- `aoa-evals/AUDIT.md`
- `PATCH_SNIPPETS.md` for bounded updates to `AGENTS.md` and `Agents-of-Abyss/ECOSYSTEM_AUDIT_INDEX.md`

## Ownership posture

Read the future landings under these repo-home boundaries:

- `Agents-of-Abyss` owns the ecosystem-level seam description and routing discipline between workflow and proof layers
- `aoa-skills` owns bounded execution canon, trigger boundaries, invocation posture, technique traceability, overlays, and skill-derived surfaces
- `aoa-evals` owns bounded proof canon, verdict logic, claim framing, comparison posture, chooser wording, and eval-derived surfaces

This prep pack stages the seam.
It does not transfer any of those owned meanings into `Dionysus`.

## What this wave is for

Install the next audit layer after wave 1:

- an explicit bridge doc for the skill/proof seam in `Agents-of-Abyss`
- repo-local `AUDIT.md` surfaces for `aoa-skills` and `aoa-evals`
- tighter `AGENTS.md` review guidance in those repos
- tighter `Agents-of-Abyss/ECOSYSTEM_AUDIT_INDEX.md` rows for the workflow and proof layers

## What this wave is not for

- no direct downstream planting yet
- no repo-local Codex skills or eval harnesses in this slice
- no `.codex/config.toml` specialization in this slice
- no cross-repo CI orchestration in this slice
- no change to `navigation.next_live_seed`
- no new `seed_index` entry yet

## Conceptual seam to preserve

### `aoa-skills`

Future audit questions must stay about execution meaning:

- did the skill stay bounded?
- did technique truth stay upstream?
- did overlays stay thin and public-safe?
- did generated skill surfaces stay aligned with authored skill files?

### `aoa-evals`

Future audit questions must stay about proof meaning:

- did the claim remain bounded?
- did verdict shape and baseline semantics stay aligned?
- did chooser wording stay weaker than the bundle contract?
- did shared proof infra stay weaker than bundle-local interpretation?

### `Agents-of-Abyss`

The center-level bridge should keep the later wave in this order:

1. patch skill meaning first when execution changes
2. validate locally
3. inspect proof surfaces
4. only then patch eval wording if the proof surface no longer matches

## Later application order

When the future planting starts, keep the order bounded:

1. add the new files exactly as written in the bundle
2. patch `AGENTS.md` in the three repositories
3. replace the `aoa-skills` and `aoa-evals` rows in `Agents-of-Abyss/ECOSYSTEM_AUDIT_INDEX.md`
4. run each repository's existing validation
5. only then start a later wave for repo-local Codex skills, eval harnesses, or profile tightening

## Validation reminders for later planting

### `aoa-skills`

- `python scripts/release_check.py`
- `python scripts/report_skill_evaluation.py --fail-on-canonical-gaps`
- when technique dependencies change: `python scripts/report_technique_drift.py --techniques-repo ../aoa-techniques`

### `aoa-evals`

- `python scripts/build_catalog.py`
- `python scripts/validate_repo.py`
- for comparison-spine changes, also re-read:
  - `generated/comparison_spine.json`
  - `EVAL_INDEX.md`
  - `EVAL_SELECTION.md`
  - `docs/COMPARISON_SPINE_GUIDE.md`

## Preserved vocabulary

- workflow meaning
- proof meaning
- bounded execution canon
- bounded proof canon
- claim framing
- verdict shape
- chooser wording
- comparison posture
- PLAN
- DIFF
- VERIFY
- REPORT
- RESIDUAL RISK

## Final rule

Use this prep pack to stage later bounded skill/proof audit plantings.
Do not let the seam itself become permission to collapse workflow meaning into proof meaning or proof meaning into workflow meaning.
