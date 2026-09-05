# Changelog

All notable changes to `Dionysus` are documented here in a human-first form.
The release ledger is part of the public record; it is not a substitute for
the source history.

## [Unreleased]

- Retired the frozen seed-garden `legacy/` subtree from the current checkout;
  DION-D-0005 preserves the exact commit, original paths, and recovery route.
- Agent guidance now routes the skeleton check through an on-demand
  `VALIDATION.md` surface that is itself required by the public topology.

## [0.4.0-alpha.2] - 2026-08-23

### Summary

- This is the sole campaign prerelease: it consolidates the complete material
  union of alpha.1 and alpha.2 into the existing `v0.4.0-alpha.2` identity;
  no alpha.3 or second campaign Release is created.
- It preserves the immutable alpha.1 tag/body divergence as an explicit
  historical erratum while making the final alpha.2 tag, changelog, Release
  body, and history agree with the exact landed source.
- It retains every capability, fix, migration, validation, limitation,
  non-claim, erratum, release carrier, and historical identity from both
  campaign prereleases in the nested conservation record below.
- It remains a source-only prerelease; stable `v0.3.0` remains the latest
  stable GitHub Release and no package or runtime artifact is published.

### Added

- Five named skeleton interview families—baseline, depth, counterportrait,
  refresh, and event—with shared consent, retention, evidence, review, and
  close behavior.
- Separate `interview-session` and `portrait-claim` schemas with fictional
  fixtures, evidence and counterevidence references, alternatives, review
  state, and supersession fields.
- An evidence-, rights-, language-, population-, and mode-aware instrument
  registry. `admitted`, `external-only`, `pilot`, and `excluded` remain
  explicit dispositions; the registry does not contain test items, scoring
  keys, norms, responses, or personal results.
- A dependency-free Russian local reflection workbook with current-strivings,
  life-story, and counterexample passes, bounded follow-up questions,
  pause/resume, explicit JSON export, and explicit local reset.
- Accepted decisions `DION-D-0001`, `DION-D-0002`, and `DION-D-0003`, plus a
  public/private boundary and fictional-only examples.
- An owner-local prerelease gate and publisher that bind the annotated tag,
  canonical changelog body, exact landed `main`, prerelease marker, and
  postpublish identity, including workbook syntax and static HTTP smoke.
- The alpha.2 release-contract correction surfaces: exact SemVer prerelease
  identity, the immutable alpha.1 baseline record, and the 9/9 campaign
  first-parent reconciliation below.
- A lossless alpha.1/alpha.2 conservation record carrying the prior tagged
  changelog bodies and prior GitHub Release bodies verbatim inside this
  canonical alpha.2 history.

### Changed

- The active owner boundary separates conversation, private capture,
  transcript, evidence slice, candidate claim, reviewed claim, and projection.
- Current documentation and CI validate only active Dionysus surfaces;
  `legacy/` remains preservation material and is excluded from active search
  and sparse validation.
- Instrument use remains a narrow hypothesis route. A result can suggest a
  question, but cannot become a portrait claim without evidence, alternatives,
  counterevidence, scope, and explicit human review.
- The active release marker and owner gate continue to name `v0.4.0-alpha.2`;
  the gate now uses stable `v0.3.0` as its durable baseline because the
  alpha.1 public ref is removed by this explicitly authorized consolidation.
- The former alpha.1 top-level changelog section is nested as conserved
  historical material here, so one canonical alpha.2 changelog/body/history
  carries the whole campaign.
- Contract versions under `interviews/`, `schemas/`, and `instruments/`
  remain `0.1.0`; they are API contract versions and are not mass-rewritten
  to the repository release version.

### Fixed

- The alpha.1 tag-to-Release/changelog identity mismatch is retained as a
  disclosed historical fact rather than silently rewritten or lost.
- The final alpha.2 Release body is derived from the exact landed canonical
  alpha.2 changelog section and is byte-consistent with it.
- The owner gate accounts for all nine campaign first-parent commits through
  the prior alpha.2 carrier, while the final reconsolidation carrier remains
  release-only and outside that product ledger.
- The target-only reconciliation removes only alpha.1 and retargets the
  existing alpha.2 Release; stable `v0.3.0` and all older refs/Releases remain
  unchanged.
- Public examples and the workbook route contain no real personal material,
  protected instrument content, standardized scores, or hidden dependencies.
- A repeatable local HTTP smoke checks browser-serving and no-network claims
  rather than inferring them from a successful Python validator alone.

### Deprecated

- The former seed-garden, dispatch, generated KAG family, MCP/runtime,
  stats/eval/memo/quest, and local-skill surfaces are retired from active
  Dionysus use. Retained files are historical only.
- Protocol IDs ending in `-v0` and all current catalog entries remain
  `skeleton`; they are not validated questionnaires.

### Removed

- The old active seed-garden machinery, generated KAG family, former release
  helper, seed-surface CI, and former ports were removed during the archive and
  recharter transition.
- The public alpha.1 GitHub Release and tag are removed only as the authorized
  duplicate campaign carrier; their exact identity and content remain in the
  digest-bound recovery snapshot and the historical conservation blocks below.
- No compatibility adapter is provided from former seed-route consumers to
  the portrait-laboratory contracts.

### Security

- No real audio, transcript, claims, scores, responses, credentials, or
  identifying evidence is included. Public fixtures are fictional, and the
  ignored `vault/` directory retains only its boundary documentation.
- The workbook has no backend, accounts, analytics, remote assets, network
  submission, or provider. Browser drafts use unencrypted origin-local
  storage; exported JSON remains private personal material.
- The repository does not claim encrypted storage, access control,
  retention/backup policy, threat-model completion, clinical validity,
  standardized score equivalence, or biometric/prosodic inference capability.
- No secret, sibling repository, protected `aoa-session-memory` GitHub
  surface, archived route, or unrelated active work is part of this repair.

### Compatibility and Migration

- The archive/recharter is a breaking active-surface change from `v0.3.0`.
  Former seed-garden, KAG, MCP/runtime, stats/eval/memo/quest, and release
  helper consumers must migrate to their actual owner repositories or use
  `pre-archive-2026-07-23` and Git history for archaeology.
