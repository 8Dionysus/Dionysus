# Dionysus instrument registry guidance

## Purpose

This directory owns Dionysus admission metadata for non-clinical instruments
that may orient an interview. It does not own the cited instruments, their
scientific claims, a scoring service, or a person's results.

## Admission discipline

- Treat `registry.toml` as the current Dionysus disposition, not as stronger
  authority than an instrument owner, license, manual, or validation study.
- Pin an exact form, language, intended use, and administration mode. Evidence
  for one version or population does not automatically transfer to another.
- An `admitted` entry must have no unresolved blocking gaps for its narrowly
  stated role. A broader use requires a new review.
- `external-only` content stays at an official or otherwise authorized source.
- `pilot` does not mean ready for a real personal portrait. Before Phase 2 it
  permits only fictional or synthetic dry runs.
- Keep exclusions explicit. Do not quietly reintroduce a typology, diagnostic
  instrument, or biometric personality inference through interview wording.

## Content and privacy boundary

- Never copy item text, response forms, scoring keys, norms, or manuals into
  the repository without explicit redistribution rights.
- Never commit real responses, scores, interpretations, or person-specific
  instrument metadata. Those are private artifacts governed by the vault
  boundary.
- A score may route follow-up questions. It cannot become a portrait claim
  without concrete evidence, alternatives, scope, and human review.
- Do not claim that voice administration is equivalent to a validated form
  without evidence for that exact mode, wording, response format, language,
  and target population.

## Change rule

Every status change must update `reviewed_on`, cite current sources, explain
the changed evidence or permission, and pass `python scripts/validate_skeleton.py`.
