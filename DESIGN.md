# DESIGN.md — сайт «Лирейт» (черновик)

**Статус:** черновик от **2026-11-19**. Любой блок с пометкой **«требует утверждения владельцем»** не считается продакшен-каноном, пока Юрий Горбачев / владелец не зафиксирует выбор.

**Приоритет:** утверждённая айдентика «Лирейт» и текущий продакшен-сайт (`PUBLIC_SITE_URL`) важнее карточек Refero.

## Контекст продукта

- Юридическая компания / патентное бюро: регистрация и защита товарных знаков, патентов, договоров ИС, программ ЭВМ.
- Аудитория: предприниматели и малый/средний бизнес РФ.
- Tone of voice (наблюдаемо на сайте): экспертиза, честные сроки, «оплата за результат», без агрессивных продаж.

## Наблюдаемое состояние UI (публичный сайт, 2026-11-19)

**Источник:** главная и метаданные (не полный CSS-аудит).

| Наблюдение | Применение |
|------------|------------|
| Блоки услуг: ТЗ, договоры, патенты, ПО | Карточки с «Подробнее» и заявкой |
| Доверие: год основания, число специалистов, SLA ответа | Trust strip в hero |
| Формы: «Обратный звонок», «Оставить заявку», Telegram | CTA + мессенджер |
| Команда: сетка фото + должности | Социальное доказательство |
| Блог /news/ | Отдельный контентный кластер |

**Требует утверждения:** точные HEX, шрифты и радиусы **текущей** темы (код сайта вне этого репозитория) — зафиксировать после согласования с владельцем.

## Отдельно: блог EXCALIBUR в этом репо

Палитра обложек блога (**не** смешивать с корпоративным лендингом без решения владельца):

- `memory/brief/site-brief.md`: `#0B1220`, `#1E3A5F`, `#3B82F6`
- Визуальный язык: `memory/cover/cover-design-code.json` (zine/collage для статей)

## Референсы Refero Styles (согласованные направления)

Полные карточки: [`shared/design-references/legal-site-curated/refero-styles-curated.md`](shared/design-references/legal-site-curated/refero-styles-curated.md).

