# AGENTS.md

Local guidance for `archive/` in `Dionysus`. Read the root `AGENTS.md` first. This file adds local rules for archived lineage surfaces.

## Read first

Before changing anything in `archive/`, read:
1. the repository root `AGENTS.md`
2. the relevant `*_wave.manifest.json`
3. the matching closure note when one exists
4. `seed-registry.yaml`
5. any planting report or target-repo reference that still points at the archived surface

## Local role

`archive/` is the canonical archive root for historical seed sources, archived seed packs, post-wave packs, and other lineage surfaces that must remain replayable.

Representative subtrees include:

- `seed_bundle/`
- `seed_rootline/`
- `seed_witness/`
- `seed_branches/`
- `seed_soil/`
- `seed_templates/`
- `seed_pack_2026-03-22/`
- `seed_post_wave/`

`archive/seed_pack_exports/` may hold derived ingress or transport bundles, but those bundles are not canonical seed meaning.

## Editing posture

Treat archived material as historical canon for lineage and replay, not as a draft workspace.

Preserve whenever possible:
- original filenames
- paths and anchors
- chronology
- provenance notes
- the seed's own voice

Fix archived content only when needed to preserve readability, reference integrity, or replayability.

If a live surface moves into `archive/`, update registry, closure, report, and linked references in the same bounded change.

## Hard no

Do not:
- normalize archived seed voice just to make it prettier
- mix new live work or speculative staging into `archive/`
- silently rename or delete files that manifests, reports, or registry entries may still reference
- treat archive cleanup as permission to rewrite history

## Validation

If you changed archived paths or anchors, run:

```bash
python scripts/validate_seed_surfaces.py
```

Then manually verify touched references in manifests, closure notes, registry entries, and durable planting reports.
