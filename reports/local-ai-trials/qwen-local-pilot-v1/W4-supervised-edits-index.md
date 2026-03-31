# W4 Low-Risk Supervised Edits

Bounded edit candidates with frozen file scopes and required validation.

- Gate result: `pass`
- Cases: `8`
- Status counts: `{"pass": 8, "fail": 0, "planned": 0}`
- Next action: W4 gate passed. Review landed edits and decide whether a broader autonomous pilot is warranted.

## Truth Status
- source_authored: `true`
- deployed: `true`
- trial_proven: `true`
- live_available: `true`
- note: Wave-level source_authored refers to the canonical aoa-local-ai-trials contract.
- note: Wave-level deployed refers to the operator-visible runner under /srv/abyss-stack/Configs/scripts/aoa-local-ai-trials.
- note: trial_proven is backed by a passing wave gate.
- note: live_available is true only when the passing wave also maps to the deployed runner surface.

## Cases
- `aoa-skills-doc-wording-alignment`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.aoa-skills-doc-wording-alignment.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.aoa-skills-doc-wording-alignment.md)
  aoa-skills Docs Wording Alignment
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-routing-doc-boundary-alignment`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.aoa-routing-doc-boundary-alignment.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.aoa-routing-doc-boundary-alignment.md)
  aoa-routing Boundary Doc Alignment
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-evals-contract-wording-alignment`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.aoa-evals-contract-wording-alignment.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.aoa-evals-contract-wording-alignment.md)
  aoa-evals Contract Wording Alignment
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-techniques-doc-index-alignment`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.aoa-techniques-doc-index-alignment.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.aoa-techniques-doc-index-alignment.md)
  aoa-techniques Doc And Index Alignment
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `agents-of-abyss-role-clarity-docs`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.agents-of-abyss-role-clarity-docs.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.agents-of-abyss-role-clarity-docs.md)
  Agents-of-Abyss Role Clarity Docs Only
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `8dionysus-profile-routing-clarity`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.8dionysus-profile-routing-clarity.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.8dionysus-profile-routing-clarity.md)
  8Dionysus Public Entry Routing Clarity
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-routing-generated-surface-refresh`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.aoa-routing-generated-surface-refresh.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.aoa-routing-generated-surface-refresh.md)
  aoa-routing Generated Surface Refresh
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-evals-generated-catalog-refresh`: `pass` [2026-03-29.qwen-local-pilot-v1.W4.aoa-evals-generated-catalog-refresh.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W4.aoa-evals-generated-catalog-refresh.md)
  aoa-evals Generated Catalog Refresh
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true

## Gate Detail
```json
{
  "pass_count": 8,
  "fail_count": 0,
  "critical_failures": [],
  "docs_lane_pass_count": 6,
  "docs_lane_critical_case_ids": [],
  "prepared_docs_cases": 6,
  "valid_docs_proposals": 6,
  "pending_approvals": 0,
  "generated_lane_unlocked": true,
  "next_action": "W4 gate passed. Review landed edits and decide whether a broader autonomous pilot is warranted."
}
```
