# AGENTS.md

Local guidance for `reports/planting/` in `Dionysus`. Read the root `AGENTS.md` first. This file adds local rules for durable planting trace.

## Read first

Before editing or adding a planting report, read:
1. the repository root `AGENTS.md`
2. the relevant `*_wave.manifest.json`
3. the exact seed source or prep-pack note being planted
4. `docs/codex/planting-protocol.md`
5. `templates/planting-report.template.md`

## Local role

This folder holds planting reports when `Dionysus` is the right place to preserve the trace.

Use it when the lineage would otherwise be scattered or fade into fog, for example:
- multi-repo plantings
- landings whose context is split across several repos
- cases where target-repo review trails may disappear or become hard to reconstruct

Reports are durable trace, not a new sovereign seed source.

## Editing posture

Prefer the target-repo PR or commit trail when that preserves lineage well enough.

Keep:
- one report per planted seed
- stable `YYYY-MM-DD...md` naming
- the required template fields intact
- exact source refs and named target repos visible
- one clearly named structural artifact
- one clearly named validation surface

When a report is revised after later slices landed, use time-scoped wording for then-current queued or deferred state rather than rewriting the past as prophecy.

## Hard no

Do not:
- let a planting report quietly replace manifest, closure, or registry state
- blur landed fact with future intention
- drop donor, license, or transplant notes when the planting depended on them
- turn reports into a second queue system

## Validation

Run:

```bash
python scripts/validate_seed_surfaces.py
```

Then manually verify:
- report naming
- source refs
- landed-surface paths
- PR, commit, or issue references against the actual landing
