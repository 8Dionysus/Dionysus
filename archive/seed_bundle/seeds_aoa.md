# seeds\_aoa.md

Собрано из диалога и отфильтровано через публичный профиль `8Dionysus` и текущую федерацию репозиториев.

Дата: 2026-03-21
Статус: curated seeds, не backlog и не roadmap.

## Grounding

Эти seeds отобраны не в вакууме, а с опорой на уже заявленную форму экосистемы:

* `Agents-of-Abyss` как конституционный центр AoA, владеющий identity, layer map, federation rules и program-level direction.
* `aoa-techniques` как канон reusable techniques.
* `aoa-skills` как execution layer для bounded workflows.
* `aoa-evals` как proof layer.
* `aoa-memo` как memory / recall layer.
* `aoa-agents` как role / persona layer.
* `aoa-playbooks` как scenario / composition layer.
* `aoa-kag` как derived knowledge substrate, а не источник истины.

## Selection rules

Отбор здесь жёсткий.

Включено только то, что:

1. усиливает швы между текущими слоями AoA;
2. не дублирует уже активную planning-wave в `aoa-techniques`;
3. помогает AoA расти как legible federation, а не как россыпь похожих репо;
4. держит self-agent как checkpoint и engineering surface, а не как туманную мифологию;
5. не пытается превратить `aoa-kag` в новую империю поверх source-first слоёв.

Не включено то, что сейчас выглядит как:

* локальный backlog отдельного репозитория;
* преждевременный graph/export/UI-heavy inflation;
* импорт чужой конституции целиком вместо extraction повторяемых приёмов;
* размытие различий `skill`, `technique`, `method`, `doctrine`.

\---

<a id="aoa-seed-01-ontology-spine-of-action"></a>
## AOA-SEED-01 — Ontology Spine of Action

### Суть

Зафиксировать на уровне AoA жёсткую грамматику действия:

* `skill` = способность
* `technique` = приём
* `method` / `playbook` = маршрут из техник и навыков
* `doctrine` = принцип выбора маршрута
* `role` / `persona` = кто действует
* `memory` = что удерживается
* `eval` = чем подтверждается качество или допустимость

### Почему это seed

Это не косметика терминов. Это позвоночник экосистемы.
Пока эта ось не закреплена, соседние репозитории будут постепенно съезжать друг на друга.

### Куда ложится

* основной дом: `Agents-of-Abyss`
* downstream consequences: `aoa-techniques`, `aoa-skills`, `aoa-playbooks`, `aoa-agents`, `aoa-evals`, `aoa-memo`

### Первый материализуемый выход

* короткий federation glossary section в `Agents-of-Abyss`
* таблица ownership: `repo -> meaning it owns`
* правила, что нельзя смешивать между слоями

### Чего не делать

* не превращать это в толстую онтологическую спецификацию;
* не добавлять десятки сущностей раньше, чем spine закреплён.

\---

<a id="aoa-seed-02-self-agent-checkpoint-stack"></a>
## AOA-SEED-02 — Self-Agent Checkpoint Stack

### Суть

Оформить self-agent как контрольную точку AoA не через романтику автономии, а через стек предохранителей:

* constitution / policy check
* approval gate
* stable rollback marker
* post-change health check
* bounded iteration loop
* explicit improvement log

### Почему это seed

Твой интерес к self-agent репо здесь не случайный. Для AoA это одна из проверочных форм зрелости системы.
Но AoA нужен не myth of selfhood, а portable stack управления самопреобразованием.

### Куда ложится

* основной дом: `aoa-agents`
* composition surface: `aoa-playbooks`
* proof hooks: `aoa-evals`
* memory traces: `aoa-memo`

### Первый материализуемый выход

* `SELF\_AGENT\_CHECKPOINT.md` или эквивалент в `aoa-agents`
* минимальный чеклист: что обязательно есть у self-changing agent surface
* 1 bounded playbook: `self-improvement with approval + rollback + health-check`

### Чего не делать

* не импортировать целиком чужую metaphysics of agency;
* не делать autonomy “самоценностью” раньше reviewability.

\---

<a id="aoa-seed-03-narrative-core-memory"></a>
## AOA-SEED-03 — Narrative-Core Memory

### Суть

Развести narrative core и retrieval substrate:

* identity / user / world memory должны оставаться короткими, читаемыми и reviewable source surfaces;
* retrieval, embeddings, graph views и derived projections должны усиливать, а не заменять narrative core.

### Почему это seed

Это одна из самых важных границ для AoA: не растворить память в рассыпанном retrieval и не превратить ядро в бессвязный набор векторов.

### Куда ложится

* основной дом: `aoa-memo`
* contracts and startup posture: `aoa-agents`
* derived lifts only later: `aoa-kag`

### Первый материализуемый выход

* memory contract: `core surfaces` vs `derived memory`
* список минимальных narrative surfaces
* правила, что именно можно lift-ить в KAG, а что должно оставаться authored memory

### Чего не делать

* не объявлять embeddings главной формой памяти;
* не плодить memory surfaces без source-of-truth discipline.

\---

<a id="aoa-seed-04-source-first-donor-refinery"></a>
## AOA-SEED-04 — Source-First Donor Refinery

### Суть

Сделать общую AoA-формулу работы с внешними донорами:

`donor project / dataset -> repeated operational pattern -> sanitized technique or skill -> bounded playbook -> eval proof surface`

### Почему это seed

Из диалога ясно: тебе интересны чужие репо не как культовые объекты, а как доноры повторяемых форм.
AoA нужен свой плавильный цех, а не чужие скелеты в витрине.

