# seed_bundle.dialogue-small-kag-federation-readiness.2026-03-23.md

Дата: 2026-03-24  
Статус: archived compressed bundle  
Назначение: сохранить сжатую форму трёх ближайших KAG frontier seed-линий после их посадки в owning repos без смешения KAG, routing и ToS-авторитета.

## Grounding

Этот bundle собран под уже существующую форму федерации:

- `aoa-kag` уже держит derived substrate posture, compact registry и validator;
- `aoa-routing` уже держит thin navigation surfaces и tiny-model starters;
- `Tree-of-Sophia` уже держит tree-first knowledge law и bounded Zarathustra route;
- `Dionysus` здесь нужен как seed-soil, а не как новый источник федерального смысла.

Цель не в том, чтобы сделать один “umbrella seed” про всё сразу.
Цель в том, чтобы сохранить, как raw-материал был разложен на три малых, связных и отдельно сеемых нерва, которые затем уже получили реальные landed surfaces.

---

## Archived outcome

- `FED-KAG-01` теперь живёт в landed public surfaces `aoa-kag`
- `FED-KAG-02` теперь живёт в landed public surfaces `aoa-routing`
- `TOS-KAG-01` теперь живёт в landed public surfaces `Tree-of-Sophia`

---

## NOW

### 1. FED-KAG-01 — Federation KAG Readiness Contract

Почему сейчас:
- KAG-ось уже признана важной, но ещё не стала федеральной дисциплиной публикации;
- без общего export contract `aoa-kag` рискует начать скрейпить markdown вместо чтения source-owned surfaces;
- малым моделям нужен не “общий граф”, а проверяемые короткие derived surfaces.

Практический выход:
- `federation_kag_export`
- `generated/kag_export.min.json` per source repo
- `federation_spine.min.json` и соседние bounded KAG views
- model-sized packaging: `tiny / standard / deep`

### 2. FED-KAG-02 — Federation Entry / Orientation ABI

Почему сейчас:
- текущий routing-контур уже помогает, но пока не покрывает федерацию целиком;
- для ИИ федерация должна читаться как набор entry cards, а не как атмосфера из README и длинных доктрин;
- различие `orientation plane` и `authority plane` уже фактически есть, но ещё не собрано в одно правило.

Практический выход:
- `federation_entrypoint`
- `generated/federation_entrypoints.min.json`
- расширенная taxonomy и starters в `aoa-routing`
- budget-tests на путь `pick -> inspect -> expand`

### 3. TOS-KAG-01 — Tree-First KAG Entry Seam

Почему сейчас:
- ToS очень сильна как authored source-first architecture, но вход всё ещё высок для малых моделей;
- tree-first rule уже есть, значит нужен не новый смысл, а короткий machine seam;
- bounded Zarathustra route уже даёт честный первый worked example.

Практический выход:
- `tos_tiny_entry_route`
- короткий ToS entry shell для малых моделей
- один bounded worked example на текущем Zarathustra route
- явная downstream boundary для `aoa-kag` и `aoa-routing`

---

## SUPPORTING, BUT NOT PRIMARY

### 1. Quickstart shells

Сюда относятся:
- `AoA in 7 lines`
- `ToS in 6 lines`
- короткий zero-hop вход перед длинными doctrinal stacks

Это не отдельные seeds.
Это supporting surfaces внутри `Federation Entry / Orientation ABI` и `Tree-First KAG Entry Seam`.

### 2. Glossary / examples / subtitle lifts

Сюда относятся:
- поднятие словаря и worked examples в первый хоп
- plain-language subtitles к doctrine-heavy файлам
- README contract alignment across repos

Это high-ROI moves, но не самостоятельные корневые seeds на этой фазе.

### 3. Full-federation rollout

Сюда относятся:
- обязательные KAG exports для всех source repos сразу
- единый федеральный посев по всем AoA layers
- дальние downstream adapters beyond first frontier

Это deliberately held later.
Сначала нужно доказать форму на `aoa-kag`, `aoa-routing`, `Tree-of-Sophia`.

---

## NOT SELECTED AS CORE SEEDS

### 1. Graph engine buildout

Причина:
- сейчас нужен publication contract и bounded surfaces;
- полноценный graph engine будет преждевременным расширением.

### 2. KAG as sovereign source

Причина:
- это прямо нарушило бы source-of-truth discipline;
- KAG здесь должна остаться derived substrate.

### 3. Total symmetry across the federation

Причина:
- `Tree-of-Sophia`, `aoa-techniques`, `aoa-routing`, `abyss-stack` и другие слои по природе не симметричны;
- export contract должен быть общий по дисциплине, но не одинаковый по смыслу.

---

## Compression

Если ужать этот pack до трёх главных нервов, они такие:

1. федерации нужен общий KAG-ready publication contract, а не один большой граф;
2. федерации нужен machine-readable ABI входа, где orientation не притворяется authority;
3. ToS нужен свой короткий tree-first seam для малых моделей, не размывающий authored source.
