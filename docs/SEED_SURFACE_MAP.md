# Dionysus Seed Surface Map

## Purpose

This note explains where seed surfaces live now and which ones actually control
current reading order.

The main cleanup rule is simple:

- root now stays mostly for canonical navigation and live control surfaces
- structured transport and staging packs live under `seed_staging/`
- informal exploratory seed texts live under `seed_notes/exploratory/`

## Read Order

When you need real planting truth, read in this order:

1. relevant `*_wave.manifest.json`
2. exact source seed named by that manifest
3. matching closure note for that wave when present
4. `seed-registry.yaml`
5. `seed_expansion/`
6. owner repository state
7. the relevant note under `seed_staging/`

Do not infer current owner-repo planting state from a staging note alone.

## Root

Root is now reserved for the strongest navigation and lifecycle surfaces:

- `seed-registry.yaml`
- `seed_expansion/`
- `*_wave.manifest.json`
- `ninth_wave.closure.md`
- `README.md`
- `QUESTBOOK.md`
- `archive/`
- `docs/codex/planting-protocol.md`

Use root when the question is:

- what is live
- what is gated
- what is archived
- what controls read order

## `seed_staging/`

Structured transport notes now live here.
They carry:

- `lifecycle_status`
- `lifecycle_note`
- `reality_checked_at`

Read those markers first, then verify the owner repos directly.

### `seed_staging/questbook/`

- upstream-landed lineage packs for `foundation`, `source-proof`, and `boundary-runtime`
- one partially landed pack for `seedgarden-profile`

### `seed_staging/rpg/`

- upstream-landed lineage packs for the whole current RPG line
- keep these as replay and transport, not as active queue control

### `seed_staging/root_docs/`

- replayable root-docs refresh packs
- already landed upstream, retained for lineage

### `seed_staging/audit/`

- `seed_wave1_codex_audit_spine.md` and `seed_wave2_codex_skill_proof_audit_bridge.md` are now landed upstream and retained here for lineage
- `seed_wave3_codex_repo_local_skills_trace_harness.md` remains true staging
- `seed_federated_audit_remediation_pack.md` is a newer staged-only cross-repo remediation transport surface and must not be mistaken for owner-repo truth

### `seed_staging/future/`

- future bounded candidate packs and prep packs
- still real staging soil, not planted owner-repo truth

### `seed_staging/donor/`

- donor extraction surfaces only
- bounded transplant planning, not landed rollout

## `seed_notes/exploratory/`

These are informal exploratory seed texts.
They may be fertile, but they are not queue control surfaces.

Current exploratory notes live under:

- `seed_notes/exploratory/seed_agents_1st.md`
- `seed_notes/exploratory/seed_donors_inside.md`
- `seed_notes/exploratory/seed_expat.md`
- `seed_notes/exploratory/seed_self-agent.md`
- `seed_notes/exploratory/seed_trio.md`

## Verified Layout

### `landed_upstream_retained_for_lineage`

- `seed_staging/root_docs/seed_wave1_root_docs_refresh.md`
- `seed_staging/root_docs/seed_wave2_root_docs_refresh.md`
- `seed_staging/root_docs/seed_wave3_root_docs_refresh.md`
- `seed_staging/audit/seed_wave1_codex_audit_spine.md`
- `seed_staging/audit/seed_wave2_codex_skill_proof_audit_bridge.md`
- `seed_staging/questbook/seed_questbook_foundation_pack.md`
- `seed_staging/questbook/seed_questbook_source_proof_pack.md`
- `seed_staging/questbook/seed_questbook_boundary_runtime_pack.md`
- `seed_staging/rpg/seed_rpg_first_wave_pack.md`
- `seed_staging/rpg/seed_rpg_second_wave_pack.md`
- `seed_staging/rpg/seed_rpg_architecture_rfc_pack.md`
- `seed_staging/rpg/seed_rpg_bridge_wave_pack.md`
- `seed_staging/rpg/seed_rpg_sdk_addendum_pack.md`
- `seed_staging/rpg/seed_rpg_runtime_projection_pack.md`

### `partially_landed_retained_for_lineage`

- `seed_staging/questbook/seed_questbook_seedgarden_profile_pack.md`

Reading:

- the `Dionysus` slice landed
- the `8Dionysus` slice remains deferred

### `staged_only_not_landed`

- `seed_staging/audit/seed_wave3_codex_repo_local_skills_trace_harness.md`
- `seed_staging/audit/seed_federated_audit_remediation_pack.md`
- `seed_staging/future/seed_architecture_fit_pack.md`
- `seed_staging/future/seed_dialogue_memory_pack.md`
- `seed_staging/future/seed_federation_conductor_pack.md`
- `seed_staging/future/seed_memory_evals_skills_docs_pack.md`
- `seed_staging/future/seed_future_agent_systems_prep_pack.md`

### `donor_only_not_planted`

- `seed_staging/donor/seed_clawrouter_donor_graft.md`
- `seed_staging/donor/seed_aoa_session_donor_harvest.md`

## Audit Wave Sync

As of `2026-04-05` UTC owner-repo state:

- `seed_wave1_codex_audit_spine.md` is landed upstream through merged audit surfaces in `Agents-of-Abyss`, `ATM10-Agent`, and `abyss-stack`
- `seed_wave2_codex_skill_proof_audit_bridge.md` is landed upstream through merged audit surfaces in `Agents-of-Abyss`, `aoa-skills`, and `aoa-evals`
- `seed_wave3_codex_repo_local_skills_trace_harness.md` remains unlanded and should not be inferred from wave 1 and wave 2 being done
- `seed_federated_audit_remediation_pack.md` is newly staged and still needs owner-repo reality checks before any downstream application order is trusted

## Practical Rule

When you open a file under `seed_staging/` or `seed_notes/`, classify it
before doing anything else:

1. lineage-only staging pack
2. partially landed staging pack
3. staged-only future pack
4. donor extraction note
5. exploratory note

If it is not a canonical root surface, verify the owner repo before deciding
whether the project still needs that seed now.
