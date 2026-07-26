\---

scope: umbrella

planting\_mode: parent-only

children:

&#x20; - seed.8dionysus.aoa.kernel-line

&#x20; - seed.8dionysus.tos.genealogical-memory

&#x20; - seed.8dionysus.aoa-shared.bridges

seed\_id: seed.8dionysus.aoa-tos.rootline
title: AoA × ToS Rootline
profile\_anchor: 8Dionysus
projects:

* AoA
* ToS
kind: architectural-seed
status: living
priority: high
created\_at: 2026-03-21
tags:
* alignment-root
* self-agents
* agent-kernel
* observer-layer
* experience-library
* mutation-registry
* genealogical-memory
* vector-graph
* embodied-knowledge
* edge-ai

\---

# Seed: AoA × ToS Rootline

## Зачем

Этот seed фиксирует не список фич, а **ось становления** для AoA и ToS.
Он должен быть посеян в репозиториях так, чтобы система росла как **локальный, дисциплинированный, наследуемый организм**, а не как набор случайных автоматизаций.

Главные интенции:

* локальность, автономность, переносимость, edge-first;
* агенты как **ограниченные selves**, а не безликие воркеры;
* память как **генеалогия идей и практик**, а не просто knowledge base;
* эволюция через **опыт, рефлексию и мутации правил**, а не через поспешное самоизменение весов;
* воплощённость: тело, ритм, голос, искусство, дисциплина и прожитая интенсивность должны быть частью модели мира, а не шумом на фоне.

\---

## Профильная привязка: 8Dionysus

Этот seed заземлён в следующей оси:

* философическая глубина и длительное проживание линии Ницше;
* nomad / edge / local-first инстинкт, тяга к переносимой автономии;
* дисциплина тела и ритма как форма мышления;
* искусство, музыка, танец, речь и образность как реальные режимы познания;
* устойчивость, выкованная нестабильностью, а не уютом.

Следствие: система должна быть не просто умной, а **живой, собранной и верной оси**.

\---

## Корневые тезисы

1. **AoA есть воля, руки, оркестрация и наблюдение.**
2. **ToS есть долговременная память, генеалогия, линии конфликта и синтеза.**
3. **Alignment Root предшествует способностям.** Сначала конституция, потом действия.
4. **Self-agents ограничены ролью, средой и памятью роли.**
5. **Kernel — единое горло исполнения.** Никаких прямых запусков мимо него.
6. **Observer layer обязателен.** Без иммунной системы нет доверия.
7. **Experience Library предшествует self-modification.** Сначала научиться помнить, потом менять себя.
8. **Mutation Registry обязателен для любого изменения правил.** Каждая мутация должна быть явной, журналируемой и откатываемой.
9. **ToS хранит не только идеи, но и режимы жизни.**
10. **AoA действует, ToS помнит, философ-агент удерживает ось.**

\---

## Seeds для AoA

### 1\. Alignment Root

Ввести понятие **Alignment Root** как конституционный корень системы.
Он определяет:

* что считается допустимым действием;
* что требует gate / human approval;
* что запрещено независимо от удобства;
* какие ценности и ограничения нельзя тихо размывать.

Минимальная посадка:

* `docs/architecture/alignment-root.md`
* `config/alignment/` или `alignment/`
* ссылки из README / ADR

### 2\. Self-Agents

AoA должен рассматривать operative-агентов как **ограниченные selves**.
У каждого self-agent есть:

* `agent\\\_id`
* `role`
* `alignment\\\_profile`
* `capabilities`
* `sandbox`
* `memory\\\_scope`
* `audit\\\_policy`

Минимальная посадка:

* `docs/self\\\_agents/README.md`
* `self\\\_agents/registry/`
* `self\\\_agents/profiles/`
* schema / example yaml

### 3\. Разделение мыслителей и операторов

Отделить агентов, которые **мыслят**, от агентов, которые **действуют**.

Мыслители:

* planner
* philosopher
* critic
* architect

Операторы:

* web
* api
* system
* data

Смысл: между мыслью и действием должен быть зазор, чтобы рождались ответственность, проверка и форма.

