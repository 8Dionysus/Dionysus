---
id: seed.aoa.federation-kag-readiness-contract.v0
title: Федеративный KAG-ready контракт публикации
en_title: Federation KAG Readiness Contract
project: AoA
status: seed
priority: high
kind: interface-architecture
sow_targets:
  - aoa-kag
  - aoa-techniques
  - aoa-skills
  - aoa-evals
  - aoa-memo
  - aoa-playbooks
  - aoa-agents
  - Tree-of-Sophia
tags:
  - aoa
  - kag
  - federation
  - provenance
  - export
  - source-owned
  - small-models
  - bounded-surfaces
---

# Seed: Федеративный KAG-ready контракт публикации

## Суть

Федерация должна стать KAG-пригодной не через один “общий граф”, а через дисциплину публикации:

- source repos публикуют компактные KAG-ready surfaces;
- `aoa-kag` собирает из них bounded derived views;
- `aoa-routing` и модели читают эти views как guide surfaces, а не как новый трон смысла.

Иными словами, KAG здесь должна стать не императором графа, а переводчиком федерации.

---

## Человеческое заземление

Сейчас `aoa-kag` уже не пуст.
Там есть:

- роль слоя;
- границы;
- compact registry;
- validator;
- первые generated packs.

Но пока нет федерального закона публикации.
Если его не ввести, дальше почти неизбежно начнётся одно из трёх:

1. прямой парсинг сырого markdown из соседних репо;
2. молчаливая подмена authored source derived слоем;
3. graph theater раньше, чем появится reviewable contract.

---

## Проблема

### 1. KAG легко притворяется источником

Когда derived layer становится самым удобным местом входа, появляется соблазн начать считать его главным.
Для этой федерации это опасно.

### 2. Нет общего export contract

Пока у source repos нет общего compact shape, `aoa-kag` нечего честно композитить на федеральном уровне.

### 3. Один формат не подходит всем

`Tree-of-Sophia`, `aoa-techniques`, `aoa-routing`, `aoa-agents`, `abyss-stack` и другие репо асимметричны.
Им нужен общий publication law, но не одинаковая смысловая схема.

### 4. Малые модели страдают от избытка

Им нужны короткие bounded surfaces.
Большой “граф всего” только усилит распыление.

---

## Предложение

### 1. Ввести `federation_kag_export`

Каждый source repo должен публиковать минимальный экспортный контракт, достаточный для derived KAG сборки.

```yaml
federation_kag_export:
  owner_repo: string
  kind: string
  object_id: string
  primary_question: string
  summary_50: string
  summary_200: string
  source_inputs: []
  entry_surface:
    repo: string
    path: string
    match_key: string
    match_value: string
  section_handles: []
  direct_relations: []
  provenance_note: string
  non_identity_boundary: string
```

### 2. Собрать четыре bounded surface families

- `federation_spine.min.json`
- section / chunk maps for bounded retrieval
- context packs for modes such as `local_search`, `global_search`, `drift_search`
- one-hop edge hints, retrieval-axis bundles, counterpart hints

### 3. Сделать KAG упаковку бюджетной по размеру модели

- `tiny`
  - top entry objects only
  - one-hop only
  - short summaries
- `standard`
  - more direct relations
  - section handles
- `deep`
  - axis bundles
  - provenance notes
  - conflict or tension refs

### 4. Сохранить асимметрию репо

Экспорт должен подстраиваться под repo type:

- ToS экспортирует source / concept / lineage / context paths
- AoA repos экспортируют techniques, skills, evals, agents, playbooks, memo objects
- infrastructure repos экспортируют capabilities and dependency surfaces

### 5. Начать с малого

Первый посев должен оставить:

- schema-backed contract в `aoa-kag`
- один RFC про federal KAG readiness
- один composed spine view
- один pilot export из соседнего source repo

---

## Границы, которые должны выжить

1. `aoa-kag` остаётся derived substrate.
2. KAG не становится authored source, proof layer, routing layer или memory truth.
3. Export surfaces ведут обратно к authority surfaces.
4. Reviewable provenance важнее “богатого графа”.
5. Repo asymmetry не должна стираться ради удобства схемы.

---

## Что не сеять сюда

- прямой федеративный markdown scraping как норму;
- vendor-first graph platform как новый канон;
- полную симметрию между ToS, AoA layer repos и runtime repos;
- огромный graph engine раньше export discipline;
- routing logic inside `aoa-kag`.

---

## Первый материализованный выход

- `aoa-kag/schemas/federation-kag-export.schema.json`
- `aoa-kag/docs/FEDERATION_KAG_READINESS.md`
- `aoa-kag/examples/federation_kag_export.example.json`
- `aoa-kag/generated/federation_spine.min.json`
- один pilot `generated/kag_export.min.json` в соседнем source repo

---

## Признак удачной посадки

После посадки можно честно сказать:

- каждый важный source repo умеет публиковать маленький KAG-ready export;
- `aoa-kag` композитит эти exports, а не выдумывает их из воздуха;
- малые модели получают bounded entry surfaces;
- никто не перепутал derived карту с authored источником.
