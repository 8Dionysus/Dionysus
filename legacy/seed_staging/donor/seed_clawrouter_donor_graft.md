seed_id: seed.clawrouter.donor-graft.v0
title: ClawRouter Donor Graft for AoA Runtime Surfaces
profile_anchor: 8Dionysus
projects:
  - AoA
kind: donor-note
lifecycle_status: donor_only_not_planted
lifecycle_note: Donor extraction note only; no bounded owner-repo planting is verified yet.
reality_checked_at: '2026-04-04'
status: pending_archive
priority: medium
parent_seed: null
tags:
  - donor
  - gateway
  - cache
  - session
  - budget
  - fallback
  - compression
  - selector

# Seed Note: ClawRouter Donor Graft

## Purpose

Harvest bounded donor internals from `BlockRunAI/ClawRouter` and translate them into Dionysus-ready seeds for later planting across `abyss-stack`, `ATM10-Agent`, `aoa-evals`, `aoa-playbooks`, `aoa-agents`, and, only at the edge, `aoa-routing`.

This note does not open a new wave, replace the current `navigation.next_live_seed`, or make Dionysus the runtime home of ClawRouter-shaped code.
It exists to keep donor extraction bounded, inspectable, and transplant-focused.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
It stores seed sources, wave manifests, archived planting surfaces, and the minimal protocol needed to move seeds into owning repositories.

This donor note belongs here because:

- the donor logic spans multiple repo homes
- no single target repo should own the extraction plan before the first plantings exist
- the current `next_live_seed` should remain untouched
- the donor needs explicit boundaries before code is transplanted

## Grounding posture

Read this note under these ownership boundaries:

- `abyss-stack` owns gateway/runtime body, context-budget enforcement, and local floor posture
- `ATM10-Agent` owns the local-first operator-facing companion surface and run artifacts
- `aoa-evals` owns proof surfaces, regression bundles, and artifact-to-verdict seams
- `aoa-playbooks` owns scenario composition, named fallback posture, and activation meaning
- `aoa-agents` owns role contracts, tier doctrine, and runtime seam meaning
- `aoa-routing` owns navigation and dispatch hints, not runtime selector authorship
- `aoa-techniques` is the later public home for generalized reusable patterns after evidence exists

## Donor harvest scope

### Take

- request deduplication
- response cache
- session pinning
- ephemeral work journal
- spend control
- usage aggregation
- capability filters
- fallback posture
- layered context compression
- selector microkernel patterns

### Do not take

- wallet / x402 / payment shell
- vendor or provider commitments as canon
- doctor surfaces that require external paid AI analysis
- ClawRouter tier vocabulary as AoA doctrine
- remote free-tier dependence as the canonical floor
- donor codebooks trained on someone else's logs as a default local truth

## Preserved vocabulary

- request deduplication
- response cache
- cache key normalization
- inflight
- session persistence
- session journal
- spend control
- graceful degrade
- strict stop
- capability filters
- context-length-aware routing
- structured output minimum tier
- selector microkernel
- local floor

## Anti-goals

- reopen any closed wave
- replace `navigation.next_live_seed`
- turn Dionysus into a runtime repo
- move routing authorship into `aoa-routing`
- turn ephemeral journal into `aoa-memo` canon
- compress authored or source-linked canon surfaces
- import wallet/payment shell into AoA canon
- smuggle vendor-first design into repo-owned meaning

## Extraction order

Plant in this order unless a target repo forces a smaller dependency-first move:

1. `AOA-SEED-CR1` Gateway Dedup and Response Cache Lane
2. `AOA-SEED-CR3` Budget Governor, Usage Spine, and Local Ops Doctor Split
3. `AOA-SEED-CR2` Session Continuity and Ephemeral Work Journal
4. `AOA-SEED-CR4` Capability Filters and Fallback Modes
5. `AOA-SEED-CR5` Context Compression Preprocessor
6. `AOA-SEED-CR6` Runtime Selector Microkernel
7. `AOA-SEED-CR7` Technique Promotion Surface (later only)

The order prefers runtime hygiene before runtime cleverness.

---

<a id="aoa-seed-cr1-gateway-dedup-and-response-cache-lane"></a>
## AOA-SEED-CR1 Gateway Dedup and Response Cache Lane

### Purpose

Make the gateway layer reentrant, cost-aware, and retry-safe through bounded request deduplication and normalized response caching.

### Donor surfaces

- `src/dedup.ts`
- `src/response-cache.ts`
- `docs/features.md#response-cache`

### Repo homes

- `abyss-stack`
- `ATM10-Agent`

### First artifact hint

- gateway cache contract note
- cache status schema or example artifact
- minimal validator or test stub for cache-key and dedup behavior

### Preserved vocabulary

- request deduplication
- inflight
- completed TTL
- cache key normalization
- no-cache
- hit rate
- eviction

### Explicit non-goals

- make cache the owner of truth
- move routing authorship into the gateway note
- silently mutate request semantics beyond normalization rules
- bind the contract to one vendor or proxy brand

### What stays in neighboring repos

