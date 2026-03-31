# W3 Selection And Orchestration

Check skill, playbook, agent, tier, and eval-selection choices before execution.

- Gate result: `pass`
- Cases: `12`
- Status counts: `{"pass": 12, "fail": 0, "planned": 0}`
- Next action: Proceed to W4 supervised edits under the same per-case reporting contract.

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
- `select-skill-family-change-protocol`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-skill-family-change-protocol.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-skill-family-change-protocol.md)
  Select Skill Family For Bounded Change
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-skill-family-review`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-skill-family-review.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-skill-family-review.md)
  Select Skill Family For Post-Change Inspection
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-playbook-cross-repo-boundary-rollout`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-playbook-cross-repo-boundary-rollout.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-playbook-cross-repo-boundary-rollout.md)
  Select Playbook For Multi-Repo Source-Of-Truth Change
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-playbook-restartable-inquiry-loop`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-playbook-restartable-inquiry-loop.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-playbook-restartable-inquiry-loop.md)
  Select Playbook For Long-Horizon Inquiry
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-tier-router`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-tier-router.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-tier-router.md)
  Select Tier For Single Ownership Lookup
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-tier-planner`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-tier-planner.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-tier-planner.md)
  Select Tier For Non-Trivial Bounded Edit Planning
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-agent-coder`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-agent-coder.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-agent-coder.md)
  Select Agent Role For Approved Bounded Change
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-agent-reviewer`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-agent-reviewer.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-agent-reviewer.md)
  Select Agent Role For Post-Execution Review
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-eval-scope-drift-detection`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-eval-scope-drift-detection.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-eval-scope-drift-detection.md)
  Select Eval For Silent Scope Expansion
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `select-eval-return-anchor-integrity`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.select-eval-return-anchor-integrity.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.select-eval-return-anchor-integrity.md)
  Select Eval For Honest Return Anchors
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `decide-memo-stay-unused`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.decide-memo-stay-unused.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.decide-memo-stay-unused.md)
  Decide Whether Memo Must Stay Unused
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true
- `decide-kag-use-required`: `pass` [2026-03-29.qwen-local-pilot-v1.W3.decide-kag-use-required.md](/srv/Dionysus/reports/local-ai-trials/qwen-local-pilot-v1/2026-03-29.qwen-local-pilot-v1.W3.decide-kag-use-required.md)
  Decide Whether KAG Is Needed For Derived Retrieval
  truth_status: source_authored=true, deployed=true, trial_proven=true, live_available=true

## Gate Detail
```json
{
  "pass_count": 12,
  "fail_count": 0,
  "unsafe_selection_errors": 0,
  "unsafe_case_ids": [],
  "exact_match_rate": 1.0,
  "next_action": "Proceed to W4 supervised edits under the same per-case reporting contract."
}
```
