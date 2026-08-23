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
- The installed shared `aoa release` route owns federation preflight,
  prerelease-aware publication, exact tag identity, canonical GitHub Release
  publication, and strict postpublish audit. `scripts/release_publish.py` is
  retained as an owner-local compatibility/reference helper.
- `interviews/`, `schemas/`, and `instruments/` retain their own `0.1.0`
  contract versions. They are not repository release markers and must not be
  mass-rewritten to `0.4.0-alpha.2`.

## Historical route for `v0.4.0-alpha.1`

The exact alpha publication ran from a clean `main` checkout synchronized with
`origin/main`, after the release-prep PR had landed:

```bash
aoa release audit /srv/AbyssOS --phase preflight --repo Dionysus --strict --json
aoa release publish /srv/AbyssOS --repo Dionysus --dry-run --json
```

The plan was then published exactly once through the installed shared route:

```bash
aoa release publish /srv/AbyssOS --repo Dionysus --confirm --json
```

The strict shared postpublish audit completed the route:

```bash
aoa release audit /srv/AbyssOS --phase postpublish --repo Dionysus --strict --json
```

The shared route created the annotated `v0.4.0-alpha.1` tag and existing
source-only GitHub prerelease, published no assets, and verified the peeled tag
commit, annotated tag type, prerelease flag, stable latest marker, exact
canonical body, empty asset set, clean synchronized `main`, and source-only
artifact posture.

The alpha.1 publication and its disclosed post-release correction are
historical evidence for the current alpha.2 repair. Do not rerun a publish
command for `v0.4.0-alpha.1`, move its tag, or retrospectively redefine its
tagged source.

## Current required route for `v0.4.0-alpha.2`

The alpha.2 correction release runs from a clean `main` checkout synchronized
with `origin/main`, after its release-prep PR has landed:

```bash
python scripts/release_check.py
aoa release audit /srv/AbyssOS --phase preflight --repo Dionysus --strict --json
aoa release publish /srv/AbyssOS --repo Dionysus --dry-run --json
```

Inspect the dry-run to confirm that it creates only an annotated
`v0.4.0-alpha.2` tag and a new prerelease Release. Then publish exactly once
through the installed shared route:

```bash
aoa release publish /srv/AbyssOS --repo Dionysus --confirm --json
```

Finish with the strict shared postpublish audit:

```bash
aoa release audit /srv/AbyssOS --phase postpublish --repo Dionysus --strict --json
```

The route must preserve alpha.1, keep stable `v0.3.0` as GitHub's latest
stable Release, publish no assets, and verify that the alpha.2 tag peels to
the exact landed `main` commit and that the Release body matches the canonical
alpha.2 changelog section. A dry-run that proposes updating alpha.1 is stale
and must not be confirmed.

## Federation helper boundary

`aoa-sdk` PR [#263](https://github.com/8Dionysus/aoa-sdk/pull/263) landed exact
SemVer prerelease support before the alpha.1 publication. The installed shared
`aoa release publish` route supports the exact alpha.2 identity as well; no
stable alias is permitted. The owner-local `scripts/release_publish.py`
remains a compatibility/reference helper and is not the canonical publication
route.

The owner route remains subject to the common distinction between source
landing, GitHub checks, tag, Release publication, artifact admission, runtime
health, proof, deployment, and human acceptance. This source release proves
only its public source and release-surface identity.

## Recovery and migration

If alpha.2 publication fails after its tag is pushed, preserve that tag and
rerun the strict shared postpublish audit after resolving the GitHub Release
operation. Do not move or recreate alpha.1 or alpha.2. A future product or
release correction requires a new owner-approved version; an editorial body
erratum may update only the corresponding existing Release body from corrected
canonical source.
Former seed-garden consumers must migrate to their actual owner repositories;
`legacy/` and `pre-archive-2026-07-23` are archaeology/recovery paths only.
