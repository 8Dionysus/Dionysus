# Titan Memory Loom Preflight

## Scope

Prepare the fifth Titan wave for cross-session recall. The wave plants docs, schemas, CLI, prompts, eval canaries, metrics, and memory posture.

## Required gates

- Memory sovereignty denial is written.
- Recall result includes source and authority notes.
- Redaction workflow exists before broad ingestion.
- Retention policy is explicit.
- Forge and Delta gate semantics are unchanged.

## Expected smoke

```bash
bash tools/smoke_titan_memory_loom.sh
```
