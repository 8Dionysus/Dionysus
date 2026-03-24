seed_id: seed.aoa.agents-runtime-pack.v0
title: AoA Agents Runtime Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: seed-pack
status: landed_post_wave
priority: medium
parent_seed: null
tags:
  - runtime-seam
  - playbooks
  - memory-writeback
  - trace
  - eval-bridge
  - kag

# Seed Pack: AoA Agents Runtime Pack

## Purpose

This pack harvests bounded planting slices from `seed_agents_1st.md`.

It does not reopen the ninth wave, replace the current `next_live_seed`, or turn one donor note into a new sovereign canon.
It records small repo-owned follow-on seeds with explicit homes and explicit anti-goals.

## Provenance

- donor note: `seed_agents_1st.md`
- extraction goal: turn one strategy note into bounded repo-home seeds
- lifecycle posture: landed post-wave seed-pack retained in the registry after archive cleanup while `seed_expansion/` returns to next-live-only navigation
- planting outcome: `AOA-SEED-R1` through `AOA-SEED-R5` have landed across `aoa-agents`, `aoa-playbooks`, `aoa-memo`, `aoa-evals`, and `aoa-kag`
- next live seed unchanged: `seed.tos.wider-world-thought-expansion.v0`

## Preserved Vocabulary

- `MCP inward`
- `A2A outward`
- `role × tier`
- `route -> plan -> do -> verify -> deep? -> distill`
- `WitnessTrace`
- `inquiry_checkpoint`
- `state_capsule`
- `decision`
- `episode`
- `audit_event`
- `distillation_pack`

## Anti-Goals

- reopen the ninth wave
- replace `navigation.next_live_seed`
- turn `aoa-agents` into a hidden runtime monolith
- make vendor or framework references canonical
- collapse routing, playbooks, memo, evals, and kag into one repo

## Protocol Spine (examples only)

This pack keeps protocol references as tactical examples, not as canonical obligations.

- `MCP inward` stays a useful example for repo-owned tool and prompt servers
- `A2A outward` stays a useful example only when an agent becomes a separate service boundary
- local sub-agents remain preferable to network hops for internal composition
- Agent Card publication is a future outward-facing option, not a required public contract here
- model hierarchy and UI surfaces remain deferred until they have a clean repo home

## Reference Scenarios

Use these as reference scenarios and future example runs only:

- `AOA-P-0008 long-horizon-model-tier-orchestra`
- `AOA-P-0009 restartable-inquiry-loop`
- `AOA-P-0006 self-agent-checkpoint-rollout`
- `AOA-P-0007 witness-to-compost-pilot`

<a id="aoa-seed-r1-agents-runtime-seam"></a>
## AOA-SEED-R1 Agents Runtime Seam

### Purpose

Define a contract-first runtime seam in `aoa-agents` that binds the role axis and tier axis without adding runtime code.

### Repo Homes

- `aoa-agents`

### First Artifact Hint

- runtime seam contract note plus a public schema pack for tier artifacts

### Preserved Vocabulary

- `role × tier`
- `route -> plan -> do -> verify -> deep? -> distill`
- `route_decision`
- `bounded_plan`
- `work_result`
- `verification_result`
- `transition_decision`
- `deep_synthesis_note`
- `distillation_pack`

### Explicit Non-Goals

- `runtime/*.py`
- MCP or A2A networking
- internal router implementation
- direct memo writeback canon
- vendor-locked runtime commitments

### What Stays In Neighboring Repos

- `aoa-routing` keeps task-to-tier navigation and dispatch hints
- `aoa-playbooks` keeps scenario composition and activation meaning
- `aoa-memo` keeps memory objects and writeback doctrine
- `aoa-evals` keeps proof doctrine and verdict logic
- `abyss-stack` keeps runtime and infrastructure implementation

### Public Contract

Keep the seam small and explicit:

```text
run
= task
+ route_hint
+ playbook
+ tier_state_machine
+ role_binding
+ skill_calls
+ eval_hooks
+ memory_writeback
```

Public role-to-tier mapping for the first planting slice:

- `router + architect -> route_decision`
- `planner + architect -> bounded_plan`
- `executor + coder -> work_result`
- `verifier + reviewer -> verification_result`
- `conductor + architect/reviewer -> transition_decision`
- `deep + evaluator/architect -> deep_synthesis_note`
- `archivist + memory-keeper -> distillation_pack`

### First Planting Slice

