# AGENTS.md

Local guidance for `reports/planting/` in `Dionysus`.

Read the root `AGENTS.md` first. This file only adds local rules for durable planting trace.

## Scope

This folder holds planting reports when Dionysus is the right place to preserve the trace.

Use it for cases such as:

- multi-repo plantings
- context that would be scattered across several target repos
- target-repo review trails likely to disappear or become hard to reconstruct

## Local contract

- Prefer the target-repo PR or commit trail when that preserves lineage well enough.
- Keep one report per planted seed using `YYYY-MM-DD.<target-repo>.<seed-id>.md`.
- Start from `templates/planting-report.template.md` and keep the required fields intact.
- Reports are durable trace, not a new sovereign seed source.
- Hydrate landed reports with merged PR, commit, or issue refs once they exist.
- If you revise an older report after later slices landed, use time-scoped wording for then-current queued or deferred state.

## Change rules

- Keep reports public-safe and reviewable.
- Preserve the exact source ref and the named target repo.
- Leave one clearly named structural artifact and one clearly named validation surface in every report.
- Do not let a report quietly replace registry, closure, or manifest state.

## Validate

Run:

```bash
python scripts/validate_seed_surfaces.py
```

Then manually verify naming, source refs, landed-surface paths, and PR or commit references against the actual landing.
