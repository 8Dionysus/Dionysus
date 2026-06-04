# AGENTS.md

## Guidance for `docs/decisions/`

`docs/decisions/` is the durable decision-rationale lane for the Dionysus seed
garden.

Use it when the repository needs to preserve why a seed route, planting trace,
wave manifest boundary, seed registry policy, prep-pack posture, replay route,
owner-repo handoff, generated seed capsule, or validation guard was chosen.

Do not use this lane for source seed meaning, target-repo doctrine, runtime
behavior, mutable backlog status, private evidence, or live memory. Seed files
and wave manifests own seed meaning. Target repositories own planted meaning.
Generated indexes under this lane are read models only.

## Record Law

- Decision files use full canonical filenames:
  `DION-SEED-D-####-short-slug.md`.
- Each decision has an `## Index Metadata` block with:
  `Decision ID`, `Original date`, `Surface classes`, `Seed surfaces`,
  `Owner lanes`, `Guard families`, and `Posture`.
- Decision IDs are stable handles. Historical filenames belong to git and PR
  history, not to a compatibility lookup layer.
- Generated indexes under `docs/decisions/indexes/` are read models only. Do
  not edit them by hand.
- Material changes to rationale should usually add a new decision with explicit
  supersession prose instead of silently rewriting an accepted route.

## Boundary

Decision notes explain why Dionysus chose a route. They are weaker than the
surfaces they describe:

- seed sources stay in the exact seed files;
- wave order stays in `*_wave.manifest.json`;
- seed navigation stays in `seed-registry.yaml`;
- planting protocol stays in `docs/codex/`;
- generated seed capsules stay in `generated/`;
- schemas, examples, scripts, and tests own their local contracts;
- target repositories own planted AoA, ToS, runtime, SDK, profile, and
  implementation meaning.

## When To Add A Decision

Add or update a decision record when a change materially affects:

- which seed surface is stronger than another;
- whether Dionysus keeps trace or routes it fully to a target repo;
- seed registry, wave manifest, closure note, or replay policy;
- prep-pack lifecycle and owner-repo reality checks;
- generated seed capsule or validation index policy;
- boundaries between seed garden staging and target-repo ownership.

Small copy edits, routine generated-output refreshes, local test maintenance,
and ordinary seed file additions do not need a decision unless they change one
of those routes.

## Verify

Run:

```bash
python scripts/generate_decision_indexes.py --check
python scripts/validate_decision_records.py
```

When decision metadata changes, regenerate first:

```bash
python scripts/generate_decision_indexes.py
```

Also run the owning validator for the changed surface, usually:

```bash
python scripts/validate_seed_surfaces.py
python -m pytest -q tests
```
