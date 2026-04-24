# AGENTS.md
Local guidance for `schemas/` in `Dionysus`.

Read the root `AGENTS.md` first. Schema changes are contract changes for seed
lineage, owner landing trace, quest follow-through, and compact route maps.

## Local role
This directory holds structural contracts such as `seed-route-map.schema.json`,
`seed_lineage_entry.schema.json`, `seed_owner_landing_trace.schema.json`, and
quest-related schemas. They make the garden verifiable; they do not create new
seed authority.

## Editing posture
Pair contract changes with paired examples, validators, docs, and generated
surfaces when applicable. Keep required fields, enums, `$schema`, ids, and path
references explicit.

## Hard no
Do not loosen a schema to hide invalid seed state. Do not let quest schemas
become a second sovereignty layer over owner repos.

## Validation
Run the relevant schema/example validators and the seed-surface entrypoint:

```bash
python scripts/validate_seed_surfaces.py
python scripts/validate_seed_lineage_examples.py
python scripts/validate_seed_owner_landing_trace.py
```
