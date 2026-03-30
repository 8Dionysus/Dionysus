# langgraph-sidecar-llamacpp-v1 Comparison Memo

## Summary
- This pilot compares graph-shaped orchestration against the existing W4 bounded runner.

## Current Evidence
- Docs case pass: `False`
- Generated case pass: `False`
- Pause observed: `True`
- Resume observed: `True`

## Comparison Notes
- Pause/resume is explicit through persisted `graph.state.json`, `graph.history.jsonl`, and `approval.status.json`.
- Proposal and worktree safety continue to reuse the established W4 bounded-mutation contract.
- Glue code increases slightly because the pilot stays side-by-side with the existing runner instead of replacing it.

## Recommendation
This fixture pilot is not yet suitable as a promotion gate because the disposable docs case has not passed.
