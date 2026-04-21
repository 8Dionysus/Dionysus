# Agon Wave XV Seed: Epistemic Agon

This seed marks the first transition from mechanical honesty to epistemic conflict.

## Landing order

1. `Agents-of-Abyss`
2. `aoa-agents`
3. `aoa-techniques`
4. `aoa-skills`
5. `aoa-evals`
6. `aoa-memo`
7. `aoa-stats`
8. `aoa-sdk`

## What this seed allows

- define center-owned epistemic Agon law;
- add epistemic move-extension candidates without live protocol activation;
- prepare actor postures for model-of-other prediction and concept-map delta;
- request technique and skill candidates for epistemic conflict;
- align eval, memo, stats, and SDK surfaces around epistemic candidates;
- expose recurrence observation points over epistemic drift and false-consensus pressure.

## What this seed forbids

- live verdict authority;
- durable scar writes;
- retention execution;
- rank or trust mutation;
- direct KAG or Tree-of-Sophia promotion;
- hidden scheduler action;
- assistant contestant drift;
- automatic doctrine rewrites.

## Commands

In `Agents-of-Abyss`:

```bash
python scripts/build_agon_epistemic_agon_registry.py --check
python scripts/validate_agon_epistemic_agon.py
python -m pytest -q tests/test_agon_epistemic_agon.py
```

In `aoa-agents`:

```bash
python scripts/build_agon_epistemic_actor_posture_registry.py --check
python scripts/validate_agon_epistemic_actor_posture.py
python -m pytest -q tests/test_agon_epistemic_actor_posture.py
```

In `aoa-techniques`:

```bash
python scripts/build_agon_epistemic_technique_candidates.py --check
python scripts/validate_agon_epistemic_technique_candidates.py
python -m pytest -q tests/test_agon_epistemic_technique_candidates.py
```

In `aoa-skills`:

```bash
python scripts/build_agon_epistemic_skill_candidates.py --check
python scripts/validate_agon_epistemic_skill_candidates.py
python -m pytest -q tests/test_agon_epistemic_skill_candidates.py
```

In `aoa-evals`:

```bash
python scripts/build_agon_epistemic_eval_alignment_registry.py --check
python scripts/validate_agon_epistemic_eval_alignment.py
python -m pytest -q tests/test_agon_epistemic_eval_alignment.py
```

In `aoa-memo`:

```bash
python scripts/build_agon_epistemic_memo_bridge_registry.py --check
python scripts/validate_agon_epistemic_memo_bridge.py
python -m pytest -q tests/test_agon_epistemic_memo_bridge.py
```

In `aoa-stats`:

```bash
python scripts/build_agon_epistemic_stats_observability_registry.py --check
python scripts/validate_agon_epistemic_stats_observability.py
python -m pytest -q tests/test_agon_epistemic_stats_observability.py
```

In `aoa-sdk`:

```bash
python scripts/build_agon_epistemic_sdk_helpers.py --check
python scripts/validate_agon_epistemic_sdk_helpers.py
python -m pytest -q tests/test_agon_epistemic_sdk_helpers.py
```
