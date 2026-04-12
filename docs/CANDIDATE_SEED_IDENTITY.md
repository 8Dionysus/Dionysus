# Candidate To Seed Identity

## Purpose

This note defines the `Dionysus` side of the growth-refinery lineage route.

The route stays:

`cluster_ref -> candidate_ref -> seed_ref -> object_ref`

`Dionysus` is the first honest home of `seed_ref`.
It is not the first honest home of reviewed `candidate_ref`, and it is not the
final home of planted `object_ref`.

## Boundary

Keep the owner split explicit:

- `aoa-sdk` may carry `cluster_ref` and bounded lineage hints
- `aoa-skills` may mint reviewed `candidate_ref`
- `Dionysus` may stage and trace `seed_ref`
- the owner repository may mint or confirm `object_ref`

This bridge is real, but it is not a new sovereign lineage layer.

## What Dionysus Must Carry

When a reviewed candidate becomes a staged seed, keep these fields legible:

- `cluster_ref`
- `candidate_ref`
- `seed_ref`
- `owner_hypothesis`
- `owner_shape`
- `lifecycle_status`
- `status_posture`
- `evidence_refs`
- `supersedes`
- `merged_into`
- `drop_reason`
- `object_ref`

The repo-local structural surface for that entry lives in:

- `schemas/seed_lineage_entry.schema.json`
- `examples/seed_lineage_entry.example.json`
- `scripts/validate_seed_lineage_examples.py`

Once `seed_ref` already exists and the route needs a visible post-staging
followthrough witness, continue with:

- `docs/SEED_OWNER_LANDING_TRACE.md`
- `schemas/seed_owner_landing_trace.schema.json`
- `examples/seed_owner_landing_trace.example.json`
- `scripts/validate_seed_owner_landing_trace.py`

## Negative Rules

- do not mint `seed_ref` without a reviewed `candidate_ref`
- do not treat staging as final owner truth
- do not mint `candidate_ref` here
- do not require `object_ref` while the seed is only staged
- do not turn the example validator into a cross-repo sovereign contract

## Lifecycle Posture

The local seed-lineage example is intentionally structural:

- `staged`, `open-wave`, and `planting-in-progress` may keep `object_ref: null`
- `planted` must carry a non-null `object_ref`
- `superseded` must point at `merged_into`
- `dropped` must explain `drop_reason`
- `status_posture` must stay within `early`, `reanchor`, `thin-evidence`,
  or `stable`

That is enough for local consistency without claiming proof that an owner-repo
planting already landed.

## Current Bridge Example

The current growth-refinery bridge example keeps one reviewed candidate from
`aoa-skills` visible as a staged `seed_ref` in `Dionysus`.

That example is not the final rollout report.
It is the local contract witness that the `candidate_ref -> seed_ref` step can
be carried honestly inside this repo.

The separate seed-owner trace example starts only after that step and records
what happened next without outranking the owner repository.