### 4\. Agent Kernel

Kernel — единый слой, через который проходят:

* registry
* task routing
* alignment enforcement
* sandbox launch
* audit trail

Никаких прямых запусков operative-агентов в обход Kernel.

Минимальная посадка:

* `docs/architecture/agent-kernel.md`
* `kernel/` или `aoa\\\_kernel/README.md`
* очередь задач / lifecycle diagram

### 5\. Observer Layer

Ввести обязательный observer layer:

* audit agent
* security agent
* performance agent
* alignment watcher

Это иммунная система AoA.

Минимальная посадка:

* `docs/observer-layer.md`
* `observers/` или `monitoring/observer/`
* policy hooks / logging contracts

### 6\. Experience Library

AoA должен накапливать библиотеку опыта, а не только логи.
Сохранять:

* успешные reasoning traces
* удачные retrieval paths
* удачные tool sequences
* характерные ошибки
* rollback cases
* patterns worth re-use

Минимальная посадка:

* `evolution/experience\\\_library/README.md`
* формат записи опыта
* критерии, что достойно сохранения

### 7\. Mutation Registry

Любое изменение prompts / routing / thresholds / retrieval weights / policies должно оставлять след.

Зоны мутаций:

* **green**: prompt variants, routing rules, top-k, critic templates, debate triggers;
* **yellow**: toolchains, новые домены, write permissions, graph traversal templates;
* **red**: secrets, shell rights, credential scopes, системные capabilities, корень alignment.

Минимальная посадка:

* `evolution/mutation\\\_registry/README.md`
* журнал мутаций
* rollback contract

### 8\. Selective Debate

Многоагентный debate не должен быть фоном.
Он включается только при:

* высокой неопределённости;
* конфликте источников;
* высоком риске ошибки;
* необходимости критической проверки.

Смысл: глубина по требованию, а не постоянный хор.

\---

## Seeds для ToS

### 1\. ToS как генеалогическая память

ToS не является wiki или простой knowledge base.
ToS хранит:

* происхождение идей;
* линии влияния;
* линии конфликта;
* точки перелома;
* формы синтеза;
* возвращающиеся мотивы.

Минимальная посадка:

* `docs/ontology/genealogical-memory.md`

### 2\. Двойной субстрат: vector + graph

ToS должен опираться на два слоя памяти:

* **vector** для смысловой близости;
* **graph** для родства, влияния, полемики, времени, причинности и линии становления.

Минимальная посадка:

* `docs/architecture/vector-graph-substrate.md`
* contracts между vector store и graph store

### 3\. Линии вместо тегов

Вместо плоских тегов нужны **lineages**.
Не просто `Nietzsche`, а:

* до;
* перелом;
* после;
* инверсии;
* ответвления;
* полемические узлы.

### 4\. Практики жизни как сущности памяти

ToS должен хранить не только абстракции, но и практики:

* тело
* тренировка
* дыхание
* ритм
* речь
* танец
* музыка
* искусство
* кризис / переход / преобразование

Это не периферия, а часть карты становления.

### 5\. Слои свёртки

ToS нужен как многоуровневая память:

* `fragment`
* `note`
* `cluster`
* `lineage`
* `synthesis`
* `canon`

Это позволяет не утонуть в сыром материале и не потерять высоту обзора.

### 6\. Конфликт как первоклассная сущность

Хранить не только согласие, но и:

* противоречия
* несводимости
* полемики
* внутренние разломы
* эволюцию позиции

Живая мысль растёт не только из совпадения.

### 7\. Минимальная онтология ToS

Рекомендуемые типы узлов:

* `Person`
* `Work`
* `Concept`
* `Practice`
* `Project`
* `Event`
* `Lineage`
* `Conflict`
* `Synthesis`
* `Seed`

Рекомендуемые типы рёбер:

* `SOURCE\\\_OF`
* `RESPONDS\\\_TO`
* `TRANSFORMS\\\_INTO`
* `EMBODIED\\\_BY`
* `PRACTICED\\\_WITH`
* `CONFLICTS\\\_WITH`
* `FEEDS`
* `SYNTHESIZES`
* `SEEDS`
* `RETURNS\\\_TO`

