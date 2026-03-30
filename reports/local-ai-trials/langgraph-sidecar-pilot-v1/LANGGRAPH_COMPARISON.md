# langgraph-sidecar-pilot-v1 Comparison Memo

## Summary
- This pilot compares graph-shaped orchestration against the existing W4 bounded runner.

## Current Evidence
- Docs case pass: `True`
- Generated case pass: `True`
- Pause observed: `True`
- Resume observed: `True`

## Comparison Notes
- Pause/resume is explicit through persisted `graph.state.json`, `graph.history.jsonl`, and `approval.status.json`.
- Proposal and worktree safety continue to reuse the established W4 bounded-mutation contract.
- Glue code increases slightly because the pilot stays side-by-side with the existing runner instead of replacing it.

## Recommendation
LangGraph sidecar is recommended as the next bounded W5 execution substrate, while keeping `aoa-local-ai-trials` as the baseline comparator.
