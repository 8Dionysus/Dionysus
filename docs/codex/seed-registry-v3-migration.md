# Seed Registry v3 Migration

## Goal

Move `Dionysus` from the current registry contract to a v3 contract that makes donor provenance, redistribution obligations, and transplant policy visible and reviewable.

## What this migration changes

It adds three explicit maps to each seed entry:

- `provenance`
- `redistribution`
- `transplant`

It also introduces an optional `freshness` map and two new navigation pointers:

- `provenance_policy`
- `donor_capture_template`

## What this migration does not do

- It does not change manifest sovereignty.
- It does not let the registry override source seed meaning.
- It does not force speculative donor metadata into the live registry.
- It does not widen Dionysus into a full legal archive.

## Recommended sequence

### 1. Land the supporting surfaces first

Merge the following before editing `seed-registry.yaml`:

- `schema/seed-registry.contract.yaml`
- `docs/codex/seed-provenance-policy.md`
- `templates/donor-capture.template.md`
- `scripts/check_seed_registry_v3_readiness.py`

At this stage the main CI validator can remain unchanged.

### 2. Run the readiness checker

Use the advisory checker to find missing v3 fields and, if useful, emit per-entry stub files.

Suggested command:

```bash
python scripts/check_seed_registry_v3_readiness.py seed-registry.yaml --emit-stub-dir .seed-registry-v3-stubs
```

### 3. Backfill donor-shaped entries first

Prioritize any entry that actually depends on external donor material.

Recommended order:

1. entries that carry or adapt upstream material
2. entries that extract reusable patterns from public donors
3. native entries that just need explicit `native` defaults

### 4. Keep native entries lightweight but explicit

Native entries should still carry the new maps with small honest values:

- `provenance.origin_mode: native`
- `transplant.policy: native`
- redistribution booleans set to false
- `obligations_note` saying there are no third-party redistribution duties at seed level

### 5. Bump the registry version only after full coverage

Once every seed entry carries v3 maps, bump:

```yaml
registry_version: 2
```

`contract_version` refers to the field contract document. `registry_version` is the live data shape.

### 6. Only then tighten the main validator

After data coverage is complete, fold the v3 checks into the main registry validator and release checks.

## Entry-level migration rules

### provenance

- use `native` unless a real external donor materially shaped the seed
- use `donor_derived` when a public donor is part of the seed's meaning
- use `mixed` only when native and donor materials are intentionally fused

### redistribution

Record practical obligations, not whole license essays.

At minimum decide:

- is there an upstream license to record?
- must the license travel with redistribution?
- must attribution or NOTICE text be retained?
- were upstream files modified?
- where is the short obligations note?

### transplant

Do not leave donor-shaped transplant fields vague.

Every donor-shaped entry should say:

- what survives
- what stays behind
- what is explicitly out of scope

## Conservative CI posture

Until the backfill is complete:

- keep the current validator authoritative
- treat the readiness checker as advisory
- do not fail release checks on missing v3 fields yet

After the backfill:

- make the v3 fields mandatory in CI
- reject donor-shaped entries with null donor repo/ref
- reject donor-shaped entries with empty `what_survives` / `what_stays_behind`

## Failure smells

Back up and narrow scope if the migration starts to become:

- a speculative legal rewrite
- a guess-heavy donor census
- a registry-wide copyedit spree without real provenance gain
- a hidden attempt to import donor doctrine wholesale

## Minimal success criteria

The migration is good when:

- every seed entry can distinguish native versus donor-shaped origin
- donor-shaped entries expose repo, ref, obligations, and transplant policy
- native entries stay lightweight
- the registry becomes easier to review, not heavier to believe
