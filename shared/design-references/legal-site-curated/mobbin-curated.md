# Mobbin → сценарии сайта «Лирейт» (5 опорных экрана)

Дата: **2026-11-19**. Источник: [Mobbin](https://mobbin.com/).

## Сценарии продукта (проверка)

**Источники:** [`DESIGN.md`](../../../DESIGN.md), наблюдения публичного `PUBLIC_SITE_URL` (частичный HTML-fetch 2026-11-19: подтверждён блок **Telegram**; полный список услуг — вне этого fetch).

| ID сценария | Задача посетителя | На сайте (ожидаемо) | E-commerce |
|-------------|-------------------|---------------------|------------|
| S1 | Оставить **заявку / консультацию** | Формы «Обратный звонок», «Оставить заявку» | **Нет** корзины в репозитории |
| S2 | **Выбрать услугу** ИС (ТЗ, патенты, договоры, ПО) | Карточки услуг + «Подробнее» | Нет |
| S3 | Понять **стоимость / пакет** | «Оплата за результат», ориентиры цен на услугах | Нет checkout |
| S4 | Прочитать **блог /news/** | Контентный кластер EXCALIBUR + новости на корп. сайте | Нет |
| S5 | **Связаться** (телефон, мессенджер) | Telegram, телефоны в шапке | N/A |

**Не придумываем:** поиск по реестру ТЗ, полноценный «кабинет клиента», корзина — в репо **нет**; для будущих фич — раздел «MCP поиск» ниже.

**Ограничение Mobbin:** без аккаунта виден **один кадр** screen + теги flows; **последовательность шагов flow** для примеров ниже взята из **meta description** и тегов Mobbin, **не** из просмотра полного flow (**не проверено** пошагово).

---

## MB-01 — Legal Website Design (категория)

| | |
|--|--|
| Mobbin | https://mobbin.com/explore/sites/categories/legal-website-design (**200**) |
| Продукт | Агрегатор **юридических** маркетинговых сайтов (не одно приложение) |
| Платформа | Web (site category) |
| Сценарий **S2** | «Понять, что фирма занимается моей задачей» |

**Шаги (типовой legal marketing site — обобщение категории, не один flow ID):** лендинг → блок практик/услуг → trust → контакт. **Не проверено** на конкретном сайте из каталога без входа.

**Состояния:** default лендинг; CTA hover — **не проверено**.

**Приём для «Лирейт»:** сравнение с **юр. нише**, не копия макета; сочетать с RS-02 и SH-01.

**Доступ:** категория публична; **галерея внутри** может требовать signup.

---

## MB-02 — Docusign Web Account Setup

| | |
|--|--|
| Mobbin | https://mobbin.com/explore/screens/c0248abe-0324-4739-83e6-cbc310da9912 (**200**) |
| Продукт | [Docusign](https://www.docusign.com/) |
| Платформа | **Web** |
| Сценарий **S2** | Выбор типа аккаунта / сценария (аналог «какая услуга ИС вам нужна») |

**Описание Mobbin (из meta):** Account Setup, UI **Tile**, flows: [Starting & Completing](https://mobbin.com/explore/web/flows/starting-completing), Account Setup, Select.

**Шаги (интерпретация, не проверен flow):** вход в setup → **выбор плитками** варианта → следующий шаг. Состояния: default tiles; selected tile — **не проверено** на скрине.

**Приём:** **tile/grid выбора услуги** (ТЗ / патент / договор) вместо длинного выпадающего списка; спокойный B2B тон.

**Доступ:** превью screen публично; Save/Copy → `/signup/modal`.

---

## MB-03 — PandaDoc Web Welcome form

| | |
|--|--|
| Mobbin | https://mobbin.com/explore/screens/03ff48b7-f0e9-47e0-aa74-dc3f1b8c115e (**200**) |
| Продукт | [PandaDoc](https://www.pandadoc.com/) |
| Платформа | **Web** |
| Сценарий **S1** | Сбор контактов и контекста **до** консультации |

**Описание Mobbin:** «Welcome form with fields for additional user information»; flows: Creating Account, Onboarding, Setting Up.

**Шаги (не проверен flow):** после регистрации/CTA → **короткая форма** уточняющих полей → продолжение онбординга.

**Состояния:** empty fields; валидация/error — **не проверено** на этом кадре.

**Приём:** после клика «Заявка» — **один экран** с минимумом полей + что будет дальше (срок ответа из trust strip).

---

## MB-04 — Stripe Web Billing Plans

| | |
|--|--|
| Mobbin | https://mobbin.com/explore/screens/ee2be444-b26c-488a-8ff1-a3eb3535f94a (**200**) |
| Продукт | [Stripe](https://stripe.com/) (Dashboard UX) |
| Платформа | **Web** |
| Сценарий **S3** | Сравнение **пакетов** (не интернет-магазин) |

**Описание Mobbin:** «Billing plan comparison with updated current plan»; tags: Pricing, Subscription & Paywall, Card, Subscribing & Upgrading.

**Шаги (не проверен flow):** просмотр тарифов → выделение текущего/рекомендуемого → действие upgrade.

**Приём для «Лирейт»:** карточки «Регистрация ТЗ», «Патент», «Комплекс» с **ясным сравнением** и одним primary CTA; без жёлтого Ramp из RS-05 без утверждения владельца.

**Не путать:** это **SaaS billing UI**, не публичный прайс юрфирмы — адаптировать иерархию, не копировать.

---

## MB-05 — Stripe Web Billing Overview (success)

| | |
|--|--|
| Mobbin | https://mobbin.com/explore/screens/4d780773-1703-4ea7-a1a1-9c1028da2a8b (**200**) |
| Продукт | Stripe Dashboard |
| Платформа | **Web** |
| Сценарий **S1** (завершение) | Подтверждение успешного действия после формы |

**Описание Mobbin:** «Billing overview page **confirming subscription creation**»; tags: Acknowledgement & Success, **Toast**, Adding & Creating.

**Шаги (не проверен flow):** действие завершено → **toast + overview** с понятным next step.

**Приём:** после отправки заявки — **не только** «Спасибо», а «что дальше» (звонок в течение N часов, номер заявки); связать с DS-L04/L09 из Design Spells.

---

### Дополнительно: блог (S4), без включения в топ-5

| Mobbin | https://mobbin.com/explore/screens/2cdf0d69-b63f-4eee-99f1-19c89b988902 (**200**) — The New Yorker Web Article (long-read). Использовать при редизайне `/news/`, не смешивать с zine-блогом EXCALIBUR.

---

## Ожидает подключения Mobbin MCP (владелец Pro/Team)

До OAuth **не** фиксировать выдуманные flow URL. Искать через MCP / поиск Mobbin:

| Сценарий | Запросы для агента |
|----------|-------------------|
| S1 Заявка | `web contact form success confirmation B2B`, `lead form multi-step professional services` |
| S2 Услуга | `web service selection tiles`, `legal services website navigation` |
| S3 Цена | `web pricing professional services`, `service packages comparison cards` |
| S4 Блог | `web article detail long form blog B2B` |
| S5 Мессенджер | `web chat widget telegram alternative`, `customer support contact options footer` |
| (будущее) Проверка ТЗ | `trademark search tool onboarding`, `intellectual property checklist web` — **только если появится продукт на сайте** |

После авторизации: дополнить этот файл id **MB-06+** с полными flow из MCP; указать `design_ref: MB-xx` в PR.

Атрибуция: `design_ref: MB-xx` + URL `https://mobbin.com/explore/screens/<uuid>` + продукт-источник.