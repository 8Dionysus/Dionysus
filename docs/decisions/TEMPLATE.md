# DION-SEED-D-#### Short Decision Title

## Index Metadata

- Decision ID: DION-SEED-D-####
- Original date: YYYY-MM-DD
- Surface classes: docs/protocol
- Seed surfaces: seed registry
- Owner lanes: Dionysus
- Guard families: owner-repo handoff
- Posture: proposed

## Context

What seed-garden pressure made the decision necessary?

Name the seed, manifest, registry, protocol, generated, schema, example, script,
test, archive, report, or target-owner surfaces that shaped the choice.

## Decision

State the chosen route in one or two paragraphs.

## Options Considered

- Option A:
- Option B:
- Option C:

## Rationale

Explain why this route fits `Dionysus` as a seed garden and dispatch layer where
target repositories own planted meaning.

## Consequences

Name what becomes easier, what remains constrained, and what future contributors
must not infer from this decision.

## Source Surfaces

- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `seed-registry.yaml`
- `docs/codex/planting-protocol.md`

## Validation

Run:

```bash
python scripts/generate_decision_indexes.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_decision_records.py
```

Also run the validator for the owning surface the decision describes.
