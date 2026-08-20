# DION-D-0002: Instrument registry and interview boundary

- Status: accepted
- Date: 2026-08-10

## Context

Structured non-clinical instruments can expose useful questions before a
voice interview: broad tendencies, value trade-offs, current goals, vocational
interests, or a reason to seek counterexamples. They can also create a false
identity authority if scores are copied directly into a portrait, if several
overlapping batteries are accumulated, or if a model silently rewrites a
validated item into conversational language.

Dionysus needs a research basis for selecting such methods without becoming a
test publisher, diagnostic service, scoring engine, or public store of personal
results.

## Decision

Add an `instruments/` surface that owns only Dionysus admission metadata:
intended role, exact evidence and owner sources, language posture, rights,
content posture, voice posture, interpretation limits, blocking gaps, and one
of four dispositions: `admitted`, `external-only`, `pilot`, or `excluded`.

Keep standardized assessment and conversational inquiry as separate lanes.
Standardized wording, order, response format, scoring, and mode remain fixed by
their source contract. Conversational adaptation may generate an interview
question but cannot retain the standardized score claim.

Instrument output is a private hypothesis source. It may route questions but
does not become a portrait claim without concrete evidence, scoped alternatives
and counterevidence, and explicit human review.

An interview-session manifest may carry metadata-only `orientation_refs` to a
private result so the route remains auditable. It must not embed responses or
scores.

Do not vendor item text, forms, scoring keys, norms, or manuals until explicit
redistribution rights and provenance are recorded. Do not call a voice form
equivalent without evidence for that exact form, language, population, and
mode.

## Consequences

- Dionysus can research and compare high-quality methods without presenting a
  pile of questionnaires as a finished portrait system.
- The initial foundation distinguishes traits, values, goals, interests,
  temperament, strengths, and narrative identity instead of collapsing them
  into one score.
- BFI-2, PVQ-RR, HEXACO, ATQ, and VIA remain external under their current
  permissions; IPIP-NEO-120 and O*NET remain pilot candidates until their named
  Russian and voice gaps close.
- Personal Strivings and Life Story Interview II are admitted only as
  non-normative elicitation and interview-design sources.
- Clinical instruments, biometric inference, and excluded typologies remain
  outside the owner boundary even if a future model can generate plausible
  interpretations from them.
