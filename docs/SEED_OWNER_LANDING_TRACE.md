# Seed Owner Landing Trace

Use this note after `seed_ref` already exists and the next honest question is:
what happened after staging?

This trace is weaker than owner-repo truth. It keeps seed-to-owner followthrough
visible without letting seed staging masquerade as completion.

## Purpose

Once a reviewed candidate becomes a staged seed, the route still needs one
visible witness for what happened next:

- landed as owner status
- landed as owner object
- reanchored
- merged
- deferred
- dropped

Without this trace:

- seed staging can look complete when it is not
- later stats can overread staging as landing
- pruning can disappear into silence
- writeback loses concrete route context

## Boundary

This surface is:

- route-first
- repo-local
- subordinate to the seed registry and planting protocol
- weaker than owner receipts and landed owner objects

This surface is not:

- a replacement for `seed_lineage_entry`
- final owner truth
- proof authority
- schedule authority

## Required Identity

Keep these fields explicit:

- `candidate_ref`
- `seed_ref`
- target `owner_repo`
- target `owner_shape`
- `outcome`
- `observed_at`
- `evidence_refs`

Carry `cluster_ref` when it is already available from the upstream lineage
chain.

## Allowed Outcomes

- `landed_owner_status`
- `landed_owner_object`
- `reanchored`
- `merged`
- `deferred`
- `dropped`

## Relationship To Existing Seed Lineage

`schemas/seed_lineage_entry.schema.json` and
`examples/seed_lineage_entry.example.json` remain the local structural witness
for `candidate_ref -> seed_ref`.

`schemas/seed_owner_landing_trace.schema.json` and
`examples/seed_owner_landing_trace.example.json` begin only after that seed
bridge already exists.

## Negative Rules

Do not:

- let this trace outrank owner receipts
- let seed status alone count as proof or final landing
- mint `candidate_ref` or `seed_ref` here
- silently hide merge, defer, or drop outcomes
