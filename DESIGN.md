# Dionysus design

## Intent

A useful personal portrait is neither a raw autobiography nor a model's
personality verdict. It is a reviewed, revisable set of claims grounded in what
a person said, the concrete episodes they described, and the limits or
counterexamples they supplied.

Voice is the preferred interaction because a sustained conversation can reach
material that forms and checklists miss. Voice is not an authority signal:
transcribed words and explicit review are the evidence surface. The protocol
must also work in text or hybrid mode.

## Artifact layers

The layers must remain distinct:

1. **Conversation** — the live exchange and consent state.
2. **Raw capture** — audio or text capture, private by default.
3. **Transcript** — a reviewable record with stable evidence anchors.
4. **Evidence slice** — the smallest useful excerpt plus context.
5. **Candidate claim** — a scoped interpretation with alternatives and
   counterevidence.
6. **Reviewed claim** — accepted, edited, contested, or retired by the person.
7. **Projection** — a purpose-bounded view assembled from reviewed claim IDs.

Raw capture, transcripts, claims, and projections have different sensitivity
and retention needs. A future implementation must not collapse them into one
opaque vector store or conversation history.

## Instrument-assisted orientation

Non-clinical instruments may precede an interview when they add a distinct
question that the conversation can test. They remain a separate lane:

```text
exact authorized instrument and mode
  -> private result
  -> bounded hypotheses for inquiry
  -> episodes, conditions, and counterexamples
  -> candidate claims under human review
```

The result is not itself a portrait claim. Standardized wording, response
format, scoring, language, and administration mode must follow the admitted
source conditions. If a model paraphrases an item into natural conversation,
the result becomes an ordinary interview response and loses any standardized
score claim.

The public [instrument registry](instruments/README.md) records the current
Dionysus disposition and open gaps. It contains no items, scoring keys, norms,
or personal results.

## Local reflection workbook

The initial [text workbook](web/README.md) is a pre-interview interaction
prototype, not a standardized assessment surface. Its three passes use only
admitted Dionysus-authored elicitation or existing interview structure:
current personal strivings, selected narrative life scenes, and a countermap
for testing one self-description against exceptions and alternate readings.

The workbook keeps the epistemic direction visible:

```text
person's own text
  -> reflected themes and bounded questions
  -> later episode-based interview
  -> candidate claims under explicit human review
```

It does not reverse that direction by turning a response pattern into an
identity verdict. The summary can quote answers and ask about gaps such as high
importance with low perceived progress, but it cannot assert why the gap
exists.

The page is dependency-free and makes no network requests. Browser
`localStorage` enables pause and return but is unencrypted convenience storage,
not the future private vault. JSON export is an explicit person action and the
result is a private source artifact. A server, synchronization layer, or real
personal-data pilot remains deferred.

## Interview loop

Each interview follows a common conversational loop:

```text
consent and retention choice
  -> open prompt
  -> concrete episode
  -> motives, conditions, and consequences
  -> exception or counterexample
  -> interviewer reflects candidate claims
  -> person accepts, edits, contests, or defers
  -> retention and next-step close
```

The interviewer should pursue depth through concrete episodes and careful
reflection, not through diagnostic labels. Silence, uncertainty, contradiction,
and refusal are valid outputs.

## Interview family

The initial catalog defines five complementary forms:

- **baseline** establishes breadth and an initial vocabulary;
- **depth** follows one lens or recurring tension through concrete episodes;
- **counterportrait** searches for disconfirming evidence and hidden context;
- **refresh** asks what changed since a prior reviewed state;
- **event** captures the meaning of one consequential episode near its time.

These are protocol families, not fixed questionnaires. Versioned prompt packs
will come only after the conversational structure and review experience have
been tested.

## Portrait projections

The canonical material is the reviewed claim set, not a single master
biography. Initial projections are deliberately small:

- `KERNEL` — relatively durable values, tendencies, and conditions;
- `NOW` — current horizon, commitments, pressures, and open changes;
- `COUNTERWEIGHTS` — contradictions, contexts, and claims that must not be
  overgeneralized.

A projection is disposable and reproducible. It must declare its purpose,
source claim IDs, and review date.

## Deferred choices

This skeleton deliberately defers:

- voice transport and realtime interaction stack;
- transcription and speaker-segmentation providers;
- encrypted storage and key management;
- agent or MCP integration;
- prompt wording and interview pacing;
- a repository-owned standardized instrument or scoring implementation;
- claim comparison and longitudinal diff algorithms;
- selective context release into other systems.

Those choices require tested protocols, explicit threat modeling, and a private
data owner. The public repository can evolve without choosing them prematurely.
