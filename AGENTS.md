# AGENTS.md

Local guidance for `Dionysus`.

## Scope

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem. It stores wave manifests, source seed files, archived canonical surfaces, planting protocol, registry overlays, and durable planting trace when that trace would otherwise be lost.

Nearest-file precedence applies for work inside:

- `archive/AGENTS.md`
- `docs/codex/AGENTS.md`
- `reports/planting/AGENTS.md`
- `seed_expansion/AGENTS.md`

## Source-of-truth order

When files pull in different directions, treat these as authoritative in this order:

1. relevant `*_wave.manifest.json`
2. exact canonical source seed file
3. matching closure note for the same wave
4. `seed-registry.yaml`
5. planting protocol and contract files
6. target repository structure and ownership
7. `README.md`

This `AGENTS.md` explains how to work in the repo. It does not overrule the seed surfaces above.

## Local contract

- Keep `Dionysus` small, legible, lineage-preserving, and transplant-focused.
- Prefer the smallest source-linked change that makes planting, replay, or navigation clearer.
- Preserve filenames, anchors, and referenced paths whenever possible.
- Keep AoA and ToS boundaries explicit. Do not let bridge language become identity collapse.
- Do not turn `Dionysus` into a shadow owner of runtime behavior or target-repo doctrine.
- Keep public surfaces public-safe. Do not place secrets, private chat fragments, or operationally sensitive runtime detail here unless they were deliberately curated as public seed material.

## Change rules

- If you change manifest, registry, closure, archive, or seed-expansion linkage, update the linked surfaces together in one bounded diff.
- Prefer manifests, registry, reports, templates, and protocol notes over derived exports or decorative growth.
- Preserve seed vocabulary unless the mapping is explicit and source-linked.
- Use `reports/planting/` only when the target-repo PR or commit trail would not preserve the lineage well enough on its own.
- When adding local operating guidance, keep it close to the working directory and keep it compact.

## Validate

Run the repository entrypoint:

```bash
python scripts/validate_seed_surfaces.py
```

That gate should remain the single CI-facing command for seed-surface validation.
