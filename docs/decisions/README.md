# Decision Records Index

This directory is the durable decision surface for `Dionysus`.

Use it when a future contributor needs the rationale for a seed route, planting
trace, wave manifest boundary, seed registry policy, prep-pack posture, replay
route, owner-repo handoff, generated seed capsule, or validation guard.

Ordinary implementation notes, source seed content, generated output, private
evidence, live memory, target-repo doctrine, and one-off planning thoughts route
to their owning surfaces instead.

## Operating Card

| Field | Route |
| --- | --- |
| role | durable seed-garden decision rationale entrypoint and index chooser |
| input | changed seed route, planting trace, registry policy, wave boundary, prep-pack posture, owner-repo handoff, generated seed capsule, or validation guard |
| output | canonical decision note, generated lookup indexes, and route back to the owning seed, protocol, generated, validation, or target-repo surface |
| owner | `docs/decisions/AGENTS.md` for lane law; decision notes for rationale; generated indexes for lookup only |
| next route | owning seed/manifest/registry/protocol/generated/script/test surface first, then nearest route card, `README.md`, `ROADMAP.md`, generated lookup indexes, or the affected target owner |
| validation | `python scripts/generate_decision_indexes.py --check` and `python scripts/validate_decision_records.py`, plus the owning validator for the changed surface |

## Authority

Decision notes explain why a seed-garden route was chosen.

They are weaker than the source surface they describe:

- seed files and wave manifests keep stronger seed truth;
- `seed-registry.yaml` keeps stronger navigation and lifecycle truth;
- planting protocol and provenance policy stay in `docs/codex/`;
- generated seed route maps stay in `generated/`;
- build and validation behavior stays in `scripts/`;
- regression proof stays in `tests/`;
- target repositories keep stronger truth for planted AoA, ToS, runtime, SDK,
  profile, and implementation meaning.

Generated decision indexes are weaker than the decision notes. They exist to
make lookup cheaper for agents, not to carry decision rationale.

## Index Shape

Each decision owns:

- a canonical `Decision ID: DION-SEED-D-####`;
- a full canonical-ID filename, for example `DION-SEED-D-0001-*.md`;
- an `## Index Metadata` block naming original date, surface classes, seed
  surfaces, owner lanes, guard families, and posture.

The lookup indexes under [indexes](indexes/README.md) are generated from that
metadata:

- [Decisions by canonical ID and number](indexes/by-number.md)
- [Decisions by date](indexes/by-date.md)
- [Decisions by surface class](indexes/by-surface.md)
- [Decisions by seed surface](indexes/by-seed-surface.md)
- [Decisions by owner lane](indexes/by-owner-lane.md)
- [Decisions by validation or guard family](indexes/by-guard.md)

Regenerate the read models after decision metadata changes:

```bash
python scripts/generate_decision_indexes.py
```

Check generated parity before closeout:

```bash
python scripts/generate_decision_indexes.py --check
```

## Lookup Route

Do not hand-maintain a "latest decision" roster in this README. That list drifts
as soon as a new decision lands.

Use the generated indexes instead:

- [by number](indexes/by-number.md) for the complete canonical ledger;
- [by date](indexes/by-date.md) for recent landings;
- [by surface](indexes/by-surface.md), [by seed surface](indexes/by-seed-surface.md),
  and [by owner lane](indexes/by-owner-lane.md) for route-pressure lookup;
- [by guard](indexes/by-guard.md) for validation, owner-boundary, seed registry,
  planting trace, generated-output, lifecycle, or replay pressure.

## Addressing

Full canonical-ID decision paths are the active source files:

- `docs/decisions/DION-SEED-D-0001-*.md`
- `docs/decisions/DION-SEED-D-0002-*.md`
- `docs/decisions/DION-SEED-D-####-*.md`

Canonical IDs remain stable handles. Previous path names belong to git, PR, or
release history, not to a compatibility lookup layer.

## Naming

Use the full canonical decision ID as the filename prefix:

`DION-SEED-D-0001-short-decision-slug.md`

Prefer short titles that name the seed route, not the whole debate.

## Template

Start from [TEMPLATE.md](TEMPLATE.md) for new decisions. Keep notes concise, but
include enough context, options, rationale, consequences, source surfaces, and
validation for a future agent to avoid repeating the same seed-route question.
