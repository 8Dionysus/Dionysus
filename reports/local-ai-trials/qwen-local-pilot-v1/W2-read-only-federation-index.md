# W2 Read-Only Federation Tasks

Check useful read-only work across repo docs, validators, runtime, and route-api.

- Gate result: `pass`
- Cases: `18`
- Status counts: `{"pass": 18, "fail": 0, "planned": 0}`
- Next action: Proceed to W3 selection and orchestration under the same per-case reporting contract.

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
- `skills-validate-and-explain`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.skills-validate-and-explain.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.skills-validate-and-explain.md)
  Run aoa-skills Validator And Explain Boundary
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `routing-validate-and-explain`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.routing-validate-and-explain.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.routing-validate-and-explain.md)
  Run aoa-routing Validator And Explain Boundary
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `evals-validate-and-explain`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.evals-validate-and-explain.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.evals-validate-and-explain.md)
  Run aoa-evals Validator And Explain Boundary
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `kag-validate-and-explain`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.kag-validate-and-explain.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.kag-validate-and-explain.md)
  Run aoa-kag Validator And Explain Boundary
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-charter-lookup`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.aoa-charter-lookup.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.aoa-charter-lookup.md)
  Look Up AoA Constitutional Source Refs
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `tos-boundary-lookup`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.tos-boundary-lookup.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.tos-boundary-lookup.md)
  Look Up ToS Source Boundary Refs
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `playbook-activation-lookup`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.playbook-activation-lookup.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.playbook-activation-lookup.md)
  Look Up Playbook Activation Surface
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `memo-checkpoint-contract-lookup`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.memo-checkpoint-contract-lookup.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.memo-checkpoint-contract-lookup.md)
  Look Up Memo Checkpoint Contract
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `route-api-surface-status-read`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.route-api-surface-status-read.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.route-api-surface-status-read.md)
  Read Route API Surface Status
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `route-api-federation-entrypoints-read`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.route-api-federation-entrypoints-read.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.route-api-federation-entrypoints-read.md)
  Read Route API Federation Entrypoints
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `route-api-evals-catalog-read`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.route-api-evals-catalog-read.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.route-api-evals-catalog-read.md)
  Read Route API Evals Catalog
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `route-api-playbooks-activation-read`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.route-api-playbooks-activation-read.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.route-api-playbooks-activation-read.md)
  Read Route API Playbooks Activation
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `route-api-kag-tos-export-read`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.route-api-kag-tos-export-read.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.route-api-kag-tos-export-read.md)
  Read Route API ToS Export Surface
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `runtime-inspect-langchain-health`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-langchain-health.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-langchain-health.md)
  Inspect Langchain API Health
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `runtime-inspect-route-api-health`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-route-api-health.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-route-api-health.md)
  Inspect Route API Health
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `runtime-inspect-platform-adaptation`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-platform-adaptation.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-platform-adaptation.md)
  Inspect Latest Platform Adaptation Record
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `runtime-inspect-runtime-bench-summary`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-runtime-bench-summary.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-runtime-bench-summary.md)
  Inspect Latest Runtime Bench Summary
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `runtime-inspect-rendered-services`: `pass` [2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-rendered-services.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W2.runtime-inspect-rendered-services.md)
  Inspect Rendered Services For Intel Plus Federation
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true

## Gate Detail
```json
{
  "pass_count": 18,
  "fail_count": 0,
  "fabricated_ref_or_command_cases": 0,
  "fabricated_case_ids": [],
  "honest_nonzero_cases": [
    "evals-validate-and-explain"
  ],
  "exact_ref_coverage_rate": 1.0,
  "next_action": "Proceed to W3 selection and orchestration under the same per-case reporting contract."
}
```
