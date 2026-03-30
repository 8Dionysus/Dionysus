# Local AI Trial Reports

This folder keeps durable human+AI-readable mirrors of bounded local model trials.

It is a mirror surface, not the owner of runtime truth.

Keep here:

- case-level Markdown reports
- wave-level Markdown digests

Keep out of here:

- raw runtime artifacts
- secret-bearing render output
- private host facts
- machine-readable truth packets that belong in `abyss-stack`

Runtime truth stays in:

- `/srv/abyss-stack/Logs/local-ai-trials/`

Durable program roots:

- `qwen-local-pilot-v1/`
  Original Ollama-backed `W0` through `W4` baseline.
- `langgraph-sidecar-pilot-v1/`
  Initial `W4` LangGraph comparison pilot on the baseline runtime.
- `qwen-llamacpp-pilot-v1/`
  `llama.cpp` promotion and parity mirrors for the promoted local backend path.
- `langgraph-sidecar-llamacpp-v1/`
  Early failed `llama.cpp` fixture-gate mirror kept visible as a reviewable failure.
- `langgraph-sidecar-llamacpp-promotion-gate/`
  Passing disposable `W4` fixture gate used in the final `llama.cpp` promotion path.
- `w5-langgraph-llamacpp-v1/`
  Long-horizon supervised pilot on promoted `llama.cpp + LangGraph`.
- `w6-bounded-autonomy-llamacpp-v1/`
  Bounded-autonomy pilot on the same promoted substrate.

Do not keep scratch or debug-only roots here as durable mirrors.
