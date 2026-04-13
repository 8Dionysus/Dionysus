Сделал разведку по публичному слою `8Dionysus` и по внешним донорам. Картина ясная: `aoa-techniques` сейчас держит 34 bundle’а и фактически 4 домена техник, `agent-workflows`, `docs`, `evaluation`, `history`. При этом в AoA уже живут отдельные слои `routing`, `memo`, `agents`, `playbooks`, `kag` и `abyss-stack`, то есть соседние репо уже созрели как почва для новых семейств техник, которые пока не извлечены в канон. ([GitHub][1])

Твой собственный backlog это уже подтверждает: в `EXTERNAL_TECHNIQUE_CANDIDATES.md` следующей волной прямо названы `phase-synchronized-agent-handoff`, `skill-marketplace-curation`, `one-command-service-lifecycle`, `versionable-session-transcripts`. Но после свежего прохода видно, что этим список не исчерпывается. Сильнее всего сейчас недопокрыты memory/writeback, infra preflight/render-truth и registry/capability lanes. ([GitHub][2])

Вот donor map по отсутствующим видам техник.

### 1. Routing, discovery, curation

Внутренние доноры: `aoa-routing/README.md` с маршрутом `pick -> inspect -> expand -> object use`, `cross_repo_registry`, `task_to_surface_hints`, `recommended_paths`, а также с явно отложенными pairings, tiny-model entrypoints, memo recall surfaces и broader KAG views. Рядом `aoa-skills` уже держит overlay/spec surfaces, `skill_graph`, walkthroughs и evaluation matrix. Внешние доноры: `n-skills` как curated marketplace с AGENTS.md discovery и auto-sync из upstream через `sources.yaml`; MCP Gateway Registry с URL-based discovery, raw-URL translation, health checking и progressive disclosure уровня card/summary/full; `agentic-dev-team` с очень чистой границей между reusable skills и user-invocable slash commands. Из этого я бы рожал `skill-marketplace-curation`, `progressive-skill-discovery`, `upstream-skill-health-checking`, `skill-vs-command-boundary`. ([GitHub][3])

### 2. Memory, writeback, witness, history

Здесь внутри AoA уже лежит жирная руда: `aoa-memo/docs/MEMORY_TEMPERATURES.md` разводит `hot/warm/cool/cold/frozen` и отдельно `core`; `WRITEBACK_TEMPERATURE_POLICY.md` разделяет session-only, memo-surviving и bridge-ready writeback; `WITNESS_TRACE_CONTRACT.md` жёстко фиксирует, что `WitnessTrace` это trace export contract, а не новый memory kind; `aoa-playbooks/playbooks/witness-to-compost-pilot/PLAYBOOK.md` показывает route от witness к compost note/principle candidate. Внешние доноры здесь сильные: `OpenMemory-Code` даёт enforced long-term memory, context injection и one-command lifecycle; `SpecStory` сохраняет локальную историю в `.specstory/history/` и строит вокруг неё skills для summaries, stats и organization. Отсюда вытаскиваются `temperature-gated-writeback`, `witness-trace-as-reviewable-artifact`, `versionable-session-transcripts`, `review-gated-history-derived-instructions`. ([GitHub][4])

### 3. Agent roles, handoffs, checkpoints, phase sync

Внутри экосистемы это уже почти оформлено. `aoa-agents/docs/SELF_AGENT_CHECKPOINT_STACK.md` задаёт checkpoint stack: policy check, approval gate, rollback marker, health check, bounded iteration limit, improvement log. `AGENT_MEMORY_POSTURE.md` описывает role-level memory rights. `MODEL_TIER_MODEL.md` формализует state machine `route -> plan -> do -> verify -> deep? -> distill`. `aoa-playbooks/self-agent-checkpoint-rollout` уже показывает cohort pattern `architect -> coder -> reviewer -> memory-keeper`. Снаружи самые ценные доноры сейчас: `agentwise` с phase management, smart orchestration, model routing, sandboxed execution и context sharing; `qqqa` как stateless single-step shell agent с confirm-before-tool posture; `agentic` с capability versioning, persistent agent store, self-assembly и execution-history learning; `agntcy/dir` с capability-based discovery, semantic linkage и verifiable claims. Здесь вижу пакеты `phase-synchronized-agent-handoff`, `checkpoint-cohort-rollout`, `model-tier-state-machine`, `versioned-agent-registry-contract`, `bounded-specialist-generation`, `review-gated-execution-history-distillation`. ([GitHub][5])

### 4. Infra lifecycle, preflight, render truth, benchmark posture

