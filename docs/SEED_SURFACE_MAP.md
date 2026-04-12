# Dionysus Seed Surface Map

## Purpose

This note explains where seed surfaces live now and which ones actually control
current reading order.

The main cleanup rule is simple:

- root now stays mostly for canonical navigation and live lifecycle surfaces
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

Within `archive/`, treat `archive/seed_pack_exports/` as derived ingress and
transport only, not as canonical seed meaning.

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
- `seed_federated_audit_remediation_pack.md` is now a landed cross-repo remediation lineage surface and must not be mistaken for owner-repo sovereignty; use its linked ledger and reality canary when replaying or rechecking the owner-repo state

### `seed_staging/future/`

- future bounded candidate packs and prep packs
- mostly real staging soil, but some packs may later be retained here for
  lineage after upstream landing
- `seed_aoa_session_harvest_family_pack.md` now records a landed upstream
  family-growth rollout for post-session AoA project-growth skills around
  `aoa-session-donor-harvest`
- `seed_aoa_automation_opportunity_scan_pack.md` is a newer staged add-on pack
  for automation-readiness detection around the live session-harvest family and
  the existing playbook automation-seed posture
- `seed_aoa_growth_refinery_docket_pack.md` is now landed upstream and retained
  for lineage as the route-order record for the post-Codex internal lineage
  chain `cluster_ref -> candidate_ref -> seed_ref -> object_ref`
- `seed_aoa_growth_refinery_contract_seed_pack.md` is now landed upstream and
  retained for lineage as the contract companion to that docket pack: it
  preserves the v1 contract substrate, acceptance gates, examples, and tiny
  structural validator posture without replacing owner-repo truth
- `seed_aoa_first_wave_candidate_lineage_pack.md` is now landed upstream and
  retained for lineage as the first-wave hardening record for the aligned
  `cluster_ref -> candidate_ref -> seed_ref` example chain, center validator,
  and closed schema/example/doc seams
- `seed_aoa_remaining_seeds_execution_pack.md` is now landed upstream and
  retained for lineage as the follow-through capsule whose selected new owner
  slice was the `aoa-evals` `aoa-diagnosis-cause-discipline` bundle; Wave D
  automation remains deferred
- `seed_aoa_wave2_refinery_convergence_pack.md` is a newly staged future pack
  for the downstream Growth Refinery convergence layer across `aoa-stats`,
  `aoa-evals`, `aoa-playbooks`, and `aoa-memo`; use it to harden existing
  repo-owned surfaces and add one shared validator without widening authority
- `seed_aoa_wave3_owner_landing_followthrough_pack.md` is now landed upstream
  and retained for lineage as the post-candidate owner-followthrough and
  pruning layer across `Agents-of-Abyss`, `aoa-sdk`, `aoa-skills`,
  `Dionysus`, `aoa-stats`, `aoa-playbooks`, and `aoa-memo`
- `seed_aoa_wave4_kernel_automation_pack.md` is a newly staged future pack
  for one governed session-growth kernel cycle across `aoa-sdk`,
  `aoa-skills`, `aoa-playbooks`, and `aoa-stats`; keep it
  recommendation-only, review-gated, and derived-only, with no scheduler
  authority or silent-mutation drift
- `seed_aoa_wave5_portability_regeneration_pack.md` is a newly staged future
  pack for source-owned Codex-plane portability and regeneration across
  `8Dionysus`, `aoa-sdk`, and the shared-root `.codex` projection seam; use
  it to move path-bound deploy surfaces onto manifest-driven regeneration
  while preserving stable MCP names, owner boundaries, and explicit rejection
  of bundled `__pycache__` transport noise
- `seed_aoa_wave7_trusted_rollout_ops_pack.md` is a newly staged future pack
  for trusted shared-root Codex rollout operations across `8Dionysus`,
  `aoa-stats`, `aoa-playbooks`, `aoa-memo`, and `aoa-sdk`; use it to keep
  rollout campaigns, drift windows, rollback windows, derived summaries, and
  bounded recall reviewable while preserving `8Dionysus` rollout authority and
  rebinding landed examples to the current local date
