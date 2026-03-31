# W0 Runtime Qualification

Qualify the local Qwen runtime path before any higher-layer trials.

- Gate result: `pass`
- Cases: `6`
- Status counts: `{"pass": 6, "fail": 0, "planned": 0}`
- Next action: Proceed to W1 routing and ownership under the same per-case reporting contract.

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
- `warm-exact-reply`: `pass` [2026-03-29.qwen-local-pilot-v1.W0.warm-exact-reply.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W0.warm-exact-reply.md)
  Warm Exact Reply Through Langchain Run Path
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `warm-repo-routing`: `pass` [2026-03-29.qwen-local-pilot-v1.W0.warm-repo-routing.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W0.warm-repo-routing.md)
  Warm Repo Routing Through Langchain Run Path
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `intel-full-smoke-internal`: `pass` [2026-03-29.qwen-local-pilot-v1.W0.intel-full-smoke-internal.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W0.intel-full-smoke-internal.md)
  Intel Full Smoke With Internal Probes
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `federation-smoke`: `pass` [2026-03-29.qwen-local-pilot-v1.W0.federation-smoke.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W0.federation-smoke.md)
  Federation Smoke
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `cold-restart-recovery`: `pass` [2026-03-29.qwen-local-pilot-v1.W0.cold-restart-recovery.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W0.cold-restart-recovery.md)
  Cold Restart Recovery
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `agent-full-parity-sample`: `pass` [2026-03-29.qwen-local-pilot-v1.W0.agent-full-parity-sample.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W0.agent-full-parity-sample.md)
  Agent Full Parity Sample
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true

## Gate Detail
```json
{
  "all_cases_passed": true,
  "exact_reply_mean_s": 2.516,
  "repo_routing_mean_s": 10.868,
  "exact_reply_budget_s": 3.5,
  "repo_routing_budget_s": 12.0,
  "no_timeout_or_5xx_shared_bench": true,
  "intel_not_worse_than_agent_full_by_stability": true
}
```
