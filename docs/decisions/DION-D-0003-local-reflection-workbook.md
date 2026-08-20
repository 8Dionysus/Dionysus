# DION-D-0003: Local reflection workbook

- Status: accepted
- Date: 2026-08-10

## Context

An interview benefits from deliberate prework, but a pile of standardized
questionnaires would make Dionysus look like a personality scoring service and
would import unresolved item, language, mode, and redistribution rights. A
person also needs a usable way to pause, revisit, inspect, export, or discard
long-form answers before any voice runtime or encrypted private vault exists.

## Decision

Add a dependency-free static `web/` surface for three Russian text passes:
current Personal Strivings, selected narrative life scenes inspired by Life
Story Interview II, and a countermap derived from `counterportrait-v0`.

Embed only Dionysus-authored prompts admitted by the instrument or interview
contracts. Do not embed external-only or pilot forms and do not calculate
standardized scores, types, percentiles, ranks, diagnoses, or automatic
portrait claims.

Keep the page local-only: no backend, network requests, accounts, analytics,
remote scripts, or remote assets. Save a resumable draft in browser
`localStorage`, state clearly that it is not encrypted, and require an explicit
person action for JSON export or deletion. Treat an exported workbook as a
private source artifact that must not be committed.

The summary may quote the person's answers and derive bounded interview
questions. It cannot silently promote either into a portrait claim; evidence,
counterevidence, scope, and explicit human review remain required.

## Consequences

- The text interaction and pacing can be tested before choosing a voice stack
  or private storage implementation.
- A person can complete modules in any order, skip questions, pause, revise,
  print, export, and delete without an account.
- Browser storage is a convenience boundary, not the Phase 2 encrypted vault;
  shared-device and origin-specific storage risks remain visible.
- Standardized trait, value, temperament, interest, and strength instruments
  remain outside this page until their exact registry gaps are closed.
- A future server, synchronization layer, real-data pilot, or automatic claim
  generation requires a new privacy and authority decision.
