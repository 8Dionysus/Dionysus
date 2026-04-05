# Planting Reports

This folder holds durable planting trace when Dionysus is the right place to preserve it.

Prefer a target-repo PR description when the planting can be reviewed there without loss. Use this folder when a seed touches multiple repos, when the original PR context is likely to disappear, or when you need Dionysus to keep the lineage visible.

These reports are historical trace, not current queue control.
If you need current planting truth, read `seed-registry.yaml`,
`docs/SEED_SURFACE_MAP.md`, and then verify the owner repo directly.

Hydrate durable reports with merged target-repo PR and commit refs once the planting lands.
If a report is revised after later slices land, use time-scoped wording for any then-current queued or deferred notes instead of leaving false present-tense state behind.

## Naming convention

Use one file per planted seed:

`YYYY-MM-DD.<target-repo>.<seed-id>.md`

Examples:

- `2026-03-22.aoa-memo.aoa-memory-thermodynamics.md`
- `2026-03-22.tree-of-sophia.tos-context-node-template.md`

Start from `templates/planting-report.template.md`.
