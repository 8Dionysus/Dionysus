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

The alpha.1 publication and its disclosed post-release correction are now
historical evidence only. The final campaign does not retain a second public
alpha.1 carrier. Its tag object, peeled commit, Release ID/body/assets, and
tagged changelog are preserved in the digest-bound pre-mutation recovery
ledger and in the nested alpha.2 changelog history. Do not rerun a publish
command for alpha.1 or recreate it after the one-time consolidation.

## Current required route for the sole `v0.4.0-alpha.2`

The final alpha.2 reconsolidation runs from a clean `main` checkout synchronized
with `origin/main`, after its release-repair PR has landed. The source gate uses
stable `v0.3.0` as the durable baseline and accounts for the complete 9/9
campaign first-parent range. The final reconsolidation commit is the exact
landed source that the existing alpha.2 tag and Release must publish.

```bash
python scripts/release_check.py
```

Before mutation, require the external pre-mutation ledger to match the live
identity: exactly two campaign Releases/tags, alpha.1 Release `375088635`,
alpha.2 Release `375135773`, zero campaign assets, both annotated tag objects,
both peeled commits, stable `v0.3.0` latest, and unchanged full tag/Release
inventories. A missing or mismatched digest-bound snapshot is a hard stop.

The ordinary shared publisher is intentionally not the final mutation route
when alpha.2 already exists at an earlier commit: a dry-run that proposes a
new Release or an unapproved tag move must fail closed. The owner-approved
single-release sequence is target-only and does exactly this:

1. create one new annotated alpha.2 tag object for the exact landed `main`;
2. delete only the alpha.1 GitHub Release and `refs/tags/v0.4.0-alpha.1`;
3. delete/recreate only the existing alpha.2 tag ref to the new tag object;
4. PATCH the existing alpha.2 Release ID `375135773` with the final body,
   `draft=false`, `prerelease=true`, `tag_name=v0.4.0-alpha.2`, and the exact
   landed target, without creating a Release or uploading assets.

The sequence is permitted only after the full snapshot and exact landed-main
gate. It must leave stable `v0.3.0` and every older tag/Release untouched. It
does not create alpha.3.

```bash
aoa release audit /srv/AbyssOS --phase postpublish --repo Dionysus --strict --json
```

The postpublish audit must prove exactly one campaign Release/tag remains:
alpha.2 is annotated and peels to exact landed `main`, the existing Release ID
is retained, its body equals the canonical alpha.2 section, assets are empty,
alpha.2 is prerelease, and stable `v0.3.0` remains the latest stable Release.
The final full tag/Release census must equal the pre-mutation census except
for the explicitly authorized alpha.1 deletion and alpha.2 identity/body
reconciliation.

## Federation helper boundary

`aoa-sdk` PR [#263](https://github.com/8Dionysus/aoa-sdk/pull/263) landed exact
SemVer prerelease support before the alpha.1 publication. The installed shared
route supports the exact alpha.2 identity; no stable alias is permitted. The
owner-local `scripts/release_publish.py` remains a compatibility/reference
helper for a genuinely absent target and refuses an existing mismatched tag.
The one-time target-only reconciliation above is the owner-documented route
for this already-published campaign target and preserves the existing Release
ID rather than publishing a second Release.

The owner route remains subject to the common distinction between source
landing, GitHub checks, tag, Release publication, artifact admission, runtime
health, proof, deployment, and human acceptance. This source release proves
only its public source and release-surface identity.

## Recovery and migration

If the one-time alpha.2 reconciliation fails after a tag object/ref effect,
preserve the exact observed state and stop mutation until the existing alpha.2
Release can be reconciled. Do not create another Release or alpha.3. After the
final postpublish proof, future product or release corrections require a new
owner-approved immutable version; an editorial erratum may update only the
corresponding existing Release body from corrected canonical source.
Former seed-garden consumers must migrate to their actual owner repositories;
The former `legacy/` tree is available through the immutable source recorded in
[DION-D-0005](decisions/DION-D-0005-seed-history-outside-current-tree.md), not in
the current checkout. `pre-archive-2026-07-23` remains an earlier operational
archaeology/recovery reference only.
