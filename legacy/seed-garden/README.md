# Dionysus — archived seed garden

> **Archived on 2026-07-23.** This repository is a historical, read-only
> record. It no longer operates as a seed dispatcher, staging queue, MCP
> service, or active OS Abyss component.

## Why it was archived

`Dionysus` was created to preserve, expand, stage, and dispatch early AoA and
Tree of Sophia seeds into their owning repositories. That intermediary is no
longer needed: current seeds can be planted directly with a capable coding
agent and reviewed in the repository that owns the resulting meaning.

Keeping the intermediary active would add routing cost, duplicated machinery,
and false queue authority. Freezing it preserves the useful material without
requiring OS Abyss to maintain another organ.

## What remains

The final tree keeps only seed material, direct planting history, and the
minimum metadata needed to understand the archive:

- `archive/` — canonical historical seeds and packaged seed exports;
- `seed_expansion/` — source-like seeds that were on the former launch ledge;
- `seed_notes/` — exploratory notes whose signal may still be useful;
- `seed_staging/` — former staging and donor packs, preserved as historical
  seed material;
- `*_wave.manifest.json`, `ninth_wave.closure.md`, and
  `seed-registry*.yaml` — the frozen wave and registry record;
- `reports/planting/` — durable planting, preflight, closure, and proposed
  planting trace;
- `examples/seed_lineage_entry.titans_first_appearance.example.json` — the
  lineage example referenced directly by `tenth_wave.manifest.json`;
- `docs/decisions/DION-SEED-D-0001-seed-decision-rationale-lane.md` and
  `CHANGELOG.md` — retained repository history.

Original paths were deliberately preserved. Many manifests, reports, and seed
documents refer to one another by path, and reorganizing them during the
freeze would make later archaeology less reliable.

All lifecycle labels inside the archive — including `opened`, `gated_next`,
`staged`, `staged_only_not_landed`, and `partially_landed` — describe the
state recorded before the freeze. They are not a current queue, mandate, or
claim about the present state of any owner repository.

Packaged ZIP exports remain because some contain the most convenient surviving
form of a seed packet. Generated KAG indexes, validators, tests, schemas,
runtime adapters, MCP code, local skills, stats/eval/memo ports, quest
machinery, CI, and transient audit or local-AI mirrors were removed from the
final tree.

## Recovering the former operational repository

Nothing removed by the cleanup was erased from Git history.

- `pre-archive-2026-07-23` points to the complete repository immediately
  before the cleanup.
- `v0.3.0` is the last published operational release.
- Commit `8529c00` is the final pre-cleanup `main` snapshot.

Examples:

```bash
git show pre-archive-2026-07-23:scripts/release_check.py
git log --all -- path/to/a/removed/file
git worktree add ../Dionysus-pre-archive pre-archive-2026-07-23
```

Use the live owner repository for current truth:

- `Agents-of-Abyss` for AoA doctrine;
- `Tree-of-Sophia` for ToS authored meaning;
- `aoa-sdk`, `aoa-skills`, `aoa-evals`, `aoa-routing`, `aoa-memo`,
  `aoa-stats`, `aoa-playbooks`, and `aoa-agents` for their respective
  contracts and mechanisms;
- `abyss-stack` for runtime and deployment.

This archive does not designate a successor and should not be reopened merely
to restore the old intermediary.