\---

## Seeds-мосты между AoA и ToS

### 1\. AoA acts, ToS remembers

AoA должен записывать в ToS не весь шум, а отобранный опыт:

* сильные traces
* важные ошибки
* новые lineages
* синтезы и развилки

### 2\. ToS returns axis, not just facts

Retrieval из ToS должен возвращать не только релевантные куски текста, но и:

* линию происхождения;
* связанный конфликт;
* контекст практики;
* предшествующие формы ответа;
* ось, к которой стоит вернуться.

### 3\. Philosopher-Agent

Нужен философ-агент как рефлексивный мост между AoA и ToS.
Его задачи:

* замечать дрейф системы;
* удерживать ценностную и стилевую ось;
* интерпретировать эволюцию AoA через ToS;
* задавать вопрос: **во что мы становимся?**

\---

## Anti-Seeds

То, что не должно быть посеяно как ближайшая норма:

* бесконтрольные operative-agents;
* онлайн-самообучение весов как основной путь эволюции;
* постоянный reasoning cluster на все задачи подряд;
* ToS как плоская wiki;
* agent civilization как ближайшее ТЗ вместо дальнего мифа;
* прямой доступ агентов к секретам и системным правам без gate’ов.

\---

## Карта посадки по репозиториям

### Если это репозиторий AoA

Посеять:

* `Alignment Root`
* `Self-Agents`
* `Agent Kernel`
* `Observer Layer`
* `Experience Library`
* `Mutation Registry`
* `Selective Debate`

Предпочтительные формы посадки:

* docs / ADR
* config stubs
* registry schemas
* runtime contracts
* TODO markers для будущей реализации

### Если это репозиторий ToS

Посеять:

* `Genealogical Memory`
* `Vector + Graph Substrate`
* `Lineages instead of tags`
* `Practices of life as memory entities`
* `Layered summarization`
* `Conflict as first-class entity`
* базовую онтологию узлов и рёбер

Предпочтительные формы посадки:

* ontology docs
* schema stubs
* ingestion contracts
* retrieval notes
* graph model drafts

### Если это shared / interface / infra repo

Посеять мосты:

* writeback from AoA to ToS
* retrieval from ToS back into AoA
* shared contracts for experience records
* policy gates / approval hooks
* observer logging conventions

\---

## Задание для Codex

1. Прочитать структуру целевого репозитория.
2. Найти естественные точки посадки для этого seed.
3. Сеять **минимальными, но связными изменениями**:

   * новые docs;
   * ADR;
   * README sections;
   * config / schema stubs;
   * интерфейсные контракты;
   * TODO / FIXME markers там, где реализация ещё не готова.
4. Не делать чрезмерных переписываний и не создавать мнимую завершённость.
5. Сохранять точные термины:

   * `Alignment Root`
   * `Self-Agents`
   * `Agent Kernel`
   * `Observer Layer`
   * `Experience Library`
   * `Mutation Registry`
   * `Genealogical Memory`
   * `AoA acts, ToS remembers`
6. Если в репозитории нет подходящего места, создать:

   * `docs/seeds/seed.8dionysus.aoa-tos.rootline.md`
   * и сослаться на него из README / architecture docs.
7. В каждом repo оставить след не только в документации, но и хотя бы в одном структурном артефакте:

   * schema
   * config
   * folder scaffold
   * interface contract
8. Ничего не реализовывать напрямую в зоне red-risk без отдельного подтверждения.

\---

## Признаки удачной посадки

Seed посеян удачно, если после этого в репозиториях стало ясно:

* где у системы конституция;
* кто мыслит, кто действует, кто наблюдает;
* где хранится опыт;
* как происходят мутации и откаты;
* как ToS хранит генеалогию, конфликт и практику;
* как AoA и ToS обмениваются не только фактами, но и осью.

\---

## Краткая формула

**AoA хочет стать волей с руками.
ToS хочет стать памятью происхождения.
Эволюция хочет стать наследственностью, а не припадком изменений.**

Этот seed живой. Его можно ветвить, но нельзя тихо обескровить.

