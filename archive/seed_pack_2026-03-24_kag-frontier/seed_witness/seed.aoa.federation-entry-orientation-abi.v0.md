---
id: seed.aoa.federation-entry-orientation-abi.v0
title: Федеративный ABI входа и ориентации
en_title: Federation Entry and Orientation ABI
project: AoA
status: seed
priority: high
kind: architecture-seed
sow_targets:
  - aoa-routing
  - Agents-of-Abyss
  - aoa-agents
  - aoa-playbooks
  - aoa-memo
  - Tree-of-Sophia
tags:
  - aoa
  - routing
  - abi
  - orientation
  - small-models
  - entrypoints
  - budget-tests
  - federation
---

# Seed: Федеративный ABI входа и ориентации

## Суть

Если федерация делается в первую очередь для ИИ, то критерий дизайна меняется.

Главный вопрос уже не:
- красива ли архитектура;
- насыщен ли канон;
- сколько сильных идей есть на корне.

Главный вопрос такой:

**может ли самая слабая из целевых моделей найти следующий истинный объект без галлюцинации топологии.**

Для этого нужен не просто routing.
Нужен федеральный ABI входа и ориентации.

---

## Жёсткий принцип

**2B-first, GPT-5.4-complete.**

Малый агент не обязан понимать всю федерацию.
Но он обязан:

1. определить kind задачи;
2. получить самый маленький следующий объект;
3. понять, что этот объект делает;
4. знать, куда идти дальше;
5. не перепутать обзор с authority.

---

## Проблема

### 1. Слишком много концептуальной высоты на входе

Сильная модель выдержит длинный doctrinal stack.
Малая модель чаще потеряет маршрут раньше, чем дойдёт до истинного owning repo.

### 2. Нет общего public object card

Сейчас агент часто понимает слой через README, настроение и накопление контекста.
Для ИИ это слишком дорого.

### 3. Orientation и authority ещё не названы единым законом

Эта разница уже живёт в федерации, но не оформлена в компактный общий контракт.

### 4. Routing taxonomy пока уже, чем сама федерация

Текущий tiny-model contour полезен, но пока не покрывает многие реальные object kinds.

---

## Предложение

### 1. Ввести `federation_entrypoint`

Каждый публичный объект федерации должен уметь компилироваться в краткую ориентирующую карточку.

```yaml
federation_entrypoint:
  kind: string
  id: string
  owner_repo: string
  title: string
  capsule_surface: string
  authority_surface: string
  next_actions: []
  fallback: string
  risk: string
  next_hops: []
```

### 2. Развести две плоскости

`orientation plane` должна держать:
- capsule
- next hop
- fallback
- risk

`authority plane` должна держать:
- README
- doctrine docs
- full sections
- templates
- canonical examples

### 3. Собрать единый entry index

Нужен один федеральный short-entry surface, например:

- `generated/federation_entrypoints.min.json`

Чтобы агент начинал с маленькой карты, а не гадал, какой корневой README сегодня важнее.

### 4. Расширить routing taxonomy

Минимальный ближайший набор kinds:

- `agent`
- `tier`
- `playbook`
- `tos_node`
- `kag_view`
- `runtime_surface`
- `seed`

### 5. Ввести navigation budget-tests

Проверять не только валидность JSON, но и проходимость:

- reachable in `pick -> inspect -> expand`
- явный fallback
- явный next hop
- no authority confusion

---

## Supporting moves внутри этого seed

- zero-hop quickstarts
- glossary lift в первый маршрут
- worked example near the root
- plain-language subtitles for doctrine-heavy filenames
- README contract alignment across repos

Это полезные меры высокой отдачи, но здесь они подчинены ABI входа, а не живут как отдельные корневые seeds.

---

## Границы, которые должны выжить

1. `aoa-routing` остаётся navigation and dispatch layer.
2. Orientation plane не подменяет authority plane.
3. Entry cards не должны становиться новым каноном смысла.
4. Роутер не становится автором техники, навыка, eval, memory object, ToS node или KAG meaning.
5. Малый путь не должен ломать большой путь; он должен его открывать.

---

## Что не сеять сюда

- новый монорепозиторий поверх федеральных слоёв;
- “умный индекс”, который заменяет source repos;
- бесконечный routing ontology before working starters;
- длинные doctrinal rewrites вместо коротких entry surfaces.

---

## Первый материализованный выход

- `aoa-routing/generated/federation_entrypoints.min.json`
- расширенный `tiny_model_entrypoints.json`
- `aoa-routing/docs/FEDERATION_ENTRY_ABI.md`
- один budget-test contract или eval example
- короткие root-entry shells для AoA center и ToS

---

## Признак удачной посадки

После посадки малая модель может:

- зайти в федерацию с короткой карты;
- различить overview и authority;
- дойти до следующего истинного объекта за 2-3 хода;
- не утонуть в длинной лестнице README и doctrine до того, как увидит правильную дверь.
