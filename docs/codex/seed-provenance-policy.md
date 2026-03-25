# Seed Provenance Policy

## Purpose

This document defines how `Dionysus` should record donor provenance, redistribution obligations, and transplant policy for seed entries that are shaped by external open-license repositories.

Dionysus remains seed soil and dispatch layer. The goal here is not to widen the registry into a legal encyclopedia. The goal is to leave enough provenance for a human or agent to answer three practical questions without guesswork:

1. **Where did this shape come from?**
2. **What may be carried forward?**
3. **What must stay behind?**

## Core rule

Treat external repositories as donors, not as canon.

A donor is useful when the registry can say:

- what bounded form survives
- what donor doctrine or implementation accident stays behind
- what redistribution obligations must still be honored if anything upstream was copied or adapted

If those three answers are not visible yet, the donor is still evidence or soil, not a clean seed entry.

## When v3 provenance is required

Record the v3 maps for every seed entry.

Use the smallest honest values for native seeds:

- `provenance.origin_mode: native`
- `redistribution` fields set to explicit false/null defaults
- `transplant.policy: native`

Use donor-shaped values whenever a public external repo materially influenced the seed, even if nothing was copied verbatim.

## Required donor capture

When a seed is donor-derived or mixed, capture all of the following:

- donor repository URL
- exact donor ref used for reading or extraction
- upstream SPDX identifier when known
- donor paths that were actually mined
- local provenance note
- transplant policy
- bounded surviving form
- donor material intentionally left behind
- concrete redistribution obligations

## Transplant policies

### `native`

Authored inside the AoA / ToS ecosystem. No external donor dependency is being carried at the seed level.

### `idea_only`

A donor helped orient the design, but the landing does not redistribute donor material. Keep provenance visible anyway if the donor materially shaped the seed.

### `pattern_extract`

A repeated operational form was extracted from the donor. The reusable object is the pattern, not the donor codebase or worldview.

### `adapt_with_attribution`

Some upstream structure, text, or code was adapted. Attribution and redistribution duties must be recorded explicitly.

### `vendor_verbatim`

Upstream material is carried near-verbatim. This is the heaviest path and should preserve license, notice, and modification markers as required.

### `read_only_donor`

The donor remains a referenced source surface or evidence pack. No redistribution into target repos is claimed by the seed itself.

## What survives / what stays behind

For donor-derived and mixed entries, the registry should make these lists inspectable:

### `what_survives`

Name the bounded reusable form that is actually being kept.

Good examples:

- one-source to many-target sync contract
- bounded local lifecycle command
- reviewable transcript packaging pattern

### `what_stays_behind`

Name what the donor brought that is intentionally not imported.

Good exclusions:

- donor identity mythology
- private environment assumptions
- orchestration sprawl
- registry or routing doctrine outside the extracted seam
- donor-specific naming that is not part of the reusable pattern

## Redistribution recording rule

Do not force the registry to restate the whole license text.

Do record the operationally meaningful obligations:

- license identifier
- where the upstream license was found
- whether a copy of the license must travel
- whether NOTICE or attribution text must be retained
- whether modified upstream files require change markers
- whether the current landing is modified from upstream
- where a short obligations note lives

## Donor capture note

When `provenance.origin_mode` is `donor_derived` or `mixed`, `provenance.provenance_note` should point to a local Markdown note that answers:

- why this donor was admitted
- which paths were mined
- what survives
- what stays behind
- what redistribution obligations were recorded
- what revalidation cadence is needed

Use `templates/donor-capture.template.md` as the default shape.

## Freshness and supersession

External donors drift.

When the donor matters beyond a one-time read, prefer filling:

- `freshness.last_revalidated_at`
- `freshness.revalidate_after_days`
- `freshness.superseded_by`

This is especially useful for donor-shaped seeds that point to moving branches, external catalogs, or repos that may change structure.

## Stop rules

Do not bless a donor-shaped entry as ready when any of the following is still unknown:

- the actual donor repo or ref
- whether material was only studied versus adapted
- whether NOTICE or attribution text must be retained
- what donor doctrine must remain outside the seed
- whether the current entry is already superseded

If that information is not ready yet, keep the donor in notes, evidence, or donor-capture surfaces instead of pretending the registry is already clean.
