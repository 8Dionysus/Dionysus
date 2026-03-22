---
seed_id: seed.8dionysus.aoa-shared.bridges
title: AoA-ToS Bridge Contracts
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: interface-seed
status: living
priority: high
parent_seed: seed.8dionysus.aoa-tos.rootline
tags:
  - writeback
  - retrieval
  - shared-contracts
  - policy-gates
  - observer-logging
---

# Seed: AoA-ToS Bridge Contracts

## Назначение
Этот seed предназначен для shared / interface / infra / `aoa-*` репозиториев, которые соединяют AoA runtime и ToS memory layer.

Он не описывает весь AoA и не заменяет ToS ontology. Он описывает мосты.

---

## Корневой импульс
AoA действует. ToS помнит.
Но мост между ними должен быть явным, дисциплинированным и обратимым.

---

## Что сеять

### 1. Writeback from AoA to ToS
AoA должен уметь писать в ToS не шум, а отобранный опыт:
- сильные traces
- важные ошибки
- новые lineages
- синтезы
- развилки

Минимальная посадка:
- `docs/contracts/aoa-writeback.md`
- schema experience record

### 2. Retrieval from ToS back into AoA
Retrieval должен возвращать не только facts, но и axis:
- линия происхождения
- связанный конфликт
- контекст практики
- предшествующие формы ответа
- узлы, к которым стоит вернуться

Минимальная посадка:
- `docs/contracts/tos-retrieval-axis.md`
- retrieval response schema

### 3. Shared Experience Record
Нужен общий контракт записи опыта.
Минимальные поля:
- `trace_id`
- `source_agent`
- `task_type`
- `outcome`
- `confidence`
- `lineage_refs`
- `conflict_refs`
- `practice_refs`
- `mutation_refs`
- `eligible_for_writeback`

### 4. Policy Gates and Approval Hooks
На мостах должны быть gate'ы:
- перед записью чувствительных артефактов;
- перед действиями, требующими human approval;
- перед переходом из green в yellow/red зоны.

### 5. Observer Logging Conventions
Мост должен быть наблюдаемым.
Ввести единые конвенции логов для:
- retrieval events
- writeback events
- policy interruptions
- rollbacks
- mutation-linked events

### 6. Philosopher-Agent Touchpoint
Если в repo уместно, оставить точку интеграции для philosopher-agent:
- drift checks
- axis checks
- reflective summaries

---

## Что не сеять сюда
- полную онтологию ToS;
- полный kernel AoA;
- repo-specific runtime детали, которые принадлежат дочерним репозиториям.

---

## Предпочтительные формы посадки
- interface contracts
- schemas
- event specs
- logging conventions
- approval hook notes
- bridge readmes

---

## Задание для Codex
1. Найти repo-границы: где кончается runtime и начинается memory/interface.
2. Посеять мосты как контракты, а не как абстрактные лозунги.
3. Свести философию к рабочим интерфейсам.
4. Оставить хотя бы один явный schema / contract / event spec.
5. Не расползаться в детали, которые должны жить в AoA или ToS repo отдельно.

---

## Признак удачной посадки
После посадки ясно:
- как AoA пишет опыт в ToS;
- что именно возвращает ToS AoA;
- как проходят gates, approvals и observer logging;
- где проходит общий интерфейс между действием и памятью.
