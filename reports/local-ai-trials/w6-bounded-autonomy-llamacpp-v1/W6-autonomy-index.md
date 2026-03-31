# W6 Bounded Autonomy Pilot

Focused LangGraph autonomy pilot on the promoted llama.cpp substrate with reduced approval touchpoints and bounded live-repo mutations.

- Gate result: `pass`
- Cases: `6`
- Status counts: `{"pass": 6, "fail": 0, "planned": 0}`
- Next action: W6 passed on the promoted llama.cpp + LangGraph autonomy track. Use this substrate and approval posture as the baseline for the next implementation-heavy autonomy wave.

## Truth Status
- source_authored: `true`
- deployed: `true`
- trial_proven: `true`
- live_available: `true`
- note: This wave-level truth status tracks the two W6 promoted runtime-control surfaces together.
- note: source_authored requires both aoa-sync-federation-surfaces --check --json and aoa-llamacpp-pilot verify in the canonical source checkout.
- note: deployed requires both surfaces in the operator-visible Configs/scripts mirror.
- note: trial_proven is backed by passing W6 packets for both implementation scenarios.
- note: live_available is true only because both surfaces are deployed and both W6 implementation packets passed.

## Cases
- `runtime-inspect-langchain-health`: `pass` [2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.runtime-inspect-langchain-health.md](/srv/Dionysus/reports/local-ai-trials/w6-bounded-autonomy-llamacpp-v1/2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.runtime-inspect-langchain-health.md)
  Inspect Langchain API Health
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `runtime-inspect-route-api-health`: `pass` [2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.runtime-inspect-route-api-health.md](/srv/Dionysus/reports/local-ai-trials/w6-bounded-autonomy-llamacpp-v1/2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.runtime-inspect-route-api-health.md)
  Inspect Route API Health
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-evals-contract-wording-alignment`: `pass` [2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.aoa-evals-contract-wording-alignment.md](/srv/Dionysus/reports/local-ai-trials/w6-bounded-autonomy-llamacpp-v1/2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.aoa-evals-contract-wording-alignment.md)
  aoa-evals Contract Wording Alignment
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `aoa-routing-generated-surface-refresh`: `pass` [2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.aoa-routing-generated-surface-refresh.md](/srv/Dionysus/reports/local-ai-trials/w6-bounded-autonomy-llamacpp-v1/2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.aoa-routing-generated-surface-refresh.md)
  aoa-routing Generated Surface Refresh
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `stack-sync-federation-json-check-report`: `pass` [2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.stack-sync-federation-json-check-report.md](/srv/Dionysus/reports/local-ai-trials/w6-bounded-autonomy-llamacpp-v1/2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.stack-sync-federation-json-check-report.md)
  Add JSON Check Report To Federation Sync
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `llamacpp-pilot-verify-command`: `pass` [2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.llamacpp-pilot-verify-command.md](/srv/Dionysus/reports/local-ai-trials/w6-bounded-autonomy-llamacpp-v1/2026-03-30.w6-bounded-autonomy-llamacpp-v1.W6.llamacpp-pilot-verify-command.md)
  Add Verify Command To llama.cpp Pilot
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true

## Gate Detail
```json
{
  "pass_count": 6,
  "fail_count": 0,
  "critical_failures": 0,
  "pause_resume_proved": true,
  "novel_implementation_passes": 2,
  "implementation_case_passed": true,
  "generated_case_passed": true,
  "preexisting_noop_count": 0,
  "repair_attempted_count": 0,
  "repair_success_count": 0,
  "unauthorized_scope_expansion": 0,
  "post_change_validation_failure": 0,
  "local_commit_refs": {
    "runtime-inspect-langchain-health": null,
    "runtime-inspect-route-api-health": null,
    "aoa-evals-contract-wording-alignment": "no-op-clean",
    "aoa-routing-generated-surface-refresh": "no-op-clean",
    "stack-sync-federation-json-check-report": "aa5422fad3c6246b7fd406c115f9c6320370569f",
    "llamacpp-pilot-verify-command": "e7b42fb44e44fe0c239ea1dcefba3a028a77acad"
  },
  "next_action": "W6 passed on the promoted llama.cpp + LangGraph autonomy track. Use this substrate and approval posture as the baseline for the next implementation-heavy autonomy wave."
}
```
