# W4 LangGraph Sidecar Pilot

Bounded disposable W4 fixture used as a backend promotion gate.

- Gate result: `fail`
- Cases: `1`
- Status counts: `{"pass": 0, "fail": 1, "planned": 0}`
- Next action: Inspect the failed case packet and compare it against the baseline W4 runner before promoting LangGraph.

## Cases
- `fixture-docs-wording-alignment`: `fail` [2026-03-30.langgraph-sidecar-llamacpp-v1.W4.fixture-docs-wording-alignment.md](/srv/Dionysus/reports/local-ai-trials/langgraph-sidecar-llamacpp-v1/2026-03-30.langgraph-sidecar-llamacpp-v1.W4.fixture-docs-wording-alignment.md)
  Disposable Docs Fixture Wording Alignment

## Gate Detail
```json
{
  "pass_count": 0,
  "fail_count": 1,
  "planned_count": 0,
  "critical_failures": [
    "fixture-docs-wording-alignment"
  ],
  "pause_resume_proved": true,
  "comparison_memo": "/srv/Dionysus/reports/local-ai-trials/langgraph-sidecar-llamacpp-v1/LANGGRAPH_COMPARISON.md",
  "fixture_mode": true,
  "next_action": "Inspect the failed case packet and compare it against the baseline W4 runner before promoting LangGraph."
}
```
