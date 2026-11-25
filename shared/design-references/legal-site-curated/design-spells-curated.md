# Design Spells → юридический корпоративный сайт (курируемая подборка)

Дата отбора: **2026-11-19**. Источник: [Design Spells](https://designspells.com/).  
Ограничение проверки: агент **не просматривал MP4** на spell-страницах; ниже — заголовок, продукт, теги, meta/JSON-LD и миниатюра (где доступна). Поведение описано только в той мере, в какой оно следует из **названия spell** и **краткого description** сайта; детали тайминга и easing — гипотеза для реализации, не утверждение о ролике.

Тон адаптации: сдержанный B2B, без «fun»/easter egg; юридический доверительный стиль.

---

## DS-L01 — Индикатор длительной операции (поиск / отправка)

| | |
|--|--|
| Spell | #179 |
| Продукт | Perplexity |
| Ссылка | https://designspells.com/spells/loading-animations-when-performing-a-pro-search-on-perplexity |
| Теги | Desktop, Animation |
| Описание (meta) | Desktop animation in Perplexity during Pro Search |

**Наблюдаемое поведение (из названия + meta):** во время «тяжёлого» поиска показываются **анимированные состояния загрузки**, а не статичный спиннер.

**Применение на сайте:** после отправки заявки, проверки статуса дела, загрузки результата калькулятора или длительного поиска по базе знаний — **пошаговая или пульсирующая** обратная связь «идёт обработка».

**Критерии приёмки:** на мобильном — читаемый статус без блокировки скролла; `prefers-reduced-motion` → статичный текст/прогресс; только `transform`/`opacity`; основное действие доступно без hover.

**Ограничение просмотра:** MP4 не воспроизведён; кадр: `cdn.designspells.com/first-frames/perplexity-first-frame.jpg`.

---

## DS-L02 — Прогресс многошагового сценария

| | |
|--|--|
| Spell | #173 |
| Продукт | Linear |
| Ссылка | https://designspells.com/spells/animated-progress-indicator-when-using-linears-import-assistant |
| Теги | Desktop, Interaction, Animation, Unique, Beautiful |
| Описание (meta) | Unique, beautiful desktop animation in Linear's import assistant |

**Наблюдаемое поведение:** при прохождении **import assistant** отображается **анимированный индикатор прогресса** (не только процент).

**Применение:** форма «Оставить заявку» / «Регистрация ТЗ» из 3–5 шагов; визуальная связь между шагами при импорте документов.

**Критерии приёмки:** фокус с клавиатуры сохраняется между шагами; видимый focus ring; reduced motion → дискретная смена шага без декоративной анимации.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L03 — Микро-анимация пунктов выпадающего меню

| | |
|--|--|
| Spell | #196 |
| Продукт | Supabase |
| Ссылка | https://designspells.com/spells/icon-micro-animations-when-hovering-on-dropdown-menu-items-in-supabase |
| Теги | Desktop, Interaction, Animation |
| Описание (meta) | Desktop animation on dropdown menu items on hover |

**Наблюдаемое поведение:** иконки пунктов **реагируют анимацией при наведении** в dropdown.

**Применение:** меню «Услуги», «О компании», языковой/региональный переключатель в шапке сайта.

**Критерии приёмки:** на touch — та же обратная связь по `:focus-visible` / `aria-expanded`, не только `:hover`; CTA не прячется за hover-only.

**Ограничение просмотра:** MP4 не воспроизведён; spell завязан на hover — **обязательна** touch/keyboard-паритетная реализация.

---

## DS-L04 — Переключение режима панели инструментов

| | |
|--|--|
| Spell | #125 |
| Продукт | Figma |
| Ссылка | https://designspells.com/spells/toolbar-animation-when-toggling-between-design-and-dev-mode-in-figma |
| Теги | Desktop, Interaction, Animation |
| Описание (meta) | Desktop animation when toggling design/dev mode |

**Наблюдаемое поведение:** при переключении **design ↔ dev mode** **анимируется toolbar** (смена контекста).

**Применение:** переключатель «Физ. лицо / Юр. лицо», «Заявка онлайн / Звонок», табы на странице услуги.

**Критерии приёмки:** `role="tablist"` / кнопки с `aria-selected`; анимация индикатора через `transform`; reduced motion.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L05 — Выбор варианта в форме (сегментированный контроль)

| | |
|--|--|
| Spell | #333 |
| Продукт | ChatGPT |
| Ссылка | https://designspells.com/spells/effort-selection-animations-in-chatgpt |
| Теги | Desktop, Interaction, Animation |
| Описание (meta) | Desktop animation for effort selection |

**Наблюдаемое поведение:** при выборе уровня **effort** — **анимация выбора** (не мгновенная смена состояния).

**Применение:** выбор типа услуги (регистрация ТЗ, споры, договоры), срочности обращения, канала связи.

**Критерии приёмки:** выбранное значение доступно с клавиатуры; размер touch-target ≥ 44px; без layout thrash.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L06 — Плавный sheet при мобильной навигации

| | |
|--|--|
| Spell | #338 |
| Продукт | Sudoku a Day |
| Ссылка | https://designspells.com/spells/smooth-sheet-transitions-in-sudoku-a-day |
| Теги | Mobile, Transition |
| Описание (meta) | Mobile transition |

**Наблюдаемое поведение (из названия):** **плавные переходы** при открытии/закрытии **sheet**-панелей.

**Применение:** мобильное меню, короткая форма «Заказать консультацию», фильтры практик.

**Критерии приёмки:** фокус в sheet при открытии; закрытие Esc; `transform` для slide; reduced motion → мгновенное появление с сохранением `opacity` fade ≤ 150ms или без анимации.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L07 — «Жидкие» sheet-взаимодействия

| | |
|--|--|
| Spell | #267 |
| Продукт | Are.na |
| Ссылка | https://designspells.com/spells/fluid-sheet-interactions-in-are-na |
| Теги | Mobile, Interaction, Transition |
| Описание (meta) | Mobile transition |

**Наблюдаемое поведение (из названия):** **fluid** (связанные с жестом) взаимодействия с **sheet**.

**Применение:** выдвижная панель с деталями услуги или юриста; подтверждение отправки заявки.

**Критерии приёмки:** основной CTA остаётся на странице без жеста; drag-to-close опционален; keyboard dismiss.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L08 — Переходы bookmark sheet (оверлей)

| | |
|--|--|
| Spell | #344 |
| Продукт | X (Twitter) |
| Ссылка | https://designspells.com/spells/bookmark-sheet-transitions-in-x |
| Теги | Mobile, Transition |
| Описание (meta) | Mobile transition |

**Наблюдаемое поведение (из названия):** **анимированные переходы** при работе с **bookmark sheet**.

**Применение:** модальное «Спасибо, заявка принята» с следующими шагами; сохранение статьи блога / кейса.

**Критерии приёмки:** ловушка фокуса; `aria-modal`; reduced motion; нет обязательного swipe-only.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L09 — Карусель карточек (команда / направления)

| | |
|--|--|
| Spell | #342 |
| Продукт | Spotify (SongDNA) |
| Ссылка | https://designspells.com/spells/contributors-carousel-in-spotify-songdna |
| Теги | Mobile, Motion, Unique |
| Описание (meta) | Unique mobile design detail — contributors carousel |

**Наблюдаемое поведение (из названия):** **карусель contributors** с motion-переходами.

**Применение:** блок «Направления практики» или «Команда» на сайте; горизонтальный скролл с snap.

**Критерии приёмки:** кнопки prev/next и клавиатура; `scroll-snap`; без автоплея, мешающего чтению; reduced motion — без parallax.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## DS-L10 — Плавные переходы между карточками услуг

| | |
|--|--|
| Spell | #346 |
| Продукт | Doji |
| Ссылка | https://designspells.com/spells/smooth-transitions-when-browsing-looks-on-doji |
| Теги | Mobile, Motion, Transition |
| Описание (meta) | Mobile transition when browsing looks |

**Наблюдаемое поведение (из названия):** **smooth transitions** при **листании/переключении карточек** «looks».

**Применение:** галерея кейсов, переключение тарифов/пакетов услуг на мобильном.

**Критерии приёмки:** контент не прыгает по layout; cross-fade/slide через compositor; Lighthouse без просадки CLS.

**Ограничение просмотра:** MP4 не воспроизведён.

---

## Журнал ссылок (HTTP)

Все URL выше проверены **2026-11-19** (HTTP 200 через веб-fetch).