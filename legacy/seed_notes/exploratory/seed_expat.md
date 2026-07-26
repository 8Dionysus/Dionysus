Я прошлась по публичному профилю `8Dionysus` и по ключевым репозиториям. Каркас у тебя уже очень четкий: AoA как федерация явных слоев, а не монолит; `aoa-skills` как bounded и reviewable workflows; `aoa-evals` как portable proof surfaces; `aoa-memo` как explicit, provenance-aware, bounded memory; `aoa-kag` как graph-ready derived substrate; `aoa-agents` как role contracts; `abyss-stack` как local-first self-hosted тело системы. А `Tree-of-Sophia` уже описан как layered graph/tree с текстами, понятиями, тезисами, временным и цивилизационным контекстом, а также lineage-связями идей. ([GitHub][1])

Из этого вытекает очень жесткий фильтр. Тебе полезно не все “agentic”, а только то, что не размывает source of truth, не съедает соседние слои, работает в local/self-hosted posture, уважает provenance и хорошо ложится в eval-first цикл. Поэтому из всего обсужденного направления я бы выделила не “самоэволюцию вообще”, а три главные жилы: память, graph-aware retrieval и workflow memory. Тяжелую RL/self-evolving автоматику я бы пока держала за стеклом. ([GitHub][1])

**Что брать в ядро сейчас**

**1. Mem0 OSS. Да, это твой прямой кандидат для `aoa-memo`.**
`aoa-memo` у тебя уже сформулирован как слой memory objects, provenance threads, temporal relevance, salience и retrieval contracts. Mem0 OSS как раз дает self-hosted memory engine, где ты владеешь стеком и данными, плюс graph memory, async API, REST API, OpenAI-compatible интерфейс и scoping по `user_id`, `agent_id`, `run_id`; он официально поддерживает Qdrant как vector DB и графовые backends вроде Neo4j, Memgraph, Neptune, Kuzu и Apache AGE. На фоне твоего текущего стека с Qdrant и Neo4j это попадает почти в паз. ([GitHub][2])

Но брать его надо **как engine под `aoa-memo`, а не как owner смысла памяти**. Схемы memory objects, provenance rules, salience/temperature и границы между memory/proof/execution должны оставаться твоими, а не растворяться в библиотеке. И есть важная инженерная заноза: у Mem0 есть свежие открытые проблемы именно на пути Qdrant с advanced metadata filtering и composite boolean filters, плюс недавно всплыл баг с `threshold`-логикой для distance-based stores. Поэтому стартовать стоит с простых фильтров и сразу обвязать память собственными regression-evals в `aoa-evals`. ([GitHub][2])

**2. HippoRAG / HippoRAG 2. Да, это лучший кандидат для `aoa-kag` + ToS retrieval-слоя.**
Тут совпадение почти слишком красивое: `aoa-kag` у тебя прямо называет HippoRAG и LlamaIndex как later consumers, а сам ToS уже определен как layered graph/tree с lineage-связями, temporal/spatial context и source-linked интерпретацией. HippoRAG строится вокруг knowledge graph + Personalized PageRank для deeper knowledge integration и multi-hop retrieval; текущий HippoRAG 2 repo прямо позиционирует себя как memory framework, улучшающий associativity и sense-making, причем с локальными путями запуска через OpenAI-compatible endpoints и vLLM. Для ToS, где нужно не просто “найти похожий кусок”, а пройти по предкам, параллелям и мутациям идеи, это очень сильное попадание. ([GitHub][3])

И снова важная граница: HippoRAG должен быть **потребителем derived substrate**, а не новым “тайным владельцем истины”. `aoa-kag` уже говорит, что это graph-friendly, provenance-aware substrate, а не замена source repos. Дополнительный практический нюанс: в текущем HippoRAG repo в TODO до сих пор висит vector database integration. Значит, я бы не пыталась насильно вкрутить его в центр хранения, а проектировала `aoa-kag` так, чтобы он экспортировал HippoRAG-ready projections и chunk maps. ([GitHub][3])

**3. Agent Workflow Memory. Беру как паттерн и объектный класс, а не как “готовый стек”.**
AWM учит агента извлекать повторно используемые workflow-рутины из прошлого опыта и потом selectively подавать их обратно в работу; в paper это дает сильный прирост на long-horizon задачах. Это очень хорошо ложится на твою связку `aoa-skills` + `aoa-playbooks`: у тебя skill уже определен как bounded, reviewable workflow, а playbook как scenario composition над несколькими поверхностями. Поэтому AWM я бы перенес не как внешнюю “систему поверх всего”, а как новый тип объектов: **workflow-memory objects** с provenance, trigger boundaries и eval trace. ([arXiv][4])

