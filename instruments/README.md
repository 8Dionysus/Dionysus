# Instrument registry

Dionysus uses instruments as maps for inquiry, not as verdicts about a person.
This directory records which non-clinical methods may orient an interview,
under which conditions, and what still blocks their use.

The registry contains no test items, scoring keys, norms, or personal results.
External authors and publishers retain authority over their instruments;
`registry.toml` records only the current Dionysus admission decision.

## Admission states

- `admitted` — suitable for the narrowly stated Dionysus role with no open
  blocking gap;
- `external-only` — potentially useful through an official or authorized
  external surface, but not vendored or administered by this repository;
- `pilot` — promising, but a named evidence, language, licensing, or mode gap
  blocks ordinary use;
- `excluded` — outside the portrait foundation or too weak for the stated use.

The complete gate is defined in [admission-contract.md](admission-contract.md).
The machine-readable disposition is [registry.toml](registry.toml).

## Initial foundation

The v0 registry supports a layered portrait rather than one totalizing test:

1. one dispositional-trait instrument, never two overlapping batteries by
   default;
2. values and current goals as distinct from traits;
3. interests only when work or creation is in scope;
4. narrative episodes and counterexamples as the evidence surface;
5. optional temperament or strengths modules only when they answer a concrete
   question not already covered.

For a Russian personal pilot, BFI-2 is the strongest current external trait
candidate in the registry. IPIP-NEO-120 is the stronger open-content direction,
but no Russian voice form is admitted yet. Personal Strivings and Life Story
Interview II are admitted only as non-normative design sources: they elicit
goals and episodes and do not yield an authoritative score.

## Two separate lanes

```text
standardized lane
  exact authorized form and mode
  -> private result
  -> bounded interview hypotheses

conversational lane
  open question
  -> concrete episode and context
  -> counterexample
  -> candidate claim
  -> human review
```

An interviewer may explain a standardized item but must not improvise a new
wording and continue reporting the old score. If conversational adaptation is
useful, it becomes an interview question and loses the standardized-score
claim.
