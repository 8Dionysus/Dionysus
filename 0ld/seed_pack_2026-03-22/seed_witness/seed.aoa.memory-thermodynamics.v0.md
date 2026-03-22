---
id: seed.aoa.memory-thermodynamics.v0
title: Термодинамика памяти
en_title: Memory Thermodynamics
project: AoA
status: seed
priority: high
kind: memory-architecture
sow_targets:
  - aoa-memo
  - aoa-agents
  - aoa-routing
  - abyss-stack
  - memory-bridge
tags:
  - aoa
  - memory
  - thermodynamics
  - forgetting
  - salience
  - routing
  - writeback
---

# Seed: Термодинамика памяти

## Суть

Память AoA не должна быть одним бесформенным хранилищем.
Она должна быть термодинамической системой, где есть:

- ядро;
- горячая рабочая память;
- тёплая эпизодическая память;
- холодная долговечная память;
- правила продвижения, понижения и угасания.

Это не поэзия и не UX-метафора.
Это operational law для длинной агентной системы.

---

## Человеческое заземление

В режиме solo+AI, на локальном железе, в длинных задачах и нестабильной среде проблема не только в качестве модели.
Проблема в том, что:

- внимание ограничено;
- контекст дорог;
- прошлый опыт должен помогать, а не душить;
- память должна быть inspectable;
- забывание должно быть честной функцией, а не аварией.

Плоская память перегружает.
Отсутствие памяти заставляет каждый раз рождаться заново.
Нужна память, которая помнит переломы.

---

## Проблема

Без термодинамики память быстро ломается в одну из трёх форм:

### 1. Свалка
- всё сохраняется;
- retrieval тащит мусор;
- важное тонет в шуме.

### 2. Хрупкий канон
- остаются только красивые summaries;
- исчезают ошибки, развилки, причины;
- система теряет процессуальную мудрость.

### 3. Псевдопамять
- всё живёт только в текущем контексте;
- агенты не держат continuity;
- глубина имитируется длиной окна.

---

## Предложение

Ввести многоуровневую operational-память.

### Слои

#### 1. Core
Почти неизменяемая память:
- конституция;
- identity / role law;
- проектные принципы;
- базовые safety boundaries;
- тонкое хотение к цели.

#### 2. Hot
Короткая рабочая память:
- текущая задача;
- активные ограничения;
- последние решения;
- текущее дерево шага;
- краткий локальный план.

#### 3. Warm
Эпизодическая память:
- решения;
- удачные / провальные паттерны;
- баги;
- развилки;
- recurring motifs;
- workflow traces worth keeping.

#### 4. Cold
Долговечная память:
- зрелые принципы;
- стабильные эвристики;
- review-passed protocols;
- durable source-linked operational knowledge.

---

## Memory steward

Нужен отдельный daemon / steward / librarian, который:

- читает witness traces, summaries, reports;
- считает salience;
- решает temperature placement;
- проводит promotion / demotion;
- удаляет дубли;
- готовит writeback;
- следит за decay.

Он не основной мыслитель.
Он садовник памяти.

---

## Agent-specific memory posture

Память должна быть различной для разных ролей.

### Router
Читает:
- `core`
- `hot`

Пишет:
- почти ничего, кроме минимальных route marks.

Не должен тащить архив.

### Archivist
Читает:
- `hot`
- selected `warm`

Пишет:
- `warm`
- compression notes
- memory candidates

Его долг — сгущать, а не спорить.

### Conductor
Читает:
- `core`
- `hot`
- selected `warm`

Пишет:
- checkpoints
- escalation marks
- handoff summaries

Его долг — держать форму и последовательность шага.

### Deep agent
Читает:
- `core`
- selected `warm`
- selected `cold`

Пишет:
- synthesis
- arbitration notes
- high-value principles
- canon candidates

Его нельзя заливать всем архивом.

### Verifier / Critic
Читает:
- `hot`
- selected `warm`

Пишет:
- contradiction markers
- correction traces
- confidence deltas

---

## Salience equation

Минимальная формула важности:

