На **22 марта 2026** я бы качала `aoa-agents` не в сторону ещё одного “agent framework repo”, а в сторону **протокольного позвоночника** всей твоей экосистемы. Самая живая связка сейчас выглядит так: **MCP внутрь, A2A наружу, durable orchestration посередине**. MCP уже встроен в актуальный tool-layer у OpenAI через remote MCP/connectors, Anthropic тоже умеет подключать удалённые MCP servers через Messages API, а A2A оформляется как стандарт межагентной совместимости и уже живёт как отдельная спецификация. ([OpenAI Платформа][1])

Судя по твоей нынешней архитектуре, у тебя уже есть верная ось: `Tree of Sophia` как источник знания, `aoa-agents` как orchestration-layer, `aoa-memo` / `aoa-playbooks` / `aoa-kag` как специализированные органы, и `abyss-stack` как почва под ногами. Поэтому `aoa-agents` лучше делать не “одним умным агентом”, а **runtime-слоем**, который собирает остальные части в единую ткань.

Первый и главный ход: **преврати `aoa-*`-репозитории в first-class servers**. `aoa-memo` я бы делала MCP server-ом для памяти, `aoa-kag` MCP server-ом для retrieval/reasoning, а `aoa-playbooks` не пассивным складом markdown, а **MCP prompt/tool server-ом** с исполняемыми сценариями. Это особенно сильно потому, что MCP-prompts уже являются отдельным примитивом протокола, а в Claude Code они могут всплывать как slash-команды. То есть playbook-слой становится не документацией, а живым интерфейсом действия. ([Model Context Protocol][2])

`aoa-agents` при этом должен стать **orchestration runtime-ом**: он потребляет MCP servers, решает, кого и когда звать, а вовне говорит по A2A там, где агент действительно живёт отдельно. Не выноси каждый внутренний модуль в сеть. Документация ADK довольно мудро разделяет **local sub-agents** и **remote A2A agents**: локальные быстры, дешевы и хороши для внутренней композиции; A2A нужен, когда это уже отдельный сервис со своими правами, ключами, SLA или собственной жизнью. Для внешних AoA-агентов я бы сразу ввела **Agent Card** и публиковала его по `/.well-known/agent-card.json`. ([Google GitHub][3])

Второй ход: **жёстко разведи память, знание и процедуры**. Для `aoa-memo` natural shape сейчас не “один vector store на все случаи”, а три слоя памяти: **semantic memory** для устойчивых фактов и профилей, **episodic memory** для траекторий, удачных и неудачных действий, и **procedural memory** для правил работы, которые почти естественно утекают в `aoa-playbooks`. LangGraph как раз формализует short-term vs long-term memory и отдельно проговаривает semantic, episodic и procedural memory. А состояние текущего выполнения стоит держать отдельно, либо через OpenAI Conversations/Responses, либо через checkpoints/persistence в LangGraph. Иначе агент начнёт путать “кто я” с “что я сейчас делаю”. ([Документация LangChain][4])

Третий ход: **подними `aoa-kag` от обычного RAG до reasoning substrate**. В KAG уже есть движение к multi-index базе с `Outline`, `Summary`, `KnowledgeUnit`, `AtomicQuery`, `Chunk` и `Table`, плюс MCP-интеграция reasoning/Q&A. У GraphRAG, в свою очередь, есть `Local Search`, `Global Search` и `DRIFT Search` поверх entity/relationship/community structure. Для твоего мира это прямо по нерву: local нужен для конкретных сущностей и фрагментов, global для больших синтезов и архитектоники смысла, drift для разведки неожиданных связей, где и рождается живая мысль. ([GitHub][5])

Четвёртый ход: **дай `aoa-agents` долговечность, а не только “ум”**. Если брать framework-layer, LangGraph сейчас силён именно в long-running stateful workflows, persistence и human-in-the-loop. Там уже встроена логика `interrupt/resume` и решения `approve` / `edit` / `reject`. На OpenAI стороне похожую дисциплину стоит держать через stateful Responses/Conversations, compaction для длинных окон и ограничение риска через `require_approval` и `allowed_tools` для MCP-инструментов. Это база, если AoA будет писать код, трогать файлы, ходить в веб или работать с внешними сервисами. ([Документация LangChain][6])

Пятый ход: **ставь evals раньше, чем новых агентов**. OpenAI прямо советует trace grading для workflow-level ошибок, а не только оценку финального текста. Если хочешь слой, не привязанный к одному вендору, LangSmith сейчас удобен тем, что он framework-agnostic и поддерживает offline и online evaluation; при сильной тяге к приватности у него есть и self-hosted/standalone варианты, хотя это уже более тяжёлая артиллерия. Для AoA я бы не добавляла новый playbook или handoff без датасета, contract-теста и метрики на качество memory/retrieval. ([OpenAI Платформа][7])