- one human-readable contract note
- one schema pack for the seven tier artifacts
- reference scenarios only: `AOA-P-0008` and `AOA-P-0009`

<a id="aoa-seed-r2-playbooks-executable-scenarios"></a>
## AOA-SEED-R2 Playbooks as Executable Scenarios

### Purpose

Keep scenario composition in `aoa-playbooks` while making playbooks executable inputs to the future runtime seam.

### Repo Homes

- `aoa-playbooks`

### First Artifact Hint

- executable playbook contract note plus one scenario activation surface

### Preserved Vocabulary

- executable scenarios
- required skill families
- participating agents
- evaluation posture
- memory posture

### Explicit Non-Goals

- move agent identity into playbooks
- move skill execution into `aoa-agents`
- hide scenario composition inside runtime code

### What Stays In Neighboring Repos

- `aoa-agents` binds roles to tiers
- `aoa-skills` keeps bounded workflow execution
- `aoa-evals` keeps eval doctrine
- `aoa-memo` keeps durable memory capture

<a id="aoa-seed-r3-runtime-writeback-to-memo"></a>
## AOA-SEED-R3 Runtime Writeback to Memo

### Purpose

Define how a future runtime writeback layer maps run-local state into `aoa-memo` without turning runtime scratchpad into memory canon.

### Repo Homes

- `aoa-memo`

### First Artifact Hint

- runtime writeback mapping note plus checkpoint-to-memory contract

### Preserved Vocabulary

- `state_capsule`
- `decision`
- `episode`
- `audit_event`
- `claim`
- `pattern`
- `bridge`
- `inquiry_checkpoint`

### Explicit Non-Goals

- runtime scratchpad as durable memory canon
- direct freezing or promotion policy inside `aoa-agents`
- replacing memory review with silent writeback

### What Stays In Neighboring Repos

- `aoa-agents` keeps role memory posture and writeback boundaries
- `aoa-memo` keeps object meaning, lifecycle, and review rules
- `aoa-playbooks` keeps checkpoint-shaped scenario meaning

### Mapping To Preserve

- run scratchpad stays runtime-local
- checkpoint export becomes `state_capsule`
- approval and transition records become `decision`
- execution and review traces become `episode` and `audit_event`
- `distillation_pack` yields candidates for `claim`, `pattern`, and `bridge` after review

<a id="aoa-seed-r4-trace-and-eval-bridge"></a>
## AOA-SEED-R4 Trace and Eval Bridge

### Purpose

Define the bridge between runtime artifacts, witness trace, and eval surfaces so that workflow-level judgment stays inspectable.

### Repo Homes

- `aoa-evals`

### First Artifact Hint

- trace-to-eval contract note plus one artifact-to-verdict hook surface

### Preserved Vocabulary

- `WitnessTrace`
- trace grading
- eval hooks
- contract test
- verification artifact

### Explicit Non-Goals

- secret internal judge inside runtime code
- proof doctrine embedded in `aoa-agents`
- final-text-only grading without workflow evidence

### What Stays In Neighboring Repos

- `aoa-agents` keeps artifact contracts
- `aoa-playbooks` keeps scenario-level eval anchors
- `aoa-evals` keeps verdict logic, datasets, and proof bundles

<a id="aoa-seed-r5-kag-reasoning-handoff"></a>
## AOA-SEED-R5 KAG Reasoning Handoff

### Purpose

Define how a future runtime hands off retrieval and reasoning work to `aoa-kag` without letting derived substrate replace source-owned meaning.

### Repo Homes

- `aoa-kag`

### First Artifact Hint

- reasoning handoff note plus source-vs-derived retrieval guardrail surface

### Preserved Vocabulary

- reasoning substrate
- local search
- global search
- drift search
- derived surface
- provenance

### Explicit Non-Goals

- routing ownership inside `aoa-kag`
- direct canon authorship from derived retrieval
- implicit AoA and ToS collapse

### What Stays In Neighboring Repos

- `aoa-agents` keeps role and tier contracts
- `aoa-routing` keeps navigation
- `aoa-memo` keeps memory canon
- `Tree-of-Sophia` keeps source-authored meaning

## Deferred Notes

The core `R1` through `R5` slices are landed.
The donor note also names useful but not yet cleanly owned follow-ons.
Keep them deferred here until a later planting opens a better home:

- UI surfaces for memory timeline, playbook editing, knowledge map, and task dashboard
- model hierarchy guidance tied to specific model families or vendors
- network-facing protocol bindings beyond contract-level notes
- remote Agent Card publication
