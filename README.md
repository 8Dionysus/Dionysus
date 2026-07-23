# Dionysus

Dionysus is a voice-first, evidence-grounded laboratory for building a
human-reviewed portrait of a person over time.

The repository does not contain a person. It contains the open protocols,
schemas, and projection formats needed to conduct reflective interviews,
retain the provenance of candidate claims, expose disagreement, and produce
small context views for deliberate use.

## Current state

This is a skeleton, not a finished interview system.

- `interviews/` defines the first interview family and the conversation
  contract.
- `schemas/` separates an interview session from a portrait claim.
- `portrait/` contains disposable projection templates, never an authoritative
  dossier.
- `vault/` documents the private boundary. Its contents are ignored by Git.
- `legacy/seed-garden/` preserves the former Dionysus seed-garden repository
  intact.

No voice transport, transcription provider, agent runtime, or personal dataset
is selected yet.

## Core rule

Conversation is evidence collection, not automatic truth production:

```text
voice or text conversation
  -> transcript and evidence slices
  -> candidate claims
  -> human accept / edit / contest / retire
  -> purpose-bounded portrait views
```

Claims must remain traceable to evidence and review. Derived portraits must be
small enough to inspect, must cite claim IDs, and must never silently become a
generic memory authority.

## Start here

1. Read [DESIGN.md](DESIGN.md).
2. Review [docs/PRIVACY.md](docs/PRIVACY.md).
3. Inspect the interview family in [interviews/catalog.toml](interviews/catalog.toml).
4. Run `python scripts/validate_skeleton.py`.

The former seed garden remains available at
[legacy/seed-garden/README.md](legacy/seed-garden/README.md) and at the
`pre-archive-2026-07-23` Git tag.

## License

Apache-2.0. See [LICENSE](LICENSE).