Шестой ход, уже почти эстетический, но на деле очень практичный: **дай AoA глаза**. MCP Apps с января 2026 умеют возвращать интерактивные UI-компоненты прямо в диалог, а OpenAI Apps SDK строится поверх MCP. Это значит, что `aoa-agents` может стать не только текстовым оракулом, но и интерфейсом с memory timeline, редактором playbooks, картой знаний и task dashboard. Для такого проекта это не косметика, а способ сделать архитектуру зримой. ([Model Context Protocol Blog][8])

По моделям я бы строила **гибридную иерархию**. `gpt-5.4` годится как главный planner/orchestrator для сложного reasoning и coding, `GPT-5.3-Codex` я бы отдала coding-agent’у для длинных репозиторных задач, `o3-deep-research` или `o4-mini-deep-research` поставила бы на исследовательские ветки, а под `abyss-stack` держала бы локальных или специализированных workers на open-weight моделях вроде `gpt-oss-20b` и `gpt-oss-120b`, если тебе важны приватность, автономность и собственный ритм вычисления. ([OpenAI Developers][9])

Если выбирать **один** путь, я выбираю такой: **протоколизируй AoA**. `aoa-agents` как runtime и handoff-layer, `aoa-memo` как memory MCP, `aoa-playbooks` как executable prompt/policy MCP, `aoa-kag` как retrieval/reasoning MCP, а межагентную федерацию выведи в A2A. Фреймворки ещё не раз поменяют кожу, а такие границы переживают линьку. ([OpenAI Платформа][1])

Порядок, с которого я бы начала, очень земной:

1. `aoa-memo` как первый MCP server
2. `aoa-playbooks` как MCP prompt/tool server
3. один A2A-exposed агент в `aoa-agents`
4. traces + evals
5. UI-слой поверх MCP Apps / Apps SDK

Так ты построишь не туман над бездной, а мост, который выдерживает шаг.

**Сводка для всех и ни для кого:** твоя сила в том, что ты мыслишь не фичами, а мирами. Риск тоже там же: мир может разрастись быстрее, чем его контракты. Лекарство простое и редкое: каждую красивую сущность заставь говорить по протоколу, помнить по слоям и отвечать по trace.

Следующим ходом я могу разложить это в **конкретный blueprint `aoa-agents`**: структуру репозитория, MCP/A2A-контракты, типы памяти и минимальный roadmap первой рабочей версии.

[1]: https://platform.openai.com/docs/guides/tools-remote-mcp "https://platform.openai.com/docs/guides/tools-remote-mcp"
[2]: https://modelcontextprotocol.io/legacy/concepts/prompts "https://modelcontextprotocol.io/legacy/concepts/prompts"
[3]: https://google.github.io/adk-docs/a2a/intro/ "https://google.github.io/adk-docs/a2a/intro/"
[4]: https://docs.langchain.com/oss/javascript/langgraph/memory "https://docs.langchain.com/oss/javascript/langgraph/memory"
[5]: https://github.com/OpenSPG/KAG/releases "https://github.com/OpenSPG/KAG/releases"
[6]: https://docs.langchain.com/oss/python/langgraph/overview "https://docs.langchain.com/oss/python/langgraph/overview"
[7]: https://platform.openai.com/docs/guides/agent-evals "https://platform.openai.com/docs/guides/agent-evals"
[8]: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/ "https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/"
[9]: https://developers.openai.com/api/docs/models "https://developers.openai.com/api/docs/models"








Да. Я прошла по твоим публичным слоям, и следующий ход для `aoa-agents` вижу очень чётко: не раздувать его в ещё один “всё-движок”, а сделать **исполняемым швом** между уже разведёнными границами. Сейчас у тебя `aoa-agents` владеет role/persona contracts и handoff posture, `aoa-playbooks` владеет сценарной композицией, `aoa-memo` владеет памятью и её доктриной, `aoa-kag` владеет производными knowledge-поверхностями, `aoa-routing` владеет навигацией, а `abyss-stack` владеет телом runtime и инфраструктуры. И во всех этих слоях публично видна одна и та же установка: это bootstrap-фаза, а не попытка сразу вырастить гигантский монолит. Значит, самый точный следующий ход для твоего проекта сейчас: **маленькое исполняемое ядро, которое читает чужие контракты, а не поглощает их**. ([GitHub][1])

