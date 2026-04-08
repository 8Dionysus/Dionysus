seed_id: seed.tos.graph-curation-pack.v0
title: ToS Graph Curation Pack
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: ToS graph curation remains staged in Dionysus; no owner-repo rollout is verified yet.
reality_checked_at: '2026-04-08'
status: pending_archive
priority: now
parent_seed: null
tags:
  - tos
  - graph
  - curation
  - abyss-stack
  - neo4j
  - source-first

# Seed Note: ToS Graph Curation Pack

## Purpose

Prepare the ToS graph curation bundle as a bounded cross-repo prep pack inside
`Dionysus`.

This pack preserves the route-first runtime helper idea without turning a zip
handoff into seed canon, and without letting `abyss-stack` or Neo4j become the
 source of ToS meaning.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source artifact is a transport bundle, not an owner-repo patchset
- the rollout spans runtime ownership in `abyss-stack` and source authority in
  `Tree-of-Sophia`
- the package is stronger as staging and lineage than as a new wave or direct
  `seed_expansion/` promotion
- the bundle currently carries intent, plan, and prompt surfaces, so it still
  needs repo-native adaptation before owner rollout begins

## Bundle contents to preserve

The source artifact is `archive/seed_pack_exports/tos_graph_curation_seed.zip`.

It carries:

- `codex_tos_graph_handoff.md`
- `codex_tos_graph_plan.yaml`
- `codex_tos_graph_prompt.txt`

## Ownership posture

Read later landings under these owner boundaries:

- `abyss-stack` owns the helper service, compose/profile posture, localhost
  runtime surface, and Neo4j projection mechanics
- `Tree-of-Sophia` owns canonical authored meaning, relation packs, registries,
  and validator truth about canonical writeback
- `Dionysus` owns only seed-garden staging and transport lineage

This pack does not make `Dionysus` a runtime owner, a graph authority, or a
shadow source of ToS doctrine.

## Application posture

Treat this pack as a bounded prep source.

The honest first owner-repo landing is:

1. plant the contract and quest anchors in `abyss-stack`
2. land a read-only route-first projection slice before any writeback path
3. use `Tree-of-Sophia` as the validator and authority boundary for any later
   patch/apply route
4. only then consider validator-gated writeback and rollback

When planted later, regenerate repo-native files from the live owner repo
surfaces rather than copying transport text into implementation trees
unchanged.

## What this pack is not for

- no new numbered wave
- no `seed_index` promotion yet
- no replacement of `navigation.next_live_seed`
- no direct live write enablement from `Dionysus`
- no silent treatment of Neo4j as canonical truth
- no canonical editing through mirrored `tos-source` runtime surfaces
- no widening of host exposure beyond localhost
- no LLM-driven autonomous writes into ToS canon

## Final rule

Plant the boundary before the editor.
The real win here is a route-first runtime helper that stays subordinate to ToS
source authority, validator law, and explicit write gates.
