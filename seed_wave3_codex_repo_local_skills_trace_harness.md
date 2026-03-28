seed_id: seed.wave3.codex-repo-local-skills-trace-harness.v0
title: Wave 3 Codex Repo-Local Skills and Trace Harness Prep Pack
profile_anchor: 8Dionysus
projects:
  - AoA
kind: audit-pack-note
status: pending_archive
priority: medium
parent_seed: null
tags:
  - audit
  - codex
  - local-skills
  - trace-harness
  - workflow
  - proof

# Seed Note: Wave 3 Codex Repo-Local Skills and Trace Harness

## Purpose

Prepare the third cross-repo audit update wave from
`wave3_codex_audit_update_pack.zip` without planting into the target
repositories yet.

This wave turns the earlier audit contracts from waves 1 and 2 into repeatable
repo-local helper workflows and one bounded proof harness, while keeping helper
skills weaker than public AoA skill canon and helper-skill proof weaker than
public eval bundle doctrine.

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This prep pack belongs here because:

- the update spans four owning repositories
- the first coherent slice is cross-repo staging, not immediate downstream edits
- the work is follow-on to the existing wave 1 and wave 2 audit prep surfaces
- the current next-live ToS gate should remain untouched

## Bundle contents to preserve

The source artifact is `wave3_codex_audit_update_pack.zip`.

It carries:

- `Agents-of-Abyss/docs/CODEX_REPO_LOCAL_SKILLS_PATTERN.md`
- `aoa-evals/docs/CODEX_REPO_LOCAL_TRACE_HARNESS.md`
- repo-local skill directories for `ATM10-Agent` and `abyss-stack`
- starter proof surfaces in `aoa-evals/examples/`
- `PATCH_SNIPPETS.md` for bounded `AGENTS.md` additions

## Ownership posture

Read the future landings under these repo-home boundaries:

- `Agents-of-Abyss` owns doctrine about what repo-local helper skills are and are not
- `ATM10-Agent` owns local workflow verification and safety-audit helper skills for its repo
- `abyss-stack` owns runtime-side change-verification and boundary-audit helper skills for its repo
- `aoa-evals` owns the bounded trace harness and starter proof fixtures

This prep pack stages repeatable helper workflows for those owners.
It does not move their meaning into `Dionysus`.

## What this wave is for

- repo-local helper skill doctrine in the ecosystem center
- first local helper skill families for `ATM10-Agent`
- first local helper skill families for `abyss-stack`
- one bounded trace-harness pattern and starter fixtures in `aoa-evals`
- small `AGENTS.md` additions so the pattern is routable and reviewable

## What this wave is not for

- no direct downstream planting yet
- no public `aoa-skills` canon expansion in this slice
- no broad helper-skill eval bundles yet
- no CI or GitHub Actions rollout yet
- no `.codex` profile specialization in this slice
- no change to `navigation.next_live_seed`

## Later application order

When the later planting starts, keep the order bounded:

1. add the bundled files as written
2. patch the four `AGENTS.md` files
3. use the new repo-local skills manually on real or dummy work
4. only then materialize the first bounded proof bundles in `aoa-evals`

## Final rule

Use this prep pack to stage later bounded helper-skill plantings.
Do not let repo-local helper skills quietly become public skill canon or a broad proof claim about Codex itself.