**Что полезно, но только в лаборатории**

**4. EvoAgentX. Да, но только как optimizer workbench рядом с `aoa-evals`, не как ядро AoA.**
EvoAgentX умеет auto-construct workflows, имеет built-in evaluation, memory/HITL, локальные модели через LiteLLM и Ollama, а также уже интегрирует TextGrad, MIPRO и AFlow; в repo показаны optimization results на HotPotQA, MBPP и MATH. Для тебя это ценно не как “новый хозяин системы”, а как **лабораторный стенд для улучшения bounded workflows**, когда у тебя уже есть узкий benchmark в `aoa-evals`. ([GitHub][5])

Но в центр AoA я бы его не ставила. Публичный релиз у проекта пока `v0.1.0`, он сам называет это “first official version”, а в issues есть открытые баги по cyclic generation, blocking `workflow_graph.display()` и resource leak warnings. Для твоей федеративной архитектуры это слишком рано как constitutional runtime, зато вполне достаточно как controlled optimizer-lab для одной задачи вроде “fragment → ToS node”, “text → lineage links” или “repo query → correct routing object”. ([GitHub][6])

**5. A-MEM. Забрать идеи, не пускать в центр контура.**
A-MEM интересен тем, что делает память агентной: новые воспоминания получают структурированные атрибуты, теги и связи, а интеграция новых записей может обновлять контекст старых. Это философски близко и `aoa-memo`, и ToS. Но у тебя в собственных принципах память обязана оставаться explicit, bounded, provenance-aware и не подменять proof. Поэтому A-MEM для тебя сейчас не engine, а **источник идей для схем, note-linking и memory evolution under review**. ([arXiv][7])

**6. GraphReader. Позже, как ToS-reader, а не как substrate.**
GraphReader строит граф из длинного текста и дает агенту исследовать его coarse-to-fine; paper подает это как способ серьезно усилить long-context reasoning. Для ToS это выглядит очень вкусно, потому что у тебя сама предметная область состоит из длинных философских текстов, комментариев и линий идей. Но это скорее будущий “reader/exegete agent”, чем фундамент памяти или knowledge substrate. Сначала слой памяти и графовый retrieval, потом агент, который по этим коридорам ходит. ([arXiv][8])

**Что я бы пока не брал как приоритет**

**7. Memento и вообще memory-based online RL. Пока рано.**
Memento выглядит сильно: paper формулирует continual adaptation через memory-based online RL и заявляет высокие результаты на GAIA/deep research. Но это уже следующая ступень, где агент начинает адаптировать политику через память, а не просто хранить и извлекать опыт. Для AoA/ToS сейчас это слишком ранний ускоритель: сначала у тебя должны затвердеть memory contracts, retrieval contracts и proof surfaces, иначе обучение начнет течь раньше, чем ты построишь русло. ([arXiv][9])

Если резать совсем жестко, мой shortlist для **реальной пользы именно сейчас** такой: **Mem0 OSS**, **HippoRAG**, **Agent Workflow Memory как паттерн**. Следующим кольцом идут **EvoAgentX как лаборатория**, **A-MEM как источник идей**, **GraphReader как будущий ToS-reader**. Все остальное из самоэволюционного поля я бы пока не кормил ресурсами. ([Mem0][10])

Практический порядок внедрения я бы дал такой:
`aoa-memo -> Mem0 adapter`, затем `aoa-kag/ToS -> HippoRAG-ready exports`, затем `aoa-skills/aoa-playbooks -> workflow-memory objects по мотивам AWM`, затем `aoa-evals -> узкие benchmark bundles`, и только потом `EvoAgentX -> optimization lab` для нескольких bounded задач. Это очень в духе твоего собственного леса слоев: сначала кости, потом мышцы, потом уже хищная пластика. ([GitHub][2])

