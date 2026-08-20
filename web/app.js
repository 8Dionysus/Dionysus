"use strict";

const STORAGE_KEY = "dionysus.reflection-workbook.v0.1";
const SCHEMA_VERSION = "0.1.0";

const MODULES = {
  strivings: {
    number: "01",
    title: "Мои стремления",
    description: "Что вы сейчас пытаетесь начать, сохранить, изменить или довести до конца.",
    time: "8–12 минут",
    method: "personal-strivings",
    steps: [
      {
        eyebrow: "Слой 1 · Направление",
        title: "Что вы стараетесь делать сейчас?",
        intro: "Продолжите фразу «В последнее время я стараюсь…». Это могут быть большие цели, повседневные усилия или то, что вы пытаетесь не потерять.",
      },
      {
        eyebrow: "Слой 2 · Внутренняя карта",
        title: "Как ощущается каждое стремление?",
        intro: "Отметьте субъективное ощущение. Это не шкала личности и не сравнение с другими людьми.",
      },
      {
        eyebrow: "Слой 3 · Связи",
        title: "Где стремления помогают и мешают друг другу?",
        intro: "Ищем не идеальный баланс, а реальные напряжения и опоры для будущего разговора.",
      },
    ],
  },
  lifeStory: {
    number: "02",
    title: "Жизненные сцены",
    description: "Несколько эпизодов, через которые видны изменения, выбор и смысл.",
    time: "15–25 минут",
    method: "life-story-interview-ii",
    steps: [
      {
        eyebrow: "Слой 1 · Главы",
        title: "Если жизнь — книга, какие в ней главы?",
        intro: "Дайте каждой главе короткое название. Даты и подробный пересказ не обязательны — важна ваша собственная разбивка.",
      },
      {
        eyebrow: "Слой 2 · Высокая точка",
        title: "Вспомните сцену, в которой жизнь ощущалась особенно полной",
        intro: "Опишите один конкретный момент: что происходило, кто был рядом и почему именно эта сцена важна сейчас.",
      },
      {
        eyebrow: "Слой 3 · Трудность и поворот",
        title: "Какая сцена изменила направление?",
        intro: "Трудная точка и поворот могут быть одним событием или разными. Можно ответить только на одну часть.",
      },
      {
        eyebrow: "Слой 4 · Продолжение",
        title: "Что продолжается — и что может стать следующей главой?",
        intro: "Отделите устойчивую нить от желаемого будущего. Ни то ни другое не обязано быть окончательным.",
      },
    ],
  },
  countermap: {
    number: "03",
    title: "Контркарта",
    description: "Проверка удобного рассказа о себе на исключения, контекст и другую трактовку.",
    time: "10–15 минут",
    method: "counterportrait-v0",
    steps: [
      {
        eyebrow: "Слой 1 · Формулировка",
        title: "Какое описание себя кажется вам правдоподобным?",
        intro: "Возьмите одну фразу, которую вы уже используете или легко могли бы принять. Мы не будем считать её фактом — только проверим границы.",
      },
      {
        eyebrow: "Слой 2 · За и против",
        title: "Где эта фраза работает, а где ломается?",
        intro: "Нужны конкретные ситуации по обе стороны. Исключение не отменяет наблюдение, но помогает не сделать его слишком общим.",
      },
      {
        eyebrow: "Слой 3 · Другой угол",
        title: "Как ещё можно объяснить тот же материал?",
        intro: "Попробуйте отделить вашу привычную версию от взгляда другого человека и от альтернативного объяснения.",
      },
      {
        eyebrow: "Слой 4 · Более точная версия",
        title: "Как теперь звучит осторожная формулировка?",
        intro: "Хорошая версия называет условия и оставляет место для неизвестного. Её всё равно предстоит проверить в разговоре.",
      },
    ],
  },
};

const app = document.querySelector("#app");
const privacyDialog = document.querySelector("#privacy-dialog");
const toast = document.querySelector("#toast");
const liveRegion = document.querySelector("#live-region");

let currentView = "home";
let activeModule = null;
let toastTimer = null;
let storageAvailable = canUseLocalStorage();
let state = loadState();

function canUseLocalStorage() {
  try {
    const probe = "__dionysus_storage_probe__";
    window.localStorage.setItem(probe, "1");
    window.localStorage.removeItem(probe);
    return true;
  } catch (_error) {
    return false;
  }
}

