# W5 Long-Horizon Supervised Pilot

Scenario-based LangGraph pilot on the promoted llama.cpp substrate with milestone approvals and bounded live-repo mutations.

- Gate result: `pass`
- Cases: `8`
- Status counts: `{"pass": 8, "fail": 0, "planned": 0}`
- Next action: W5 passed on promoted llama.cpp + LangGraph. Use this substrate as the bounded baseline for the next autonomy-focused wave.

## Cases
- `runtime-inspect-langchain-health`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.runtime-inspect-langchain-health.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.runtime-inspect-langchain-health.md)
  Inspect Langchain API Health
- `runtime-inspect-route-api-health`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.runtime-inspect-route-api-health.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.runtime-inspect-route-api-health.md)
  Inspect Route API Health
- `runtime-inspect-platform-adaptation`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.runtime-inspect-platform-adaptation.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.runtime-inspect-platform-adaptation.md)
  Inspect Latest Platform Adaptation Record
- `evals-validate-and-explain`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.evals-validate-and-explain.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.evals-validate-and-explain.md)
  Run aoa-evals Validator And Explain Boundary
- `aoa-evals-contract-wording-alignment`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.aoa-evals-contract-wording-alignment.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.aoa-evals-contract-wording-alignment.md)
  aoa-evals Contract Wording Alignment
- `aoa-routing-doc-boundary-alignment`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.aoa-routing-doc-boundary-alignment.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.aoa-routing-doc-boundary-alignment.md)
  aoa-routing Boundary Doc Alignment
- `aoa-routing-generated-surface-refresh`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.aoa-routing-generated-surface-refresh.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.aoa-routing-generated-surface-refresh.md)
  aoa-routing Generated Surface Refresh
- `stack-sync-federation-check-mode`: `pass` [2026-03-30.w5-langgraph-llamacpp-v1.W5.stack-sync-federation-check-mode.md](/srv/Dionysus/reports/local-ai-trials/w5-langgraph-llamacpp-v1/2026-03-30.w5-langgraph-llamacpp-v1.W5.stack-sync-federation-check-mode.md)
  Add Check Mode To Federation Sync

## Gate Detail
```json
{
  "pass_count": 8,
  "fail_count": 0,
  "critical_failures": 0,
  "pause_resume_proved": true,
  "implementation_case_passed": true,
  "generated_case_passed": true,
  "unauthorized_scope_expansion": 0,
  "post_change_validation_failure": 0,
  "local_commit_refs": {
    "runtime-inspect-langchain-health": null,
    "runtime-inspect-route-api-health": null,
    "runtime-inspect-platform-adaptation": null,
    "evals-validate-and-explain": null,
    "aoa-evals-contract-wording-alignment": "ef4b1973c19fd95c143db256a0a6e27a90357f01",
    "aoa-routing-doc-boundary-alignment": "848cda1c5a3165a95922c2915f2ea6f381c9af75",
    "aoa-routing-generated-surface-refresh": "no-op-clean",
    "stack-sync-federation-check-mode": "no-op-clean"
  },
  "next_action": "W5 passed on promoted llama.cpp + LangGraph. Use this substrate as the bounded baseline for the next autonomy-focused wave."
}
```