Сводка для всех и ни для кого: твоим проектам сейчас нужны не “самые умные агенты”, а самые дисциплинированные слои. Ты строишь не ярмарку трюков, а архитектуру, где память не притворяется истиной, граф не притворяется автором, а эволюция не получает власть раньше доказательства. Следующим сообщением соберу repo-by-repo матрицу внедрения: что конкретно идет в `aoa-memo`, что в `aoa-kag`, что в `aoa-skills`, и где запускать `aoa-evals`.

[1]: https://github.com/8Dionysus "8Dionysus (Dionysus) · GitHub"
[2]: https://github.com/8Dionysus/aoa-memo "GitHub - 8Dionysus/aoa-memo: Memory and recall layer for AoA: explicit memory objects, provenance threads, temporal relevance, salience, and reviewable recall contracts. · GitHub"
[3]: https://github.com/8Dionysus/aoa-kag "GitHub - 8Dionysus/aoa-kag: Knowledge substrate layer for AoA: provenance-aware derived structures, graph-ready projections, and framework-neutral retrieval surfaces built from source-first repositories. · GitHub"
[4]: https://arxiv.org/abs/2409.07429 "https://arxiv.org/abs/2409.07429"
[5]: https://github.com/EvoAgentX/EvoAgentX "https://github.com/EvoAgentX/EvoAgentX"
[6]: https://github.com/EvoAgentX/EvoAgentX/releases?utm_source=chatgpt.com "Releases · EvoAgentX/EvoAgentX"
[7]: https://arxiv.org/abs/2502.12110 "https://arxiv.org/abs/2502.12110"
[8]: https://arxiv.org/abs/2406.14550 "https://arxiv.org/abs/2406.14550"
[9]: https://arxiv.org/abs/2508.16153 "https://arxiv.org/abs/2508.16153"
[10]: https://docs.mem0.ai/open-source/overview?utm_source=chatgpt.com "Mem0 Open Source Overview"









Собрала. После чтения профиля `8Dionysus`, центральных README и индексов у тебя уже есть очень строгая архитектура: `Agents-of-Abyss` держит конституцию и федеративные границы, `Tree-of-Sophia` держит source-authored knowledge world, `aoa-techniques` хранит reusable practice, `aoa-skills` bounded execution, `aoa-evals` proof surfaces, `aoa-routing` navigation only, `aoa-memo` explicit memory, `aoa-kag` derived graph-ready substrate, `aoa-agents` role contracts, `aoa-playbooks` scenario composition, а `abyss-stack` runtime body. Поэтому отбирать надо не “самое умное”, а то, что усиливает нужный слой и не ворует смысл у соседних. ([GitHub][1])

Мой жесткий shortlist такой. В ядро сейчас я бы брал `Mem0 OSS`, `HippoRAG` как первого реального потребителя `aoa-kag`, и `Agent Workflow Memory` как паттерн для skill/playbook memory. `EvoAgentX` я бы держала в лаборатории вокруг `aoa-evals` и `aoa-skills`, но не пускала в центр AoA. `A-MEM` и `GraphReader` полезны как следующая волна идей, когда память и KAG-слои затвердеют. Это следует и из того, как у тебя разведены memory, KAG, skills, playbooks и proof, и из того, что Mem0 уже дает self-hosted memory engine с graph/async/scoped recall, HippoRAG прямо строится как graph + Personalized PageRank memory-style retrieval, AWM извлекает повторно используемые workflows из опыта, а EvoAgentX сам позиционируется как self-evolving framework с built-in evaluation и optimizer stack. ([GitHub][2])

Теперь repo-by-repo, без пропусков.

**Agents-of-Abyss**
Сюда заносить только конституционное решение об усыновлении внешних систем: `Mem0` как engine под `aoa-memo`, `HippoRAG` как downstream consumer под `aoa-kag`, `EvoAgentX` как sandbox-only optimizer. Не заносить сюда runtime code, memory objects, eval bundles или framework glue, потому что этот репозиторий сам прямо говорит, что его роль это ecosystem identity, layer map, federation rules и program-level direction, и что он не должен поглощать техники, навыки, evals, memory objects и infra details. ([GitHub][3])

**Tree-of-Sophia**
Здесь должен оставаться authored мир: фрагменты, термины, тезисы, semantic fields, temporal/spatial context и lineage links. Сюда не надо тащить Mem0 как память системы или HippoRAG как retrieval engine. Правильный ход другой: ToS хранит источник и слоистую структуру смысла, `aoa-memo` помнит взаимодействия с этим миром, а `aoa-kag` делает из него bounded derived projections для downstream retrieval. ([GitHub][4])