`salience = novelty + impact + recurrence + risk`

Где:
- `novelty` — насколько это новое;
- `impact` — насколько это меняет траекторию;
- `recurrence` — повторяется ли паттерн;
- `risk` — важно ли удержать это ради безопасности, отката или проверки.

Не обязательно держать одну формулу навсегда.
Но salience должен быть явным.

---

## Инварианты

1. Не всё заслуживает памяти.
2. Не всё, что попало в память, должно жить долго.
3. Каждое повышение слоя хранит provenance.
4. Каждое понижение слоя должно быть объяснимо.
5. Агент не получает весь архив по умолчанию.
6. Core не переписывается случайными сессиями.
7. Cold не становится священным: у него есть review cycle.
8. Человек может заморозить, понизить или отменить канонизацию.
9. Derived memory не подменяет source-authored truth.
10. Чувствительные данные редактируются по умолчанию.

---

## Минимальный контракт данных

### memory_item
```yaml
memory_id: string
temperature: core | hot | warm | cold
kind: identity | constraint | decision | episode | pattern | principle | policy | contradiction | artifact | question
title: string
summary: string | null
content_ref: string | null
source_refs: []
created_at: iso8601
updated_at: iso8601
owner_scope: system | agent | project | task
read_scope: []
write_scope: []
novelty_score: 0.0-1.0 | null
impact_score: 0.0-1.0 | null
recurrence_score: 0.0-1.0 | null
risk_score: 0.0-1.0 | null
salience_score: 0.0-1.0 | null
promotion_state: pending | promoted | blocked | demoted | retired
review_after: iso8601 | null
ttl_days: integer | null
provenance_refs: []
sensitive: boolean
```

### memory_promotion_event
```yaml
event_id: string
memory_id: string
from_temperature: hot | warm | cold | null
to_temperature: hot | warm | cold | retired
reason: string
actor: steward | human | agent
trigger_refs: []
created_at: iso8601
```

### agent_memory_posture
```yaml
agent_role: string
preferred_reads:
  - core
  - hot
forbidden_reads: []
preferred_writes: []
max_items_per_call: integer | null
max_tokens_from_memory: integer | null
promotion_authority: none | suggest_only | direct
requires_human_review_for_cold: boolean
```

---

## Правила продвижения

### Core
Попадает только то, что:
- конституционно;
- долговременно;
- проходит review;
- не должно зависеть от случайной задачи.

### Hot -> Warm
Продвигать, если:
- принято решение;
- обнаружен повторяющийся паттерн;
- найден значимый баг;
- произошло застревание и найден выход;
- у trace есть operational value beyond current task.

### Warm -> Cold
Продвигать, если:
- паттерн пережил повторные задачи;
- есть проверка или доказательство пользы;
- известны пределы применимости;
- сохранено provenance.

### Любой слой -> Retire
Уводить из активной памяти, если:
- объект устарел;
- больше не подтверждается;
- был замещён лучшей формой;
- создаёт шум без operational gain.

---

## Куда сажать

### `aoa-memo`
- memory temperatures
- salience model
- promotion / demotion contracts
- steward schemas

### `aoa-agents`
- agent memory posture
- forgetting posture
- max memory scope per role

### `aoa-routing`
- hints, какой role и какой tier какой слой памяти читает

### `abyss-stack`
- operational limits, budgets, storage placement
- warm/cold persistence policy
- archive paths

### `ToS` bridge
- что из `warm/cold` может become compost input
- что остаётся purely operational

---

## Первые материальные артефакты

- `aoa-memo/docs/MEMORY_TEMPERATURES.md`
- `aoa-memo/schemas/memory_item.schema.json`
- `aoa-memo/schemas/memory_promotion_event.schema.json`
- `aoa-agents/docs/AGENT_MEMORY_POSTURE.md`
- `aoa-agents/generated/agent_memory_profiles.json`

---

## Признак удачной посадки

После посадки система знает:
- что помнить сейчас;
- что помнить потом;
- что забывать;
- кто распределяет память;
- почему одно пережило сессию, а другое умерло.
