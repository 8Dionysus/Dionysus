# AGENTS.md

Local guidance for `archive/` in `Dionysus`.

Read the root `AGENTS.md` first. This file only adds local rules for archived lineage surfaces.

## Scope

`archive/` is the canonical archive root for historical seed sources, archived seed packs, post-wave packs, and other lineage surfaces that still need to be replayable.

Representative subtrees include:

- `seed_bundle/`
- `seed_rootline/`
- `seed_witness/`
- `seed_branches/`
- `seed_soil/`
- `seed_templates/`
- `seed_pack_2026-03-22/`
- `seed_post_wave/`

## Local contract

- Treat archived material as historical canon for lineage and replay, not as a draft workspace.
- Preserve original filenames, paths, anchors, chronology, and provenance notes whenever possible.
- Fix archived content only when needed to preserve readability, reference integrity, or replayability.
- Keep archive additions clearly historical: closed-wave packs, archive cleanup moves, or explicit lineage captures.
- If a live surface moves into `archive/`, update registry, closure, report, and any linked refs in the same bounded change.

## Change rules

- Do not rewrite archived seed voice just to normalize style.
- Do not mix new live work or speculative notes into `archive/`; use `seed_expansion/` or the owning target repo instead.
- Do not silently rename or delete archived files that may be referenced from manifests, reports, or `seed-registry.yaml`.
- When adding a new archived pack, include or update the pack-level provenance note when the folder would otherwise be hard to replay.

## Validate

If you changed archived paths or anchors, run:

```bash
python scripts/validate_seed_surfaces.py
```

Then double-check any touched refs in manifests, closure notes, registry entries, and durable planting reports.