- The final campaign consumer target is the single immutable `v0.4.0-alpha.2`
  Release. Alpha.1's public carrier is not retained as a second campaign
  choice; its content is conserved here and in the recovery ledger.
- Alpha.2 is a release-contract correction and consolidation, not a new
  protocol API or package ABI. Stable `v0.3.0` remains the migration baseline.
- `legacy/` is a read-only preservation boundary, not a compatibility adapter
  or current queue. There is no package ABI, network API, or stable external
  SDK in this alpha.
- The local workbook draft key is `dionysus.reflection-workbook.v0.1`;
  schema mismatch intentionally starts fresh local state rather than claiming
  an upgrade migration.

### Deployment, Observability, Recovery, and Rollback

- Deployment is limited to serving the static `web/` directory locally with
  Python's HTTP server. No hosted deployment, server-side store, runtime
  health, telemetry, or provider integration is part of this release.
- Recovery uses the digest-bound pre-mutation snapshot, stable `v0.3.0`, the
  sole final alpha.2 tag/Release, `legacy/`, and the `pre-archive-2026-07-23`
  recovery tag. The removed alpha.1 carrier is not recreated.
- Rollback execution is not claimed. A future product or release correction
  requires another owner-approved immutable version; this consolidation does
  not create alpha.3.

### Artifacts, Attestation, and Admission

- Dionysus produces no package, container, model, runtime, media, SBOM,
  signature, provenance sidecar, or durable artifact-registry record for this
  source-only release.
- The OS Abyss artifact trust loop is `not_applicable` for a Dionysus release
  artifact. No `allow`, `warn`, `deny`, `manual_review_required`, or `unknown`
  verdict is rewritten, collapsed, or promoted by this source repair.
- GitHub's generated source archive is a view of the exact final tag, not an
  admitted Dionysus-produced artifact or runtime proof.

### Validation

- `python scripts/validate_skeleton.py`
- `node --check web/app.js`
- `python scripts/smoke_workbook.py` (loopback-only static HTTP smoke)
- `python scripts/release_check.py` on exact landed `main`, using stable
  `v0.3.0` and the 9/9 campaign ledger.
- `git diff --check`
- GitHub `Repo Validation` on the release-repair PR and exact landed commit.
- Owner release preflight/reconciliation checks before mutation, followed by
  exact tag object/peel, existing Release ID, body, empty-assets, stable-latest,
  one-campaign-release, and unrelated-ref/Release conservation checks.
- The immutable pre-mutation recovery ledger is
  `sha256:2155d6ea057b6a6610e847641fa9b614181036ade3d10f5bcabfa66be363ac3f`;
  it records both tag objects, peeled commits, Release IDs/flags/bodies/assets,
  exact tagged changelog slices, complete campaign first-parent history, and
  merged PR coverage before mutation.
- The final report records source, CI, merge, tag, Release, artifact,
  runtime, proof, delivery, closure, and acceptance claims separately.

### First-Parent Reconciliation (9/9)

The exact campaign range is `v0.3.0..HEAD^` at the final alpha.2 carrier.
The final reconsolidation carrier itself is release-only and remains outside
this product/history range. Every prior campaign first-parent commit is listed
once; release carriers are retained as material identity records rather than
silently counted as product capabilities.

