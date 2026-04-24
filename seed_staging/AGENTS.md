# AGENTS.md
Local guidance for `seed_staging/` in `Dionysus`.

Read the root `AGENTS.md` first. This directory holds structured transport and
staging packs for future planting work.

## Local role
Staging helps shape candidate work before it becomes an opened wave, a planted
owner-repo slice, or archived lineage. It must not overrule manifests,
`seed-registry.yaml`, opened waves, or owner-repo reality.

## Editing posture
Keep staging packs explicit about owner repo, lifecycle status, source refs,
what survives, what stays behind, and what still needs review. Prefer small,
linked staging packets over vague backlog piles.

## Hard no
Do not treat staging as canon, queue control, or a way to keep landed work in
suspension after the owner repo is clear.

## Validation
Run:

```bash
python scripts/validate_seed_surfaces.py
```

Then verify any matching `.map.yaml`, registry entry, and owner-repo reference.
