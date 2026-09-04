# AGENTS.md

`Dionysus` is a frozen, read-only archive as of 2026-07-23.

## Archive boundary

This repository no longer owns an active seed queue, dispatch workflow,
planting protocol, MCP service, runtime, KAG provider, stats or eval port,
quest surface, or local skill family.

Treat every lifecycle label in the retained files as historical. In
particular, `opened`, `gated_next`, `staged`, and similar labels do not
authorize work and do not describe current owner-repository state.

## Reading route

- For archive-wide archaeology or interpretation of former queue states, start
  with `README.md`.
- For one named artifact, start with the relevant `*_wave.manifest.json` or
  `seed-registry.yaml` entry, then inspect the exact seed and a matching file
  under `reports/planting/` when present.
- Return to the current owning repository, which is the only source of live
  truth. Use the archive README for broader topology only when that context is
  needed.

## Preservation rules

- Prefer analysis over edits.
- Preserve original seed text, filenames, paths, chronology, and provenance.
- Do not add new seeds, revive queue semantics, or restore removed machinery.
- Do not treat archived seed content as current AoA, ToS, runtime, SDK, or
  owner-repository doctrine.
- Use `pre-archive-2026-07-23` or commit `8529c00` when removed operational
  material is needed for historical analysis.
- Route new work directly to the repository that owns its meaning.

There is intentionally no executable repository validation gate after the
freeze. For archive-integrity inspection, use read-only Git checks such as
`git diff --check`, `git fsck --full --strict`, and targeted path/history
inspection.
