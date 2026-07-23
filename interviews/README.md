# Interview family

The interview layer describes how a conversation gathers evidence and returns
interpretations to the person for review. It is voice-first but works in text
or hybrid form.

`catalog.toml` names the initial interview forms and the lenses they may use.
`session-contract.md` defines behavior shared by every form.

The catalog is deliberately not a prompt library yet. Good questions require
research, dry runs, and comparison. Adding dozens of plausible-sounding
questions now would make an untested script look authoritative.

## Initial forms

- **Baseline** — broad first pass across the relevant lenses.
- **Depth** — sustained inquiry into one lens, pattern, or tension.
- **Counterportrait** — active search for exceptions and alternate readings.
- **Refresh** — bounded review of what changed since a prior portrait state.
- **Event** — timely reflection on one consequential episode.

## Versioning

Protocol IDs are stable and versions are explicit. A substantive change to
question sequence, review behavior, consent, or retention creates a new
protocol version. Editorial clarification may update documentation without
changing an ID.

Protocol maturity must be stated as one of:

- `skeleton` — contract shape only;
- `draft` — prompts exist but have not passed comparative dry runs;
- `pilot` — used in consented, reviewed pilot sessions;
- `validated` — evidence supports a stated use under named conditions.

No protocol in the initial catalog is validated.
