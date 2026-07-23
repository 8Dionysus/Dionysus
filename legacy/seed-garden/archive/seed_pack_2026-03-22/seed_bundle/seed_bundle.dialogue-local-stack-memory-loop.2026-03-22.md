# seed_bundle.dialogue-local-stack-memory-loop.2026-03-22.md

Дата: 2026-03-22  
Статус: compressed priority bundle  
Назначение: выбрать ближайшие seeds из текущего диалога без смешения ядра, runtime и железной тактики.

## Grounding

Этот bundle собран под текущую форму экосистемы `8Dionysus`.

Не цель:
- переписать уже существующие seeds;
- канонизировать конкретные модели и железо;
- растворить `aoa-memo`, `aoa-agents`, `aoa-playbooks`, `aoa-routing` и `abyss-stack` в один “супер-репо”.

Цель:
- усилить то, чего ещё нет в seed-корпусе;
- не дублировать `Self-Agent`, `Witness Protocol`, `Context Compost`;
- добавить missing middle между памятью, оркестрацией и длинной петлёй.

---

## NOW

### 1. AOA-SEED-09 — Memory Thermodynamics
Почему сейчас:
- тема памяти стала центральной осью диалога;
- уже есть `Context Compost`, но не хватает именно runtime-термодинамики памяти;
- без температурной стратификации память быстро превращается либо в свалку, либо в мнимый канон.

Практический выход:
- `memory temperatures`: `core / hot / warm / cold`;
- salience gate: `novelty × impact × recurrence × risk`;
- decay / promotion / demotion contracts;
- role-specific memory posture.

### 2. AOA-SEED-10 — Model-Tier Orchestration
Почему сейчас:
- связка моделей уже мыслится как иерархия ролей, а не как одна универсальная сеть;
- у крупной модели появилась правильная роль: не делать всё, а держать мета-уровень;
- эта ось связывает `aoa-agents`, `aoa-routing`, `aoa-playbooks` и `abyss-stack`.

Практический выход:
- tier registry;
- conductor contract;
- deep-escalation triggers;
- internal mode contract;
- quantization sibling roles (`Q4` как conductor, `Q5` как deep judge).

### 3. AOA-SEED-11 — Restartable Inquiry Loop
Почему сейчас:
- ты прямо поставил вопрос о длинной, глубокой и многогранной петле;
- без restart protocol большие задачи будут распадаться на усталые монологи;
- этот seed даёт playbook для крупных философских и архитектурных задач.

Практический выход:
- inquiry checkpoint pack;
- artifact-first long-horizon cycle;
- restart / relaunch protocol for large agents;
- contradiction pack + canon delta + memory delta.

---

## SUPPORTING, BUT NOT PRIMARY

### STACK-NOTE-01 — Context Budget Matrix
Сюда относятся:
- бюджет `core / short / long / memory access`;
- профили по классам моделей;
- правила, когда контекст растить нельзя и надо сжимать память.

### STACK-NOTE-02 — Storage Spillover Contract
Сюда относятся:
- перегруз встроенного SSD;
- spillover на внешний SSD;
- перенос холодных моделей, логов, индексов, архивов;
- path / mount / sync policy.

---

## NOT SELECTED AS CORE SEEDS

### 1. Exact hardware shopping details
Причина:
- полезно для рабочего стека;
- но это implementation note, а не несущая балка seed-корпуса.

### 2. Specific model names as doctrine
Причина:
- сегодня годится одна модель, завтра другая;
- seed должен кодировать роль, а не бренд.

### 3. ARC-AGI as a standalone operational seed
Причина:
- это сильный философский импульс;
- но на текущем этапе он лучше служит оправданием seeds про память и рождение правила, а не самостоятельным артефактом.

---

## Compression

Если ужать всё до трёх главных нервов этого диалога, они такие:

1. память должна иметь температуру и право на забывание;
2. крупная модель должна быть судьёй и дирижёром, а не вечным грузчиком;
3. длинная задача должна жить через checkpoint packs и restartable loops, а не через бесконечный контекст.