| # | Exact commit / PR | Meaning | Classification | Release treatment |
|---:|---|---|---|---|
| 1 | `8529c00c731ce560c0d8d2719fabbaf9dcbe222e` / [#150](https://github.com/8Dionysus/Dionysus/pull/150) | Portable KAG v3 manifest/shards, compatibility assembly, budgets, and pinned owner gate; 536 paths, mostly generated | `generated_churn` and intentionally superseded | Retained as historical migration material; #151 removed it from the active product. |
| 2 | `209cc4888be3896d5da6db1d25ca0ac42bb45786` / [#151](https://github.com/8Dionysus/Dionysus/pull/151) | Retire/archive the seed garden, remove old machinery, preserve historical material and recovery boundary | `changelog_worthy` | Included in Summary, Deprecated, Removed, Compatibility, and Recovery. |
| 3 | `6c463f6b89a11e85b37e2606525afc7d45005fbd` / [#152](https://github.com/8Dionysus/Dionysus/pull/152) | Recharter as a conversational self-portrait laboratory; add contracts, skeleton protocols, schemas, fixtures, validator, and DION-D-0001 | `changelog_worthy` | Included in Added, Changed, Security, and Notes. |
| 4 | `8c5c8ec960c507e097b37472e9e8353c369919bf` / [#153](https://github.com/8Dionysus/Dionysus/pull/153) | Flatten/isolate legacy material, remove former-role links, and scope validator/CI to active paths | `merged_with_151` | Included with #151; its active-search and CI consequence is stated separately. |
| 5 | `b2ed9208e5712e45be4eb08d65ed60826c745170` / [#154](https://github.com/8Dionysus/Dionysus/pull/154) | Instrument admission metadata, privacy boundary, local workbook, schemas/fixtures, and current validator | `changelog_worthy` | Included in Added, Changed, Security, and Validation. |
| 6 | `bddfc4618edf249f6bbe532846e76e3757695e12` / [#155](https://github.com/8Dionysus/Dionysus/pull/155) | Prepare the immutable alpha.1 release carrier and its source-only release surfaces | `release_carrier_history` | Conserved below; the public alpha.1 ref/Release is removed only after snapshot. |
| 7 | `e52439b6a8cdcdd718918de3ed88d2dd9367dc6c` / [#156](https://github.com/8Dionysus/Dionysus/pull/156) | Correct the documented alpha.1 publication route after publication | `changelog_worthy` | Included as a release-route erratum. |
| 8 | `785999b8bbf971976acac09a2fa813f446f275db` / [#157](https://github.com/8Dionysus/Dionysus/pull/157) | Anchor the release ledger at the immutable alpha.1 identity | `changelog_worthy` | Included as an immutable-identity/gate correction. |
| 9 | `4a50762a4a4f9b27a79ed081f467fd1099d918b4` / [#158](https://github.com/8Dionysus/Dionysus/pull/158) | Prepare the prior alpha.2 carrier and its exact release-contract body | `release_carrier_history` | Conserved below; the existing alpha.2 Release ID is reconciled, never duplicated. |

No commit in this range is hidden, duplicated, or silently reclassified. The
next landed commit is the final reconsolidation carrier and is checked against
this exact prior range by the owner gate.

### Historical Campaign Material (Conserved)

This is the canonical alpha.2 history for the removed alpha.1 carrier and the
prior alpha.2 carrier. The blocks below preserve every nonblank material line
from the pre-mutation tagged changelog slices and GitHub Release bodies. The
digest-bound snapshot remains the recovery authority for exact bytes, line
hashes, Release IDs, tag objects, peeled commits, and assets.

| Historical source | Release ID | Tag object | Peeled commit | Assets | Body SHA-256 |
|---|---:|---|---|---:|---|
| alpha.1 | `375088635` | `b66a913dcc69f3c06ae3242bf7b61093e78998d0` | `bddfc4618edf249f6bbe532846e76e3757695e12` | 0 | `sha256:6eb5d6a2424a7720e05abf17dfdbcfddd0d80085192e822332a0960f0bf36504` |
| alpha.2 pre-reconciliation | `375135773` | `fb48f995ae1d7e8e5480f99b701686ac82abe632` | `4a50762a4a4f9b27a79ed081f467fd1099d918b4` | 0 | `sha256:263bdcf791cd49ff18082c8c7af8824a163ddc7885843a47efc4082216c7c5fe` |

#### Alpha.1 tagged CHANGELOG body (verbatim)

```markdown
### Summary

- This prerelease starts the new Dionysus line as a voice-first,
  evidence-grounded laboratory for a small, human-reviewed portrait over time.
- It retires the former seed-garden and dispatch product from the active owner
  surface while preserving its material under `legacy/` for historical recovery.
- It adds explicit interview, consent, evidence, claim-review, instrument
  admission, privacy, and local-reflection contracts without claiming a finished
  interview system.
- It is a source-only alpha: the public tag and GitHub Release carry no package,
  runtime, model, media, or binary artifact.

### Added

- Five named skeleton interview families—baseline, depth, counterportrait,
  refresh, and event—with shared consent, retention, evidence, review, and
  close behavior.
- Separate `interview-session` and `portrait-claim` schemas with fictional
  fixtures, evidence and counterevidence references, alternatives, review
  state, and supersession fields.
- An evidence-, rights-, language-, population-, and mode-aware instrument
  registry. `admitted`, `external-only`, `pilot`, and `excluded` remain
  explicit dispositions; the registry does not contain test items, scoring
  keys, norms, responses, or personal results.
- A dependency-free Russian local reflection workbook with current-strivings,
  life-story, and counterexample passes, bounded follow-up questions,
  pause/resume, explicit JSON export, and explicit local reset.
- Accepted decisions `DION-D-0001`, `DION-D-0002`, and `DION-D-0003`, plus a
  public/private boundary and fictional-only examples.
- An owner-local prerelease gate and publisher that bind the annotated tag,
  canonical changelog body, exact landed `main`, prerelease marker, and
  postpublish identity. The gate includes workbook syntax and static HTTP
  smoke coverage.

### Changed

- The active owner boundary now separates conversation, private capture,
  transcript, evidence slice, candidate claim, reviewed claim, and projection.
- Current documentation and CI validate only active Dionysus surfaces;
  `legacy/` remains preservation material and is excluded from active search
  and sparse validation.
- Instrument use is now a narrow hypothesis route. A result can suggest a
  question, but cannot become a portrait claim without evidence, alternatives,
  counterevidence, scope, and explicit human review.
- The release marker is aligned across `README.md`, `ROADMAP.md`, the dated
  changelog section, the owner release route, and the exact publish plan.
- Schema/catalog/registry contract versions remain `0.1.0`; they are API
  contract versions and are intentionally not rewritten to the repository
  release version.

### Fixed

- Prevented public examples and the workbook route from embedding real
  personal material, protected instrument content, standardized scores, or
  hidden owner/runtime dependencies.
- Preserved the former seed-garden tree and recovery references without
  leaving its queue, dispatch, KAG, MCP, runtime, stats, eval, memo, quest, or
  local-skill semantics active in the new owner surface.
- Added a repeatable local HTTP smoke so browser-serving and no-network claims
  are checked rather than inferred from a successful Python validator alone.

### Deprecated

- The former seed-garden, dispatch, generated KAG family, MCP/runtime,
  stats/eval/memo/quest, and local-skill surfaces are retired from active
  Dionysus use. Retained files are historical only.
- Protocol IDs ending in `-v0` and all current catalog entries remain
  `skeleton`; they are not validated questionnaires.

### Removed

- The old active seed-garden machinery, generated KAG family, former release
  helper, seed-surface CI, and former ports were removed during the archive and
  recharter transition.
- No compatibility adapter is provided from former seed-route consumers to the
  portrait-laboratory contracts.

### Security

- No real audio, transcript, claims, scores, responses, credentials, or
  identifying evidence is included. Public fixtures are fictional, and the
  ignored `vault/` directory retains only its boundary documentation.
- The workbook has no backend, accounts, analytics, remote assets, network
  submission, or provider. Browser drafts use unencrypted origin-local
  storage; exported JSON remains private personal material.
- The repository does not claim encrypted storage, access control,
  retention/backup policy, threat-model completion, clinical validity,
  standardized score equivalence, or biometric/prosodic inference capability.

### Compatibility and Migration

- The archive/recharter is a breaking active-surface change from `v0.3.0`.
  Former seed-garden, KAG, MCP/runtime, stats/eval/memo/quest, and release
  helper consumers must migrate to their actual owner repositories or use
  `pre-archive-2026-07-23` and Git history for archaeology.
- `legacy/` is a read-only preservation boundary, not a compatibility adapter
  or current queue. There is no package ABI, network API, or stable external
  SDK in this alpha.
- The local workbook draft key is `dionysus.reflection-workbook.v0.1`;
  schema mismatch intentionally starts fresh local state rather than claiming
  an upgrade migration.

### Deployment, Observability, Recovery, and Rollback

- Deployment is limited to serving the static `web/` directory locally with
  Python's HTTP server. No hosted deployment, server-side store, runtime
  health, telemetry, or provider integration is part of this release.
- Recovery is through the clean Git tag, GitHub source archive, `legacy/`, and
  the `pre-archive-2026-07-23` recovery tag. The release publisher refuses to
  move a mismatched target tag.
- Rollback execution is not claimed. A future correction requires a new
  owner-approved version; runtime rollback and live health belong to stronger
  owners.

### Artifacts, Attestation, and Admission

- This is a source-only GitHub prerelease. GitHub's generated source archive is
  a view of the exact tag, not a Dionysus-produced package or attestation.
- No package, container, model, runtime, media, SBOM, signature, provenance
  sidecar, or durable artifact-registry record is produced or consumed by this
  release. The OS Abyss artifact trust route is therefore not applicable to a
  release artifact; a bounded empty-registry trust query remains unknown and
  fail-closed for any hypothetical consumer.
- No runtime, installation, fit, proof, admission, deployment, health, or
  human-acceptance claim follows from this source release.

### Validation

- `python scripts/validate_skeleton.py`
- `node --check web/app.js`
- `python scripts/smoke_workbook.py` (loopback-only static HTTP smoke)
- `python scripts/release_check.py` (exact baseline, first-parent ledger,
  clean synchronized `main`, privacy boundary, and owner validators)
- `git diff --check`
- GitHub `Repo Validation` on the release-prep PR and exact landed release
  commit
- Exact owner-local prerelease dry-run before publication, then tag/commit
  identity, prerelease/latest marker, canonical body, empty-assets, and
  postpublish audit after publication
- First-parent reconciliation: the five product commits from `v0.3.0` through
  the parent of the release-preparation commit are accounted for below. The
  release-preparation commit itself is the tag commit and is intentionally
  outside that product range, matching the repository's prior release
  convention.

### First-Parent Reconciliation (5/5)

The exact range is `v0.3.0..HEAD^` at the release-preparation commit. Each
first-parent commit is classified once; release-only metadata is not presented
as a product capability.

| # | Exact commit / PR | Meaning | Classification | Release treatment |
|---:|---|---|---|---|
| 1 | `8529c00c731ce560c0d8d2719fabbaf9dcbe222e` / [#150](https://github.com/8Dionysus/Dionysus/pull/150) | Portable KAG v3 manifest/shards, compatibility assembly, budgets, and pinned owner gate; 536 paths, mostly generated | `generated_churn` and intentionally superseded | Recorded here as historical migration evidence only; #151 removed it from the active product. |
| 2 | `209cc4888be3896d5da6db1d25ca0ac42bb45786` / [#151](https://github.com/8Dionysus/Dionysus/pull/151) | Retire/archive the seed garden, remove old machinery, preserve historical material and recovery boundary | `changelog_worthy` | Included in Summary, Deprecated, Removed, Compatibility, and Recovery. |
| 3 | `6c463f6b89a11e85b37e2606525afc7d45005fbd` / [#152](https://github.com/8Dionysus/Dionysus/pull/152) | Recharter as a conversational self-portrait laboratory; add contracts, skeleton protocols, schemas, fixtures, validator, and DION-D-0001 | `changelog_worthy` | Included in Summary, Added, Changed, Security, and Notes. |
| 4 | `8c5c8ec960c507e097b37472e9e8353c369919bf` / [#153](https://github.com/8Dionysus/Dionysus/pull/153) | Flatten/isolate legacy material, remove former-role links, and scope validator/CI to active paths | `merged_with_151` | Included with #151 because it completes the archive boundary; its active-search and CI consequence is stated separately. |
| 5 | `b2ed9208e5712e45be4eb08d65ed60826c745170` / [#154](https://github.com/8Dionysus/Dionysus/pull/154) | Instrument admission metadata, privacy boundary, local workbook, schemas/fixtures, and current validator | `changelog_worthy` | Included in Added, Changed, Security, Validation, and Notes. |

No commit in the reconciled product range is an unexplained duplicate or
unclassified internal noise. The release-preparation tag commit is a separate
release-only carrier and is verified by the owner-local gate and postpublish
receipt rather than being counted as another product change.

### Notes

- This alpha is a prerelease of a new 0.x owner surface, not a 1.0 identity
  system. The nearest reasonable follow-up is `v0.4.0-beta.1` only after the
  Phase 1 evidence named in `ROADMAP.md` exists.
- Voice transport, transcription, encrypted vault/storage, private pilot,
  agent/MCP integration, claim comparison, selective context release,
  deployment, observability, and rollback automation are deferred.
- Instrument owners and cited evidence remain authoritative; the registry
  records only a narrow Dionysus disposition.
- `aoa-session-memory` is protected and untouched. `aoa-routing` and
  `abyss-stack_old` are archived/maintenance boundaries and were not unarchived
  or republished.
- The installed federation helper's current parser accepts only stable
  `X.Y.Z` changelog headings and would otherwise publish the wrong `v0.4.0`.
  This prerelease therefore uses the owner-local prerelease route; that shared
  helper compatibility gap is recorded as a federation follow-up, not hidden
  by a stable alias.
```

#### Alpha.1 GitHub Release body (verbatim)

```text
Released: 2026-08-22

Canonical changelog: [CHANGELOG.md](https://github.com/8Dionysus/Dionysus/blob/main/CHANGELOG.md)

## Highlights
- This prerelease starts the new Dionysus line as a voice-first, evidence-grounded laboratory for a small, human-reviewed portrait over time.
- It retires the former seed-garden and dispatch product from the active owner surface while preserving its material under `legacy/` for historical recovery.
- It adds explicit interview, consent, evidence, claim-review, instrument admission, privacy, and local-reflection contracts without claiming a finished interview system.
- It is a source-only alpha: the public tag and GitHub Release carry no package, runtime, model, media, or binary artifact.

## Full Release Notes
### Summary

- This prerelease starts the new Dionysus line as a voice-first,
  evidence-grounded laboratory for a small, human-reviewed portrait over time.
- It retires the former seed-garden and dispatch product from the active owner
  surface while preserving its material under `legacy/` for historical recovery.
- It adds explicit interview, consent, evidence, claim-review, instrument
  admission, privacy, and local-reflection contracts without claiming a finished
  interview system.
- It is a source-only alpha: the public tag and GitHub Release carry no package,
  runtime, model, media, or binary artifact.

### Added

- Five named skeleton interview families—baseline, depth, counterportrait,
  refresh, and event—with shared consent, retention, evidence, review, and
  close behavior.
- Separate `interview-session` and `portrait-claim` schemas with fictional
  fixtures, evidence and counterevidence references, alternatives, review
  state, and supersession fields.
- An evidence-, rights-, language-, population-, and mode-aware instrument
  registry. `admitted`, `external-only`, `pilot`, and `excluded` remain
  explicit dispositions; the registry does not contain test items, scoring
  keys, norms, responses, or personal results.
- A dependency-free Russian local reflection workbook with current-strivings,
  life-story, and counterexample passes, bounded follow-up questions,
  pause/resume, explicit JSON export, and explicit local reset.
- Accepted decisions `DION-D-0001`, `DION-D-0002`, and `DION-D-0003`, plus a
  public/private boundary and fictional-only examples.
- An owner-local prerelease gate and publisher that bind the annotated tag,
  canonical changelog body, exact landed `main`, prerelease marker, and
  postpublish identity. The gate includes workbook syntax and static HTTP
  smoke coverage.

### Changed

- The active owner boundary now separates conversation, private capture,
  transcript, evidence slice, candidate claim, reviewed claim, and projection.
- Current documentation and CI validate only active Dionysus surfaces;
  `legacy/` remains preservation material and is excluded from active search
  and sparse validation.
- Instrument use is now a narrow hypothesis route. A result can suggest a
  question, but cannot become a portrait claim without evidence, alternatives,
  counterevidence, scope, and explicit human review.
- The release marker is aligned across `README.md`, `ROADMAP.md`, the dated
  changelog section, the owner release route, and the exact publish plan.
- Schema/catalog/registry contract versions remain `0.1.0`; they are API
  contract versions and are intentionally not rewritten to the repository
  release version.

### Fixed

- Prevented public examples and the workbook route from embedding real
  personal material, protected instrument content, standardized scores, or
  hidden owner/runtime dependencies.
- Preserved the former seed-garden tree and recovery references without
  leaving its queue, dispatch, KAG, MCP, runtime, stats, eval, memo, quest, or
  local-skill semantics active in the new owner surface.
- Added a repeatable local HTTP smoke so browser-serving and no-network claims
  are checked rather than inferred from a successful Python validator alone.

### Deprecated

- The former seed-garden, dispatch, generated KAG family, MCP/runtime,
  stats/eval/memo/quest, and local-skill surfaces are retired from active
  Dionysus use. Retained files are historical only.
- Protocol IDs ending in `-v0` and all current catalog entries remain
  `skeleton`; they are not validated questionnaires.

### Removed

- The old active seed-garden machinery, generated KAG family, former release
  helper, seed-surface CI, and former ports were removed during the archive and
  recharter transition.
- No compatibility adapter is provided from former seed-route consumers to the
  portrait-laboratory contracts.

### Security

- No real audio, transcript, claims, scores, responses, credentials, or
  identifying evidence is included. Public fixtures are fictional, and the
  ignored `vault/` directory retains only its boundary documentation.
- The workbook has no backend, accounts, analytics, remote assets, network
  submission, or provider. Browser drafts use unencrypted origin-local
  storage; exported JSON remains private personal material.
- The repository does not claim encrypted storage, access control,
  retention/backup policy, threat-model completion, clinical validity,
  standardized score equivalence, or biometric/prosodic inference capability.

### Compatibility and Migration

- The archive/recharter is a breaking active-surface change from `v0.3.0`.
  Former seed-garden, KAG, MCP/runtime, stats/eval/memo/quest, and release
  helper consumers must migrate to their actual owner repositories or use
  `pre-archive-2026-07-23` and Git history for archaeology.
- `legacy/` is a read-only preservation boundary, not a compatibility adapter
  or current queue. There is no package ABI, network API, or stable external
  SDK in this alpha.
- The local workbook draft key is `dionysus.reflection-workbook.v0.1`;
  schema mismatch intentionally starts fresh local state rather than claiming
  an upgrade migration.

### Deployment, Observability, Recovery, and Rollback

- Deployment is limited to serving the static `web/` directory locally with
  Python's HTTP server. No hosted deployment, server-side store, runtime
  health, telemetry, or provider integration is part of this release.
- Recovery is through the clean Git tag, GitHub source archive, `legacy/`, and
  the `pre-archive-2026-07-23` recovery tag. The release publisher refuses to
  move a mismatched target tag.
- Rollback execution is not claimed. A future product or release correction
  requires a new owner-approved version; this editorial post-release erratum
  does not create or move a version. Runtime rollback and live health belong to
  stronger owners.

### Artifacts, Attestation, and Admission

- This is a source-only GitHub prerelease. GitHub's generated source archive is
  a view of the exact tag, not a Dionysus-produced package or attestation.
- No package, container, model, runtime, media, SBOM, signature, provenance
  sidecar, or durable artifact-registry record is produced or consumed by this
  release. The OS Abyss artifact trust route is therefore not applicable to a
  release artifact; a bounded empty-registry trust query remains unknown and
  fail-closed for any hypothetical consumer.
- No runtime, installation, fit, proof, admission, deployment, health, or
  human-acceptance claim follows from this source release.

### Validation

- `python scripts/validate_skeleton.py`
- `node --check web/app.js`
- `python scripts/smoke_workbook.py` (loopback-only static HTTP smoke)
- `python scripts/release_check.py` (exact baseline, first-parent ledger,
  clean synchronized `main`, privacy boundary, and owner validators)
- `git diff --check`
- GitHub `Repo Validation` on the release-prep PR and exact landed release
  commit
- Installed shared `aoa release` preflight and dry-run before publication,
  then tag/commit identity, prerelease/latest marker, canonical body,
  empty-assets, and strict shared postpublish audit after publication
- First-parent reconciliation: the five product commits from `v0.3.0` through
  the parent of the release-preparation commit are accounted for below. The
  release-preparation commit itself is the tag commit and is intentionally
  outside that product range, matching the repository's prior release
  convention.

### First-Parent Reconciliation (5/5)

The exact range is `v0.3.0..HEAD^` at the release-preparation commit. Each
first-parent commit is classified once; release-only metadata is not presented
as a product capability.

| # | Exact commit / PR | Meaning | Classification | Release treatment |
|---:|---|---|---|---|
| 1 | `8529c00c731ce560c0d8d2719fabbaf9dcbe222e` / [#150](https://github.com/8Dionysus/Dionysus/pull/150) | Portable KAG v3 manifest/shards, compatibility assembly, budgets, and pinned owner gate; 536 paths, mostly generated | `generated_churn` and intentionally superseded | Recorded here as historical migration evidence only; #151 removed it from the active product. |
| 2 | `209cc4888be3896d5da6db1d25ca0ac42bb45786` / [#151](https://github.com/8Dionysus/Dionysus/pull/151) | Retire/archive the seed garden, remove old machinery, preserve historical material and recovery boundary | `changelog_worthy` | Included in Summary, Deprecated, Removed, Compatibility, and Recovery. |
| 3 | `6c463f6b89a11e85b37e2606525afc7d45005fbd` / [#152](https://github.com/8Dionysus/Dionysus/pull/152) | Recharter as a conversational self-portrait laboratory; add contracts, skeleton protocols, schemas, fixtures, validator, and DION-D-0001 | `changelog_worthy` | Included in Summary, Added, Changed, Security, and Notes. |
| 4 | `8c5c8ec960c507e097b37472e9e8353c369919bf` / [#153](https://github.com/8Dionysus/Dionysus/pull/153) | Flatten/isolate legacy material, remove former-role links, and scope validator/CI to active paths | `merged_with_151` | Included with #151 because it completes the archive boundary; its active-search and CI consequence is stated separately. |
| 5 | `b2ed9208e5712e45be4eb08d65ed60826c745170` / [#154](https://github.com/8Dionysus/Dionysus/pull/154) | Instrument admission metadata, privacy boundary, local workbook, schemas/fixtures, and current validator | `changelog_worthy` | Included in Added, Changed, Security, Validation, and Notes. |

No commit in the reconciled product range is an unexplained duplicate or
unclassified internal noise. The release-preparation tag commit is a separate
release-only carrier and is verified by the owner-local gate and postpublish
receipt rather than being counted as another product change.

### Post-release Correction

This correction was added after the immutable `v0.4.0-alpha.1` tag and GitHub
Release were published. The annotated tag object
`b66a913dcc69f3c06ae3242bf7b61093e78998d0` and its peeled commit
`bddfc4618edf249f6bbe532846e76e3757695e12` remain unchanged; this source
correction is not part of that tagged commit.

- [aoa-sdk PR #263](https://github.com/8Dionysus/aoa-sdk/pull/263) landed the
  prerelease support in the shared `aoa release` helper before publication.
- The exact `v0.4.0-alpha.1` release was published through the installed shared
  `aoa release publish` route. The owner-local `scripts/release_publish.py`
  was not the publication route for this release.
- The earlier publication-route note was incorrect and is superseded by this
  correction; the immutable tag and its release identity were not rewritten.

### Notes

- This alpha is a prerelease of a new 0.x owner surface, not a 1.0 identity
  system. The nearest reasonable follow-up is `v0.4.0-beta.1` only after the
  Phase 1 evidence named in `ROADMAP.md` exists.
- Voice transport, transcription, encrypted vault/storage, private pilot,
  agent/MCP integration, claim comparison, selective context release,
  deployment, observability, and rollback automation are deferred.
- Instrument owners and cited evidence remain authoritative; the registry
  records only a narrow Dionysus disposition.
- `aoa-session-memory` is protected and untouched. `aoa-routing` and
  `abyss-stack_old` are archived/maintenance boundaries and were not unarchived
  or republished.
- The publication-route correction above records the exact shared helper and
  release command used for this alpha. It does not claim runtime, proof, or
  human acceptance, and it does not alter the immutable tag.
```

#### Alpha.2 tagged CHANGELOG body before reconsolidation (verbatim)

```markdown
### Summary

- This corrective prerelease publishes the already-landed release-semantic
  correction as a new immutable identity instead of redefining `v0.4.0-alpha.1`.
- It closes the alpha.1 tag-to-canonical changelog identity defect while
  preserving alpha.1's tag, GitHub Release, and disclosed post-release erratum.
- It remains a source-only prerelease; stable `v0.3.0` remains the latest stable
  GitHub Release and no package or runtime artifact is published.

### Added

- A new immutable `v0.4.0-alpha.2` release surface for the two landed
  post-alpha.1 release-contract corrections.
- A complete `First-Parent Reconciliation (2/2)` ledger covering the exact
  semantic correction commits without counting this release carrier as a third
  product change.

### Changed

- The active release marker now names `v0.4.0-alpha.2` across `README.md`,
  `ROADMAP.md`, the canonical changelog, and the owner release gate.
- The owner release gate now treats immutable `v0.4.0-alpha.1` as the baseline
  and anchors the correction ledger at the exact new release tag after landing.
- The documented publication route remains the installed shared `aoa release`
  preflight, dry-run, publish, and strict postpublish sequence.

### Fixed

- The release body for alpha.2 is derived from this exact tagged changelog
  section, so its canonical source and GitHub Release body are byte-consistent.
- The post-release semantic correction is represented by a new version rather
  than by moving alpha.1 or pretending its tagged source contained later edits.
- The owner gate's first-parent range now covers only the two landed correction
  commits after alpha.1: PR #156 and PR #157.

### Deprecated

- No protocol, schema, catalog, instrument, or interview surface is deprecated
  by this corrective prerelease.

### Removed

- No public Dionysus surface is removed by this corrective prerelease.

### Security

- No real audio, transcript, claims, scores, responses, credentials, or
  identifying evidence is included; the existing public/private boundary is
  unchanged.
- No secret, personal material, sibling repository, protected
  `aoa-session-memory` GitHub surface, archived route, or runtime state is part
  of this release change.

### Compatibility and Migration

- Alpha.2 is a release-contract correction, not a new protocol API or package
  ABI. Consumers of alpha.1 may continue to resolve that immutable historical
  release; consumers needing the corrected release semantics should use alpha.2.
- The alpha.1 tag and GitHub Release remain the prior prerelease identity, and
  stable `v0.3.0` remains the stable migration baseline.
- No compatibility adapter, provider pin, or cross-repository dependency is
  introduced.

### Deployment, Observability, Recovery, and Rollback

- This remains a source-only GitHub prerelease with no hosted deployment,
  runtime activation, health, telemetry, or provider integration claim.
- Recovery uses the immutable alpha.1 and alpha.2 tags and GitHub source
  archives. Existing tags are never moved or recreated by this route.
- Rollback execution is not claimed; any future product or release correction
  requires another owner-approved immutable version.

### Artifacts, Attestation, and Admission

- Dionysus produces no package, container, model, runtime, media, SBOM,
  signature, provenance sidecar, or durable artifact-registry record for this
  source-only release.
- The OS Abyss artifact trust loop is therefore `not_applicable` for a
  release artifact here; no `allow`, `warn`, `deny`, `manual_review_required`,
  or `unknown` verdict is rewritten or promoted.
- GitHub's generated source archive is a view of the exact tag, not an admitted
  Dionysus-produced artifact or runtime proof.

### Validation

- `python scripts/validate_skeleton.py`
- `node --check web/app.js`
- `python scripts/smoke_workbook.py` (loopback-only static HTTP smoke)
- `python scripts/release_check.py` on exact landed `main` with alpha.1 as the
  immutable baseline and the alpha.2 tag as the release carrier
- `git diff --check`
- GitHub `Repo Validation` on the release-prep PR and exact landed release
  commit
- Installed shared `aoa release` strict preflight and dry-run before
  publication, then exact annotated tag/commit identity, prerelease marker,
  stable-latest marker, canonical body, empty-assets, and strict postpublish
  audit after publication
- First-parent reconciliation: the two post-alpha.1 semantic correction
  commits are accounted for below; the alpha.2 release-preparation commit is a
  release-only carrier outside that product range.

### First-Parent Reconciliation (2/2)

The exact range is `v0.4.0-alpha.1..HEAD^` before the alpha.2 release-prep
commit is tagged. Each first-parent correction commit is classified once.

| # | Exact commit / PR | Meaning | Classification | Release treatment |
|---:|---|---|---|---|
| 1 | `e52439b6a8cdcdd718918de3ed88d2dd9367dc6c` / [#156](https://github.com/8Dionysus/Dionysus/pull/156) | Correct the documented alpha.1 publication route after the immutable release had been published; align the canonical erratum and release instructions with the installed shared helper | `changelog_worthy` | Included as the release-route correction; alpha.1 tag and Release remain unchanged. |
| 2 | `785999b8bbf971976acac09a2fa813f446f275db` / [#157](https://github.com/8Dionysus/Dionysus/pull/157) | Anchor the release ledger before the immutable alpha.1 tag so later semantic documentation corrections are not misclassified as product commits | `changelog_worthy` | Included as the immutable-identity/gate correction; the alpha.2 release carrier remains outside the product range. |

No commit in this two-commit correction range is hidden, duplicated, or
reclassified as a new product capability. The release-preparation commit is a
separate carrier verified by the owner gate and shared postpublish route.

### Notes

- Alpha.2 is still a prerelease of the new 0.x owner surface, not a 1.0
  identity. A future beta requires the Phase 1 evidence named in `ROADMAP.md`.
- Voice transport, transcription, encrypted vault/storage, private pilot,
  agent/MCP integration, claim comparison, selective context release,
  deployment, observability, and rollback automation remain deferred.
- Publication proves source, tag, GitHub Release, and release-body identity
  only; it does not prove artifact admission, deployment, runtime health, proof,
  terminal closure, master acceptance, or human acceptance.
- `aoa-session-memory` remains protected and untouched; `aoa-routing` and
  `abyss-stack_old` remain archived and were not unarchived or republished.
```

#### Alpha.2 GitHub Release body before reconsolidation (verbatim)

```text
Released: 2026-08-23

Canonical changelog: [CHANGELOG.md](https://github.com/8Dionysus/Dionysus/blob/main/CHANGELOG.md)

## Highlights
- This corrective prerelease publishes the already-landed release-semantic correction as a new immutable identity instead of redefining `v0.4.0-alpha.1`.
- It closes the alpha.1 tag-to-canonical changelog identity defect while preserving alpha.1's tag, GitHub Release, and disclosed post-release erratum.
- It remains a source-only prerelease; stable `v0.3.0` remains the latest stable GitHub Release and no package or runtime artifact is published.

## Full Release Notes
### Summary

- This corrective prerelease publishes the already-landed release-semantic
  correction as a new immutable identity instead of redefining `v0.4.0-alpha.1`.
- It closes the alpha.1 tag-to-canonical changelog identity defect while
  preserving alpha.1's tag, GitHub Release, and disclosed post-release erratum.
- It remains a source-only prerelease; stable `v0.3.0` remains the latest stable
  GitHub Release and no package or runtime artifact is published.

### Added

- A new immutable `v0.4.0-alpha.2` release surface for the two landed
  post-alpha.1 release-contract corrections.
- A complete `First-Parent Reconciliation (2/2)` ledger covering the exact
  semantic correction commits without counting this release carrier as a third
  product change.

### Changed

- The active release marker now names `v0.4.0-alpha.2` across `README.md`,
  `ROADMAP.md`, the canonical changelog, and the owner release gate.
- The owner release gate now treats immutable `v0.4.0-alpha.1` as the baseline
  and anchors the correction ledger at the exact new release tag after landing.
- The documented publication route remains the installed shared `aoa release`
  preflight, dry-run, publish, and strict postpublish sequence.

### Fixed

- The release body for alpha.2 is derived from this exact tagged changelog
  section, so its canonical source and GitHub Release body are byte-consistent.
- The post-release semantic correction is represented by a new version rather
  than by moving alpha.1 or pretending its tagged source contained later edits.
- The owner gate's first-parent range now covers only the two landed correction
  commits after alpha.1: PR #156 and PR #157.

### Deprecated

- No protocol, schema, catalog, instrument, or interview surface is deprecated
  by this corrective prerelease.

### Removed

- No public Dionysus surface is removed by this corrective prerelease.

### Security

- No real audio, transcript, claims, scores, responses, credentials, or
  identifying evidence is included; the existing public/private boundary is
  unchanged.
- No secret, personal material, sibling repository, protected
  `aoa-session-memory` GitHub surface, archived route, or runtime state is part
  of this release change.

### Compatibility and Migration

- Alpha.2 is a release-contract correction, not a new protocol API or package
  ABI. Consumers of alpha.1 may continue to resolve that immutable historical
  release; consumers needing the corrected release semantics should use alpha.2.
- The alpha.1 tag and GitHub Release remain the prior prerelease identity, and
  stable `v0.3.0` remains the stable migration baseline.
- No compatibility adapter, provider pin, or cross-repository dependency is
  introduced.

### Deployment, Observability, Recovery, and Rollback

- This remains a source-only GitHub prerelease with no hosted deployment,
  runtime activation, health, telemetry, or provider integration claim.
- Recovery uses the immutable alpha.1 and alpha.2 tags and GitHub source
  archives. Existing tags are never moved or recreated by this route.
- Rollback execution is not claimed; any future product or release correction
  requires another owner-approved immutable version.

### Artifacts, Attestation, and Admission

- Dionysus produces no package, container, model, runtime, media, SBOM,
  signature, provenance sidecar, or durable artifact-registry record for this
  source-only release.
- The OS Abyss artifact trust loop is therefore `not_applicable` for a
  release artifact here; no `allow`, `warn`, `deny`, `manual_review_required`,
  or `unknown` verdict is rewritten or promoted.
- GitHub's generated source archive is a view of the exact tag, not an admitted
  Dionysus-produced artifact or runtime proof.

### Validation

- `python scripts/validate_skeleton.py`
- `node --check web/app.js`
- `python scripts/smoke_workbook.py` (loopback-only static HTTP smoke)
- `python scripts/release_check.py` on exact landed `main` with alpha.1 as the
  immutable baseline and the alpha.2 tag as the release carrier
- `git diff --check`
- GitHub `Repo Validation` on the release-prep PR and exact landed release
  commit
- Installed shared `aoa release` strict preflight and dry-run before
  publication, then exact annotated tag/commit identity, prerelease marker,
  stable-latest marker, canonical body, empty-assets, and strict postpublish
  audit after publication
- First-parent reconciliation: the two post-alpha.1 semantic correction
  commits are accounted for below; the alpha.2 release-preparation commit is a
  release-only carrier outside that product range.

### First-Parent Reconciliation (2/2)

The exact range is `v0.4.0-alpha.1..HEAD^` before the alpha.2 release-prep
commit is tagged. Each first-parent correction commit is classified once.

| # | Exact commit / PR | Meaning | Classification | Release treatment |
|---:|---|---|---|---|
| 1 | `e52439b6a8cdcdd718918de3ed88d2dd9367dc6c` / [#156](https://github.com/8Dionysus/Dionysus/pull/156) | Correct the documented alpha.1 publication route after the immutable release had been published; align the canonical erratum and release instructions with the installed shared helper | `changelog_worthy` | Included as the release-route correction; alpha.1 tag and Release remain unchanged. |
| 2 | `785999b8bbf971976acac09a2fa813f446f275db` / [#157](https://github.com/8Dionysus/Dionysus/pull/157) | Anchor the release ledger before the immutable alpha.1 tag so later semantic documentation corrections are not misclassified as product commits | `changelog_worthy` | Included as the immutable-identity/gate correction; the alpha.2 release carrier remains outside the product range. |

No commit in this two-commit correction range is hidden, duplicated, or
reclassified as a new product capability. The release-preparation commit is a
separate carrier verified by the owner gate and shared postpublish route.

### Notes

- Alpha.2 is still a prerelease of the new 0.x owner surface, not a 1.0
  identity. A future beta requires the Phase 1 evidence named in `ROADMAP.md`.
- Voice transport, transcription, encrypted vault/storage, private pilot,
  agent/MCP integration, claim comparison, selective context release,
  deployment, observability, and rollback automation remain deferred.
- Publication proves source, tag, GitHub Release, and release-body identity
  only; it does not prove artifact admission, deployment, runtime health, proof,
  terminal closure, master acceptance, or human acceptance.
- `aoa-session-memory` remains protected and untouched; `aoa-routing` and
  `abyss-stack_old` remain archived and were not unarchived or republished.
```

### Notes

- This alpha is a prerelease of a new 0.x owner surface, not a 1.0 identity.
  A future beta requires the Phase 1 evidence named in `ROADMAP.md`.
- Voice transport, transcription, encrypted vault/storage, private pilot,
  agent/MCP integration, claim comparison, selective context release,
  deployment, observability, and rollback automation remain deferred.
- Publication and reconciliation prove source, tag, GitHub Release, and
  release-body identity only; they do not prove artifact admission, deployment,
  runtime health, proof, terminal closure, master acceptance, or human
  acceptance.
- `aoa-session-memory` remains protected and untouched; `aoa-routing` and
  `abyss-stack_old` remain archived and were not unarchived or republished.
