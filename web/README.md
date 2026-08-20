# Local reflection workbook

`web/` is a dependency-free Russian pre-interview page. It contains three
short, non-diagnostic passes:

1. current personal strivings;
2. selected life-story scenes;
3. a countermap for testing one easy self-description against context and
   counterexamples.

The page produces no personality type, standardized score, percentile, rank,
or portrait claim. It reflects the person's wording and routes questions into
a later reviewed interview.

## Run locally

From the repository root:

```bash
python -m http.server 8765 --bind 127.0.0.1 --directory web
```

Then open `http://127.0.0.1:8765/`. Keep the same address and port when
returning to a draft because browser storage is origin-specific.

The page has no network requests, remote assets, analytics, accounts, or
backend. Draft answers are stored in the browser's unencrypted `localStorage`.
The person must explicitly request JSON export or local deletion. Exported JSON
is private personal material and must not be committed to this repository.

## Method boundary

- `personal-strivings` permits Dionysus-authored, non-normative goal
  elicitation.
- `life-story-interview-ii` is used only as an adaptable narrative interview
  design source; the page claims no validated coding or score.
- `counterportrait-v0` is a Dionysus interview protocol for recovering
  exceptions and alternate explanations.

No `external-only`, `pilot`, or `excluded` instrument content is embedded.