- `seed_aoa_codex_surface_plane_pack.md` is now a partially landed lineage
  pack for the Codex access plane: the workspace-level `aoa_workspace` MCP is
  live through `aoa-sdk` and `/srv/.codex`, the repo-local `aoa_stats` MCP is
  now live through `aoa-stats` and `/srv/.codex`, the repo-local `dionysus`
  MCP is now live through `Dionysus` and `/srv/.codex`, and the first
  skill-to-MCP wiring slice is now live through `aoa-skills` plus workspace
  route-discipline guidance, the first `aoa-agents` subagent projection is now
  live through `aoa-agents` plus `/srv/.codex/agents/`, the first launcher
  plugin slice is now live through `/srv/.codex/plugins/` plus
  `/srv/.agents/plugins/marketplace.json`, the first convergence slice is now
  live through `/srv/.codex/tools/`, `/srv/.codex/scripts/`,
  `/srv/.codex/bin/`, and `/srv/.codex/generated/codex/`, and the first
  hooked-doctor slice is now live through
  `/srv/.codex/tools/aoa_codex_hooks/`,
  `/srv/.codex/scripts/aoa_codex_hooks_doctor.py`, `/srv/.codex/hooks/`, and
  `/srv/.codex/generated/codex/hooks/`, while the wider lineage route remains
  deferred
- `seed_aoa_rag_skeleton_pack.md` is now a partially landed lineage pack for a
  thin RAG spine across public AoA and ToS owner surfaces; the first
  `abyss-stack` consumer slice is live, while owner-surface regrounding and
  runtime-reference revalidation remain explicit follow-through
- `seed_tos_graph_curation_pack.md` is now a partially landed lineage pack for
  the first route-first ToS graph helper slice in `abyss-stack`, while
  validator-gated writeback and any later `Tree-of-Sophia` repo-local
  hardening remain deferred
- `seed_aoa_stats_telemetry_pack.md` is now a partially landed lineage pack for
  the first owner-local receipt wave across `aoa-skills` and `aoa-evals`,
  while later derived stats layers remain deferred

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
- `seed_staging/future/seed_aoa_session_harvest_family_pack.md`
- `seed_staging/audit/seed_federated_audit_remediation_pack.md`
- `seed_staging/future/seed_aoa_growth_refinery_docket_pack.md`
- `seed_staging/future/seed_aoa_growth_refinery_contract_seed_pack.md`
- `seed_staging/future/seed_aoa_first_wave_candidate_lineage_pack.md`
- `seed_staging/future/seed_aoa_remaining_seeds_execution_pack.md`
- `seed_staging/future/seed_aoa_wave3_owner_landing_followthrough_pack.md`

### `partially_landed_retained_for_lineage`

- `seed_staging/questbook/seed_questbook_seedgarden_profile_pack.md`
- `seed_staging/future/seed_aoa_stats_telemetry_pack.md`
- `seed_staging/future/seed_aoa_codex_surface_plane_pack.md`
- `seed_staging/future/seed_tos_graph_curation_pack.md`
- `seed_staging/future/seed_aoa_rag_skeleton_pack.md`

Reading:

- the `Dionysus` slice landed
- the `8Dionysus` slice remains deferred
- the first owner-local telemetry receipt wave landed, but the derived stats
  adjunct remains deferred
- the workspace-level `aoa_workspace` MCP, project-level `/srv/.codex` glue,
  the repo-local `aoa_stats` and `dionysus` MCPs, and the first `aoa-skills`
  skill-to-MCP wiring slice landed, the first `aoa-agents` subagent
  projection plus `/srv/.codex/agents/` install seam landed, the first
  launcher plugin slice landed through `/srv/.codex/plugins/` and
  `/srv/.agents/plugins/marketplace.json`, the first convergence slice landed
  through workspace-local `.codex` tooling and reports, the first hooked-doctor
  slice landed through workspace-local `.codex` tooling, hooks, and reports,
  while wider lineage follow-through remains deferred
