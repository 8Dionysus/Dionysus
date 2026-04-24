# AGENTS.md
Local guidance for `schema/` in `Dionysus`.

Read the root `AGENTS.md` first. This legacy contract pocket currently contains
`seed-registry.contract.yaml`.

## Local role
Treat this as a legacy registry contract surface, not as the broad home for new
JSON schema work. Prefer `schemas/` for new structured contracts unless an
existing reader explicitly depends on this path.

## Editing posture
A change here can alter how seed registry intent is read. Keep compatibility,
name the consumer, and update docs or validators in the same diff when the
contract shape changes.

## Hard no
Do not fork registry truth between `schema/` and `schemas/`. Do not move or
rename this surface without an explicit migration note.

## Validation
Run:

```bash
python scripts/validate_seed_surfaces.py
```