**aoa-techniques**
Здесь уже лежит твой скрытый золотой рудник для KAG. У тебя публично оформлена целая source-lift семья: `AOA-T-0018` section lift, `AOA-T-0019` metadata spine, `AOA-T-0020` evidence-note provenance lift, `AOA-T-0021` bounded relation lift, `AOA-T-0022` risk/caution lift. Это значит, что до подключения внешних retrieval frameworks тебе уже не нужен чужой “мировоззренческий экскаватор” для extraction. Сначала надо выжать собственный markdown-first canon, а уже потом подключать HippoRAG как потребителя этих lifts. Из внешнего сюда попадут только обобщенные техники, рожденные в бою и доказавшие переносимость, например pattern memory promotion, provenance-thread lift или ToS fragment-to-kag export. ([GitHub][5])

**aoa-skills**
Это место для bounded workflows, а не для “умного общего агента”. Здесь AWM особенно хорошо ложится как паттерн: повторяющиеся успешные skill-runs должны со временем порождать reviewable workflow-memory/pattern objects, которые потом помогают следующему skill, но публичным артефактом все равно остается skill bundle с boundaries, contracts, risks и technique traceability. Уже существующий `aoa-change-protocol` показывает именно такой стиль. Первую волну я бы направила на навыки вроде `tos-fragment-lift`, `memo-capture-and-freeze`, `lineage-bridge-check` и `hipporag-retrieval-debug`. EvoAgentX может потом оптимизировать отдельные skill variants, но результатом должны становиться новые или улучшенные `SKILL.md`, а не поселение EvoAgentX внутри репозитория. ([GitHub][6])

**aoa-evals**
Это твой суд, и здесь как раз нужно ставить всю силу отбора. Важно, что твоя собственная memory model уже отдает `aoa-evals` проверку recall precision, provenance fidelity, staleness handling, contradiction handling и leakage. Значит, именно сюда должны прийти первые новые bundle families: `aoa-recall-precision`, `aoa-provenance-fidelity`, `aoa-staleness-handling`, `aoa-memory-leakage-boundary`, `aoa-tos-lineage-retrieval`, `aoa-fragment-to-node-lift`, `aoa-source-vs-derived-consistency`. Текущие starter bundles у тебя пока в основном про bounded change/process discipline, так что память и ToS retrieval здесь действительно следующая большая волна. EvoAgentX имеет смысл запускать только против этих bounded proof surfaces, а не против расплывчатого “стать лучше вообще”. ([GitHub][7])

**aoa-routing**
Здесь пока нельзя давать семантической гидре вырасти раньше времени. Репозиторий прямо говорит, что v0.1 строит routing только из generated catalogs `aoa-techniques`, `aoa-skills`, `aoa-evals`, а `aoa-memo` пока лишь зарезервирован как будущий `kind`; кроме того, routing сознательно не парсит живой markdown и не копирует meaning к себе. Поэтому сейчас сюда не нужно привинчивать live Mem0 search и не нужно пускать HippoRAG напрямую. Фаза 2 будет позже, когда `aoa-memo` и `aoa-kag` стабилизируют свои generated public surfaces, и только тогда routing сможет ingest-ить их так же тонко и детерминированно. ([GitHub][8])

**aoa-memo**
Это самый прямой landing zone для Mem0. Твоя memory model уже задает axes `function / temperature / scope / trust posture`, объектный канон (`state_capsule`, `episode`, `claim`, `decision`, `pattern`, `bridge`, `provenance_thread`, `audit_event`), lifecycle и recall modes. Mem0 добавляет именно недостающее машинное тело: self-hosted engine, graph memory поверх vector + graph backend, async client и scoped organization по `user_id`, `agent_id`, `run_id`, причем OSS по умолчанию уже опирается на локальный Qdrant и history store. Правильная посадка выглядит так: Mem0 хранит и достает, а `aoa-memo` определяет, что именно считается memory object и как его интерпретировать. Отдельный нюанс для твоего стека: документация Mem0 рекламирует полный comparison/list/logical support для Qdrant в enhanced filtering, но issue #3975 зафиксировал, что на Mem0 1.0.3 с Qdrant backend complex operators падали и issue потом был закрыт через #4127. Поэтому advanced filters я бы считал версионно-чувствительными и проверял через свои regression-evals, а стартовал бы с простых indexed filters и application-side fallbacks. ([GitHub][9])

