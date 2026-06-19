# AGENTS.md

Root route card for `Dionysus`.

## Purpose

`Dionysus` is the seed garden and dispatch layer for AoA / ToS.
It keeps early forms, wave manifests, seed files, closure notes, prep packs, registry overlays, and planting trace legible until stronger owner repositories can receive them.

## Owner lane

This repository owns:

- seed sources before or between plantings
- wave manifests, closure notes, prep packs, archive surfaces, and seed registry overlays
- planting protocol, replay route, and durable lineage trace when target-repo history is not enough

It does not own:

- final AoA doctrine, final ToS meaning, runtime behavior, SDK helper behavior, or target-repo implementation law
- a shadow backlog disguised as seed canon
- quest or continuity language that hides missing owner routes

## Start here

1. the relevant `*_wave.manifest.json` or current live gated seed surface
2. the exact source seed file
3. the matching closure note when one exists
4. `seed-registry.yaml`
5. `ROADMAP.md`
6. `docs/SEED_SURFACE_MAP.md`
7. `docs/codex/planting-protocol.md`
8. `docs/decisions/README.md` for durable seed-route rationale
9. the target repository ownership docs
10. `docs/AGENTS_ROOT_REFERENCE.md` for preserved full root guidance


## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Memory route

For recall, continuity, compaction recovery, comparison with past work, or
preserved lessons, start with `aoa-memo` and the workspace memory map. Session
grounding routes through `.aoa`; local candidate writing routes through this
repository's `memo/` port when that port exists; durable reviewed memory lands
through `aoa-memo`.

## Route away when

- the seed has landed and the owner repository is clear
- source-linked knowledge belongs in `Tree-of-Sophia`
- ecosystem doctrine belongs in `Agents-of-Abyss`
- runtime belongs in `abyss-stack`
- typed helper behavior belongs in `aoa-sdk`
- operator companion behavior belongs in `ATM10-Agent`

## GitHub landing workflow

Root `AGENTS.md` owns the repository-wide branch, PR, CI, and merge route.
`.github/AGENTS.md` owns the GitHub-native files that support it.

When the user asks to commit, push, and merge in this repository, use this route:

1. Start from a branch based on the current `origin/main`. If the worktree is already dirty, inventory it first and carry forward only the intended diff.
2. Commit the intended change with a message that names the changed surface.
3. Push the branch and open a pull request that states changed surfaces, validation run, skipped checks, and remaining risk.
4. Wait for GitHub `Repo Validation` and any required GitHub checks. If a check fails, fix the branch and wait for the new result.
5. Merge through GitHub after green validation. Use squash unless repository settings report a different required method; report the method that landed.
6. Return to `main`, fast-forward from `origin/main`, and confirm the worktree is clean before closeout.

If GitHub status or merge permissions cannot be observed, stop the landing route and report the exact blocker instead of guessing.

## Verify

Default seed-surface check:

```bash
python scripts/validate_seed_surfaces.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_decision_records.py
```

When the compact seed route capsule changes:

```bash
python scripts/build_seed_route_map.py --check
python scripts/validate_seed_route_map.py
python scripts/validate_abyss_machine_seed_route_bundle.py
```

For repo-local reinforcement, also run:

```bash
python -m pytest -q tests
```

## Report

State which seed surface changed, whether meaning or only staging/routing changed, whether lineage or replay posture changed, and whether follow-up now belongs in a stronger owner repo.

## Full reference

`docs/AGENTS_ROOT_REFERENCE.md` preserves the former detailed root guidance for source-of-truth order, prep-pack posture, MCP route details, and planting trace review.
