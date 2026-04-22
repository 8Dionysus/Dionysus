---
title: AoA Titans Runtime Harness Pack
pack_id: seed_aoa_titans_runtime_harness_pack
lifecycle_status: staged
lifecycle_note: >
  Second Titan wave. This pack moves from first appearance to runtime harness:
  roster, receipts, gates, closeout, route, and Codex control-plane seed.
reality_checked_at: "2026-04-22"
status_posture: implementation_seed
owner_hypothesis:
  - Dionysus
  - aoa-agents
  - 8Dionysus
  - aoa-sdk
  - aoa-skills
  - aoa-playbooks
  - aoa-evals
  - aoa-memo
  - aoa-stats
  - aoa-routing
non_goals:
  - hidden background autonomy
  - unreviewed workspace mutation
  - Delta proof sovereignty
  - memory writeback without owner acceptance
  - remote WebSocket app-server exposure
---

# AoA Titans Runtime Harness Pack

## Purpose

The first wave named the Titans and staged their service-cohort law. The second wave gives them a runtime harness that can be inspected by humans and by Codex.

## Cohort

- Atlas: architect
- Sentinel: reviewer
- Mneme: memory-keeper
- Forge: coder
- Delta: evaluator

## Default rule

Atlas, Sentinel, and Mneme may accompany the session after explicit summon. Forge and Delta are locked until the relevant gate is recorded.

## Runtime artifacts

The second wave plants these surfaces:

1. runtime roster
2. session receipt schema
3. titanctl CLI seed
4. summon and closeout prompts
5. hook context snippet
6. route map
7. eval canaries
8. memory closeout candidates
9. stats derivation notes
10. closure report

## Promotion condition

This wave is complete when the operator can run:

```bash
python scripts/titanctl.py summon --workspace /srv --operator Dionysus --out /srv/.titan/receipts/example.json
python scripts/titanctl.py validate --receipt /srv/.titan/receipts/example.json
```

and the receipt proves that Forge and Delta stayed locked unless explicitly gated.
