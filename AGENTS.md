# Dionysus agent guidance

## Purpose

Dionysus owns interview protocols and evidence-grounded, human-reviewed
personal portrait formats. It should help a person articulate a changing
self-understanding without pretending that a model has discovered an
authoritative or complete identity.

## Owner boundary

This repository owns:

- conversational interview families and their evolution;
- local pre-interview reflection surfaces and their private export contract;
- evidence, language, license, and mode admission metadata for non-clinical
  instruments that may orient an interview;
- consent, evidence, claim, review, and projection contracts;
- compact portrait views derived from reviewed claims;
- the boundary between public protocol and private personal material.

This repository does not own:

- generic AoA memory or memo retention;
- `.aoa` session archives or transcript lifecycle;
- speech, transcription, or agent runtime infrastructure;
- the public `8Dionysus` profile;
- psychological diagnosis, test publishing, personality scoring, normative
  interpretation, or an AI replica of a person;
- automatic loading of a complete personal dossier into every agent session.

Route runtime capabilities to their stronger owners. Keep Dionysus transport
and provider neutral until a concrete integration is deliberately chosen.

## Safety and epistemic rules

- Never commit real audio, transcripts, personal claims, secrets, or identifying
  evidence. Put private working material under ignored `vault/`.
- Do not infer psychological traits from vocal prosody, appearance, or other
  biometric signals.
- Do not copy protected test items, forms, scoring keys, or norms without
  explicit redistribution rights.
- A standardized result may route interview questions, but it does not become
  a portrait claim without evidence and human review.
- Do not claim equivalence for a new language or voice mode without evidence
  for that exact form and use.
- A model-generated statement starts as a candidate claim, not a fact.
- Preserve the evidence reference, basis, confidence, scope, alternatives, and
  review state of every claim.
- Make contradiction visible. Do not force a single coherent portrait when the
  evidence is contextual or contested.
- Every derived portrait must cite claim IDs and state its purpose and review
  date.
- Keep fictional examples unmistakably fictional.

## Change discipline

Meaningful changes to topology, authority, privacy, or claim semantics require
a decision record under `docs/decisions/`.

Before landing a change, run:

```bash
python scripts/validate_skeleton.py
```
