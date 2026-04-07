seed_id: seed.audit.federated-audit-remediation-pack.v0
title: Federated Audit Remediation Pack
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: audit-pack-note
lifecycle_status: landed_upstream_retained_for_lineage
lifecycle_note: Waves 0 through 4 are now fully planted through bounded owner-repo landings, including the trimmed WS05 follow-through, the Wave 2 canary mesh, the landed Wave 3 WS03/WS04/WS07/WS11 slices, and the GitHub-only WS12 product-edge contract in ATM10-Agent; the pack remains in Dionysus only for lineage, replay, and ongoing owner-repo reality checks.
reality_checked_at: '2026-04-07'
status: pending_archive
priority: high
parent_seed: null
tags:
  - audit
  - remediation
  - federation
  - compatibility
  - canary
  - governance
  - contracts

# Seed Note: Federated Audit Remediation Pack

## Purpose

Convert the full audit dialogue into one bounded transport surface that can
drive real owner-repo fixes without turning `Dionysus` into the owner of those
fixes.

The pack is intentionally split into workstreams rather than one giant
checklist so Codex can land the smallest coherent slices without losing
dependency order.

Current first-slice reality is tracked in:

- `reports/ecosystem-audits/federated-audit-remediation-ledger.yaml`
- `reports/ecosystem-audits/2026-04-07.federated-audit-remediation.reality-check.md`
- `reports/ecosystem-audits/federated-audit-remediation.reality-canary.yaml`

## Why this belongs in Dionysus

`Dionysus` is the seed garden and dispatch layer.
This pack belongs here because:

- the remediation spans many owner repositories across AoA, ToS, and the public
  profile surfaces
- the first coherent slice is staging and reality-checking, not immediate
  multi-repo rollout
- the pack came from direct audit dialogue and needs a durable, replayable
  transport home
- `Dionysus` can preserve ordering, lineage, and non-goals without claiming
  sovereignty over the owner repos

## Bundle contents to preserve

The source artifact is
`archive/seed_pack_exports/federated_audit_remediation_seed_pack.zip`.

It carries:

- `README.md`
- `seed_federated_audit_remediation_pack.md`
- `seed_federated_audit_remediation_pack.map.yaml`
- `PACK_MANIFEST.json`
- `WORKSTREAMS.yaml`
- `EXECUTION_ORDER.md`
- `TASKS_BY_PRIORITY.md`
- `VALIDATION_MATRIX.md`
- `FINDINGS_INDEX.md`
- `PATCH_SNIPPETS.md`
- `repo_targets/*.md`
- `reports/planting-report.stub.md`

## Ownership posture

Read this pack as landing guidance, not sovereignty.

Owner-repo truth wins whenever the live repo has already moved beyond this
pack, and any landed cleanup should update this pack's staging markers if the
pack is preserved for lineage.

## What this pack is for

- federation compatibility and inventory hardening
- control-plane hardening across routing, sdk, and playbooks
- memory, recall, and return-path contract cleanup
- source-first ToS / KAG routing hardening
- governance-surface honesty
- CI and canary expansion
- traceability and maturity cleanup across techniques, skills, and evals
- onboarding, support-matrix, and release-semantics cleanup
- a separate preliminary ATM10-Agent endcap

## What this pack is not for

- no silent AoA / ToS collapse
- no transport-pack sovereignty over owner repos
- no broad product-edge rewrite hidden inside federation fixes
- no claim that ATM10-Agent has already been deeply audited here
- no decorative completeness without structural landings
- no downstream rollout from `Dionysus` in this staging step

## Confidence posture

Everything in `WORKSTREAMS.yaml` came from the audit dialogue.

The non-ATM10 workstreams are high-confidence relative to the dialogue because
they came from deeper repo-by-repo waves.
The ATM10 section is explicitly preliminary and should be treated as a bounded
endcap, not as a finished product audit.

## Later application order

When later planting starts, keep the order bounded:

1. federation compatibility, inventory, and release semantics
2. control-plane hardening across `aoa-routing`, `aoa-sdk`, and `aoa-playbooks`
3. memory and return-path contract hardening
4. governance-surface honesty and `aoa-skills` validator rail hardening
5. federation-wide canary expansion
6. source-first ToS / KAG seam cleanup and techniques-skills-evals traceability
7. onboarding, support matrix, and release clarity
8. ATM10-Agent preliminary endcap only after the deeper federation slices are separated

## Final rule

Land the smallest slice that removes a real lie, false green, hidden drift
path, or contract ambiguity.

Do not land broad cleanup just because the pack is large.
