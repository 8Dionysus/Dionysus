# Dionysus

> Current release: `v0.4.0-alpha.2`. See [CHANGELOG](CHANGELOG.md) for release notes.

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
- `instruments/` records evidence, rights, language, voice-mode, and admission
  boundaries for methods that may orient an interview.
- `web/` provides a local text workbook for pre-interview reflection without
  accounts, network requests, or personality scoring.
- `schemas/` separates an interview session from a portrait claim.
- `portrait/` contains disposable projection templates, never an authoritative
  dossier.
- `vault/` documents the private boundary. Its contents are ignored by Git.

No voice transport, transcription provider, agent runtime, server-side data
store, or personal dataset is selected yet.

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

A standardized instrument, when allowed, is a separate feeder into this flow:
its private result may suggest questions, but cannot directly assert a trait,
value, strength, or type. The repository does not vendor test content or own a
scoring service.

## Start here

1. Read [DESIGN.md](DESIGN.md).
2. Review [docs/PRIVACY.md](docs/PRIVACY.md).
3. Inspect the instrument boundary in
   [instruments/admission-contract.md](instruments/admission-contract.md).
4. Open the local workbook described in [web/README.md](web/README.md).
5. Inspect the interview family in [interviews/catalog.toml](interviews/catalog.toml).
6. Run `python scripts/validate_skeleton.py`.

## License

Apache-2.0. See [LICENSE](LICENSE).