- `aoa-routing` keeps navigation and task-to-tier hints
- `aoa-evals` later judges cache efficacy and regression
- `abyss-stack` remains the likely primary runtime owner
- `ATM10-Agent` may consume the same lane for local operator runs

### Suggested first planting slice

- one human-readable gateway cache note
- one structural artifact such as `gateway_cache_status.example.json` or a small schema
- one explicit validation note for:
  - timestamp stripping
  - key normalization
  - inflight replay behavior
  - `Cache-Control: no-cache` bypass

### Boundary note

This seed should land below route meaning.
It improves gateway metabolism, not AoA doctrine.

---

<a id="aoa-seed-cr2-session-continuity-and-ephemeral-work-journal"></a>
## AOA-SEED-CR2 Session Continuity and Ephemeral Work Journal

### Purpose

Keep multi-turn work stable through session pinning and capture compact run-local action traces without turning scratchpad into durable memory canon.

### Donor surfaces

- `src/session.ts`
- `src/journal.ts`
- `docs/features.md#session-persistence`

### Repo homes

- `ATM10-Agent`
- `aoa-memo`
- `aoa-agents`

### First artifact hint

- session continuity contract note
- `session_run_journal` schema or example artifact
- memo bridge note that states what can be proposed for writeback and what cannot

### Preserved vocabulary

- session persistence
- pinned model
- `x-session-id`
- derived session ID
- request fingerprint
- three-strike escalation
- session journal
- key actions

### Explicit non-goals

- durable memory canon by default
- silent promotion of scratchpad to memory object
- replacing memo review with regex extraction
- forcing `aoa-agents` to own operator-facing runtime logs

### What stays in neighboring repos

- `aoa-memo` keeps durable memory object meaning and review law
- `aoa-agents` keeps runtime seam meaning, not log storage
- `ATM10-Agent` is the most natural early home for run-local continuity artifacts

### Suggested first planting slice

- one session continuity note in `ATM10-Agent`
- one structural artifact such as `session_run_journal.example.json`
- one memo bridge note that marks journal entries as:
  - ephemeral
  - candidate-only
  - review-required before durable writeback

### Boundary note

Journal extraction is useful because it is light.
It is dangerous for the same reason.
Keep it explicitly weaker than memory canon.

---

<a id="aoa-seed-cr3-budget-governor-usage-spine-and-local-ops-doctor-split"></a>
## AOA-SEED-CR3 Budget Governor, Usage Spine, and Local Ops Doctor Split

### Purpose

Introduce explicit spend windows, status snapshots, savings surfaces, and local diagnostics without importing donor payment or vendor-analysis obligations.

### Donor surfaces

- `src/spend-control.ts`
- `src/stats.ts`
- `docs/configuration.md#routing-configuration`
- `docs/features.md#cost-tracking-with-stats`
- `src/doctor.ts` as a split source only

### Repo homes

- `abyss-stack`
- `ATM10-Agent`
- `aoa-evals`

### First artifact hint

- budget governor contract note
- usage snapshot schema or example artifact
- local ops-doctor checklist or machine-readable health example

### Preserved vocabulary

- per-request
- hourly
- daily
- session
- graceful degrade
- strict stop
- reset window
- baseline cost
- savings
- daily breakdown

### Explicit non-goals

- wallet or x402 commitments
- secret-bearing payment state in canon
- external AI analysis as a required doctor path
- treating spend data as proof of task quality

### What stays in neighboring repos

- `abyss-stack` enforces runtime budget posture
- `ATM10-Agent` can show the operator live budget and savings state
- `aoa-evals` can consume usage snapshots as evidence, not as doctrine
- any future payment rail remains a separate decision, not part of this seed

### Suggested first planting slice

- one budget contract note
- one structural artifact such as `usage_snapshot.schema.json` or `usage_snapshot.example.json`
- one local doctor note limited to:
  - gateway reachability
  - log presence
  - basic config health
  - local floor availability

### Boundary note

Split the doctor.
Keep local observability.
Do not import donor vendor-analysis dependency.

---

<a id="aoa-seed-cr4-capability-filters-and-fallback-modes"></a>
## AOA-SEED-CR4 Capability Filters and Fallback Modes

### Purpose

Make model and provider choice inspectable through capability filters and named fallback modes that can be shared between runtime and scenario layers.

### Donor surfaces

- `docs/features.md#tool-detection`
- `docs/features.md#context-length-aware-routing`
- `docs/features.md#free-tier-fallback`
- `src/router/strategy.ts`
- `docs/configuration.md#routing-configuration`

### Repo homes

- `abyss-stack`
- `aoa-playbooks`
- `aoa-routing`

### First artifact hint

- fallback-mode contract note
- capability-manifest stub or example artifact
- route-decision envelope example for downstream readers

### Preserved vocabulary

- tool-aware routing
- context-length-aware routing
- structured output minimum tier
- fallback chain
- graceful degrade
- strict stop
- local floor

### Explicit non-goals

- move scenario meaning into runtime code
- make `aoa-routing` the selector owner
- treat remote free tiers as canon
- let capability filters redefine AoA role or tier doctrine

