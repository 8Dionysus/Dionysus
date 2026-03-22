---
id: seed.aoa.model-tier-orchestration.v0
title: Оркестрация модельных ярусов
en_title: Model-Tier Orchestration
project: AoA
status: seed
priority: high
kind: runtime-architecture
sow_targets:
  - aoa-agents
  - aoa-routing
  - aoa-playbooks
  - abyss-stack
  - evals
tags:
  - aoa
  - orchestration
  - routing
  - conductor
  - deep-model
  - archivist
  - local-stack
  - quantization
---

# Seed: Оркестрация модельных ярусов

## Суть

AoA должен работать не как “одна большая модель с кучей промптов”, а как оркестр ярусов усилия.

Разные модели и кванты нужны не ради коллекции.
Они нужны ради различения труда:

- быстрое;
- среднее;
- глубокое;
- архивирующее;
- проверяющее.

Оркестрация должна стать явным контрактом.

---

## Человеческое заземление

На локальном стеке время, RAM, контекст и токены — реальные ресурсы.
Большая модель дорога.
Маленькая — быстра, но поверхностна.
Если заставить крупную модель делать всё, система станет:
- медленной;
- шумной;
- плохо проверяемой;
- капризной к контексту;
- склонной заменять структуру туманом глубины.

Нужна иерархия труда.

---

## Проблема

Без явной оркестрации связка моделей обычно ломается в один из сценариев:

### 1. Король всего
Одна большая модель решает всё:
- долго думает о простом;
- быстро устаёт на сложном;
- теряет форму;
- перегружает контекст.

### 2. Рой без закона
Есть много агентов, но:
- неясно, кто за что отвечает;
- handoff скрыт;
- память смешана;
- routing случаен.

### 3. Ложная универсальность
Одна и та же модель, один и тот же режим, одна и та же простыня system prompt — для любой задачи.

---

## Предложение

Ввести explicit model-tier orchestration.

### Роли

#### 1. Router
Самое быстрое решение:
- класс задачи;
- риск;
- нужна ли эскалация;
- какая surface следующая.

#### 2. Planner
Строит bounded plan:
- шаги;
- критерии готовности;
- точки проверки;
- когда звать глубокий режим.

#### 3. Executor
Исполняет:
- команды;
- инструменты;
- локальные действия;
- короткие итерации.

#### 4. Verifier
Проверяет:
- формат;
- ошибки;
- противоречия;
- границы риска.

#### 5. Conductor
Держит последовательность между внутренностями:
- какой режим сейчас;
- кто следующий;
- когда эскалировать;
- сколько можно тратить контекста и усилия.

#### 6. Deep
Редкий, дорогой, глубокий проход:
- синтез;
- арбитраж;
- рождение нового правила;
- финальный judgement.

#### 7. Archivist
Сгущает опыт:
- summary;
- entities;
- decisions;
- pattern extraction;
- memory candidates.

---

## State machine

Внешнее переключение должно быть явным:

`route -> plan -> do -> verify -> deep? -> distill`

Где:
- `deep?` вызывается не всегда;
- `distill` обязателен для нетривиального прогона.

---

## Internal mode contract

Даже внутри одной модели режим должен быть ограничен и именован:

- `mode: route`
- `mode: plan`
- `mode: do`
- `mode: verify`
- `mode: distill`
- `mode: deep_synthesis`

Это позволяет одной модели играть разные роли без размывания постуры.

---

## Deep escalation triggers

Глубокий проход должен включаться по триггерам:

1. высокая неопределённость;
2. конфликт источников или вариантов;
3. застревание `N` шагов без улучшения;
4. высокая цена ошибки;
5. необходимость построить новое правило;
6. финальная проверка перед важным изменением.

---

## Quantization sibling roles

Допустить sibling contract для одной и той же крупной модели:

- lighter quant -> conductor
- heavier quant -> deep

Это не закон железа.
Это закон распределения усилия.

---

## Shared constitutional core

Каждый агент любого размера должен знать:

- базовые правила;
- общую цель;
- своё место;
- allowed tools;
- memory scope;
- output contract;
- кому он передаёт эстафету;
- какой артефакт обязан оставить.

---

## Инварианты

1. Большая модель не делает всё подряд.
2. Router не автор смысла.
3. Conductor не подменяет Deep.
4. Archivist не философствует.
5. Deep не видит весь архив по умолчанию.
6. Каждый нетривиальный прогон оставляет артефакт.
7. Escalation триггеры явны.
8. Tier role важнее бренда модели.
9. Одна и та же модель может играть разные роли, если постура и бюджет различаются.
10. Человек может вручную форсировать или запретить эскалацию.

---

## Минимальный контракт данных

### model_tier_profile
```yaml
tier_id: string
role: router | planner | executor | verifier | conductor | deep | archivist
latency_class: fast | medium | slow
effort_class: low | medium | high
preferred_ctx_tokens: integer | null
hard_ctx_cap_tokens: integer | null
allowed_tools: []
memory_read_scope: []
memory_write_scope: []
output_contract: string
escalates_to: []
fallback_to: []
quant_profile: string | null
notes: string | null
```

### escalation_event
```yaml
event_id: string
from_role: string
to_role: string
reason: uncertainty | conflict | stuck | risk | synthesis | final_check
trigger_refs: []
created_at: iso8601
approved_by_human: boolean | null
```

### orchestration_step
```yaml
step_id: string
run_id: string
role: string
mode: route | plan | do | verify | distill | deep_synthesis
input_refs: []
output_ref: string | null
artifact_refs: []
next_role: string | null
confidence: 0.0-1.0 | null
```

---

## Метрики

Нужна matrix-style оценка:

- TTFT
- tokens/sec
- route accuracy
- plan quality
- verification hit-rate
- artifact completeness
- memory write quality
- deep-pass usefulness

Оркестрация без evals быстро превращается в миф.

---

## Куда сажать

### `aoa-agents`
- role contracts
- tier contracts
- handoff posture

### `aoa-routing`
- task-to-tier hints
- escalation hints
- route surfaces

### `aoa-playbooks`
- model-tier orchestra playbook
- long-horizon and high-risk recipes

### `abyss-stack`
- actual model profiles
- context budgets
- quantization deployment notes

### `aoa-evals`
- benchmark matrix for tier roles
- regression checks

---

## Первые материальные артефакты

- `aoa-agents/generated/model_tier_registry.json`
- `aoa-routing/generated/task_to_tier_hints.json`
- `aoa-playbooks/playbooks/model-tier-orchestra.md`
- `abyss-stack/docs/model_profiles.md`
- `aoa-evals/bundles/aoa-model-tier-regression/`

---

## Признак удачной посадки

После посадки ясно:
- какая роль делает что;
- когда включается Deep;
- кто архивирует;
- как устроен handoff;
- что измеряется;
- как не превратить крупную модель в грузовой мускул без закона.
