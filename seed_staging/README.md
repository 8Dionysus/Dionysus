# Seed Staging

`seed_staging/` holds structured transport and staging notes that are worth
keeping in `Dionysus` even when owner repos already landed the main slices.

Use this folder for:

- replayable lineage
- bounded future staging
- donor extraction planning
- partial follow-through that still belongs to the seed garden

Do not treat this folder as the live queue by default.

Read in this order:

1. `docs/SEED_SURFACE_MAP.md`
2. the relevant subfolder README
3. the note frontmatter:
   - `lifecycle_status`
   - `lifecycle_note`
   - `reality_checked_at`
4. owner-repo reality
5. the matching `.map.yaml`

Subfolders:

- `questbook/` for questbook transport and lineage packs
- `rpg/` for RPG transport and lineage packs
- `root_docs/` for replayable root-docs refresh packs
- `audit/` for staged audit packs that are not yet verified as landed
- `future/` for future candidate and prep packs
- `donor/` for donor extraction notes
