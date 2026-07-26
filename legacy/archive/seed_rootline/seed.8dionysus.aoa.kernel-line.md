\---

seed\_id: seed.8dionysus.aoa.kernel-line
title: AoA Kernel Line
profile\_anchor: 8Dionysus
projects:

* AoA
kind: repo-seed
status: living
priority: high
parent\_seed: seed.8dionysus.aoa-tos.rootline
tags:
* alignment-root
* self-agents
* agent-kernel
* observer-layer
* experience-library
* mutation-registry
* selective-debate
* edge-ai

\---

# Seed: AoA Kernel Line

## Назначение

Этот seed предназначен именно для репозиториев AoA и runtime-ориентированных `aoa-\*` репозиториев, где есть агенты, исполнение, orchestration, sandboxing, monitoring или policy.

Он не пытается описать весь мир. Он фиксирует только то, что должно укорениться в AoA как воли, руках и нервной системе.

\---

## Корневой импульс

AoA не должен расти как россыпь полезных автоматизаций.
AoA должен расти как дисциплинированная система действия:

* сначала конституция;
* потом роли;
* потом исполнение;
* потом наблюдение;
* потом наследуемый опыт;
* потом осторожная эволюция.

\---

## Что сеять

### 1\. Alignment Root

Ввести явный конституционный слой:

* допустимые действия;
* gated actions;
* запреты;
* red-risk зоны.

Минимальная посадка:

* `docs/architecture/alignment-root.md`
* `alignment/` или `config/alignment/`
* ссылки из README / ADR

### 2\. Self-Agents

Рассматривать operative-агентов как ограниченные selves.

У каждого self-agent должны быть:

* `agent\_id`
* `role`
* `alignment\_profile`
* `capabilities`
* `sandbox`
* `memory\_scope`
* `audit\_policy`

Минимальная посадка:

* `docs/self\_agents/README.md`
* `self\_agents/registry/`
* `self\_agents/profiles/`
* schema / examples

### 3\. Agent Kernel

Kernel должен быть единым горлом исполнения.
Через него проходят:

* registry
* task routing
* alignment enforcement
* sandbox launch
* audit trail

Никаких прямых запусков operative-агентов в обход Kernel.

Минимальная посадка:

* `docs/architecture/agent-kernel.md`
* `kernel/` или `aoa\_kernel/README.md`
* lifecycle diagram
* task contract

### 4\. Observer Layer

Ввести observer layer как иммунную систему:

* audit agent
* security agent
* performance agent
* alignment watcher

Минимальная посадка:

* `docs/observer-layer.md`
* `observers/` или `monitoring/observer/`
* logging / policy hooks

### 5\. Experience Library

AoA должен копить не просто логи, а отобранный опыт:

* успешные reasoning traces
* удачные tool sequences
* удачные retrieval paths
* характерные ошибки
* rollback cases

Минимальная посадка:

* `evolution/experience\_library/README.md`
* schema experience record
* критерии сохранения

### 6\. Mutation Registry

Любые изменения prompts / routing / thresholds / retrieval weights / policies должны быть журналируемы и откатываемы.

Зоны:

* green
* yellow
* red

Минимальная посадка:

* `evolution/mutation\_registry/README.md`
* mutation log
* rollback contract

### 7\. Selective Debate

Debate включается только по триггерам:

* высокая неопределённость;
* конфликт источников;
* высокий риск ошибки;
* критическая проверка перед действием.

Это не базовый режим дыхания, а режим усиленного мышления.

\---

## Что не сеять сюда

* детальную онтологию ToS;
* graph schema для философских lineages;
* абстрактный discourse о цивилизации агентов без привязки к runtime;
* онлайн-самообучение весов как ближайшую норму.

\---

## Предпочтительные формы посадки

* ADR
* docs
* config stubs
* registry schemas
* interface contracts
* folder scaffolds
* TODO markers

\---

## Задание для Codex

1. Найти в репозитории место, где естественно живут runtime contracts, configs, orchestration docs и monitoring hooks.
2. Посеять только то, что относится к AoA runtime и execution.
3. Если repo узкий, посадить seed фрагментарно, без мнимой полноты.
4. Оставить хотя бы один структурный след, не только документацию.
5. Не трогать red-risk зоны без отдельного подтверждения.

\---

## Признак удачной посадки

После посадки ясно:

* где у AoA конституция;
* как определяются self-agents;
* через что проходит запуск;
* кто наблюдает систему;
* где копится опыт;
* как изменения проходят через mutation discipline.

