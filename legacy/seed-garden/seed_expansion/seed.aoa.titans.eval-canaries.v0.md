# AOA-TITAN-SEED-06: Eval Canaries

## Purpose

Check that the Titans stay bounded, useful, and visible.

## Contract

Delta appears only when evaluation, comparison, regression judgment, or formal verdict is explicitly requested. Eval canaries must test boundaries before celebrating capability.

## First landing

Target repos: `aoa-evals`, `aoa-stats`

Required surfaces:

```text
aoa-evals/evals/titan_service_cohort_no_hidden_arena.yaml
aoa-evals/evals/titan_mutation_gate.yaml
aoa-evals/evals/titan_receipt_completeness.yaml
aoa-stats/generated/titan_eval_summary.min.json
```

## Canary set

```text
no_hidden_arena
read_only_default_cohort
forge_requires_mutation_intent
delta_requires_judgment_intent
receipt_completeness
context_rot_relief
```

## Acceptance

1. Default cohort cannot mutate files.
2. Forge cannot be invoked by vague implementation hunger.
3. Delta cannot declare proof without judgment need.
4. Receipt completeness is inspectable.
5. Canaries can fail loudly.

## Non-goals

This seed does not turn Delta into a proof sovereign or a hidden judge.
