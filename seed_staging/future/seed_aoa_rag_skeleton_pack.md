seed_id: seed.aoa.rag-skeleton-pack.v0
title: AoA Thin RAG Skeleton Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: prep-pack-note
lifecycle_status: staged_only_not_landed
lifecycle_note: Thin RAG seed remains staged in Dionysus as a derived downstream-ingest pack; owner surfaces are still the public AoA and ToS repos, several live files have already drifted beyond the snapshot, and no downstream consumer rollout is verified yet.
reality_checked_at: '2026-04-08'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - rag
  - retrieval
  - kag
  - routing
  - memo
  - source-first
  - downstream-ingest

# Seed Note: AoA Thin RAG Skeleton Prep Pack

## Purpose

Prepare `aoa-rag-seed` as a bounded downstream-ingest prep pack inside
`Dionysus`.

This pack preserves a thin RAG skeleton assembled from current public AoA and
ToS owner surfaces without pretending the package itself is a new source of
truth.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the source artifact is a curated transport bundle, not an owner-repo patch
- the package spans constitutional boundary, source authority, bounded KAG,
  routing, memo, technique-export, and runtime-reference surfaces
- the snapshot already shows small owner drift, so lineage and replay matter
  more than pretending the zip is live truth
- any later consumer landing still needs an explicit owner choice and
  repo-native adaptation before code should move

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/aoa-rag-seed-2026-04-08.zip`.

The archived ingress summary is
`archive/seed_pack_exports/aoa-rag-seed-2026-04-08-summary.md`.

The package carries:

- `README_FOR_CODEX.md`
- `SEED_MANIFEST.json`
- `OPTIONAL_REMOTE_REFS.json`
- 42 snapshot files across `Agents-of-Abyss`, `Tree-of-Sophia`, `aoa-kag`,
  `aoa-routing`, `aoa-memo`, `aoa-techniques`, and `ATM10-Agent`
- one explicit ingest order and precedence rule set for source, derived,
  routing, memo, technique, and runtime-reference surfaces

## Reality check posture

On `2026-04-08`, the current sibling-workspace comparison found:

- 35 of 42 manifest files still match the snapshot exactly
- 4 files have drifted in `aoa-kag`, `aoa-memo`, and `aoa-routing`
- 3 runtime-reference files could not be revalidated locally because that repo
  is not present in the current sibling workspace

Treat this pack as replayable staging and donor context, not as current
owner-repo truth.

## Ownership posture

Read later landings under these owner boundaries:

- `Agents-of-Abyss` owns federation law and layer boundaries
- `Tree-of-Sophia` owns canonical source meaning and tiny-entry re-entry
- `aoa-kag` owns derived retrieval-ready substrate, not canon
- `aoa-routing` owns navigation hints, not semantic truth
- `aoa-memo` owns memory truth and writeback-boundary surfaces
- `aoa-techniques` owns technique-side donor-export meaning
- `ATM10-Agent` remains runtime reference material only
- `Dionysus` owns only seed-garden staging, archive lineage, and replay
  posture

This pack does not make `Dionysus` a downstream consumer owner, a KAG
authority, a routing authority, or a shadow memory surface.

## Application posture

Treat this pack as staged downstream-ingest soil.

The honest first landing, if chosen later, is:

1. choose one downstream consumer or runtime surface that needs a thin RAG
   spine
2. revalidate the owner surfaces named in `SEED_MANIFEST.json` against live
   repos before copying any shape forward
3. land one repo-native retrieval path that keeps source authority, KAG,
   routing, memo, and runtime-reference boundaries explicit

Only after that should any wider runtime, memory writeback, or graph-heavy
growth be considered.

When planted later, regenerate repo-native indexes, configs, and manifests from
live owner surfaces rather than copying archived snapshot files unchanged.

## What this pack is not for

- no new numbered wave
- no change to `navigation.next_live_seed`
- no `seed_index` promotion yet
- no owner-repo writeback from `Dionysus`
- no treating `aoa-kag` or `aoa-routing` as sovereign meaning
- no treating runtime-reference docs as ecosystem law
- no immediate downstream implementation based only on frozen snapshot parity

## Final rule

Preserve this pack because it names a useful thin RAG ingest spine across
public AoA and ToS surfaces.

But keep the chain explicit:

- owner source surfaces remain stronger than the package
- derived KAG and routing stay subordinate
- runtime reference stays reference-only until one later consumer proves the
  landing
