---
seed_id: seed.8dionysus.tos.genealogical-memory
title: ToS Genealogical Memory
profile_anchor: 8Dionysus
projects:
  - ToS
kind: repo-seed
status: living
priority: high
parent_seed: seed.8dionysus.aoa-tos.rootline
tags:
  - genealogical-memory
  - vector-graph
  - lineages
  - conflict
  - embodied-knowledge
  - ontology
---

# Seed: ToS Genealogical Memory

## Назначение
Этот seed предназначен для ToS и тех репозиториев, где живут память, онтология, ingestion, retrieval, graph/vector contracts и knowledge shaping.

Он фиксирует ToS не как wiki и не как склад заметок, а как долговременную генеалогическую память.

---

## Корневой импульс
ToS должен хранить не только содержание, но и происхождение.
Не только что сказано, но:
- откуда выросло;
- чему отвечало;
- с чем спорило;
- во что преобразовалось;
- какими практиками воплотилось.

---

## Что сеять

### 1. Genealogical Memory
Ввести базовый тезис: ToS есть генеалогическая память.

Хранить:
- происхождение идей;
- линии влияния;
- полемики;
- точки перелома;
- синтезы;
- возвращающиеся мотивы.

Минимальная посадка:
- `docs/ontology/genealogical-memory.md`

### 2. Vector + Graph Substrate
Память ToS должна быть двойной:
- vector для смысловой близости;
- graph для родства, влияния, конфликта, времени и линии становления.

Минимальная посадка:
- `docs/architecture/vector-graph-substrate.md`
- storage / retrieval contracts

### 3. Lineages instead of tags
Вместо плоских тегов использовать lineages.

Не просто `Nietzsche`, а:
- до
- перелом
- после
- инверсии
- ответвления
- полемические узлы

### 4. Practices of Life as Memory Entities
ToS должен хранить не только абстракции, но и практики жизни:
- тело
- тренировка
- дыхание
- ритм
- речь
- танец
- музыка
- искусство
- кризис / переход / преобразование

### 5. Layered Summarization
Память должна иметь слои:
- `fragment`
- `note`
- `cluster`
- `lineage`
- `synthesis`
- `canon`

### 6. Conflict as First-Class Entity
Хранить:
- противоречия
- несводимости
- полемики
- внутренние разломы
- эволюцию позиции

### 7. Minimal Ontology
Рекомендуемые типы узлов:
- `Person`
- `Work`
- `Concept`
- `Practice`
- `Project`
- `Event`
- `Lineage`
- `Conflict`
- `Synthesis`
- `Seed`

Рекомендуемые типы рёбер:
- `SOURCE_OF`
- `RESPONDS_TO`
- `TRANSFORMS_INTO`
- `EMBODIED_BY`
- `PRACTICED_WITH`
- `CONFLICTS_WITH`
- `FEEDS`
- `SYNTHESIZES`
- `SEEDS`
- `RETURNS_TO`

---

## Что не сеять сюда
- детали runtime AoA;
- kernel orchestration;
- sandboxing policies;
- operative agent schemas, если repo не связан с ними напрямую.

---

## Предпочтительные формы посадки
- ontology docs
- graph schema drafts
- vector/graph contracts
- ingestion notes
- retrieval docs
- seed lineage notes

---

## Задание для Codex
1. Найти места, где уже живут ontology, storage, retrieval и ingestion.
2. Посеять тезис генеалогической памяти и поддерживающие его структуры.
3. Не превращать repo в перегруженный философский трактат.
4. Оставить не только docs, но и хотя бы один структурный артефакт: schema, ontology stub или retrieval contract.
5. Сохранить терминологию lineages / conflict / practices / synthesis.

---

## Признак удачной посадки
После посадки ясно:
- что ToS помнит происхождение, а не только фрагменты;
- как сочетаются vector и graph;
- почему lineages важнее тегов;
- где в памяти живут практики, конфликт и синтез.
