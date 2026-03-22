\---

id: seed.aoa.protocol-witness.v0
title: Протокол свидетеля
en\_title: Witness Protocol
project: AoA
status: seed
priority: high
kind: architecture
sow\_targets:

* agent-runtime
* tool-layer
* evals
* logging
* memory-bridge
tags:
* aoa
* trace
* reliability
* tool-use
* evals
* observability
* safety

\---

# Seed: Протокол свидетеля

## Суть

Каждый значимый прогон агента должен оставлять **свидетельство действия**: не просто лог, а связный след, по которому человек может понять:

* какую цель агент решал;
* какими средствами он действовал;
* что увидел в ответ;
* что изменил во внешней среде;
* насколько результат проверяем и обратим.

Это не украшение и не аналитика на потом. Это позвоночник доверия.

\---

## Человеческое заземление

AoA должен быть пригоден для **solo+AI режима**, нестабильной среды, длинных задач и кочевого способа работы. Система не может требовать идеальной памяти, постоянной сети, постоянного внимания или слепой веры в “умность” модели. Она должна быть inspectable, portable, survivable.

\---

## Проблема

Без протокола свидетеля агентность быстро становится непрозрачной:

* красивый ответ скрывает плохой путь;
* tool calls не видны или видны фрагментарно;
* побочные эффекты в среде неотслеживаемы;
* ошибки нельзя воспроизвести;
* обновления моделей и промптов ломают пайплайн незаметно;
* память копит шум вместо опыта.

Обычные application logs не решают задачу. Они пишутся для отладки сервиса, а не для понимания воли и следа агента.

\---

## Предложение

Ввести в AoA единый артефакт: **Witness Trace**.

Witness Trace создаётся для каждого нетривиального прогона и хранит:

1. цель и режим усилия;
2. краткий план или локальную гипотезу;
3. последовательность шагов;
4. все вызовы инструментов;
5. наблюдения и state deltas;
6. итог, риски, уверенность, флаги проверки;
7. указание на то, требовалось ли человеческое вмешательство.

Формат должен быть одновременно:

* **машинно-читаемым** для evals, regression и аналитики;
* **человеко-читаемым** для ревью, доверия и обучения.

\---

## Инварианты

1. **Каждый внешний эффект имеет след.** Если агент что-то меняет вне себя, это отражается в trace.
2. **Ошибки не стирают след.** Упавший прогон всё равно оставляет частичное свидетельство.
3. **Секреты редактируются по умолчанию.** В trace не храним сырые секреты, токены, ключи, чувствительные фрагменты.
4. **Не хранить сырой скрытый внутренний монолог.** Хранить решения, резюме шага, наблюдения и основания, но не полный приватный мыслительный поток.
5. **След должен быть переносимым.** Без жёсткой привязки к одному вендору, SDK или облаку.
6. **След должен поддерживать откат и проверку.** Где возможен rollback, trace должен знать как его инициировать или хотя бы зафиксировать точку невозврата.

\---

## Минимальный контракт данных

### run-level

```yaml
run\_id: string
agent\_id: string
task\_id: string | null
started\_at: iso8601
finished\_at: iso8601 | null
status: planned | running | succeeded | failed | aborted | needs\_review
mode:
  effort: quick | standard | deep | ordeal
  autonomy: advisory | semi-auto | auto
goal: string
goal\_hash: string | null
plan\_summary: string | null
context\_refs: \[]
policy\_flags: \[]
human\_review\_required: boolean
final\_summary: string | null
final\_confidence: 0.0-1.0
result\_artifacts: \[]
risk\_notes: \[]
rollback\_notes: string | null
```

### step-level

```yaml
index: integer
kind: think | tool | observe | decide | write | handoff | error
intent: string
tool\_name: string | null
tool\_input\_redacted: object | null
tool\_input\_fingerprint: string | null
tool\_output\_excerpt: string | null
observation: string | null
state\_delta: string | null
latency\_ms: integer | null
cost\_estimate: number | null
confidence: 0.0-1.0 | null
error\_type: string | null
error\_message: string | null
review\_flag: boolean
```

