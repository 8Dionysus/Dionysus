# DION-D-0005: Seed history outside the current tree

Status: accepted

## Context

The former seed garden was frozen on 2026-07-23. Its retained `legacy/`
subtree is historical evidence, not an interview protocol, portrait contract,
current queue, or runtime. Keeping it in the ordinary checkout exposes 448
historical files and competing instructions to navigation and indexing.

## Decision

Remove `legacy/` from the current source tree. Preserve original content,
paths, chronology, and provenance in Git, rather than moving the same files
into another current archive directory. This changes archive placement, not
the recorded history or the authority of current owner repositories.

No seed dispatcher is revived and no archive service or new runtime is added.
The current interview and portrait surfaces remain unchanged. Historical
release records and the one-time alpha.2 release campaign gate retain their
original scope; this retirement is not a release-preparation operation.

## Recovery

The exact pre-retirement source is commit
`dbc39628971f52549ec48f49a0589bf7ee9f618a` in this repository.

| Former path | Immutable source | Files | Tree object |
| --- | --- | ---: | --- |
| `legacy/` | [Frozen seed garden](https://github.com/8Dionysus/Dionysus/tree/dbc39628971f52549ec48f49a0589bf7ee9f618a/legacy) | 448 | `ecb506ae4458c35d1cd24c388b34b752f4a8af7b` |

Resolve any former path as `<commit>:<original repository-relative path>`;
for example, `git show dbc39628971f52549ec48f49a0589bf7ee9f618a:legacy/README.md`.
For linked seed packets, inspect the entire historical tree at that commit,
so relative links retain their original meaning. The existing
`pre-archive-2026-07-23` tag remains the recovery route for earlier operational
machinery, not a substitute for this exact retained-tree snapshot.

All 448 tracked blobs were verified against this commit before retirement.
Normal validation does not require downloading Git history or restoring the
archive. A future historical investigation can obtain the commit on demand.
