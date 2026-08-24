# DION-D-0004: Single prerelease reconsolidation

Status: accepted for the v0.4.0-alpha.2 post-audit repair

## Context

The campaign left both `v0.4.0-alpha.1` and `v0.4.0-alpha.2` public, while
alpha.1's immutable tagged changelog and GitHub Release body described
different source slices. Recreating alpha.1, publishing alpha.3, or silently
discarding either slice would lose release history or create a second campaign
truth.

## Decision

`v0.4.0-alpha.2` is the sole campaign prerelease. Its canonical changelog and
Release body carry the zero-loss union of alpha.1 and alpha.2 material,
including capabilities, fixes, migrations, validation, limitations,
non-claims, errata, release carriers, and historical identities.

After the exact digest-bound pre-mutation snapshot and landed-main owner gates:

- remove only the alpha.1 GitHub Release and `refs/tags/v0.4.0-alpha.1`;
- reconcile the existing alpha.2 tag ref to the exact final landed `main` by
  an annotated tag object;
- retain and PATCH the existing alpha.2 Release ID rather than creating a
  second Release; and
- leave `v0.3.0`, every older tag/Release, assets, sibling repositories,
  protected GitHub surfaces, and unrelated work untouched.

No alpha.3 is part of this campaign. Future product or release corrections
require a separately approved immutable version.

## Claim boundary

Source, CI, merge, tag, GitHub Release, artifact admission, runtime,
semantic proof, delivery, closure, and owner/human acceptance remain separate
claims. Dionysus is source-only here; the artifact trust route is
`not_applicable`, and no artifact verdict is inferred from GitHub source
archives.

## Recovery

The pre-mutation snapshot and conservation ledger are the recovery authority
for the removed alpha.1 identity and the prior alpha.2 identity. A failed
target-only operation stops with the observed state; it does not create a
replacement Release or broaden the mutation set.
