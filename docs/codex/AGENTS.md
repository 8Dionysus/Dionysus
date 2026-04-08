# AGENTS.md

Local guidance for `docs/codex/` in `Dionysus`. Read the root `AGENTS.md` first. This file adds local rules for Codex-facing planting discipline.

## Read first

Before editing this directory, read:
1. the repository root `AGENTS.md`
2. `README.md`
3. `docs/codex/planting-protocol.md`
4. the relevant template or report surface if the protocol change would alter landing trace
5. the owner-repo docs named by the protocol when the change narrows or widens planting behavior

## Local role

This directory holds the operational planting protocol for maintainers and coding agents.

Keep it about:
- planting discipline
- reviewability
- owner-repo reality checks
- donor and replay honesty
- stop rules for red-risk zones

Seed meaning, wave status, and repo ownership belong in manifests, closure notes, registry surfaces, or owner repos, not here.

## Editing posture

Keep the protocol stable across waves unless a real planting-contract change is needed.

Prefer language that remains valid across multiple target repos. Examples may illuminate the path, but they must not quietly harden into canon.

Quest or RPG reflection language may appear only as reader support. It must not replace manifest-first order, owner-repo reality, or the actual planting contract.

## Hard no

Do not:
- smuggle target-repo doctrine into this folder
- park future-wave content here because it feels procedural
- weaken the stop rules around secrets, destructive writes, silent policy change, hidden side effects, or vendor-locked canon
- let protocol prose outrun the owner-repo reality it is supposed to respect

## Validation

Run:

```bash
python scripts/validate_seed_surfaces.py
```

Then sanity-check that `docs/codex/planting-protocol.md` still agrees with:
- the README-level summary
- manifest-first reading order
- the current planting template and reporting surfaces
