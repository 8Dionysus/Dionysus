# AGENTS root reference

This file preserves the previous full root guidance for `Dionysus`.
The live root route card is `../AGENTS.md`.

Use this reference when:

- auditing a legacy rule from before Pack 5
- resolving a task branch that the short route card intentionally summarized
- checking whether a slimming move should become a nested `AGENTS.md`, owner doc, or validator rule

Do not treat this file as a competing root. If a preserved rule still actively governs a local directory, move or restate it at the smallest owner surface rather than re-bloating the root.

## Preserved root AGENTS.md from before Pack 5

# AGENTS.md

## Purpose

`Dionysus` is the seed garden and dispatch layer for the current AoA / ToS ecosystem. It stores wave manifests, source seed files, archived canonical planting surfaces, live gated expansion material, named prep packs, registry overlays, and durable planting trace when target-repo history would otherwise lose it.

Treat `Dionysus` as the place where early forms remain legible until they can be planted into stronger owning repositories. It is not the final owning home of AoA meaning, ToS meaning, runtime behavior, or repo-local implementation doctrine.

## Owns

This repository is the source of truth for:

- seed sources before or between plantings
- wave manifests and their ordering
- archived canonical seed surfaces and closure notes
- live gated future-work seeds that are not yet open waves
- named prep packs for flexible future-work staging
- planting protocol, registry overlays, and validation surfaces
- the compact low-context seed-entry capsule at `generated/seed_route_map.min.json`
- durable planting trace when the target-repo trail would not preserve lineage well enough
- repo-local quest follow-through for the seed garden itself, without becoming a second sovereignty layer

## Does not own

Do not treat this repository as the main home for:

- final doctrine already landed in a target repository
- runtime services or deployment posture
- derived graph, export, or UI inflation
- silent AoA ↔ ToS identity collapse
- repo-local backlog disguised as seed canon
- control-plane helper behavior that now belongs in `aoa-sdk`

If the seed has already landed and the owner repository is clear, work there instead of keeping it suspended in the garden.

## Nearest-file precedence

Follow the nearest `AGENTS.md` first when working inside:

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

The manifest defines order. The seed file defines meaning. The closure note defines the finished state of a closed wave. The registry makes navigation legible. This file explains how to work in the repo, but it does not overrule the stronger seed surfaces above.

When work starts from a named prep pack with no manifest, read the pack note and matching `.map.yaml` after checking the stronger live surfaces above. Named prep packs do not overrule an opened wave, `navigation.next_live_seed`, or canonical seed meaning.

## Read this first

Before making changes, read in this order:

1. the relevant `*_wave.manifest.json` or the current live gated seed surface
2. the exact source seed named by that manifest or live route
3. the matching closure note when one exists
4. `seed-registry.yaml`
5. `ROADMAP.md`
6. `docs/SEED_SURFACE_MAP.md`
7. `docs/codex/planting-protocol.md` and nearby contract files
8. the target repository structure and ownership
9. `README.md`, `AGENTS.md`, and the nearest nested `AGENTS.md`

If work starts from a named prep pack rather than an opened wave, read the pack note and matching `.map.yaml` after the stronger live surfaces above. Prep packs are flexible staging notes, not queue sovereignty.
`ROADMAP.md` is a garden-level direction surface after those stronger live
materials. It must not overrule manifest order, closure state, registry state,
or owner-repo reality.

## Route by intent

When the requested change is not truly seed-owned, route by the question being asked:

- `Tree-of-Sophia` for source-linked knowledge, texts, concepts, lineage, and interpretive architecture
- `Agents-of-Abyss` for ecosystem identity, charter, and federation rules
- `abyss-stack` for runtime, deployment, and service posture
- `aoa-sdk` for typed workspace integration and control-plane helper behavior
- `ATM10-Agent` for operator-facing companion behavior
- the already-landed target repository when the seed has clearly crossed into live ownership

Keep seed work here only when staging, replay, lineage preservation, or pre-canon shaping is still the real task.

When the task is specifically about repo-local Codex orientation inside
`Dionysus`, also read:

- `docs/CODEX_MCP.md`
- `scripts/dionysus_mcp_server.py`
- `src/dionysus_mcp/`
- `tests/test_dionysus_mcp_state.py`

## Local contract

- keep `Dionysus` small, legible, lineage-preserving, and transplant-focused
- prefer the smallest source-linked change that makes planting, replay, or navigation clearer
- prefer named prep packs over new numbered waves when multi-repo future work should stay flexible and need-driven
- preserve filenames, anchors, and referenced paths whenever possible
- keep AoA and ToS boundaries explicit
- keep public surfaces public-safe
- treat already-landed repositories as live homes rather than deferred future seeds
- keep repo-local questbook surfaces evidence-first and adjunct-only
- keep the `dionysus` MCP route-first, read-only, and weaker than manifests,
  registry, closure notes, and owner-repo reality

## Hard no

- do not turn `Dionysus` into a shadow owner of runtime behavior or target-repo doctrine
- do not let bridge language become identity collapse
- do not treat derived zip exports as seed canon
- do not open a new numbered wave just to store planting priority
- do not let prep packs overrule an opened wave or current live seed
- do not leave manifest, registry, closure, archive, and seed-expansion linkage out of sync when one of them changes
- do not use quest, campaign, or continuity language to hide missing owner routes or unfinished planting closure

## Workflow

`PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- which seed surface is changing: manifest, seed, closure, registry, prep pack, archive, report, or quest follow-through
- whether the owner repository already exists or is still pending
- what lineage or replay risk exists
- whether planting trace must remain in `Dionysus` or can live in the target repo history

### DIFF

Keep the change focused. Prefer the smallest linked slice that preserves source vocabulary, route clarity, and transplant legibility.

### VERIFY

Confirm that:

- manifest, registry, closure, archive, and seed-expansion surfaces still agree where they should
- stronger live seed surfaces still outrank staging notes
- the owner repository remains explicit
- public-safe boundaries are still respected
- repo-local quest surfaces still read as follow-through rather than second sovereignty

### REPORT

Summarize:

- what seed surfaces changed
- whether meaning changed or only routing / staging changed
- whether lineage or replay posture changed
- what validation was run
- whether follow-up should now happen in a stronger owner repository

## Validation

Run the repository entrypoint:

```bash
python scripts/validate_seed_surfaces.py
```

When the compact seed-entry capsule changes, also run:

```bash
python scripts/build_seed_route_map.py --check
python scripts/validate_seed_route_map.py
```

That gate should remain the single seed-surface validation entrypoint.

For repo-local and workflow reinforcement, also run:

```bash
python -m pytest -q tests
```

For the optional repo-local MCP slice, also run:

```bash
python -m pytest -q tests/test_dionysus_mcp_state.py
python scripts/dionysus_mcp_server.py
```

Use `reports/planting/` only when the target-repo PR or commit trail would not preserve the lineage well enough on its own.

If quest, schema, generated, or planting-trace surfaces change, verify that they still behave as seed-garden follow-through and not as a substitute owner layer.

Do not claim checks you did not run.