function makeId() {
  if (window.crypto && typeof window.crypto.randomUUID === "function") {
    return `workbook-${window.crypto.randomUUID()}`;
  }
  return `workbook-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function createInitialState() {
  const now = new Date().toISOString();
  return {
    schema_version: SCHEMA_VERSION,
    artifact_type: "dionysus-reflection-workbook",
    workbook_id: makeId(),
    created_at: now,
    updated_at: now,
    locale: "ru",
    modules: {
      strivings: {
        status: "not-started",
        current_step: 0,
        answers: {
          items: Array.from({ length: 5 }, () => ({
            text: "",
            importance: 3,
            progress: 3,
            ownership: 3,
          })),
          supports: "",
          conflicts: "",
          nextMove: "",
        },
      },
      lifeStory: {
        status: "not-started",
        current_step: 0,
        answers: {
          chapters: "",
          highPoint: "",
          highPointMeaning: "",
          difficultScene: "",
          turningPoint: "",
          continuity: "",
          futureChapter: "",
        },
      },
      countermap: {
        status: "not-started",
        current_step: 0,
        answers: {
          easyClaim: "",
          holds: "",
          breaks: "",
          outsideView: "",
          alternative: "",
          revisedClaim: "",
          openQuestion: "",
        },
      },
    },
  };
}

function loadState() {
  const initial = createInitialState();
  if (!storageAvailable) return initial;

  try {
    const saved = JSON.parse(window.localStorage.getItem(STORAGE_KEY));
    if (!saved || saved.schema_version !== SCHEMA_VERSION || !saved.modules) {
      return initial;
    }

    for (const moduleId of Object.keys(MODULES)) {
      if (!saved.modules[moduleId]) return initial;
    }

    return saved;
  } catch (_error) {
    return initial;
  }
}

function persist({ announce = false } = {}) {
  state.updated_at = new Date().toISOString();
  if (storageAvailable) {
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (_error) {
      storageAvailable = false;
    }
  }
  updateSaveState();
  if (announce) showToast(storageAvailable ? "Черновик сохранён в этом браузере" : "Черновик хранится только до закрытия страницы");
}

function updateSaveState() {
  const element = document.querySelector("[data-save-state]");
  if (!element) return;
  if (!storageAvailable) {
    element.textContent = "Локальное сохранение недоступно";
    return;
  }
  const time = new Date(state.updated_at).toLocaleTimeString("ru", {
    hour: "2-digit",
    minute: "2-digit",
  });
  element.textContent = `Сохранено локально · ${time}`;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function hasText(value) {
  return typeof value === "string" && value.trim().length > 0;
}

function moduleHasAnswers(moduleId) {
  const answers = state.modules[moduleId].answers;
  if (moduleId === "strivings") {
    return answers.items.some((item) => hasText(item.text)) ||
      [answers.supports, answers.conflicts, answers.nextMove].some(hasText);
  }
  return Object.values(answers).some(hasText);
}

function anyAnswers() {
  return Object.keys(MODULES).some(moduleHasAnswers);
}

function statusLabel(status) {
  return {
    "not-started": "Не начато",
    "in-progress": "В процессе",
    completed: "Пройдено",
  }[status] || "Не начато";
}

function moduleButtonLabel(status) {
  return {
    "not-started": "Начать",
    "in-progress": "Продолжить",
    completed: "Пересмотреть",
  }[status] || "Начать";
}

function renderStorageWarning() {
  if (storageAvailable) return "";
  return `
    <p class="storage-warning" role="alert">
      Браузер не разрешил локальное сохранение. Ответы останутся только в этой вкладке;
      перед закрытием экспортируйте их вручную.
    </p>
  `;
}

function renderHome() {
  currentView = "home";
  activeModule = null;
  const completedCount = Object.values(state.modules).filter((item) => item.status === "completed").length;

  app.innerHTML = `
    <section class="home-hero" aria-labelledby="home-title">
      <div>
        <p class="eyebrow">Перед разговором о себе</p>
        <h1 id="home-title">Не угадать личность. Увидеть, о чём стоит спросить.</h1>
        <p class="hero-copy">
          Три коротких текстовых прохода помогают собрать текущие стремления,
          важные жизненные сцены и исключения из привычного рассказа о себе.
          Здесь нет правильных ответов, типов и итогового балла.
        </p>
      </div>
      <aside class="hero-aside">
        <strong>Можно останавливаться</strong>
        <p>
          Любой вопрос можно оставить пустым. Черновик сохраняется только в
          этом браузере; его можно выгрузить или удалить в любой момент.
        </p>
      </aside>
    </section>

    ${renderStorageWarning()}

    <section aria-labelledby="modules-title">
      <div class="section-heading">
        <h2 id="modules-title">Выберите проход</h2>
        <p>${completedCount} из ${Object.keys(MODULES).length} пройдено</p>
      </div>
      <div class="module-grid">
        ${Object.entries(MODULES).map(([moduleId, module]) => {
          const moduleState = state.modules[moduleId];
          return `
            <article class="module-card">
              <span class="module-number" aria-hidden="true">${module.number}</span>
              <h3>${module.title}</h3>
              <p>${module.description}</p>
              <div class="module-meta">
                <span>${module.time}</span>
                <span class="status" data-status="${moduleState.status}">
                  ${statusLabel(moduleState.status)}
                </span>
              </div>
              <button class="button button-secondary" type="button" data-action="open-module" data-module="${moduleId}">
                ${moduleButtonLabel(moduleState.status)}
                <span aria-hidden="true">→</span>
              </button>
            </article>
          `;
        }).join("")}
      </div>

      <div class="home-actions">
        <p>
          Итог отражает ваши формулировки и предлагает вопросы для интервью.
          Он не превращает ответы в черты личности.
        </p>
        <button class="button button-primary" type="button" data-action="summary" ${anyAnswers() ? "" : "disabled"}>
          Открыть карту
        </button>
      </div>
    </section>
  `;

  focusMainHeading();
}

function openModule(moduleId, { restart = false } = {}) {
  if (!MODULES[moduleId]) return;
  activeModule = moduleId;
  currentView = "module";
  const moduleState = state.modules[moduleId];
  if (restart) moduleState.current_step = 0;
  if (moduleState.status === "not-started") moduleState.status = "in-progress";
  persist();
  renderModule();
}

function renderModule() {
  const module = MODULES[activeModule];
  const moduleState = state.modules[activeModule];
  const stepIndex = Math.max(0, Math.min(moduleState.current_step, module.steps.length - 1));
  moduleState.current_step = stepIndex;
  const step = module.steps[stepIndex];
  const progress = Math.round(((stepIndex + 1) / module.steps.length) * 100);
  const isLast = stepIndex === module.steps.length - 1;

  app.innerHTML = `
    <section class="wizard-shell" aria-labelledby="step-title">
      <div class="wizard-topline">
        <button class="back-link" type="button" data-action="exit-module">← Все проходы</button>
        <span class="save-state" data-save-state></span>
      </div>

      ${renderStorageWarning()}

      <div class="progress-wrap" aria-label="Прогресс прохода">
        <div class="progress-labels">
          <span>${module.title}</span>
          <span>Шаг ${stepIndex + 1} из ${module.steps.length}</span>
        </div>
        <div class="progress-track">
          <div class="progress-value" style="width: ${progress}%"></div>
        </div>
      </div>

      <div class="step-card">
        <header class="step-header">
          <p class="eyebrow">${step.eyebrow}</p>
          <h1 id="step-title">${step.title}</h1>
          <p class="step-intro">${step.intro}</p>
          <span class="optional-note">Любой ответ необязателен</span>
        </header>

        ${renderStepContent(activeModule, stepIndex)}

        <div class="step-actions">
          <div class="button-row">
            <button class="button button-secondary" type="button" data-action="previous-step">
              ${stepIndex === 0 ? "Сохранить и выйти" : "Назад"}
            </button>
          </div>
          <div class="button-row">
            <span class="shortcut-hint">Ctrl / ⌘ + Enter</span>
            <button class="button button-primary" type="button" data-action="next-step">
              ${isLast ? "Собрать карту" : "Дальше"}
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      </div>
    </section>
  `;

  updateSaveState();
  focusMainHeading();
}

function textField({ moduleId, key, label, hint = "", placeholder = "", rows = 5 }) {
  const value = state.modules[moduleId].answers[key] || "";
  const fieldId = `${moduleId}-${key}`;
  return `
    <div class="field">
      <label for="${fieldId}">${label}</label>
      ${hint ? `<p class="field-hint" id="${fieldId}-hint">${hint}</p>` : ""}
      <textarea
        id="${fieldId}"
        rows="${rows}"
        data-answer
        data-module="${moduleId}"
        data-key="${key}"
        ${hint ? `aria-describedby="${fieldId}-hint"` : ""}
        placeholder="${placeholder}"
      >${escapeHtml(value)}</textarea>
    </div>
  `;
}

function renderStepContent(moduleId, stepIndex) {
  if (moduleId === "strivings") return renderStrivingsStep(stepIndex);
  if (moduleId === "lifeStory") return renderLifeStoryStep(stepIndex);
  return renderCountermapStep(stepIndex);
}

function renderStrivingsStep(stepIndex) {
  const answers = state.modules.strivings.answers;
  if (stepIndex === 0) {
    return `
      <div class="form-stack">
        <div class="field">
          <p class="field-hint">
            Пишите своими словами. Например, стремлением может быть не только
            «завершить проект», но и «не торопиться с важным решением».
          </p>
          <div class="striving-list">
            ${answers.items.map((item, index) => `
              <label class="striving-input">
                <span class="sr-only">Стремление ${index + 1}</span>
                <input
                  type="text"
                  value="${escapeHtml(item.text)}"
                  placeholder="Я стараюсь…"
                  data-answer
                  data-module="strivings"
                  data-key="items"
                  data-index="${index}"
                  data-item-key="text"
                >
              </label>
            `).join("")}
          </div>
        </div>
      </div>
    `;
  }

  if (stepIndex === 1) {
    const entered = answers.items.map((item, index) => ({ item, index })).filter(({ item }) => hasText(item.text));
    if (!entered.length) {
      return `
        <div class="boundary-note">
          На прошлом шаге не было записано стремлений. Можно вернуться и добавить
          их или продолжить без этой части.
        </div>
      `;
    }
    return `
      <div class="ratings-list">
        ${entered.map(({ item, index }) => `
          <section class="rating-card" aria-labelledby="striving-${index}-title">
            <p class="rating-title" id="striving-${index}-title">${escapeHtml(item.text)}</p>
            <div class="rating-grid">
              ${rangeField({ index, key: "importance", label: "Важность", low: "мала", high: "очень высока", value: item.importance })}
              ${rangeField({ index, key: "progress", label: "Продвижение", low: "стою", high: "двигаюсь", value: item.progress })}
              ${rangeField({ index, key: "ownership", label: "Ощущается своим", low: "скорее чужое", high: "точно моё", value: item.ownership })}
            </div>
          </section>
        `).join("")}
      </div>
    `;
  }

  return `
    <div class="form-stack">
      ${textField({
        moduleId: "strivings",
        key: "supports",
        label: "Что поддерживает другие ваши стремления?",
        hint: "Назовите одну связку: когда движение в одном направлении облегчает другое.",
        placeholder: "Когда я…, мне становится легче…",
        rows: 4,
      })}
      ${textField({
        moduleId: "strivings",
        key: "conflicts",
        label: "Что конкурирует за время, силы или верность себе?",
        hint: "Конфликт может быть практическим или внутренним.",
        placeholder: "Одновременно трудно… и…",
        rows: 4,
      })}
      ${textField({
        moduleId: "strivings",
        key: "nextMove",
        label: "Какой небольшой следующий ход кажется честным?",
        hint: "Не обещание и не план продуктивности — просто возможный шаг.",
        placeholder: "В ближайшее время я мог бы…",
        rows: 3,
      })}
    </div>
  `;
}

function rangeField({ index, key, label, low, high, value }) {
  const id = `striving-${index}-${key}`;
  return `
    <div class="range-field">
      <div class="range-topline">
        <label for="${id}">${label}</label>
        <output class="range-value" id="${id}-output" for="${id}">${value}</output>
      </div>
      <input
        id="${id}"
        type="range"
        min="1"
        max="5"
        step="1"
        value="${value}"
        data-answer
        data-module="strivings"
        data-key="items"
        data-index="${index}"
        data-item-key="${key}"
        data-output="${id}-output"
      >
      <div class="range-ends" aria-hidden="true"><span>${low}</span><span>${high}</span></div>
    </div>
  `;
}

function renderLifeStoryStep(stepIndex) {
  if (stepIndex === 0) {
    return `
      <div class="form-stack">
        ${textField({
          moduleId: "lifeStory",
          key: "chapters",
          label: "Названия глав",
          hint: "Одна глава на строку. Обычно достаточно 3–7 названий.",
          placeholder: "Дом, который меня сформировал\nПервые собственные решения\nПериод пересборки…",
          rows: 8,
        })}
      </div>
    `;
  }
  if (stepIndex === 1) {
    return `
      <div class="form-stack">
        ${textField({
          moduleId: "lifeStory",
          key: "highPoint",
          label: "Что произошло в этой сцене?",
          hint: "Лучше один момент, чем перечень достижений.",
          placeholder: "Я был… Произошло… Я заметил…",
          rows: 6,
        })}
        ${textField({
          moduleId: "lifeStory",
          key: "highPointMeaning",
          label: "Что эта сцена говорит вам сегодня?",
          hint: "Можно описать смысл, который изменился со временем.",
          placeholder: "Тогда я думал…, а сейчас вижу…",
          rows: 4,
        })}
      </div>
    `;
  }
  if (stepIndex === 2) {
    return `
      <div class="form-stack">
        ${textField({
          moduleId: "lifeStory",
          key: "difficultScene",
          label: "Трудная точка",
          hint: "Не нужно раскрывать больше, чем безопасно. Достаточно контура события и его значения.",
          placeholder: "Ситуация была… Для меня труднее всего оказалось…",
          rows: 5,
        })}
        ${textField({
          moduleId: "lifeStory",
          key: "turningPoint",
          label: "Поворот",
          hint: "Что после этого стало возможным, невозможным или иначе видимым?",
          placeholder: "После этого я начал / перестал / понял…",
          rows: 5,
        })}
      </div>
    `;
  }
  return `
    <div class="form-stack">
      ${textField({
        moduleId: "lifeStory",
        key: "continuity",
        label: "Какая нить проходит через разные главы?",
        hint: "Это может быть ценность, вопрос, способ действовать или повторяющееся напряжение.",
        placeholder: "Снова и снова я возвращаюсь к…",
        rows: 5,
      })}
      ${textField({
        moduleId: "lifeStory",
        key: "futureChapter",
        label: "Как могла бы называться следующая глава?",
        hint: "Не предсказание — название желаемого или вероятного направления.",
        placeholder: "Следующая глава: …",
        rows: 4,
      })}
    </div>
  `;
}

function renderCountermapStep(stepIndex) {
  if (stepIndex === 0) {
    return `
      <div class="form-stack">
        ${textField({
          moduleId: "countermap",
          key: "easyClaim",
          label: "Фраза для проверки",
          hint: "Например: «Я лучше работаю один», «Мне трудно менять решения», «Я всегда ищу сложность».",
          placeholder: "Мне кажется, что я…",
          rows: 4,
        })}
      </div>
    `;
  }
  if (stepIndex === 1) {
    return `
      <div class="form-stack">
        ${textField({
          moduleId: "countermap",
          key: "holds",
          label: "Где это действительно похоже на правду?",
          hint: "Опишите конкретную ситуацию, а не ещё одно обобщение.",
          placeholder: "Это было заметно, когда…",
          rows: 5,
        })}
        ${textField({
          moduleId: "countermap",
          key: "breaks",
          label: "Когда это не сработало или оказалось наоборот?",
          hint: "Даже небольшой контрпример полезен.",
          placeholder: "Но в другой ситуации я…",
          rows: 5,
        })}
      </div>
    `;
  }
  if (stepIndex === 2) {
    return `
      <div class="form-stack">
        ${textField({
          moduleId: "countermap",
          key: "outsideView",
          label: "Что мог бы заметить человек, который знает вас в другом контексте?",
          hint: "Не нужно угадывать его оценку; попробуйте представить другой набор наблюдений.",
          placeholder: "Возможно, он бы сказал, что…",
          rows: 5,
        })}
        ${textField({
          moduleId: "countermap",
          key: "alternative",
          label: "Какое альтернативное объяснение подходит тем же эпизодам?",
          hint: "Например, дело может быть не в постоянной черте, а в роли, среде, цене ошибки или усталости.",
          placeholder: "Возможно, это происходило потому, что…",
          rows: 5,
        })}
      </div>
    `;
  }
  return `
    <div class="form-stack">
      ${textField({
        moduleId: "countermap",
        key: "revisedClaim",
        label: "Более точная и ограниченная версия",
        hint: "Полезная формулировка часто содержит «когда», «в некоторых ситуациях» или «пока».",
        placeholder: "В ситуациях…, я чаще…, но…",
        rows: 5,
      })}
      ${textField({
        moduleId: "countermap",
        key: "openQuestion",
        label: "Что всё ещё хочется проверить в разговоре?",
        hint: "Оставьте один открытый вопрос вместо поспешного вывода.",
        placeholder: "Мне важно понять…",
        rows: 4,
      })}
    </div>
  `;
}

function nextStep() {
  const module = MODULES[activeModule];
  const moduleState = state.modules[activeModule];
  if (moduleState.current_step < module.steps.length - 1) {
    moduleState.current_step += 1;
    persist();
    renderModule();
    announce(`Шаг ${moduleState.current_step + 1} из ${module.steps.length}`);
    return;
  }

  moduleState.status = "completed";
  persist();
  showToast(`«${module.title}» — проход завершён`);
  renderSummary();
}

function previousStep() {
  const moduleState = state.modules[activeModule];
  if (moduleState.current_step === 0) {
    persist({ announce: true });
    renderHome();
    return;
  }
  moduleState.current_step -= 1;
  persist();
  renderModule();
}

function updateAnswer(target) {
  const moduleId = target.dataset.module;
  const key = target.dataset.key;
  if (!moduleId || !key || !state.modules[moduleId]) return;

  let value = target.value;
  if (target.type === "range") value = Number(value);

  if (target.dataset.index !== undefined) {
    const index = Number(target.dataset.index);
    const itemKey = target.dataset.itemKey;
    state.modules[moduleId].answers[key][index][itemKey] = value;
  } else {
    state.modules[moduleId].answers[key] = value;
  }

  if (state.modules[moduleId].status === "not-started") {
    state.modules[moduleId].status = "in-progress";
  }
  if (target.dataset.output) {
    const output = document.getElementById(target.dataset.output);
    if (output) output.value = value;
  }
  persist();
}

function renderSummary() {
  currentView = "summary";
  activeModule = null;
  const questions = buildInterviewQuestions();
  const completedCount = Object.values(state.modules).filter((item) => item.status === "completed").length;

  app.innerHTML = `
    <section class="summary-shell" aria-labelledby="summary-title">
      <button class="back-link" type="button" data-action="home">← Все проходы</button>

      <div class="summary-hero">
        <div>
          <p class="eyebrow">Рабочая карта · ${completedCount} из 3 проходов</p>
          <h1 id="summary-title">Материал для разговора</h1>
          <p class="section-copy">
            Ниже собраны ваши собственные формулировки и вопросы, которые из
            них возникают. Это черновик ориентации, не психологическое заключение.
          </p>
        </div>
      </div>

      ${renderStorageWarning()}

      <p class="boundary-note">
        Карта ничего не утверждает о вас автоматически. Любую тему нужно
        проверить конкретными эпизодами, исключениями и вашим явным согласием
        прежде, чем она сможет стать кандидатом в портрет.
      </p>

      <div class="summary-grid">
        ${renderStrivingsSummary()}
        ${renderLifeStorySummary()}
        ${renderCountermapSummary()}
        <section class="summary-card" aria-labelledby="questions-title">
          <div class="summary-card-header">
            <div>
              <p class="eyebrow">Следующий разговор</p>
              <h2 id="questions-title">Вопросы, а не выводы</h2>
            </div>
          </div>
          ${questions.length ? `
            <ol class="question-list">
              ${questions.map((question) => `<li class="question-item">${escapeHtml(question)}</li>`).join("")}
            </ol>
          ` : `
            <p class="empty-state">Заполните хотя бы один проход — здесь появятся вопросы для интервью.</p>
          `}
        </section>
      </div>

      <div class="summary-actions">
        <button class="button button-primary" type="button" data-action="export">Скачать JSON</button>
        <button class="button button-secondary" type="button" data-action="print">Печать / PDF</button>
        <button class="button button-danger" type="button" data-action="reset">Удалить черновик</button>
      </div>
    </section>
  `;

  focusMainHeading();
}

function renderStrivingsSummary() {
  const answers = state.modules.strivings.answers;
  const items = answers.items.filter((item) => hasText(item.text));
  return `
    <section class="summary-card" aria-labelledby="strivings-summary-title">
      <div class="summary-card-header">
        <div>
          <p class="eyebrow">Стремления</p>
          <h2 id="strivings-summary-title">Что сейчас тянет вперёд</h2>
        </div>
        <button class="text-button" type="button" data-action="edit-module" data-module="strivings">Изменить</button>
      </div>
      ${items.length ? `
        <ul class="summary-list">
          ${items.map((item) => `
            <li class="summary-item">
              <strong>${escapeHtml(item.text)}</strong>
              <span>Важность ${item.importance}/5 · продвижение ${item.progress}/5 · ощущается своим ${item.ownership}/5</span>
            </li>
          `).join("")}
        </ul>
      ` : `<p class="empty-state">Стремления пока не записаны.</p>`}
      ${summaryText("Что поддерживает", answers.supports)}
      ${summaryText("Что конфликтует", answers.conflicts)}
      ${summaryText("Возможный следующий ход", answers.nextMove)}
    </section>
  `;
}

function renderLifeStorySummary() {
  const answers = state.modules.lifeStory.answers;
  const blocks = [
    ["Главы", answers.chapters],
    ["Высокая точка", answers.highPoint],
    ["Её нынешний смысл", answers.highPointMeaning],
    ["Трудная точка", answers.difficultScene],
    ["Поворот", answers.turningPoint],
    ["Сквозная нить", answers.continuity],
    ["Следующая глава", answers.futureChapter],
  ].filter(([, value]) => hasText(value));

  return `
    <section class="summary-card" aria-labelledby="life-summary-title">
      <div class="summary-card-header">
        <div>
          <p class="eyebrow">Жизненные сцены</p>
          <h2 id="life-summary-title">Эпизоды и продолжение</h2>
        </div>
        <button class="text-button" type="button" data-action="edit-module" data-module="lifeStory">Изменить</button>
      </div>
      ${blocks.length ? `
        <ul class="summary-list">
          ${blocks.map(([label, value]) => `
            <li class="summary-item">
              <strong>${label}</strong>
              <span class="raw-answer">${escapeHtml(value)}</span>
            </li>
          `).join("")}
        </ul>
      ` : `<p class="empty-state">Жизненные сцены пока не записаны.</p>`}
    </section>
  `;
}

function renderCountermapSummary() {
  const answers = state.modules.countermap.answers;
  const blocks = [
    ["Исходная фраза", answers.easyClaim],
    ["Где работает", answers.holds],
    ["Где ломается", answers.breaks],
    ["Взгляд из другого контекста", answers.outsideView],
    ["Другое объяснение", answers.alternative],
    ["Уточнённая версия", answers.revisedClaim],
    ["Открытый вопрос", answers.openQuestion],
  ].filter(([, value]) => hasText(value));

  return `
    <section class="summary-card" aria-labelledby="counter-summary-title">
      <div class="summary-card-header">
        <div>
          <p class="eyebrow">Контркарта</p>
          <h2 id="counter-summary-title">Границы удобной версии</h2>
        </div>
        <button class="text-button" type="button" data-action="edit-module" data-module="countermap">Изменить</button>
      </div>
      ${blocks.length ? `
        <ul class="summary-list">
          ${blocks.map(([label, value]) => `
            <li class="summary-item">
              <strong>${label}</strong>
              <span class="raw-answer">${escapeHtml(value)}</span>
            </li>
          `).join("")}
        </ul>
      ` : `<p class="empty-state">Контркарта пока не заполнена.</p>`}
    </section>
  `;
}

function summaryText(label, value) {
  if (!hasText(value)) return "";
  return `
    <div class="summary-item" style="margin-top: 12px">
      <strong>${label}</strong>
      <span class="raw-answer">${escapeHtml(value)}</span>
    </div>
  `;
}

function buildInterviewQuestions() {
  const questions = [];
  const strivings = state.modules.strivings.answers;
  const entered = strivings.items.filter((item) => hasText(item.text));
  const priority = [...entered].sort((a, b) => b.importance - a.importance)[0];
  const tension = entered.find((item) => item.importance - item.progress >= 2);
  const borrowed = entered.find((item) => item.ownership <= 2);

  if (priority) {
    questions.push(`Какие конкретные эпизоды показывают, почему стремление «${priority.text}» важно именно сейчас?`);
  }
  if (tension) {
    questions.push(`Что удерживает стремление «${tension.text}» при высокой важности и невысоком ощущении продвижения?`);
  }
  if (borrowed) {
    questions.push(`Какая часть стремления «${borrowed.text}» действительно ваша, а какая могла прийти из чужих ожиданий?`);
  }
  if (hasText(strivings.conflicts)) {
    questions.push("В каком недавнем эпизоде конфликт стремлений стал виден как реальный выбор?");
  }

  const story = state.modules.lifeStory.answers;
  if (hasText(story.highPoint)) {
    questions.push("Какие условия высокой точки можно восстановить, а какие принадлежали только тому времени?");
  }
  if (hasText(story.turningPoint)) {
    questions.push("Что в поворотной сцене было вашим выбором, а что — давлением обстоятельств?");
  }
  if (hasText(story.continuity) && hasText(story.futureChapter)) {
    questions.push("Как сквозная нить прошлого поддерживает следующую главу — и где может ей мешать?");
  }

  const counter = state.modules.countermap.answers;
  if (hasText(counter.easyClaim) && hasText(counter.breaks)) {
    questions.push(`При каких условиях фраза «${counter.easyClaim}» перестаёт работать и что это меняет в её смысле?`);
  }
  if (hasText(counter.openQuestion)) {
    questions.push(counter.openQuestion.trim().replace(/[?.!]*$/, "?") );
  }

  return questions.slice(0, 8);
}

function exportWorkbook() {
  const exportData = {
    schema_version: state.schema_version,
    artifact_type: state.artifact_type,
    workbook_id: state.workbook_id,
    created_at: state.created_at,
    updated_at: new Date().toISOString(),
    locale: state.locale,
    interpretation_boundary: "Private pre-interview material. Responses and derived questions are not diagnoses, scores, types, or portrait claims.",
    method_refs: [
      {
        id: "personal-strivings",
        role: "dionysus-authored non-normative goal elicitation",
      },
      {
        id: "life-story-interview-ii",
        role: "adapted narrative interview design source without standardized coding claims",
      },
      {
        id: "counterportrait-v0",
        role: "Dionysus interview protocol for exceptions and alternative explanations",
      },
    ],
    completion: Object.fromEntries(
      Object.entries(state.modules).map(([id, moduleState]) => [id, moduleState.status]),
    ),
    answers: Object.fromEntries(
      Object.entries(state.modules).map(([id, moduleState]) => [id, moduleState.answers]),
    ),
    interview_questions: buildInterviewQuestions(),
  };

  const blob = new Blob([`${JSON.stringify(exportData, null, 2)}\n`], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  const date = new Date().toISOString().slice(0, 10);
  anchor.href = url;
  anchor.download = `dionysus-reflection-${date}.json`;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
  showToast("JSON скачан. Он содержит личный материал — храните его осознанно.");
}

function resetWorkbook() {
  const confirmed = window.confirm(
    "Удалить весь локальный черновик Dionysus на этом устройстве? Уже скачанные файлы останутся на диске.",
  );
  if (!confirmed) return;
  if (storageAvailable) window.localStorage.removeItem(STORAGE_KEY);
  state = createInitialState();
  showToast("Локальный черновик удалён");
  renderHome();
}

function showPrivacy() {
  if (typeof privacyDialog.showModal === "function") {
    privacyDialog.showModal();
  } else {
    privacyDialog.setAttribute("open", "");
  }
}

function closePrivacy() {
  if (typeof privacyDialog.close === "function") {
    privacyDialog.close();
  } else {
    privacyDialog.removeAttribute("open");
  }
}

function showToast(message) {
  window.clearTimeout(toastTimer);
  toast.textContent = message;
  toast.classList.add("is-visible");
  toastTimer = window.setTimeout(() => toast.classList.remove("is-visible"), 3600);
}

function announce(message) {
  liveRegion.textContent = "";
  window.setTimeout(() => {
    liveRegion.textContent = message;
  }, 20);
}

function focusMainHeading() {
  window.scrollTo({ top: 0, behavior: "auto" });
  const heading = app.querySelector("h1");
  if (!heading) return;
  heading.setAttribute("tabindex", "-1");
  heading.focus({ preventScroll: true });
}

document.addEventListener("input", (event) => {
  const target = event.target.closest("[data-answer]");
  if (target) updateAnswer(target);
});

document.addEventListener("click", (event) => {
  const trigger = event.target.closest("[data-action]");
  if (!trigger) return;
  const action = trigger.dataset.action;

  if (action === "home") renderHome();
  if (action === "privacy") showPrivacy();
  if (action === "close-privacy") closePrivacy();
  if (action === "open-module") openModule(trigger.dataset.module);
  if (action === "edit-module") openModule(trigger.dataset.module, { restart: true });
  if (action === "exit-module") {
    persist({ announce: true });
    renderHome();
  }
  if (action === "previous-step") previousStep();
  if (action === "next-step") nextStep();
  if (action === "summary") renderSummary();
  if (action === "export") exportWorkbook();
  if (action === "print") window.print();
  if (action === "reset") resetWorkbook();
});

document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter" && currentView === "module") {
    event.preventDefault();
    nextStep();
  }
  if (event.key === "Escape" && privacyDialog.open) closePrivacy();
});

privacyDialog.addEventListener("click", (event) => {
  if (event.target === privacyDialog) closePrivacy();
});

renderHome();
