# Releasing `Dionysus`

`Dionysus` publishes a source-only prerelease of its protocol and local
reflection laboratory. This route does not publish a Python package, model,
runtime, container, media artifact, SBOM, signature, or artifact-registry
record. GitHub's generated source archive is a view of the exact tag, not an
owner attestation.

## Release surfaces

- `CHANGELOG.md` is the canonical human-first release body and carries the
  complete First-Parent Reconciliation ledger.
- `README.md` carries the exact current-release banner consumed by the
  federation audit.
- `ROADMAP.md` names the release line and its maturity ceiling.
- `scripts/release_check.py` owns the exact baseline/first-parent, privacy,
  validator, browser syntax, loopback HTTP smoke, clean-main, and release
  surface gate.
- `scripts/release_publish.py` owns the prerelease-aware dry-run, annotated
  tag identity, canonical GitHub Release publication, and postpublish audit.
- `interviews/`, `schemas/`, and `instruments/` retain their own `0.1.0`
  contract versions. They are not repository release markers and must not be
  mass-rewritten to `0.4.0-alpha.1`.

## Required route

Run from a clean `main` checkout synchronized with `origin/main`, after the
release-prep PR has landed:

```bash
python scripts/release_check.py
python scripts/release_publish.py --dry-run
```

Inspect the plan. Then publish exactly once:

```bash
python scripts/release_publish.py --confirm
```

Finish with the owner postpublish audit:

```bash
python scripts/release_publish.py --postpublish
```

The publisher refuses to move a mismatched `v0.4.0-alpha.1` tag, refuses to
overwrite a mismatched existing Release, publishes no assets, and verifies the
peeled tag commit, annotated tag type, prerelease flag, latest marker, exact
canonical body, empty asset set, clean synchronized `main`, and source-only
artifact posture.

## Federation helper boundary

`Dionysus` is listed in the shared federation release owner set, but the
installed `aoa-sdk` release helper currently parses only stable `X.Y.Z`
changelog headings and would derive `v0.4.0`, not the approved alpha tag. Do
not create a stable compatibility alias or invoke that helper to publish the
wrong identity. The generic `aoa release audit /srv/AbyssOS --phase preflight
--repo Dionysus --strict --json` route is therefore recorded as a known
contract mismatch for this alpha, not a green release gate. The owner-local
route above is the current canonical route for this approved prerelease; the
shared helper's prerelease support is a separate federation follow-up.

The owner route remains subject to the common distinction between source
landing, GitHub checks, tag, Release publication, artifact admission, runtime
health, proof, deployment, and human acceptance. This source release proves
only its public source and release-surface identity.

## Recovery and migration

If publication fails after the tag is pushed, preserve the tag and rerun
`--postpublish` after resolving the GitHub Release operation. Do not move or
recreate the tag. A future correction requires a new owner-approved version.
Former seed-garden consumers must migrate to their actual owner repositories;
`legacy/` and `pre-archive-2026-07-23` are archaeology/recovery paths only.