| ID | Стиль | Что заимствуем (концептуально) |
|----|-------|-------------------------------|
| RS-01 | [Seline](https://styles.refero.design/style/7967c6d9-e50c-42b5-b4d1-74003ba41781) | Тёплый фон, один спокойный акцент, карточки с border |
| RS-02 | [Increase](https://styles.refero.design/style/1ad4f49f-275a-4268-8ed1-677dc3c6e475) | Институциональный navy, «документный» тон |
| RS-03 | [Column](https://styles.refero.design/style/a76ec6ba-20b3-495c-9d89-1e58281e79e7) | Navy ledger, доверие финтеха |
| RS-04 | [Vercel](https://styles.refero.design/style/f24daf3a-d43f-4dec-85a9-8ac1d5148a03) | Сетка long-read / блог |
| RS-05 | [Ramp](https://styles.refero.design/style/b38702a0-75ab-474c-9106-00b624535825) | Иерархия CTA и карточек услуг (акцент ослабить) |

## Референсы hero (Supahero)

Композиция первого экрана: [`shared/design-references/legal-site-curated/supahero-curated.md`](shared/design-references/legal-site-curated/supahero-curated.md). Правило: [`rules/design-hero-first-screen.mdc`](rules/design-hero-first-screen.mdc).

| ID | Пример | Задача посетителя (концепт) |
|----|--------|----------------------------|
| SH-01 | [Canopy](https://supahero.io/hero/canopy) | Доверие к B2B-сервису, доказательства + логотипы |
| SH-02 | [Phamily](https://supahero.io/hero/phamily) | Экспертное сопровождение, два входа в воронку |
| SH-03 | [Cobalt](https://supahero.io/hero/cobalt) | Явный оффер для владельца МСБ (+ mockup этапов) |
| SH-04 | [Better Stack](https://supahero.io/hero/better-stack) | Быстрый контакт, форма/CTA + social proof |
| SH-05 | [ai.work](https://supahero.io/hero/ai-work) | Перечень услуг ИС в подзаголовке, спокойная асимметрия |

Скриншоты Supahero — **не** продакшен-ассеты; LCP-графика hero — только своя или лицензированная.

## Референсы motion (Design Spells)

См. [`shared/design-references/legal-site-curated/design-spells-curated.md`](shared/design-references/legal-site-curated/design-spells-curated.md) и `design_ref: DS-Lxx` в PR.

## Предлагаемые design tokens (**требует утверждения владельцем**)

Синтез **RS-01 + наблюдаемого спокойного B2B**, не копия Wise/Ramp.

### Цвет (предлагается для проекта)

| Token | HEX | Роль |
|-------|-----|------|
| `--color-canvas` | `#fafaf9` | фон страницы (из RS-01) |
| `--color-surface` | `#ffffff` | карточки |
| `--color-ink` | `#0c0a09` | заголовки |
| `--color-body` | `#44403c` | основной текст (stone-700) |
| `--color-muted` | `#78716c` | вторичный текст |
| `--color-border` | `#e7e5e4` | hairline |
| `--color-accent` | `#1e4a7a` | **предлагается:** спокойный синий вместо яркого cyan/lime (юр. контекст) |
| `--color-accent-hover` | `#163a61` | hover CTA |

**Требует утверждения:** финальные accent и соответствие фирменному стилю «Лирейт».

### Типографика (предлагается для проекта)

| Роль | Шрифт | Лицензия / кириллица (проверено 2026-11-19) |
|------|-------|---------------------------------------------|
| UI + body | **Inter** | SIL Open Font License 1.1; кириллица в Google Fonts |
| Заголовки (опция) | **PT Root UI** или **Golos Text** | OFL; кириллица — **требует утверждения** выбора |
| Mono (коды, реквизиты) | **JetBrains Mono** | OFL; кириллица |

Не использовать в продакшене: Roobert, SuisseIntl, lausanne, Wise Sans, Untitled Sans (из Refero) без отдельной лицензии.

### Сетка и отступы (из RS-01, предлагается для проекта)

| Параметр | Значение |
|----------|----------|
| Max width | 1200px |
| Base unit | 4px |
| Section gap | 64–96px |
| Card padding | 24px |
| Gutter (mobile) | 16px |

### Формы и CTA (предлагается)

- Primary button: filled `--color-accent`, белый текст, min-height **44px**, radius **8px** (не обязательные pill 9999px — **требует утверждения**).
- Secondary: outline `--color-border`, текст `--color-ink`.
- Focus: видимый `outline` 2px, offset 2px; не только `:hover`.
- Состояния: default / hover / focus-visible / disabled / loading (см. Design Spells DS-L01, DS-L06).

### Компоненты (приоритет для сайта)

1. Шапка + телефоны + «Обратный звонок»
2. Hero с trust metrics
3. Карточки 4 услуг ИС
4. Форма заявки + статус отправки
5. Сетка команды
6. Блок блога / кейсов

## Jiro MCP

- Конфиг: [`.cursor/mcp.json`](.cursor/mcp.json) → `https://mcp.jiro.build`.
- **OAuth обязателен**; tools в этой среде не проверялись.
- Любой импорт блока Jiro должен быть **перекрашен** под tokens выше и не подменять утверждённый layout без ревью.

## Экосистема инструкций

- Карта источников: [`shared/design-references/ecosystem.md`](shared/design-references/ecosystem.md)
- Hero: `rules/design-hero-first-screen.mdc`
- Новые страницы: `rules/design-pages-visual-system.mdc`
- Motion: `rules/design-micro-interactions.mdc`

## Решения, ожидающие владельца

| # | Тема | Варианты / вопрос |
|---|------|-------------------|
| 1 | Accent color | Текущий бренд vs предложенный `#1e4a7a` vs Refero cyan |
| 2 | Display-шрифт | Inter only vs PT Root UI / Golos Text для заголовков |
| 3 | Радиусы | 8px корпоратив vs pill-кнопки RS-01 |
| 4 | Тёмные секции | Нужны ли navy-блоки (RS-03) на главной |
| 5 | Ramp yellow | Допустим ли яркий акцент или только приглушённые CTA |
| 6 | Синхронизация с кодом темы | Где живёт канон CSS (WP-тема вне репо) и процесс обновления tokens |