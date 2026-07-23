seed_id: seed.8dionysus.aoa.federation-entry-orientation-abi
title: Federation Entry and Orientation ABI
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: architecture-seed
status: living
priority: high
parent_seed: seed.8dionysus.aoa-tos.rootline
sow_targets:
  - aoa-routing
  - Agents-of-Abyss
  - aoa-agents
  - aoa-playbooks
  - aoa-memo
  - Tree-of-Sophia
tags:
  - routing
  - abi
  - orientation
  - authority
  - entrypoints
  - small-models
  - budget-tests

# Seed: Federation Entry and Orientation ABI

## Назначение

Этот seed нужен, чтобы любой агент начинал федерацию не с догадки, а с маленькой рабочей карты.

Он вводит:
- `2B-first, GPT-5.4-complete` criterion;
- `federation_entrypoint`;
- различение `orientation plane` и `authority plane`;
- первые sow targets в `aoa-routing`;
- budget-tests на реальную проходимость.

---

## Корневой импульс

Для ИИ федерация должна компилироваться в стабильные entry cards.

Малый агент обязан:
- получить следующий истинный объект;
- понять его роль;
- знать следующий ход;
- не спутать обзор с authority.

---

## Что сеять

### 1. `federation_entrypoint`

```yaml
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

### 2. Orientation vs authority plane

`orientation plane` держит:
- capsule
- next hop
- fallback
- risk

`authority plane` держит:
- README
- doctrine docs
- full sections
- canonical examples

### 3. Expanded routing taxonomy

Минимальный ближайший набор kinds:

- `agent`
- `tier`
- `playbook`
- `tos_node`
- `kag_view`
- `runtime_surface`
- `seed`

### 4. Navigation budget-tests

Проверять:
- путь `pick -> inspect -> expand`
- явный fallback
- явный next hop
- отсутствие authority confusion

---

## Первый материализованный выход

- `aoa-routing/generated/federation_entrypoints.min.json`
- расширенный `aoa-routing/generated/tiny_model_entrypoints.json`
- `aoa-routing/docs/FEDERATION_ENTRY_ABI.md`
- один budget-test contract or eval
- короткие root-entry shells for AoA and ToS

---

## Границы, которые должны выжить

1. `aoa-routing` остаётся navigation and dispatch layer.
2. Orientation plane не подменяет source authority.
3. Entry cards не становятся authored meaning.
4. Малый путь открывает большой, а не заменяет его.

---

## Что не сеять сюда

- новый федеральный супер-README как единственный вход;
- роутер как автора смыслов;
- длинные doctrinal rewrites вместо коротких entry surfaces;
- taxonomy inflation before working starters.

---

## Предпочтительные формы посадки

- `aoa-routing/generated/federation_entrypoints.min.json`
- `aoa-routing/generated/tiny_model_entrypoints.json`
- `aoa-routing/docs/FEDERATION_ENTRY_ABI.md`
- small-model entry shells in root READMEs

---

## Задание для Codex

1. Начать с малого entry card contract.
2. Удержать orientation отдельно от authority.
3. Расширять routing kinds только там, где уже есть реальные surfaces.
4. Добавить хотя бы один budget-test besides shape validation.

---

## Признак удачной посадки

После посадки малая модель проходит федерацию через короткие entry cards и за 2-3 хода доходит до правильного owning surface без топологической фантазии.