\---

## Форматы хранения

Минимум два выхода:

1. **JSONL / JSON**

   * для машинной обработки, evals, регрессий, агрегации.
2. **Markdown summary**

   * для человека;
   * пригоден для ревью, заметок, ручного экспорта в ToS.

Markdown summary должен отвечать на 5 вопросов:

* что агент хотел сделать;
* что сделал;
* где был риск;
* что получилось;
* что нужно проверить человеку.

\---

## Где сажать в репозитории

Искать и внедрять в следующих местах:

* agent loop / orchestration layer;
* tool executor / tool registry;
* action layer с внешними побочными эффектами;
* eval harness / regression suite;
* docs / architecture notes;
* memory bridge, если уже есть экспорт в knowledge graph, notes, RAG или journals.

Если репозиторий не содержит полноценного агента, seed сажается частично:

* как schema;
* как adapter;
* как docs contract;
* как trace-ready интерфейс.

\---

## Срезы внедрения

### Slice 0. Schema

Создать `WitnessTrace` и `WitnessStep` как базовые типы/контракты.

### Slice 1. Runtime instrumentation

Инструментировать agent loop так, чтобы каждый значимый шаг попадал в trace.

### Slice 2. Tool visibility

Оборачивать все tool calls trace-слоем. Никаких “невидимых” вызовов.

### Slice 3. Side-effect capture

Для write/update/delete/send/create действий фиксировать state delta и уровень риска.

### Slice 4. Human-readable export

Добавить markdown renderer или summary builder.

### Slice 5. Evals bridge

Подключить trace к capability evals и regression evals.

### Slice 6. ToS bridge

Подготовить экспорт наблюдений, ошибок, успешных паттернов и принципов для последующей компостизации в ToS.

\---

## Критерии принятия

Seed считается проросшим, если:

* любой нетривиальный прогон агента создаёт witness trace;
* любой вызов инструмента виден в trace;
* любой внешний побочный эффект помечен как state delta;
* при падении система сохраняет частичный trace;
* trace не содержит сырых секретов;
* есть хотя бы 1 markdown summary на прогон;
* есть минимум 2 теста: happy path и failure path;
* есть минимум 1 regression test на полноту trace.

\---

## Anti-goals

Не превращать seed в:

* тяжёлую observability-платформу раньше времени;
* сбор полного chain-of-thought;
* vendor-locked решение;
* визуальный дашборд ради дашборда;
* бюрократию, замедляющую каждый эксперимент.

\---

## Связь с ToS

AoA оставляет след.
ToS переваривает след в:

* паттерны;
* ошибки;
* принципы;
* канон.

Witness Trace является сырьём для будущих seeds:

* Компост контекста;
* Древо происхождения;
* Карманный канон;
* Экономика усилия.

\---

## Инструкция для Codex

При посеве в конкретный репозиторий:

1. Найди agent runtime, orchestration, tool layer, evals и docs.
2. Введи минимальный контракт `WitnessTrace` без жёсткой привязки к вендору.
3. Оберни все tool calls trace-слоем.
4. Зафиксируй state deltas для write-операций.
5. Добавь экспорт в JSON и Markdown.
6. Добавь минимум 3 теста:

   * успешный прогон;
   * частичный провал;
   * отсутствие trace для запрещённого невидимого tool call должно падать тестом.
7. Обнови docs: где trace создаётся, где хранится, как читать.
8. Если репозиторий маленький, делай минимальную форму seed, но не теряй инварианты.

\---

## Названия файлов и узлов

Рекомендуемое имя seed-файла:
`seed.aoa.protocol-witness.v0.md`

Внутренние имена:

* `WitnessTrace`
* `WitnessStep`
* `TraceSummary`
* `TracePolicy`
* `TraceExporter`

\---

## Формула

Не верь ответу.
Смотри на след.
Если след чист, воспроизводим и понятен, агент достоин следующего шага.

