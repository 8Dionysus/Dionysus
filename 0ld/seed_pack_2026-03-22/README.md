# Seed pack from the dialogue — local stack, memory thermodynamics, long-horizon loop

Дата: 2026-03-22

## Что это

Это аккуратно отобранный seed-пакет из текущего диалога, собранный под уже существующую форму репозиториев `8Dionysus`.

Я не делал монолитный “общий текст”.
Я разложил материал по тем слоям, которые уже видны в профиле:

- `Agents-of-Abyss` — конституционный центр, карта слоёв, правила федерации;
- `aoa-memo` — явная память и recall-контракты;
- `aoa-agents` — роли, профили, memory posture, handoffs;
- `aoa-playbooks` — сценарии, композиции, decision points, fallback paths;
- `aoa-routing` — тонкая навигация и dispatch hints;
- `abyss-stack` — runtime, storage, mounts, deployment, model profiles;
- `Tree-of-Sophia` — source-first living knowledge architecture;
- `Dionysus` — seed-почва с уже существующими `seed_bundle`, `seed_rootline`, `seed_witness`.

## Что уже есть в seed-корпусе и что я не дублировал

В существующем seed-корпусе уже есть сильные линии:

- `Narrative-Core Memory`
- `Self-Agent Checkpoint Stack`
- `Context Compost`
- `AoA × ToS Rootline`
- `Witness Protocol`

Поэтому я не переписывал эти seeds заново.

## Что я добавил как действительно новое

### 1. Memory Thermodynamics
Чего не хватало:
- памяти внутри памяти;
- температур памяти;
- явной политики забывания;
- memory posture, зависящего от роли агента;
- отдельного memory steward / librarian daemon.

Это самый сильный новый нерв диалога.

### 2. Model-Tier Orchestration
Чего не хватало:
- явного оркестра по размерам и скоростям моделей;
- роли conductor как мета-переключателя;
- различения Q4/Q5 как разных постов одной и той же крупной модели;
- формальной state machine:
  `route -> plan -> do -> verify -> deep? -> distill`.

Это превращает связку моделей в архитектуру, а не в свалку “умных штук”.

### 3. Restartable Inquiry Loop
Чего не хватало:
- restartable long-horizon playbook для больших философских и архитектурных задач;
- checkpoint package, позволяющего перезапускать крупного агента без потери оси;
- артефакт-первого цикла для глубоких длинных задач.

Это делает “длинную петлю” не мечтой, а переносимым протоколом.

## Что я оставил только как support notes, а не как основные seeds

### Stack operational notes
Сюда вынесены:
- context budgets по классам моделей;
- storage spillover на внешний SSD;
- warm/cold data placement;
- тонкие практические решения для `abyss-stack`.

Причина: это важно, но это не корневые seeds. Это операционная плоть, а не новое ядро метафизики.

## Что я сознательно НЕ включил в seed-ядро

- конкретные USB-C кабели;
- конкретные бренды SSD-корпусов;
- точные модельные рекомендации как догму;
- ARC-AGI как самостоятельный operational seed;
- поэтическую часть про рождение дитя как отдельный артефакт.

Не потому, что это слабо.
А потому, что seed должен усиливать архитектуру, а не раздувать её атмосферой или железной мелочью.

## Как это сажать

### В `Dionysus`
Как seed-артефакты:
- `seed_bundle/`
- `seed_rootline/`
- `seed_witness/`

### В `aoa-memo`
Сажать:
- температурные слои памяти;
- salience / novelty / decay / promotion rules;
- memory steward contracts;
- explicit memory object schemas.

### В `aoa-agents`
Сажать:
- memory posture per role;
- forgetting posture per role;
- model-tier duties;
- allowed memory scopes;
- escalation contracts.

### В `aoa-playbooks`
Сажать:
- restartable inquiry loop;
- long-horizon philosophical task playbook;
- evidence-pack handoff;
- checkpoint/relaunch path.

### В `aoa-routing`
Сажать:
- task-to-tier hints;
- escalation triggers;
- deep-call conditions;
- thin dispatch surfaces only.

### В `abyss-stack`
Сажать:
- model profile registry;
- context budget contracts;
- storage tiering notes;
- spillover / mount / path policy.

## Файлы в этом пакете

- `seed_bundle/seed_bundle.dialogue-local-stack-memory-loop.2026-03-22.md`
- `seed_rootline/seed.8dionysus.aoa.memory-thermodynamics.md`
- `seed_rootline/seed.8dionysus.aoa.model-tier-orchestration.md`
- `seed_rootline/seed.8dionysus.aoa.restartable-inquiry-loop.md`
- `seed_witness/seed.aoa.memory-thermodynamics.v0.md`
- `seed_witness/seed.aoa.model-tier-orchestration.v0.md`
- `seed_witness/seed.aoa.restartable-inquiry-loop.v0.md`
- `notes/stack_operational_notes.md`