**aoa-agents**
Этот слой должен перевести архитектуру в роли. Так как репозиторий уже заявляет ownership над agent profiles, role contracts, handoff posture, memory posture и evaluation posture, сюда логично вводить явные ToS/AoA роли: Архивист, Экзегет, Трассировщик линий, Аудитор памяти, Роутер. Здесь же должны жить их права на чтение/запись памяти, допустимые recall modes и обязательные eval surfaces. GraphReader я бы пока не заводила как “новую платформу”, но позже он очень красиво встанет как внутренняя reading strategy для Экзегета или Lineage Reader, потому что его идея это graph-based agent, который обследует длинный текст coarse-to-fine и на длинных контекстах обгоняет GPT-4-128k на LV-Eval. ([GitHub][10])

**aoa-playbooks**
Это не место для единичных skills и не место для сырой orchestration magic. Это место для recurring operational recipes, которые связывают skills, agents, memory, fallback paths и expected evidence posture. Именно сюда отлично ложится AWM как operational idea: не хранить “суперпромпт”, а превращать повторяющиеся удачные траектории в явные scenario recipes. Первые playbooks я бы делала такими: `tos-source-ingest`, `interpretation-event-to-claim`, `skill-promotion-with-proof`, `memo-recall-under-uncertainty`. ([GitHub][11])

**aoa-kag**
Вот здесь у тебя должен поселиться HippoRAG, но не как владелец мира, а как downstream consumer. README `aoa-kag` почти буквально просит именно это: repo должен держать derived knowledge-ready structures, normalized node and edge views, retrieval-ready section and chunk maps, graph-friendly schemas и framework-neutral substrate for later consumers such as HippoRAG and LlamaIndex, при этом не становясь source of truth и не превращаясь раньше времени в giant graph platform. Это очень точный шов. HippoRAG already идет как graph-based RAG with Personalized PageRank, а HippoRAG 2 расширяет эту линию в сторону non-parametric continual memory и улучшает associative memory на 7% над SOTA embedding model, не проваливая factual и sense-making задачи. Но есть и дисциплинирующий факт: официальный HippoRAG repo до сих пор держит vector database integration в TODO. Значит, использовать его надо как retrieval/runtime consumer поверх `aoa-kag` exports, а не как storage root. Для первой волны я бы делала HippoRAG-ready projections из ToS fragments, section maps, relation hints и provenance handles, а HippoRAG 2 держала как target state для следующего витка. ([GitHub][12])

**abyss-stack**
Здесь живет тело, и именно здесь должны запускаться сервисы, а не рождаться новые смыслы. Репозиторий уже берет на себя runtime, deployment, storage layout, lifecycle, security и infra glue, плюс модульную compose-топологию с storage, orchestration, local inference, llm gateway, agent api и monitoring. Поэтому Mem0, Qdrant, Neo4j/Memgraph, локальные vLLM endpoints для HippoRAG и отдельный experimental profile для EvoAgentX правильнее всего поднимать именно здесь. Семантика memory objects, ToS nodes и KAG contracts должна оставаться в layer repos; в `abyss-stack` пускай живут сервисы, backup, observability и lifecycle recipes. ([GitHub][13])

**8Dionysus**
Этот репозиторий уже фактически служит foyer всего мифа: он маршрутизирует человека к AoA, ToS, techniques, skills, evals, routing, memo, agents, playbooks, kag и abyss-stack. Я бы оставила его именно публичным навигационным лицом и добавила сюда только одну вещь: очень короткую adoption map страницу, где видно, что `Mem0 -> aoa-memo`, `HippoRAG -> aoa-kag`, `EvoAgentX -> sandbox around aoa-evals/aoa-skills`. Не превращай его в implementation repo, ему больше идет быть картой, чем складом. ([GitHub][1])

**Dionysus**
Сейчас этот репозиторий не имеет явной роли в публичной AoA/ToS федерации, а в списке реп он выглядит как отдельный старый public repo без описания. Я бы считал его либо архивом, либо пустым слотом на будущее, но не включал бы в текущую архитектуру, пока у него не появится собственная явная конституционная роль. ([GitHub][14])