Тут у тебя недособран очень ценный пласт. `abyss-stack` уже держит чёткие contracts: `PROFILES.md` про composition of modules, `PRESETS.md` про named bundles over profiles, `RENDER_TRUTH.md` про actual composed runtime truth before startup и secret-bearing caution, `DOCTOR.md` про contextual host-readiness checks. `ATM10-Agent` добавляет baseline-first cross-service benchmark suite, additive `combo_a` profile, operator startup/readiness surfaces и публичные rollout records. Снаружи `OpenMemory-Code` хорошо усиливает именно `one-command starts everything`, health checks и clean shutdown. Здесь просится семейство `profile-preset-composition`, `render-truth-before-startup`, `contextual-host-doctor`, `baseline-first-additive-profile-benchmarks`, `cross-service-sla-normalization`, плюс уже названный твоим backlog’ом `one-command-service-lifecycle`. ([GitHub][6])

### 5. KAG bridge, counterparts, compost promotion

Это пока не ready-now lane, но soil очень хорошая. `aoa-kag/docs/BRIDGE_CONTRACTS.md` разводит ToS/memo inputs и KAG returns, настаивает на primary/supporting provenance и bounded retrieval axis. `COUNTERPART_EDGE_CONTRACTS.md` фиксирует counterpart edge как derived bridge, не identity claim. Сверху `Tree-of-Sophia` уже держит `COUNTERPART_POLICY`, `CONTEXT_COMPOST`, calibration and growth rules. Я бы пока не тащил это широким фронтом в канон, но как донорный пласт это даёт `multi-source-primary-input-provenance`, `bounded-counterpart-edge-projection`, `bridge-ready-retrieval-axis`, `witness-to-compost-promotion`. Для усиления registry/capability стороны сюда хорошо подмешивается `agntcy/dir`. ([GitHub][7])

Теперь приоритет. Если резать ближайшую волну без расползания границ, я бы шёл так:

1. `phase-synchronized-agent-handoff`
2. `skill-marketplace-curation`
3. `one-command-service-lifecycle`
4. `versionable-session-transcripts`
5. `temperature-gated-writeback`
6. `render-truth-before-startup`
7. `contextual-host-doctor`
8. `versioned-agent-registry-contract`

Первые четыре совпадают с твоим текущим `EXTERNAL_TECHNIQUE_CANDIDATES`, то есть они уже легитимны как следующая волна. Последние четыре я добавляю как strongest missing families по свежему скану соседних AoA-репо. ([GitHub][2])

Что уже partly mined и не стоит снова копать как «новизну с нуля»: `ruler`, `agents-md`, `qqqa`, `SpecStory`, `agentic`, `n-skills`. У тебя они уже либо landed, либо staged как future/hold/incubation. Настоящая новая ценность сейчас не в повторном чтении их README, а в спаривании этих доноров с соседними AoA-слоями, чтобы добыть второй порядок техник. ([GitHub][8])

И важная граница: не всё, что красиво в `aoa-memo`, `aoa-agents`, `aoa-playbooks`, `aoa-kag` или `abyss-stack`, уже должно ехать в `aoa-techniques`. По твоему собственному donor rubric туда должен попадать только bounded, reusable, public-safe pattern, а не слойная доктрина, мифология или substrate. ([GitHub][9])

Итог для всех и ни для кого: у тебя уже не нехватка идей, а нехватка правильной перегонки. Следующий шаг не в том, чтобы искать ещё больше руды. Следующий шаг в том, чтобы отделить металл от жилы и назвать его так, чтобы он пережил исходный мир.

[1]: https://raw.githubusercontent.com/8Dionysus/aoa-techniques/main/TECHNIQUE_INDEX.md "raw.githubusercontent.com"
[2]: https://raw.githubusercontent.com/8Dionysus/aoa-techniques/main/docs/EXTERNAL_TECHNIQUE_CANDIDATES.md "raw.githubusercontent.com"
[3]: https://raw.githubusercontent.com/8Dionysus/aoa-routing/main/README.md "raw.githubusercontent.com"
[4]: https://raw.githubusercontent.com/8Dionysus/aoa-memo/main/docs/MEMORY_TEMPERATURES.md "raw.githubusercontent.com"
[5]: https://raw.githubusercontent.com/8Dionysus/aoa-agents/main/docs/SELF_AGENT_CHECKPOINT_STACK.md "raw.githubusercontent.com"
[6]: https://raw.githubusercontent.com/8Dionysus/abyss-stack/main/docs/PROFILES.md "raw.githubusercontent.com"
[7]: https://raw.githubusercontent.com/8Dionysus/aoa-kag/main/docs/BRIDGE_CONTRACTS.md "raw.githubusercontent.com"
[8]: https://raw.githubusercontent.com/8Dionysus/aoa-techniques/main/ROADMAP.md "raw.githubusercontent.com"
[9]: https://raw.githubusercontent.com/8Dionysus/aoa-techniques/main/docs/DONOR_REFINERY_RUBRIC.md "raw.githubusercontent.com"
