# AGENTS.md

Local guidance for `docs/codex/` in `Dionysus`.

Read the root `AGENTS.md` first. This file only adds local rules for Codex-facing planting discipline.

## Scope

This directory holds the operational planting protocol for maintainers and coding agents.

At the moment the primary surface is:

- `planting-protocol.md`

## Local contract

- Keep this folder about planting discipline, reviewability, and repo-operating posture.
- Keep the rules stable across waves unless a real protocol change is needed.
- Put seed meaning, wave status, and repo-home ownership in manifests, closure notes, or `seed-registry.yaml`, not here.
- Keep examples illustrative. Do not let one example harden into canon by accident.

## Change rules

- Preserve the stop rules around secrets, destructive writes, silent policy change, hidden side effects, and vendor-locked canon.
- Prefer concise protocol language that remains valid across multiple target repos.
- If protocol wording changes the effective planting contract, update `README.md` and the relevant template or reporting surface in the same change.
- Do not use this folder to smuggle in target-repo doctrine or future-wave content.

## Validate

Run:

```bash
python scripts/validate_seed_surfaces.py
```

Then sanity-check that `docs/codex/planting-protocol.md` still agrees with the README-level summary and does not contradict the manifest-first reading order.
