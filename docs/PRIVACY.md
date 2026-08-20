# Privacy boundary

Dionysus is public protocol; personal material is private data.

## Never commit

- voice or video recordings;
- raw or edited transcripts from a real person;
- instrument responses, score reports, norm comparisons, or person-specific
  assessment metadata;
- personal claims, portrait projections, journals, or biographical notes;
- consent records containing identity or contact information;
- API keys, credentials, provider job IDs, or storage locators;
- embeddings or derived datasets that can reconstruct sensitive material.

The repository ignores `vault/` contents and common media extensions as a
last-line guard, not as a complete security control. A future real-data pilot
requires encrypted storage, access control, retention limits, deletion
semantics, backup policy, and a threat model.

## Local browser workbook

The static `web/` page has no backend, account, analytics, remote assets, or
network submission. It stores a resumable draft in browser `localStorage`.
That storage is origin-specific and not encrypted: other users or software
with access to the same browser profile may be able to read it.

Do not enter sensitive material on a shared or untrusted device. JSON export
and local deletion require explicit person actions. Exported files are private
personal artifacts and must not be committed; deleting the browser draft does
not delete a previously downloaded file. Browser storage is not the private
vault required for a real-data pilot.

## Consent is ongoing

Consent must specify:

- which modes are captured;
- which artifacts may be retained;
- the intended use;
- who or what may read them;
- when consent is renewed;
- how pause, export, correction, and deletion work.

Consent to a conversation is not consent to build a permanent profile or to
release it into other agents.

## Minimize by layer

Prefer the least revealing layer that serves the purpose:

1. a projection referencing reviewed claims;
2. reviewed claims without transcript text;
3. scoped evidence slices;
4. a transcript;
5. raw audio.

Downstream consumers should receive compact projections or selected claims,
never unrestricted vault access by default.

## Sensitive inference

The system must not derive psychological, health, identity, or credibility
claims from vocal prosody or other biometric cues. Interpretations based on
what a person says must remain scoped, reviewable, and contestable.

## Public examples

All committed examples are fictional contract fixtures. They must not be
lightly anonymized real material.