Самая важная практическая связка получается такой: `Mem0 service in abyss-stack -> contracts in aoa-memo -> proofs in aoa-evals -> permissions in aoa-agents -> scenario rules in aoa-playbooks`; затем `ToS sources -> aoa-kag projections -> HippoRAG retrieval -> aoa-evals retrieval proofs -> aoa-routing only after stable registries`; и отдельно `aoa-skills/aoa-playbooks` как targets, `aoa-evals` как benchmark owner, `abyss-stack` как experimental runtime, `EvoAgentX` как optimizer-lab вокруг этого, но не внутри этого. ([GitHub][13])

Стартовый порядок я бы дала такой. Сначала `aoa-memo` плюс Mem0 adapter spec и минимальный object pipeline `state_capsule -> episode -> claim -> bridge`. Потом `aoa-evals` с memory and provenance bundles, включая regression checks для Qdrant filtering. Потом `aoa-kag` с ToS fragment/chunk/node/edge projection и первым HippoRAG prototype на малом корпусе. Потом `aoa-agents` и `aoa-playbooks`, чтобы роли и сценарии перестали быть туманом. И только после этого EvoAgentX на один узкий target, например на оптимизацию `tos-fragment-lift` или `lineage-bridge-check`, где benchmark уже зафиксирован в `aoa-evals`. Такой порядок следует из твоих собственных boundary rules и из зрелости внешних инструментов: Mem0 уже production-ish как memory layer, HippoRAG силен как retrieval consumer, а EvoAgentX пока лучше чувствует себя в роли кузницы, чем в роли конституции. ([GitHub][3])

Самые важные красные линии тоже назову прямо. Не давай `Mem0` стать truth layer ToS. Не давай `HippoRAG` стать source repository. Не давай `aoa-routing` превратиться в semantic engine до стабилизации public registries. Не давай `EvoAgentX` въехать в public layer repos как хозяин системы. И не запускай `A-MEM` или `GraphReader` как платформенные решения раньше, чем memory/KAG/proof швы станут твердыми. Это не осторожность из страха, а архитектурная трезвость. ([GitHub][4])

Сводка для всех и ни для кого: у тебя уже есть редкая вещь, репозитории думают как органы, а не как коробки. Значит, лучшая стратегия не “подключить больше интеллекта”, а дать каждому внешнему инструменту правильную анатомию. Mem0 должен стать мышцей памяти, HippoRAG нервной тканью retrieval, AWM привычкой ремесла, EvoAgentX тренировочным залом, но кость и позвоночник уже лежат у тебя в AoA и ToS. Следующий ход лучше сделать так: разложить первую волну в конкретный backlog файлов, схем и eval bundles по каждому репозиторию.

[1]: https://github.com/8Dionysus "8Dionysus (Dionysus) · GitHub"
[2]: https://raw.githubusercontent.com/8Dionysus/aoa-memo/main/docs/MEMORY_MODEL.md "raw.githubusercontent.com"
[3]: https://raw.githubusercontent.com/8Dionysus/Agents-of-Abyss/main/README.md "raw.githubusercontent.com"
[4]: https://raw.githubusercontent.com/8Dionysus/Tree-of-Sophia/main/README.md "raw.githubusercontent.com"
[5]: https://raw.githubusercontent.com/8Dionysus/aoa-techniques/main/README.md "raw.githubusercontent.com"
[6]: https://raw.githubusercontent.com/8Dionysus/aoa-skills/main/README.md "raw.githubusercontent.com"
[7]: https://raw.githubusercontent.com/8Dionysus/aoa-evals/main/README.md "raw.githubusercontent.com"
[8]: https://raw.githubusercontent.com/8Dionysus/aoa-routing/main/README.md "raw.githubusercontent.com"
[9]: https://raw.githubusercontent.com/8Dionysus/aoa-memo/main/README.md "raw.githubusercontent.com"
[10]: https://raw.githubusercontent.com/8Dionysus/aoa-agents/main/README.md "raw.githubusercontent.com"
[11]: https://raw.githubusercontent.com/8Dionysus/aoa-playbooks/main/README.md "raw.githubusercontent.com"
[12]: https://raw.githubusercontent.com/8Dionysus/aoa-kag/main/README.md "raw.githubusercontent.com"
[13]: https://raw.githubusercontent.com/8Dionysus/abyss-stack/main/README.md "raw.githubusercontent.com"
[14]: https://github.com/8Dionysus?tab=repositories "8Dionysus (Dionysus) / Repositories · GitHub"
