# KAG Federation Frontier Seed Pack

Date: 2026-03-24  
Status: archived canonical seed pack

This pack preserves the lineage of a small KAG federation frontier built from two raw dialogue files:

- `seed_small_kag1.md`
- `seed_small_kag2.md`

Those raw files remain the lineage sources in this folder.
They are not treated as the authoritative home of the landed doctrine.

## Purpose

This pack exists to preserve how the raw material was normalized into a small set of clean seed lines for the first KAG planting frontier:

- `aoa-kag`
- `aoa-routing`
- `Tree-of-Sophia`

That frontier is no longer a pre-registry working folder.
Its three primary lines have already landed in their owning repositories, so the pack now stays here as archived lineage and replay material.

## What is here

- `seed_small_kag1.md`, `seed_small_kag2.md`
  - preserved raw intake and lineage surfaces
- `seed_bundle/`
  - human-readable bundle that explains the split and the current priority lines
- `seed_rootline/`
  - compact clean seeds for later planting
- `seed_witness/`
  - thematic witness seeds that preserve more of the dialogue texture
- `notes/raw_claim_map.md`
  - mapping from raw claims to their primary normalized output

## Landed outcome

### 1. Federation KAG Readiness Contract

This line landed in `aoa-kag` through:

- `docs/FEDERATION_KAG_READINESS.md`
- `schemas/federation-kag-export.schema.json`
- `examples/federation_kag_export.example.json`
- `generated/federation_spine.min.json`

Representative merged commits:

- `8093487` - first federation KAG readiness spine pilot
- `81fe86a` - ToS tiny-entry donor widened into the federation spine
- `e74b9c2` - downstream status refresh after the landing held

### 2. Federation Entry / Orientation ABI

This line landed in `aoa-routing` through:

- `docs/FEDERATION_ENTRY_ABI.md`
- `generated/federation_entrypoints.min.json`
- `generated/tiny_model_entrypoints.json`

Representative merged commits:

- `eb3c5bd` - first federation entry ABI orientation layer
- `249fbcd` - ToS tiny-entry handoff sync
- `453a4f3` - ToS-specific `kag_view` routing sync

### 3. ToS Tree-First KAG Entry Seam

This line landed in `Tree-of-Sophia` through:

- `docs/TINY_ENTRY_ROUTE.md`
- `examples/tos_tiny_entry_route.example.json`
- `docs/ZARATHUSTRA_TRILINGUAL_ENTRY.md`

Representative merged commits:

- `1946b00` - bounded trilingual Zarathustra entry opened
- `f321948` - first tree-first tiny-entry seam
- `ba523d1` - downstream tiny-entry docs refreshed after the seam landed

## Selected seed lines

### 1. Federation KAG Readiness Contract

Core move:
- source repos publish compact KAG-ready exports
- `aoa-kag` composes bounded derived surfaces from them
- KAG stays derived and reviewable rather than becoming canon

### 2. Federation Entry / Orientation ABI

Core move:
- every public object should compile to a small machine-readable entry card
- orientation must stay distinct from authority
- the smallest model should be able to reach the next true object without guessing topology

### 3. ToS Tree-First KAG Entry Seam

Core move:
- ToS keeps tree-first primary orientation
- small models get a short machine route into ToS
- KAG and routing consume that route downstream without replacing authored ToS meaning

## Archive rule

- do not rewrite the raw intake files unless lineage itself changes
- do not treat this folder as a live next seed or wave-opening surface
- do not treat this folder as the authoritative home of the landed contracts
- use `notes/raw_claim_map.md` when replaying how raw claims compressed into the three normalized seed lines
