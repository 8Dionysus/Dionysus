# AoA First Wave Candidate Lineage Pack Summary

## Purpose

This derived transport bundle preserves the first-wave Growth Refinery
hardening packet as one replayable lineage surface inside `Dionysus`.

It is transport and staging only. It does not replace live owner-repo truth.

## Bundle

- bundle: `archive/seed_pack_exports/aoa-first-wave-candidate-lineage-pack-2026-04-11.zip`
- assembled_at: `2026-04-11`
- assembly_root: `/home/dionysus/Загрузки`

## Source files copied into the bundle

- `aoa_first_wave_candidate_lineage_pack/README.md`
- `aoa_first_wave_candidate_lineage_pack/LIVE_STATE_ALIGNMENT.md`
- `aoa_first_wave_candidate_lineage_pack/contracts/candidate_lineage_contract_v1.md`
- `aoa_first_wave_candidate_lineage_pack/CODEX_EXECUTION_PROMPT.md`
- `aoa_first_wave_candidate_lineage_pack/PR_SLICES.md`
- `aoa_first_wave_candidate_lineage_pack/ACCEPTANCE_MATRIX.md`
- `aoa_first_wave_candidate_lineage_pack/proposed-targets/*`

## Working reading

- `README.md` names this pack as first-wave hardening, not greenfield work.
- `LIVE_STATE_ALIGNMENT.md` lists already-live surfaces that must not be
  duplicated blindly.
- `contracts/candidate_lineage_contract_v1.md` preserves the shared
  `cluster_ref -> candidate_ref -> seed_ref` seam.
- `proposed-targets/` is an adaptation guide only.

## Current workspace reality at capture time

As of `2026-04-11`:

- the Growth Refinery docket and contract companion packs are already landed
  upstream as owner-repo surfaces
- `Agents-of-Abyss`, `aoa-sdk`, `aoa-skills`, and `Dionysus` already carry
  first-wave lineage surfaces
- the remaining first-wave work is hardening: align one live example chain,
  add a cross-repo validator, and close small schema/example/doc seams
- the pack must not create a second candidate identity authority or duplicate
  doctrine docs that are already honest

## Adaptation rules to preserve

- keep the live chain internally consistent across `aoa-sdk`, `aoa-skills`,
  and `Dionysus`
- keep `aoa-sdk` provisional: it may mint `cluster_ref`, not
  `candidate_ref`, `seed_ref`, or `object_ref`
- keep `aoa-skills` as the reviewed `candidate_ref` minting owner
- keep `Dionysus` as the only `seed_ref` minting owner
- keep `object_ref` absent until owner planting exists
- prefer minimal patches over duplicate surfaces

## Recommended planting order

1. `Agents-of-Abyss` cross-repo validator
2. `aoa-sdk` closeout candidate lineage map and example alignment
3. `aoa-skills` candidate-ref bridge note and receipt-schema hardening
4. `Dionysus` seed-lineage example alignment
5. cross-repo validator pass

## Lineage center

Keep this bundle as hardening evidence for:

`cluster_ref -> candidate_ref -> seed_ref`
