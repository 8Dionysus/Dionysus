# AGENTS.md

Local guidance for `seed_expansion/` in `Dionysus`.

Read the root `AGENTS.md` first. This file only adds local rules for the next gated future-work seed surface.

## Scope

`seed_expansion/` is for explicitly gated next-live seed material that has not yet become an opened wave.

## Local contract

- Keep this directory small and intentional.
- Every live seed here must have explicit registry coverage and lifecycle wording that matches `seed-registry.yaml`.
- Preserve exact anchors and seed vocabulary because manifests or registry navigation may point here directly.
- Treat files here as source surfaces, not as loose brainstorming notes.
- When a seed here is planted, archived, split, or replaced, update the linked registry and archive surfaces in the same change.

## Change rules

- Do not park donor dumps, private notes, or repo-local backlog items here.
- Do not silently replace `navigation.next_live_seed` by editing a file without updating `seed-registry.yaml`.
- Do not let `seed_expansion/` turn into a second archive or a general staging area.
- Keep future-work material bounded, source-like, and explicit about anti-goals when those are known.

## Validate

Run:

```bash
python scripts/validate_seed_surfaces.py
```

If you changed the live seed path or anchor, verify the corresponding registry entry in the same diff.
