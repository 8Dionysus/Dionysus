# W5 Summary

## Wave Verdict
- Gate result: `pass`
- Pass count: `8`
- Fail count: `0`
- Pause/resume proved: `True`
- Generated case passed: `True`
- Implementation case passed: `True`

## Substrate
- Runtime path: `llama.cpp -> langchain-api /run` on `http://127.0.0.1:5403/run`
- Orchestration layer: `LangGraph`

## Truth Status
- source_authored: `true`
- deployed: `true`
- trial_proven: `true`
- live_available: `true`
- note: This truth status tracks the W5 implementation surface for aoa-sync-federation-surfaces --check.
- note: source_authored inspects the canonical source checkout copy.
- note: deployed inspects the operator-visible Configs/scripts copy.
- note: trial_proven is backed by the passing W5 implementation scenario packet.
- note: live_available is true only because the W5 scenario passed and the deployed script exposes --check.

## Autonomy Posture
- Operator verdict path: `aoa-status --autonomy`
- Machine-readable verdict path: `aoa-status --autonomy --json`
- trial_proven: `true`
- live_available: `true`
- This summary remains a wave-local mirror and does not replace the deployed control-loop verdict.

## Next Action
W5 passed on promoted llama.cpp + LangGraph. Use this substrate as the bounded baseline for the next autonomy-focused wave.
