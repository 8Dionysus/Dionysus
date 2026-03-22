---
id: seed.aoa.restartable-inquiry-loop.v0
title: Перезапускаемая петля исследования
en_title: Restartable Inquiry Loop
project: AoA
status: seed
priority: high
kind: playbook-architecture
sow_targets:
  - aoa-playbooks
  - aoa-memo
  - aoa-evals
  - aoa-agents
  - tos-bridge
tags:
  - aoa
  - inquiry
  - philosophy
  - checkpoints
  - restart
  - artifacts
  - long-horizon
  - depth
---

# Seed: Перезапускаемая петля исследования

## Суть

Для длинных философских, архитектурных и синтетических задач AoA нужен не “очень длинный контекст”, а restartable inquiry loop.

Крупного агента можно и нужно перезапускать,
если перед ним лежит правильно собранный пакет:
- цель;
- текущая ось;
- артефакты;
- доказательства;
- противоречия;
- открытые вопросы;
- память последнего витка.

---

## Человеческое заземление

Длинная работа редко делается в одном присесте.
Есть:
- усталость;
- отвлечения;
- смена дня;
- смена состояния;
- смена фазы проекта;
- ограничение контекста;
- ограничение локального железа.

Если большая задача зависит только от непрерывности разговора, она хрупка.
Если она зависит от checkpoint packs, она выживает.

---

## Проблема

Без restartable loop:

### 1. Контекст распухает
- важное тонет;
- повторяется уже пройденное;
- deep model тратится на самоудержание.

### 2. Теряется ось
- текущая гипотеза размывается;
- старые решения забываются;
- contradictions исчезают.

### 3. Нечем relaunch
- после паузы приходится заново “объяснять всё”;
- новый заход стартует из рваного summary;
- система начинает фантазировать continuity.

---

## Предложение

Ввести playbook длинного исследования с checkpoint-based restart.

### Базовый цикл

`gather -> frame -> test -> verify -> compress -> relaunch/deepen`

### Где:
- `gather` — собрать источники, traces, notes, evidence;
- `frame` — сформулировать текущую ось;
- `test` — породить и проверить локальные гипотезы;
- `verify` — найти слабые места, contradictions, missing proof;
- `compress` — сделать checkpoint pack;
- `relaunch/deepen` — перезапустить следующий виток с новым пакетом.

---

## Inquiry checkpoint pack

Каждый крупный виток должен уметь сжиматься в пакет.

### Обязательные поля
- objective
- mode
- core_question
- current_thesis
- evidence_pack_refs
- contradiction_pack_refs
- resolved_decisions
- open_questions
- next_tests
- witness_refs
- memory_delta_refs
- canon_delta_refs
- restart_count

### Смысл
Checkpoint pack нужен не для архива.
Он нужен, чтобы следующий большой запуск не начинал заново там, где уже пройдено.

---

## Deep-pass discipline

Глубокий агент не должен “жить внутри” всей петли.
Он вызывается на определённых витках:

1. initial framing
2. contradiction arbitration
3. synthesis of multiple lines
4. final judgement
5. crisis recovery when loop stalls

Остальное может делаться средними и малыми ярусами.

---

## Artifact-first rule

Каждый виток оставляет не просто ответ, а набор вещей:

- witness trace
- decision ledger
- contradiction map
- memory delta
- canon delta
- next-pass brief

Это делает длинную задачу переносимой.

---

## Human override

Человек может:
- остановить цикл;
- вернуть цикл на предыдущий checkpoint;
- отложить канонизацию;
- заблокировать следующий deep-pass;
- вручную повысить важное contradiction.

---

## Инварианты

1. Длинная задача не зависит от одного бесконечного чата.
2. Каждый виток оставляет portable artifact.
3. Contradictions не стираются ради гладкости.
4. Deep-pass не выполняется по привычке.
5. Перезапуск не должен требовать полного сырого контекста.
6. Checkpoint pack хранит provenance.
7. Человек может вмешаться в любой момент.
8. Canon delta и memory delta различаются.
9. Вопрос может пережить несколько витков без фальшивого закрытия.
10. Если задача остановлена на неделю, следующий запуск всё ещё держит ось.

---

## Минимальный контракт данных

### inquiry_checkpoint
```yaml
checkpoint_id: string
created_at: iso8601
objective: string
mode: philosophy | architecture | design | research | custom
core_question: string
current_thesis: string | null
evidence_pack_refs: []
contradiction_pack_refs: []
resolved_decisions: []
open_questions: []
next_tests: []
witness_refs: []
memory_delta_refs: []
canon_delta_refs: []
restart_count: integer
owner_roles: []
confidence: 0.0-1.0 | null
requires_human_review: boolean
```

### contradiction_item
```yaml
contradiction_id: string
claim_a: string
claim_b: string
source_refs: []
status: open | framed | resolved | deferred
importance: low | medium | high
```

### next_pass_brief
```yaml
brief_id: string
checkpoint_id: string
task_for_next_pass: string
must_keep: []
must_test: []
must_not_repeat: []
deep_pass_required: boolean
token_budget_hint: integer | null
```

---

## Куда сажать

### `aoa-playbooks`
- основной дом playbook
- long-horizon philosophical flow
- restart contract

### `aoa-memo`
- checkpoint object examples
- memory delta objects
- contradiction pack objects

### `aoa-evals`
- depth eval
- redundancy eval
- restart fidelity eval
- contradiction retention eval

### `aoa-agents`
- role duties for conductor / deep / archivist

### AoA -> ToS bridge
- что из inquiry loop может идти в ToS как mature synthesis
- что остаётся operational exploration

---

## Первые материальные артефакты

- `aoa-playbooks/playbooks/restartable-inquiry-loop.md`
- `aoa-memo/examples/inquiry_checkpoint.example.yaml`
- `aoa-memo/examples/next_pass_brief.example.yaml`
- `aoa-evals/bundles/aoa-restartable-inquiry/`

---

## Признак удачной посадки

После посадки длинная задача:
- не погибает от паузы;
- не раздувается бесконечным контекстом;
- умеет перезапускать deep agent на основе сжатого пакета;
- производит плотные артефакты;
- может реально жить в большом масштабе.