### What stays in neighboring repos

- `aoa-playbooks` keeps named fallback posture and scenario meaning
- `aoa-routing` may expose small route-decision envelopes only
- `abyss-stack` owns enforcement details and local floor translation

### Suggested first planting slice

- one fallback-mode note in `aoa-playbooks`
- one capability-manifest example or schema in `abyss-stack`
- one tiny route-decision envelope example for `aoa-routing` consumption only

### Boundary note

Translate donor `free fallback` into an AoA local floor where possible.
In this ecosystem the floor should prefer `ollama` or another local route before a remote free dependency becomes doctrine.

---

<a id="aoa-seed-cr5-context-compression-preprocessor"></a>
## AOA-SEED-CR5 Context Compression Preprocessor

### Purpose

Add bounded pre-send compression for large transient contexts and tool transcripts before context budgets are escalated.

### Donor surfaces

- `src/compression/index.ts`
- `docs/features.md`
- `abyss-stack` context budget posture as the receiving boundary

### Repo homes

- `abyss-stack`
- `ATM10-Agent`
- `aoa-techniques` (later, only after evidence)

### First artifact hint

- compression policy note
- compression-profile config stub
- one example artifact that shows before/after on a transient trace

### Preserved vocabulary

- deduplication
- whitespace normalization
- dictionary encoding
- path shortening
- JSON compaction
- observation compression
- dynamic codebook

### Explicit non-goals

- compress source-authored canon
- compress durable memory objects by default
- import donor codebooks trained on foreign logs
- hide provenance loss behind “token savings”

### What stays in neighboring repos

- `abyss-stack` keeps the class-based context budget policy
- `ATM10-Agent` may apply compression to large transient run traces
- `aoa-techniques` is the later promotion home if the pattern becomes portable and reviewable

### Suggested first planting slice

- one compression policy note
- one config stub with all layers explicit and default-safe
- one worked example restricted to:
  - tool output transcripts
  - large transient observations
  - non-canonical runtime traces

### Boundary note

Compression is for transport discipline, not for rewriting authored meaning.

---

<a id="aoa-seed-cr6-runtime-selector-microkernel"></a>
## AOA-SEED-CR6 Runtime Selector Microkernel

### Purpose

Isolate low-level model selection mechanics behind a pluggable interface without changing AoA role or tier doctrine.

### Donor surfaces

- `src/router/strategy.ts`
- direct `route()` posture from `docs/configuration.md#programmatic-usage`

### Repo homes

- `abyss-stack`
- `ATM10-Agent`
- `aoa-agents`

### First artifact hint

- strategy interface note
- route-decision envelope schema or example artifact
- one selector-adapter boundary note

### Preserved vocabulary

- strategy registry
- rules strategy
- routing profile
- agentic detection
- selected model
- confidence
- cost estimate
- profile suffix

### Explicit non-goals

- redefine AoA tiers
- replace `aoa-agents` duty-tier doctrine
- move authorship into `aoa-routing`
- make one donor strategy canonical without eval evidence

### What stays in neighboring repos

- `aoa-agents` keeps role contracts and tier meaning
- `aoa-routing` keeps dispatch hints only
- `aoa-playbooks` keeps scenario-level escalation posture
- `abyss-stack` remains the natural runtime owner of selector mechanics

### Suggested first planting slice

- one strategy-interface note
- one small route-decision envelope artifact
- one boundary statement that says:
  - selector picks provider/model
  - `aoa-agents` keeps duty tier meaning
  - `aoa-playbooks` keeps scenario escalation meaning

### Boundary note

This seed is a microkernel pattern, not a constitutional import.

---

<a id="aoa-seed-cr7-technique-promotion-surface"></a>
## AOA-SEED-CR7 Technique Promotion Surface

### Purpose

After at least two successful plantings and one eval-backed readout, promote generalized donor patterns into `aoa-techniques` as public reusable techniques.

### Donor surfaces

- results of `AOA-SEED-CR1` through `AOA-SEED-CR6`
- `aoa-techniques` donor intake and refinement posture

### Repo homes

- `aoa-techniques`

### First artifact hint

- donor candidate note
- adaptation notes
- validation evidence hook

### Preserved vocabulary

- donor intake
- refinement
- adaptation notes
- evidence
- promotion readiness

### Explicit non-goals

- promote before proof
- publish private-environment hacks as public canon
- skip adaptation notes
- skip negative effects review

### What stays in neighboring repos

- target repos keep their local landed meaning
- `aoa-techniques` only receives the portable pattern after evidence exists

### Suggested first planting slice

- one entry in the donor candidate surface
- one evidence note that names:
  - where it was planted
  - what changed
  - what failed
  - what stayed local

### Boundary note

A donor becomes a technique only after surviving real transplant work.

## Minimal machine-readable companion

This note expects one companion structural surface:

- `seed_clawrouter_donor_graft.map.yaml`

It should stay small, machine-readable, and cross-link the donor surfaces, repo homes, priorities, and hard boundaries.

## Final rule

Use this donor note to seed bounded landings.
Do not let donor admiration become repository capture.
