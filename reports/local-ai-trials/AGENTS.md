# AGENTS.md

Local guidance for `reports/local-ai-trials/` in `Dionysus`.

Read the root `AGENTS.md` first. This folder only adds rules for mirrored local-AI trial reports.

## Scope

This folder stores durable human+AI-readable mirrors of bounded local trial runs.

Use it for:

- one Markdown report per executed case
- one Markdown digest per wave
- compact README-level orientation for the mirror

Do not use it for:

- raw runtime truth
- private host artifacts
- secret-bearing render output
- hidden machine-readable leaderboards

## Local contract

- Keep one file per executed case using `YYYY-MM-DD.<program-id>.<wave-id>.<case-id>.md`.
- Keep wave digests named like `W0-runtime-index.md`, `W1-routing-index.md`, and so on.
- Preserve the fixed report sections and YAML frontmatter.
- Keep wording curated and bounded. This mirror explains a local run; it does not become a new sovereign source.
- Link back to local runtime artifacts in `abyss-stack` instead of copying them here.

## Change rules

- Keep reports public-safe and reviewable.
- Do not move JSON truth packets into `Dionysus`.
- Do not let mirrored wording replace `aoa-evals`, `abyss-stack`, or target-repo doctrine.
- If a wave fails, keep the failure report fully visible rather than replacing it with a vague summary.

## Validate

Run:

```bash
python scripts/validate_seed_surfaces.py
```

Then manually verify report naming, local artifact links, and the boundary between local runtime truth and mirrored Markdown.
