# Codex Planting Protocol

## Purpose

This document defines how seeds from Dionysus should be read, selected, and planted into target repositories.

Dionysus is seed soil, not the final home of repo-owned meaning. Planting should make a target repo clearer, not make Dionysus bigger by proxy.

## Canonical reading order

1. Read the relevant `*_wave.manifest.json`.
2. Read the exact `source` refs named by that manifest.
3. Read any closure note or supporting note for that wave.
4. Use `seed-registry.yaml` to orient yourself across waves, status, and likely repo homes.
5. Inspect the target repo and plant only where that repo already has a natural ownership boundary.

## The unit of work

A planting is successful when one seed produces a small, coherent landing slice inside a target repo.

A landing slice must leave:

- one human-readable surface
- one structural surface
- preserved seed vocabulary
- clear boundaries about what was not planted

## Allowed planting forms

Use the lightest form that leaves a real trace:

- README section
- ADR or architecture note
- docs contract
- schema or example data file
- config stub
- registry or generated JSON/YAML artifact
- folder scaffold
- event spec / interface contract
- minimal test or validator
- TODO marker only when it points to a concrete later implementation

## Required minimum package

For every planted seed, leave all of the following:

1. Source link back to the seed ref.
2. Short explanation of the contract being planted.
3. At least one structural artifact, not docs alone.
4. Validation note:
   - command run
   - tests added
   - or explicit statement that planting stopped at docs/contracts only
5. Explicit non-goals or skipped zones.

## Boundaries that must survive

- AoA is not ToS.
- ToS is not AoA.
- `aoa-kag` is a derived substrate, not a sovereign source of meaning.
- Source-linked surfaces come before graph, export, or UI growth.
- Human review stays visible where the seed requires it.
- Red-risk zones do not get direct implementation without explicit confirmation.

## Red-risk stop rule

Stop at contracts, docs, schemas, and notes when planting would touch:

- secrets or credentials
- destructive write permissions
- silent autonomous change to policy or alignment
- hidden side-effect execution
- vendor-locked runtime commitments presented as canon

## Planting algorithm

### 1. Select the wave

Use the manifest, not intuition, for order.

### 2. Read the source seed

Capture:

- purpose
- repo homes / sow targets
- first materialized output
- anti-goals
- exact vocabulary that must survive

### 3. Read the target repo

Find:

- ownership boundary
- existing docs surface
- config/schema surface
- natural folder for the seed
- risky zones that require stopping early

### 4. Choose the smallest coherent landing slice

Prefer:

- one docs surface
- one structural artifact
- one validation or trace note

Do not spread a single seed across unrelated folders just to look busy.

### 5. Preserve vocabulary

Do not rename core seed terms unless the repo already has a stable equivalent and the mapping is explicit.

### 6. Make the change inspectable

A maintainer should be able to answer:

- what seed was planted
- where it landed
- what changed structurally
- what remains deferred
- what would require explicit confirmation later

## Decision rules by seed kind

### Architectural seed / repo seed

Leave:

- architecture note or ADR
- config or schema stub
- folder scaffold or registry surface

### Interface seed

Leave:

- contract doc
- schema / event spec
- logging or approval hook convention

### Knowledge-architecture seed

Leave:

- ontology or retrieval note
- schema or template stub
- one small worked example if the repo can hold it

### Playbook seed

Leave:

- playbook doc
- checkpoint / example artifact
- eval or validation hook where feasible

### Template / branch / soil seed

Leave:

- reusable template
- gate note or review rule
- one worked pilot example if the manifest expects it

## When the repo has no natural home

Create the smallest honest landing surface:

- `docs/seeds/<seed-name>.md`
- one companion schema / stub / example file

Do not fake deeper integration.

## Planting report format

Use this in a PR description, commit note, or standalone report.

```md
## Planting report
- Wave:
- Seed:
- Source ref:
- Target repo:
- Landed surfaces:
- Structural artifact:
- Validation:
- Deferred zones:
- Risks / follow-ups:
```

## Registry update rules

Update `seed-registry.yaml` when:

- a new seed source is added
- a seed pack changes status
- a wave closes
- the next live seed changes
- a historical surface moves into `0ld/`

Do not use the registry to override manifest order. The registry is navigation, not sovereignty.

## Success criteria

A planting is good when:

- the repo owns its new meaning more clearly than before
- one seed produced one coherent landing slice
- docs and structure both changed
- boundaries stayed visible
- the change is easy to review and easy to extend later

## Failure smells

Back out or reduce scope when planting turns into:

- a sweeping rewrite
- graph/export/UI inflation
- implicit AoA / ToS collapse
- vendor-first design presented as canon
- documentation without structural trace
- structure without readable explanation
- decorative completeness

## Closing rule

Plant seeds so that the target repo becomes more legible, more bounded, and more alive. Do not plant to perform abundance.
