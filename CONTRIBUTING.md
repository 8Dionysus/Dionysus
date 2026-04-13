# Contributing to Dionysus

Thank you for contributing.

## What belongs here

Good contributions:
- seed documents, rootline materials, and bundle curation
- wave manifests and their supporting docs
- public-safe witness-oriented follow-up seeds
- documentation that clarifies how this repository routes work into the owning AoA or ToS repositories

Bad contributions:
- turning this repository into the canonical home of specialized AoA or ToS layer meaning
- infrastructure or runtime implementation detail that belongs elsewhere
- unsourced rewrites that flatten seed provenance or planting order
- manifest or wave changes with no explicit rationale

## Before opening a PR

Please make sure:
- seed provenance remains visible
- trunk-first and wave-order changes are made explicit when they change
- docs stay public-safe and reviewable
- this repository remains a seed-source surface rather than a replacement for the owning repositories

Run the current repo-level release audit before opening a PR:

```bash
python scripts/release_check.py
```

For a quick manifest-only precheck before that, you may also run:

```bash
python scripts/validate_manifest.py
```

## Preferred PR scope

Prefer:
- 1 wave, manifest, or seed-family update per PR
- or 1 focused documentation clarification about repository role
- or 1 focused validation improvement

## Review criteria

PRs are reviewed for:
- provenance and source traceability
- manifest consistency
- fidelity to the repository's seed role
- public safety
- clarity about what this repository does and does not own

## Security

Do not use public issues or pull requests for leaks, credentials, or sensitive unpublished operational detail.
Use the process in `SECURITY.md`.
