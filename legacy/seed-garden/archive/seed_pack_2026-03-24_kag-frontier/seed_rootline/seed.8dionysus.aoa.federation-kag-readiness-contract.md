seed_id: seed.8dionysus.aoa.federation-kag-readiness-contract
title: Federation KAG Readiness Contract
profile_anchor: 8Dionysus
projects:
  - AoA
  - ToS
kind: interface-seed
status: living
priority: high
parent_seed: seed.8dionysus.aoa-tos.rootline
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
  - kag
  - federation
  - provenance
  - export
  - source-owned
  - bounded-surfaces
  - small-models

# Seed: Federation KAG Readiness Contract

## Назначение

Этот seed нужен, чтобы сделать федерацию KAG-пригодной без превращения `aoa-kag` в источник истины.

Он вводит:
- общий федеральный export contract;
- source-owned `kag_export.min.json`;
- bounded KAG surface families;
- первые sow targets в `aoa-kag`;
- упаковку по размеру модели.

---

## Корневой импульс

Федерация должна публиковать не “граф всего”, а маленькие derived surfaces, которые:

- ведут обратно к authority;
- сохраняют provenance;
- различают repo roles;
- помогают малым моделям войти без топологической галлюцинации.

---

## Что сеять

### 1. `federation_kag_export`

Минимальный контракт:

```yaml
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

### 2. Four-surface KAG posture

- `federation_spine.min.json`
- section / chunk maps
- query-mode context packs
- one-hop edge or axis hints

### 3. Model-size packaging rule

- `tiny`
- `standard`
- `deep`

### 4. Repo asymmetry rule

Один publication law.
Не одна смысловая схема для всех репо.

---

## Первый материализованный выход

- `aoa-kag/schemas/federation-kag-export.schema.json`
- `aoa-kag/docs/FEDERATION_KAG_READINESS.md`
- `aoa-kag/examples/federation_kag_export.example.json`
- `aoa-kag/generated/federation_spine.min.json`
- один pilot `generated/kag_export.min.json`

---

## Границы, которые должны выжить

1. `aoa-kag` остаётся derived substrate.
2. KAG не становится source truth, routing, proof или memory canon.
3. Export surfaces обязаны возвращать к authority surfaces.
4. Reviewability важнее graph inflation.

---

## Что не сеять сюда

- федеративный markdown scraping;
- vendor-first graph platform как канон;
- симметрию там, где федерация асимметрична;
- routing logic inside KAG.

---

## Предпочтительные формы посадки

- `aoa-kag/schemas/federation-kag-export.schema.json`
- `aoa-kag/docs/FEDERATION_KAG_READINESS.md`
- `aoa-kag/generated/federation_spine.min.json`
- pilot export surfaces in neighboring source repos

---

## Задание для Codex

1. Сначала зафиксировать contract и example.
2. Не читать source repos через raw markdown, если можно читать их generated exports.
3. Удержать `aoa-kag` в derived posture.
4. Сохранить repo-type asymmetry.

---

## Признак удачной посадки

После посадки `aoa-kag` честно композитит source-owned exports, а малые модели получают bounded KAG entry surfaces без source collapse.