- the first owner-local ToS graph curation slice landed in `abyss-stack`, but
  validator-gated writeback and any repo-local `Tree-of-Sophia` hardening
  remain deferred
- the first owner-local thin-RAG advisory consumer slice landed in
  `abyss-stack`, but owner-surface regrounding for drifted `aoa-kag` /
  `aoa-memo` / `aoa-routing` snapshot files and `ATM10-Agent`
  runtime-reference revalidation remain deferred
- the federated audit remediation pack is now fully landed upstream and
  retained only for lineage, replay, and owner-repo reality checks
- the growth-refinery docket and contract companion packs are now landed
  upstream across `Agents-of-Abyss`, `aoa-sdk`, `aoa-skills`, `Dionysus`,
  `aoa-stats`, `aoa-evals`, `aoa-playbooks`, and `aoa-memo`; keep them as
  rollout-order, proving-chain, and acceptance-gate lineage only
- the first-wave candidate-lineage pack is now landed lineage hardening:
  the live example chain is aligned across `aoa-sdk`, `aoa-skills`, and
  `Dionysus`, the center validator lives in `Agents-of-Abyss`, and the named
  schema/doc seams are closed
- the remaining-seeds execution pack is now landed follow-through lineage:
  already-landed Growth Refinery stats/playbook/memo surfaces stayed
  untouched, `aoa-evals` owns the `aoa-diagnosis-cause-discipline` proof
  bundle, and Wave D automation remains deferred
- the wave3 owner-followthrough pack is now landed upstream lineage: owner
  landing doctrine lives in `Agents-of-Abyss`, reviewed follow-through carry
  lives in `aoa-sdk`, owner-status surfaces live in `aoa-skills`, seed trace
  lives in `Dionysus`, derived pruning summaries live in `aoa-stats`, the
  narrower campaign route lives in `aoa-playbooks`, and bounded prune
  writeback lives in `aoa-memo`

### `staged_only_not_landed`

- `seed_staging/audit/seed_wave3_codex_repo_local_skills_trace_harness.md`
- `seed_staging/future/seed_architecture_fit_pack.md`
- `seed_staging/future/seed_dialogue_memory_pack.md`
- `seed_staging/future/seed_federation_conductor_pack.md`
- `seed_staging/future/seed_memory_evals_skills_docs_pack.md`
- `seed_staging/future/seed_future_agent_systems_prep_pack.md`
- `seed_staging/future/seed_aoa_automation_opportunity_scan_pack.md`
- `seed_staging/future/seed_aoa_wave2_refinery_convergence_pack.md`
- `seed_staging/future/seed_aoa_wave4_kernel_automation_pack.md`
- `seed_staging/future/seed_aoa_wave5_portability_regeneration_pack.md`
- `seed_staging/future/seed_aoa_wave7_trusted_rollout_ops_pack.md`

### `donor_only_not_planted`

- `seed_staging/donor/seed_clawrouter_donor_graft.md`
- `seed_staging/donor/seed_aoa_session_donor_harvest.md`

## Audit Wave Sync

As of `2026-04-05` UTC owner-repo state:

- `seed_wave1_codex_audit_spine.md` is landed upstream through merged audit surfaces in `Agents-of-Abyss`, `ATM10-Agent`, and `abyss-stack`
- `seed_wave2_codex_skill_proof_audit_bridge.md` is landed upstream through merged audit surfaces in `Agents-of-Abyss`, `aoa-skills`, and `aoa-evals`
- `seed_wave3_codex_repo_local_skills_trace_harness.md` remains unlanded and should not be inferred from wave 1 and wave 2 being done
- `seed_federated_audit_remediation_pack.md` is now fully landed through Wave 0 / Wave 1 lie-removal slices, the Wave 2 canary mesh, the landed Wave 3 `WS03` / `WS04` / `WS07` / `WS11` slices, and the GitHub-only `WS12` endcap in `ATM10-Agent`; it should now be read as lineage and replay context rather than as an active queue surface

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
