# Spark lane for Dionysus

This file only governs work started from `Spark/`.

The root `AGENTS.md` remains authoritative for repository identity, ownership boundaries, reading order, and validation commands. This local file only narrows how GPT-5.3-Codex-Spark should behave when used as the fast-loop lane.

If `SWARM.md` exists in this directory, treat it as queue / swarm context. This `AGENTS.md` is the operating policy for Spark work.

## Default Spark posture

- Use Spark for short-loop work where a small diff is enough.
- Start with a map: task, files, risks, and validation path.
- Prefer one bounded patch per loop.
- Read the nearest source docs before editing.
- Use the narrowest relevant validation already documented by the repo.
- Report exactly what was and was not checked.
- Escalate instead of widening into a broad architectural rewrite.

## Spark is strongest here for

- wave-manifest, registry, and closure-note linkage audits
- seed-surface and anchor integrity repairs
- planting-protocol, report-template, or navigation-overlay cleanup
- small nested-guidance or path-consistency fixes
- bounded preflight reviews for a planting slice before a larger move

## Do not widen Spark here into

- writing final target-repository doctrine here
- runtime or deployment detail that belongs elsewhere
- multi-wave rewrites without a manifest-anchored reason
- renaming seed vocabulary without explicit source-linked mapping

## Local done signal

A Spark task is done here when:

- the planting route is clearer and more source-linked
- AoA and ToS boundaries remain explicit
- filenames, anchors, and linked paths stayed stable or were updated coherently
- the repo entrypoint validator ran: `python scripts/validate_seed_surfaces.py`
- remaining planting or target-repo follow-up is reported explicitly

## Local note

Spark is valuable here as a planting preflight and linkage repair tool, not as a second home for landed doctrine.

## Reporting contract

Always report:

- the restated task and touched scope
- which files or surfaces changed
- whether the change was semantic, structural, or clarity-only
- what validation actually ran
- what still needs a slower model or human review
