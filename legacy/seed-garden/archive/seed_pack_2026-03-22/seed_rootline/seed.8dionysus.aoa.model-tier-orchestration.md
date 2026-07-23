seed_id: seed.8dionysus.aoa.model-tier-orchestration
title: Model-Tier Orchestration
profile_anchor: 8Dionysus
projects:
  - AoA
kind: architecture-seed
status: living
priority: high
parent_seed: seed.8dionysus.aoa.kernel-line
tags:
  - orchestration
  - model-tiers
  - conductor
  - deep-agent
  - archivist
  - routing
  - playbooks
  - abyss-stack

# Seed: Model-Tier Orchestration

## Назначение

Этот seed делает из набора локальных моделей не зоопарк, а оркестр ролей.

Он нужен, чтобы:
- быстрая модель делала быстрое;
- средняя держала ход;
- крупная занималась медленной и важной работой;
- архивариус собирал след;
- переключение стало протоколом, а не настроением.

---

## Корневой импульс

Большая модель не должна быть королём всего.
Она должна быть редким, дорогим, дисциплинированным вмешательством.

Связка моделей хороша не тогда, когда их много, а тогда, когда:
- есть роли;
- есть границы;
- есть триггеры эскалации;
- есть artefact-first loop.

---

## Что сеять

### 1. Tier roles
Ввести устойчивые роли по классам усилия:

- `router` / `spark`
- `planner`
- `executor`
- `verifier`
- `conductor`
- `deep`
- `archivist`

### 2. State machine
Снаружи переключение должно быть конечным автоматом:

`route -> plan -> do -> verify -> deep? -> distill`

### 3. Internal mode contract
Внутри модели должны быть режимы, а не бесконечная простыня инструкций:

- `route`
- `plan`
- `do`
- `verify`
- `distill`
- `deep_synthesis`

### 4. Deep escalation triggers
Глубокий агент вызывается только по условиям:

- высокая неопределённость;
- конфликт вариантов;
- застревание без прогресса;
- высокая цена ошибки;
- необходимость родить новое правило.

### 5. Quantization sibling roles
Допустить, что одна и та же крупная модель в разных квантах играет разные посты:

- более лёгкий квант — conductor;
- более тяжёлый квант — deep synthesis / judgement.

### 6. Shared constitutional core
Каждый агент любого размера должен знать:
- базовые правила;
- общую цель;
- своё место;
- границы памяти;
- куда эскалировать;
- какой артефакт он обязан оставить.

---

## Что не сеять сюда

- схему “большая модель делает всё”;
- скрытый оркестратор без контракта;
- выдачу полного архива каждому агенту;
- превращение routing layer в автора смысла.

---

## Предпочтительные формы посадки

- `aoa-agents/docs/MODEL_TIER_MODEL.md`
- `aoa-agents/generated/model_tier_registry.json`
- `aoa-routing/generated/task_to_tier_hints.json`
- `aoa-playbooks/playbooks/long-horizon/model-tier-orchestra.md`
- `abyss-stack/docs/model_profiles.md`

---

## Задание для Codex

1. Описать роли, а не бренды моделей.
2. Привязать каждый tier к duty, output contract и memory scope.
3. Выделить conductor как отдельный контракт.
4. Выделить archivist как отдельный writeback-пост.
5. Вынести state machine в явный документ и/или schema-backed artifact.

---

## Признак удачной посадки

После посадки ясно:
- кто маршрутизирует;
- кто держит форму шага;
- кто исполняет;
- кто проверяет;
- кто архивирует;
- в каких случаях включается глубокий судья.
