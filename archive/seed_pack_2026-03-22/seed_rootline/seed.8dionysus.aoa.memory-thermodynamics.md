seed_id: seed.8dionysus.aoa.memory-thermodynamics
title: Memory Thermodynamics
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: architecture-seed
status: living
priority: high
parent_seed: seed.8dionysus.aoa.kernel-line
tags:
  - memory
  - hot-warm-cold
  - forgetting
  - salience
  - aoa-memo
  - aoa-agents
  - writeback
  - long-horizon

# Seed: Memory Thermodynamics

## Назначение

Этот seed вводит для AoA runtime-память как стратифицированную термодинамическую систему, а не как плоский архив.

Он не заменяет `Context Compost` в ToS.
Он дополняет его с operational-стороны:
- что помнит агент;
- что должна помнить экосистема;
- что должно быть забыто;
- как память мигрирует между температурами.

---

## Корневой импульс

Система должна помнить не всё подряд, а только то, что меняет траекторию.

Плохая память — это:
- либо свалка всего;
- либо декоративный канон;
- либо retrieval без судьбы.

Хорошая память — это температура, отбор, продвижение, затухание и возвращение.

---

## Что сеять

### 1. Memory temperatures
Ввести как минимум четыре температурных класса:

- `core` — конституция, identity, project-goal, role law;
- `hot` — текущая задача, активные ограничения, локальный план;
- `warm` — эпизоды, решения, ошибки, повторяющиеся паттерны;
- `cold` — зрелые принципы, долговечные правила, review-passed canon.

### 2. Salience gate
Каждый memory item должен оцениваться не только по похожести, но и по:
- `novelty`
- `impact`
- `recurrence`
- `risk`

Нужен явный механизм:
`keep / promote / demote / retire`.

### 3. Decay and forgetting
Забывание должно стать нормой, а не сбоем.

Нужны:
- `ttl` / `review_after`
- half-life policy
- demotion rules
- retire rules
- manual veto / rescue

### 4. Memory steward
Нужен отдельный memory steward / librarian daemon, который:
- не отвечает пользователю напрямую;
- принимает traces и summaries;
- распределяет по температурам;
- чистит дубли;
- повышает или понижает слой;
- готовит writeback.

### 5. Agent-specific memory posture
Память должна зависеть от роли агента.

Например:
- router читает почти только `core + hot`;
- archivist пишет `warm`;
- conductor читает `core + hot + selected warm`;
- deep agent получает `selected warm + selected cold`, но не весь архив;
- verifier пишет correction traces и contradiction markers.

### 6. Bridge into ToS
Нужен writeback-контракт:
- какие `warm/cold` объекты могут уходить в ToS;
- какие остаются operational-only;
- как хранится provenance.

---

## Что не сеять сюда

- огромный “единый brain store”;
- embeddings как единственную форму памяти;
- бессрочное хранение всего;
- скрытое смешение authored truth и derived memory.

---

## Предпочтительные формы посадки

- `aoa-memo/docs/MEMORY_TEMPERATURES.md`
- `aoa-memo/schemas/memory_item.schema.json`
- `aoa-memo/schemas/decay_policy.schema.json`
- `aoa-agents/docs/AGENT_MEMORY_POSTURE.md`
- `aoa-agents/generated/agent_memory_profiles.json`
- `docs/contracts/writeback_temperature_policy.md`

---

## Задание для Codex

1. Не дублировать `Context Compost`, а связать его с runtime memory.
2. Ввести температуры как operational contract, а не как красивую метафору.
3. Для каждого memory слоя определить:
   - read scope
   - write scope
   - promotion trigger
   - decay rule
4. Оставить хотя бы один schema-backed artifact.

---

## Признак удачной посадки

После посадки ясно:
- что должно помнить `ядро`;
- что должно помнить `сессия`;
- что должно переживать одну сессию;
- что имеет право исчезнуть;
- кто именно распределяет память по слоям.
