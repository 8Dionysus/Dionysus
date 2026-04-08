# AGENTS.md

Local guidance for `seed_expansion/` in `Dionysus`. Read the root `AGENTS.md` first. This file adds local rules for the next gated future-work seed surface.

## Read first

Before editing anything here, read:
1. the repository root `AGENTS.md`
2. `seed-registry.yaml`
3. the exact live seed file or prep surface you plan to touch
4. the owner-repo surfaces named by that seed when they already exist
5. the relevant archive or closure surfaces if this change is part of a handoff

## Local role

`seed_expansion/` is for explicitly gated next-live seed material that has not yet become an opened wave.

This directory is neither archive nor loose brainstorm field. It is a narrow launch ledge for source-like future work.

## Editing posture

Keep this directory:
- small
- intentional
- bounded
- source-like

Every live seed here must have:
- explicit registry coverage
- lifecycle wording that matches `seed-registry.yaml`
- preserved anchors and seed vocabulary
- explicit anti-goals when they are already known

When a seed here is planted, archived, split, replaced, or superseded, update the linked registry and archive surfaces in the same bounded change.

## Hard no

Do not:
- park donor dumps, private notes, or repo-local backlog items here
- silently replace `navigation.next_live_seed` without updating `seed-registry.yaml`
- let `seed_expansion/` become a second archive or a general staging warehouse
- let prep language overrule stronger owner-repo reality

## Validation

Run:

```bash
python scripts/validate_seed_surfaces.py
```

If you changed a live seed path, anchor, or lifecycle marker, verify the corresponding registry entry in the same diff.