Главное открытие здесь такое: у тебя уже есть **две ортогональные оси**, и они почти просятся в runtime. Первая ось отвечает на вопрос **кто действует по смыслу**: `architect`, `coder`, `reviewer`, `evaluator`, `memory-keeper`. Вторая отвечает на вопрос **какой режим усилия сейчас нужен**: `router`, `planner`, `executor`, `verifier`, `conductor`, `deep`, `archivist`. Следующий ход не в том, чтобы изобретать ещё одну роль, а в том, чтобы сделать движок, который **скрещивает role-axis и tier-axis в один исполняемый run**. ([GitHub][2])

Я бы зафиксировала сердцевину `aoa-agents` одной простой формулой:

```text
run
= task
+ route_hint
+ playbook
+ tier_state_machine
+ role_binding
+ skill_calls
+ eval_hooks
+ memory_writeback
```

И поверх этого дала бы `aoa-agents` такую надстройку:

```text
aoa-agents/
  runtime/
    registry_loader.py
    role_binder.py
    tier_engine.py
    playbook_loader.py
    skill_bridge.py
    eval_bridge.py
    memory_writeback.py
    kag_handoff.py
    checkpoint_io.py
  schemas/
    artifact.route_decision.schema.json
    artifact.bounded_plan.schema.json
    artifact.work_result.schema.json
    artifact.verification_result.schema.json
    artifact.transition_decision.schema.json
    artifact.deep_synthesis_note.schema.json
    artifact.distillation_pack.schema.json
  examples/
    long_horizon_reference_run/
    restartable_inquiry_reference_run/
```

Ключевой принцип здесь такой: runtime не придумывает второй source of truth, а читает уже существующие поверхности вроде `generated/agent_registry.min.json` и `generated/model_tier_registry.json`. ([GitHub][3])

Самые правильные первые сценарии для оживления у тебя уже написаны. Я бы делала **исполняемыми** не новые профили агентов, а прежде всего `AOA-P-0008 long-horizon-model-tier-orchestra` и `AOA-P-0009 restartable-inquiry-loop`. Первый уже почти идеально совпадает с tier-machine: там прямо перечислены `route_decision`, `bounded_plan`, `verification_result`, `transition_decision`, `distillation_pack` и точки handoff. Второй даёт то, чего почти всегда не хватает агентным системам: безопасную паузу, возобновление и честную работу с противоречиями вместо фальшивой непрерывности. После них я бы подключила `AOA-P-0006 self-agent-checkpoint-rollout` как safety spine и `AOA-P-0007 witness-to-compost-pilot` как мост от trace к осмысленному compost/canon pipeline. ([GitHub][4])

Практически это я бы связала так. Это уже моя рекомендуемая сборка, не текущий публичный контракт:

* `router + architect` → `route_decision`
* `planner + architect` → `bounded_plan`
* `executor + coder` → `work_result`
* `verifier + reviewer` → `verification_result`
* `conductor + architect/reviewer` → `transition_decision`
* `deep + evaluator/architect` → `deep_synthesis_note`
* `archivist + memory-keeper` → `distillation_pack`

Такой расклад очень хорошо ложится на твою нынешнюю модель tier-state `route -> plan -> do -> verify -> deep? -> distill` и не заставляет одну сущность незаметно стать всем сразу. ([GitHub][5])

Ещё одна важная вещь: **не прячь skills внутрь agent-profile**. В твоей публичной карте `aoa-skills` уже определён как слой bounded, reviewable workflows, а `aoa-playbooks` уже описывает `required_skill_families`, `participating_agents`, `evaluation_posture` и `memory_posture`. Значит, runtime должен делать так: playbook выбирает сценарий и нужные семейства навыков, `aoa-agents` решает кто из ролей их исполняет, а `aoa-skills` даёт конкретный bounded workflow. Это намного чище, чем превращать профили агентов в мешок скрытых prompt-ритуалов. ([GitHub][6])

То же с evals. `aoa-evals` у тебя уже позиционируется как proof-layer, а playbooks уже указывают eval anchors. Поэтому в `aoa-agents` нужен не новый “тайный судья”, а `eval_bridge`, который на каждом переходе run-а явно пишет: какие артефакты проверялись, какими anchors, с каким verdict. Иначе в системе появится красивый голос без доказательной кости. ([GitHub][7])

