---
id: seed.tos.tree-first-kag-entry-seam.v0
title: Tree-first KAG seam для малого входа в ToS
en_title: Tree-First KAG Entry Seam for ToS
project: ToS
status: seed
priority: high
kind: knowledge-architecture
sow_targets:
  - Tree-of-Sophia
  - aoa-kag
  - aoa-routing
tags:
  - tos
  - tree-first
  - entry
  - small-models
  - kag
  - zarathustra
  - provenance
  - authority
---

# Seed: Tree-first KAG seam для малого входа в ToS

## Суть

ToS уже знает свой закон:

- tree for orientation
- graph for relation
- source for authority

Но малой модели от этого закона мало, если первый маршрут всё равно слишком длинный.
Значит нужен не новый смысл, а маленький machine seam:

`tos-root -> node-kind -> capsule -> authority -> lineage/context hop`

---

## Человеческое заземление

ToS сильна именно тем, что не сводится ни к flat notes, ни к retrieval substrate.
Но её текущий public entry path всё ещё больше похож на human-liturgical ascent, чем на low-context machine route.

Это не упрёк архитектуре.
Это указание на следующий технический шов.

---

## Проблема

### 1. Малой модели трудно войти честно

Она видит длинный doctrinal путь раньше, чем получает первый stable object.

### 2. Graph-first shortcut здесь опасен

Если заменить tree-first route графовым обзором, малый вход потеряет корень раньше, чем получит relation value.

### 3. Downstream layers могут начать спешить

`aoa-kag` и `aoa-routing` будут полезны, только если ToS сначала отдаст им честный source-first seam.

### 4. Нужен первый worked example

Текущий Zarathustra route уже даёт bounded public gate.
Им нужно воспользоваться как первым машинным образцом.

---

## Предложение

### 1. Ввести `tos_tiny_entry_route`

```yaml
tos_tiny_entry_route:
  route_id: string
  root_surface: string
  node_kind: source_node | concept_node | lineage_node | context_node
  capsule_surface: string
  authority_surface: string
  lineage_or_context_hop: string | null
  fallback: string
  non_identity_boundary: string
```

### 2. Сохранить tree-first chain

Базовый маршрут для малой модели:

1. `tos-root`
2. `node-kind`
3. small capsule
4. authority surface
5. optional lineage/context hop

Graph or KAG relations могут прийти позже.
Но не раньше rooted entry.

### 3. Взять Zarathustra route как первый bounded example

Первый worked example должен держаться за уже открытый route:

- current bounded trilingual Zarathustra entry
- один shared `node_id`
- witness-linked language surfaces
- явная authority boundary

### 4. Оставить downstream handoff derived

`aoa-kag` и `aoa-routing` могут:
- индексировать tiny-entry seam
- давать starters and bridges
- строить derived projections

Но не могут:
- заменить authored ToS authority
- превратить graph relations в primary orientation

---

## Границы, которые должны выжить

1. ToS остаётся authored source-first authority.
2. Tree stays primary for entry.
3. Graph stays secondary for relation.
4. KAG stays downstream and derived.
5. Один `node_id` важнее трёх параллельных языковых деревьев.

---

## Что не сеять сюда

- graph-first ToS overview as default entry;
- три parallel language trees;
- KAG summary as replacement for source node;
- большой корпусный rollout до доказанного tiny-entry seam.

---

## Первый материализованный выход

- короткий ToS tiny-entry contract doc
- one small example file for `tos_tiny_entry_route`
- one worked example tied to `docs/ZARATHUSTRA_TRILINGUAL_ENTRY.md`
- optional first public `context_node` example only if it helps the route hold under review

---

## Признак удачной посадки

После посадки малая модель может:

- начать с короткого rooted route;
- быстро дойти до первого authored ToS object;
- понять, где authority, а где derived help surface;
- не спутать graph relations с первичным способом входа.