### Куда ложится

* federation guidance: `Agents-of-Abyss`
* technique intake: `aoa-techniques`
* skillization path: `aoa-skills`
* scenario composition: `aoa-playbooks`
* verification: `aoa-evals`

### Первый материализуемый выход

* short donor intake rubric
* rules: what counts as pattern, what counts as contamination, what counts as foreign doctrine
* two worked examples: `benchmark donor` and `self-agent donor`

### Чего не делать

* не канонизировать dataset instances как техники;
* не импортировать “целиком” чужие BIBLE/constitution surfaces.

\---

<a id="aoa-seed-05-kag-compatible-substrate-not-empire"></a>
## AOA-SEED-05 — KAG-Compatible Substrate, Not Empire

### Суть

Удержать `aoa-kag` в правильной роли:

* provenance-aware derived structures
* graph-friendly projections
* retrieval-ready maps
* framework-neutral substrate

Но не:

* источник authored meaning
* replacement для source repositories
* тихо выросшая мета-платформа, которая подменит AoA и ToS

### Почему это seed

KAG тебе подходит как логика формы, но не как новый суверен.
Этот seed нужен, чтобы derived layer не съел source-authored truth.

### Куда ложится

* основной дом: `aoa-kag`
* constitutional guardrails: `Agents-of-Abyss`

### Первый материализуемый выход

* short constitutional guardrail section: what `aoa-kag` owns / does not own
* counterpart table: source repos vs derived projections

### Чего не делать

* не переводить authored nodes и authored memory в KAG как primary home;
* не подменять graph-readiness смысловой суверенностью.

\---

<a id="aoa-seed-06-method-lives-in-playbooks"></a>
## AOA-SEED-06 — Method Lives in Playbooks

### Суть

Метод должен жить как отдельная форма, а не размазываться между техниками, навыками и сценарными заметками.

Формула:

* `technique` даёт приём;
* `skill` даёт исполнимую способность;
* `playbook` собирает маршрут действий, handoffs, decision points и proof hooks.

### Почему это seed

Это одна из главных осей диалога. Если метод не получит собственного дома, `aoa-skills` и `aoa-techniques` рано или поздно начнут смешиваться.

### Куда ложится

* основной дом: `aoa-playbooks`
* sourcing from: `aoa-techniques`, `aoa-skills`, `aoa-evals`, `aoa-memo`, `aoa-agents`

### Первый материализуемый выход

* короткая спецификация playbook bundle
* 1 canonical example маршрута: например `self-agent improvement checkpoint` или `external donor refinement path`

### Чего не делать

* не превращать playbooks в копию techniques;
* не сваливать туда identity или doctrine as such.

\---

<a id="aoa-seed-07-concept-operation-counterpart-edges"></a>
## AOA-SEED-07 — Concept ↔ Operation Counterpart Edges

### Суть

Добавить между ToS и AoA derived counterpart edges, связывающие концептуальные узлы и operational forms:

* `legibility` <-> reviewable workflow patterns
* `lineage` <-> provenance / adaptation surfaces
* `boundedness` <-> safe execution / rollback contracts
* `calibration` <-> eval and review discipline

### Почему это seed

Это один из самых плодотворных мостов между твоими двумя большими направлениями.
Но мост должен быть derived и explicit, а не сливаться в один общий котёл.

### Куда ложится

* edge ownership / mapping rules: `Agents-of-Abyss`
* derived projections: `aoa-kag`
* conceptual side remains in `Tree-of-Sophia`

### Первый материализуемый выход

* маленькая counterpart edge vocabulary
* 3–5 example mappings

### Чего не делать

* не писать operational meaning прямо в ToS source nodes;
* не делать из каждого ToS concept обязательную operational counterpart.

\---

<a id="aoa-seed-08-evidence-backed-gamified-maturation"></a>
## AOA-SEED-08 — Evidence-Backed Gamified Maturation

### Суть

Геймифицировать рост не через vanity metrics, а через заслуженное становление:

* `seed`
* `proven`
* `promoted`
* `canonical`
* `deprecated`

Плюс:

* reuse contexts
* failure / adverse notes
* unlock conditions
* lineage visibility

### Почему это seed

Ты явно тянешься к древовидной и игровой форме роста. Этот seed делает такую форму строгой: очки не за шум, а за evidence-backed maturation.

### Куда ложится

* maturity doctrine: `Agents-of-Abyss`
* concrete practice form: `aoa-techniques`
* skill / playbook analogues later: `aoa-skills`, `aoa-playbooks`

### Первый материализуемый выход

* общая maturity ladder и meanings
* правила, какие статусы shared across AoA, а какие локальны для repos

### Чего не делать

* не вводить scoring, который никто не валидирует;
* не превращать progression в нарядную обложку без доказательной базы.

\---

## Seeds consciously not selected for AoA now

### Не выбранные сейчас направления

* большой graph/export/UI program как самостоятельная активная волна;
* тотальное KAG-центричное переопределение экосистемы;
* импорт чужой self-agent constitution как закона AoA;
* пакетное раздувание domain ontology beyond the current federation map.

Причина одна: сейчас AoA сильнее всего растёт через правильные швы, а не через добавление ещё одного этажа инфраструктурной пышности.

\---

## Compression

Если ужать всё до трёх главных нервов AoA на сейчас, то они такие:

1. `skill != technique != method`
2. `memory core != retrieval substrate`
3. `self-agent != free myth of autonomy; self-agent = governed checkpoint`

Именно эти три оси сейчас лучше всего соответствуют профилю `8Dionysus` и текущей форме публичной экосистемы.
