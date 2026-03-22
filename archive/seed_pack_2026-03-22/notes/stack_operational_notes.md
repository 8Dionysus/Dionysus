# stack\_operational\_notes.md

Дата: 2026-03-22

Это не корневые seeds.
Это операционные заметки, которые выросли из диалога и должны лечь в `abyss-stack` и частично в `aoa-agents`.

\---

## 1\. Archivist as role, not as brand

Архивариус должен быть:

* быстрым;
* стабильно структурирующим;
* хорошим в summary + entity extraction + JSON-like outputs;
* способным переваривать длинный вход, но не обязанным быть самым “мудрым”.

В seed-корпусе лучше закрепить не конкретную модель, а требования к роли:

* `structured\_output\_strength`
* `compression\_fidelity`
* `entity\_recall`
* `memory\_candidate\_quality`
* `latency\_budget`

\---

## 2\. Context budgets by class, not by myth

Лучше мыслить не “модель умеет 128k”, а четырьмя корзинами:

* `core`
* `short`
* `long`
* `memory\_access`

### Practical posture

* большая глубокая модель: короткое ядро + ограниченный short window + selected memory access;
* средняя модель: основная рабочая дистанция;
* малая модель: compression / archive / route / verify.

Не seed-истина:

* точные числа по токенам;
* конкретная модель и квант как вечная норма.

Это должно жить в `abyss-stack/docs/model\_profiles.md`.

\---

## 3. Suggested landing paths

* `abyss-stack/docs/model\_profiles.md`
* `abyss-stack/docs/context\_budget\_policy.md`
* `aoa-agents/docs/ARCHIVIST\_ROLE.md`
* `aoa-agents/generated/model\_tier\_registry.json`