Самый тонкий участок у тебя, как и должно быть, это память. `aoa-memo` прямо говорит, что live working memory должна жить прежде всего в runtime-системах, а не превращать memory-layer в постоянную оперативную БД. При этом у тебя уже есть температуры `hot/warm/cool/cold/frozen`, object canon вроде `state_capsule`, `episode`, `claim`, `decision`, `pattern`, `bridge`, `audit_event`, а также lifecycle `captured -> proposed -> confirmed -> frozen -> superseded -> retracted -> archived`. Плюс в `AGENT_MEMORY_POSTURE` уже описаны права чтения и записи по ролям. Значит, я бы делала так: живой scratchpad держать внутри run-а, на checkpoint экспортировать `state_capsule`, переходы уровня approval/transition писать как `decision`, результаты работы и проверки мапить в `episode` и `audit_event`, а `distillation_pack` превращать не в “истину”, а в кандидатов для `claim/pattern/bridge` после review. И очень важно: для run-trace я бы не изобретала новый формат, а переиспользовала `WitnessTrace`; для pause/resume не изобретала бы новый контейнер, а переиспользовала `inquiry_checkpoint`. ([GitHub][8])

Есть ещё одно ограничение, которое я бы считала священным для AoA/ToS-связки: **не давай `aoa-agents` съесть routing или canon**. `aoa-routing` уже владеет навигацией и даже подхватывает `model_tier_registry` для task-to-tier hints, так что новый роутер внутри `aoa-agents` тебе не нужен. А `aoa-kag` уже сформулировал очень красивый закон: “AoA acts. ToS remembers. aoa-kag derives…”. Из этого почти автоматически следует дисциплина: executor не пишет канон напрямую, memory-keeper делает writeback в `aoa-memo`, а `aoa-kag` уже строит derived surfaces с сохранением provenance. Так твоя система будет расти как лес, а не как плющ, который душит собственные деревья. ([GitHub][9])

Если приземлить всё в **первый спринт**, я бы сделала только это:

1. Добавить в `aoa-agents` `runtime/` и 6 базовых artifact schemas для tier-machine.
2. Научить runtime читать registries, грузить playbook и собирать `role × tier` actor-instance.
3. Прогнать один эталонный end-to-end run через `AOA-P-0008`.
4. Добавить `checkpoint_io`, где trace хранится как `WitnessTrace`, а restart как `inquiry_checkpoint`.
5. Подключить `memory_writeback`, который уважает memory rights ролей и температуры `aoa-memo`.

Этого достаточно, чтобы `aoa-agents` перестал быть только хорошей хартией и стал **первым живым позвоночником** всей федерации.

Сводка для всех и ни для кого: у тебя уже есть не россыпь репозиториев, а почти этика архитектуры. Ты интуитивно строишь сущности, которые знают не только что они делают, но и чем они не являются. Это редкая сила. Следующий шаг для `aoa-agents` не в том, чтобы стать больше. Следующий шаг в том, чтобы стать исполняемым.

[1]: https://github.com/8Dionysus/aoa-agents/blob/main/CHARTER.md "https://github.com/8Dionysus/aoa-agents/blob/main/CHARTER.md"
[2]: https://github.com/8Dionysus/aoa-agents/blob/main/docs/AGENT_MODEL.md "https://github.com/8Dionysus/aoa-agents/blob/main/docs/AGENT_MODEL.md"
[3]: https://github.com/8Dionysus/aoa-agents "https://github.com/8Dionysus/aoa-agents"
[4]: https://github.com/8Dionysus/aoa-playbooks/blob/main/playbooks/long-horizon-model-tier-orchestra/PLAYBOOK.md "https://github.com/8Dionysus/aoa-playbooks/blob/main/playbooks/long-horizon-model-tier-orchestra/PLAYBOOK.md"
[5]: https://github.com/8Dionysus/aoa-agents/blob/main/docs/MODEL_TIER_MODEL.md "https://github.com/8Dionysus/aoa-agents/blob/main/docs/MODEL_TIER_MODEL.md"
[6]: https://github.com/8Dionysus/aoa-playbooks/blob/main/docs/PLAYBOOK_MODEL.md "https://github.com/8Dionysus/aoa-playbooks/blob/main/docs/PLAYBOOK_MODEL.md"
[7]: https://github.com/8Dionysus/aoa-evals "https://github.com/8Dionysus/aoa-evals"
[8]: https://github.com/8Dionysus/aoa-memo/blob/main/docs/MEMORY_MODEL.md "https://github.com/8Dionysus/aoa-memo/blob/main/docs/MEMORY_MODEL.md"
[9]: https://github.com/8Dionysus/aoa-routing "https://github.com/8Dionysus/aoa-routing"
