# AGENTS.md
Local guidance for `templates/` in `Dionysus`.

Read the root `AGENTS.md` first. This directory holds planting report templates
and other reusable shapes for preserving seed-garden trace.

## Local role
Planting report templates should keep source refs, target repos, structural
artifacts, validation, and remaining caveats visible. They support lineage; they
do not freeze future waves into one format forever.

## Editing posture
Change templates only when repeated real planting work shows the old shape is
missing a field or causing drift. Keep fields public-safe and reviewable.

## Hard no
Do not use templates to invent mandatory doctrine for owner repos. Do not remove
lineage, donor, license, or validation fields just to make reports shorter.

## Validation
After template changes, sanity-check existing reports and run:

```bash
python scripts/validate_seed_surfaces.py
```
