# Owner-Repo Reality Check

## Purpose

This note captures one hard lesson for working in `Dionysus`:

prep-pack staging truth is weaker than owner-repo planting truth.

## Core rule

Before treating a prep pack as the current queue, verify the owner repositories
directly.

Check:

- target docs surfaces
- schemas, examples, or generated artifacts named in the pack
- quest or validator anchors in the target repo
- recent planting commits or reports when available

## Why this matters

`Dionysus` intentionally preserves transport and lineage surfaces even after
owner repos land the main doctrine or contract slices.

So a file can still be present here as:

- replayable lineage
- staging memory
- archive candidate

without still being the next real planting target.

## Typical failure mode

The common mistake is:

1. read a root-level prep pack
2. see `priority`, `readiness`, or dependencies
3. assume the pack still describes current project need

That is unsafe.

Those fields are staging guidance only unless the owner repos still lack the
named surfaces.

## Structured note marker

Structured staging notes should carry:

- `lifecycle_status`
- `lifecycle_note`
- `reality_checked_at`

That marker is a readability aid, not a replacement for direct repo checks.
When reality changes upstream, update the marker in the same pass.
