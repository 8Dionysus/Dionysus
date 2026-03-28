seed_id: seed.8dionysus.tos.tree-first-kag-entry-seam
title: ToS Tree-First KAG Entry Seam
profile_anchor: 8Dionysus
projects:
  - ToS
  - AoA
kind: knowledge-architecture
status: living
priority: high
parent_seed: seed.8dionysus.aoa-tos.rootline
sow_targets:
  - Tree-of-Sophia
  - aoa-kag
  - aoa-routing
tags:
  - tos
  - tree-first
  - entry
  - kag
  - small-models
  - zarathustra
  - authority

# Seed: ToS Tree-First KAG Entry Seam

## Назначение

Этот seed нужен, чтобы малая модель могла честно войти в ToS через короткий rooted route, не ломая source-first law.

Он вводит:
- `tos_tiny_entry_route`;
- tree-first machine seam;
- bounded worked example на текущем Zarathustra route;
- первые sow targets в `Tree-of-Sophia`;
- downstream boundary для `aoa-kag` и `aoa-routing`.

---

## Корневой импульс

ToS уже знает свой закон:

- tree for orientation
- graph for relation
- source for authority

Следующий шаг не в смене закона, а в коротком входном шве для малых моделей.

---

## Что сеять

### 1. `tos_tiny_entry_route`

```yaml
route_id: string
root_surface: string
node_kind: source_node | concept_node | lineage_node | context_node
capsule_surface: string
authority_surface: string
lineage_or_context_hop: string | null
fallback: string
non_identity_boundary: string
```

### 2. Tree-first entry chain

`tos-root -> node-kind -> capsule -> authority -> lineage/context hop`

### 3. First bounded worked example

Использовать текущий Zarathustra route как первый public tiny-entry example.

---

## Первый материализованный выход

- short ToS tiny-entry contract doc
- one `tos_tiny_entry_route` example file
- one worked example tied to `docs/ZARATHUSTRA_TRILINGUAL_ENTRY.md`
- optional first public `context_node` example if it helps the route hold

---

## Границы, которые должны выжить

1. ToS остаётся authored authority.
2. Tree остаётся primary orientation.
3. Graph остаётся secondary relation layer.
4. `aoa-kag` остаётся downstream derived consumer.
5. Один `node_id` важнее трёх параллельных language trees.

---

## Что не сеять сюда

- graph-first default entry into ToS;
- KAG summary instead of source node;
- три parallel language trees;
- большой expansion wave before a proven tiny-entry seam.

---

## Предпочтительные формы посадки

- `Tree-of-Sophia/docs/TINY_ENTRY_ROUTE.md`
- `Tree-of-Sophia/examples/tos_tiny_entry_route.example.json`
- one worked example rooted in the current Zarathustra route

---

## Задание для Codex

1. Сохранить tree-first posture без упрощения authored meaning.
2. Сделать tiny-entry route коротким, но не плоским.
3. Держать KAG and routing strictly downstream.
4. Привязать первый example к уже открытому bounded route, а не к абстрактной будущей ветке.

---

## Признак удачной посадки

После посадки малая модель входит в ToS через короткий rooted chain, быстро достигает первого authored объекта и не путает derived help surfaces с authority.
