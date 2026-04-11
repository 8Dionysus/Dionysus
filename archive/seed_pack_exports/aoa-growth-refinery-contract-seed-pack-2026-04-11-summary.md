# AoA Growth Refinery Contract Seed Pack Summary

## Purpose

This derived transport bundle preserves the contract companion for the
growth-refinery route inside `Dionysus`.

It is staging and contract substrate only. It does not become owner-repo truth
and it does not replace the higher-level growth-refinery docket.

## Bundle

- bundle: `archive/seed_pack_exports/aoa-growth-refinery-contract-seed-pack-2026-04-11.zip`
- assembled_at: `2026-04-11`
- assembly_root: `/home/dionysus/Загрузки`

## Source files copied into the bundle

- `aoa_growth_refinery_contract_seed_pack/README.md`
- `aoa_growth_refinery_contract_seed_pack/WHY_NOW.md`
- `aoa_growth_refinery_contract_seed_pack/TARGET_MAP.md`
- `aoa_growth_refinery_contract_seed_pack/ACCEPTANCE_MATRIX.md`
- `aoa_growth_refinery_contract_seed_pack/CODEX_EXECUTION_PROMPT.md`
- `aoa_growth_refinery_contract_seed_pack/CODEX_REVIEW_PROMPT.md`
- `aoa_growth_refinery_contract_seed_pack/REVIEW_CHECKLIST.md`
- `aoa_growth_refinery_contract_seed_pack/contracts/candidate_lineage_contract_v1.md`
- `aoa_growth_refinery_contract_seed_pack/contracts/growth_funnel_contract_v1.md`
- `aoa_growth_refinery_contract_seed_pack/contracts/memory_writeback_contract_v1.md`
- `aoa_growth_refinery_contract_seed_pack/examples/lineage_bundle_v1/*`
- `aoa_growth_refinery_contract_seed_pack/proposed-targets/*`
- `aoa_growth_refinery_contract_seed_pack/tools/validate_lineage_examples.py`

## Working reading

- `README.md` names the contract pack as the companion to the growth-refinery
  docket, not a replacement for it
- `WHY_NOW.md` names the missing narrow lineage seam
- `TARGET_MAP.md` gives the repo-by-repo destination map
- `ACCEPTANCE_MATRIX.md` names merge gates for each owner slice
- `contracts/*.md` state the v1 chain, funnel, and memory writeback contracts
- `examples/lineage_bundle_v1/*` and `tools/validate_lineage_examples.py`
  provide a tiny structural example and validator

## Current workspace reality at capture time

As of `2026-04-11`:

- the growth-refinery docket is already staged in `Dionysus`
- the wider owner-layer route for
  `cluster_ref -> candidate_ref -> seed_ref -> object_ref` is not landed yet
- `aoa-sdk` already carries checkpoint and closeout surfaces, but no explicit
  `candidate_ref` or `seed_ref` contract exists yet
- `aoa-skills` already owns reviewed donor harvest, but no explicit
  reviewed-candidate identity contract exists yet
- `Dionysus` already owns seed staging, but no explicit candidate-to-seed
  bridge exists yet
- `aoa-stats`, `aoa-evals`, `aoa-playbooks`, and `aoa-memo` already have the
  neighboring layer posture needed for later slices, but not the
  growth-refinery-specific contract surfaces yet

## Adaptation rules to preserve

- treat this pack as the contract companion to the staged docket pack
- let the docket pack keep route order, stop-lines, and owner sequence
- let this pack provide v1 contract text, examples, acceptance gates, and the
  tiny structural validator
- adapt file placement to live repo conventions instead of copying the
  `proposed-targets/` tree unchanged
- keep `aoa-routing` and `aoa-kag` derivative
- keep stats derived-only, evals proof-only, playbooks scenario-only, and memo
  memory-only

## Recommended planting order

1. `Agents-of-Abyss`
2. `aoa-sdk`
3. `aoa-skills`
4. `Dionysus`
5. `aoa-stats`
6. `aoa-evals`
7. `aoa-playbooks`
8. `aoa-memo`

## Lineage companion

Keep this contract bundle paired with the staged docket route:

`cluster_ref -> candidate_ref -> seed_ref -> object_ref`
