# Design Spells — источник референсов

| Поле | Значение |
|------|----------|
| URL | https://designspells.com/ |
| Назначение | Курируемая коллекция коротких screen recordings: микровзаимодействия, анимации, переходы, обратная связь UI в реальных сайтах и приложениях |
| Дата проверки | **2026-11-19** |
| Кураторы сайта | Chester How, Duncan Leo (см. JSON-LD Organization на главной) |
| Контакт | chester@designspells.com, support@designspells.com |
| Документация для агентов | https://designspells.com/llms.txt |

## Что это даёт проекту

Design Spells **не публикует исходный код** и **не отдаёт дизайн-системы** — только видеозаписи поведения UI с названием, продуктом-источником и тегами. Для публичного сайта (`PUBLIC_SITE_URL`) база используется **до внедрения** эффекта: выбор приёма, адаптация под сдержанный корпоративный тон и компоненты сайта.

Курируемая подборка для юридического сайта: [`../legal-site-curated/design-spells-curated.md`](../legal-site-curated/design-spells-curated.md).

## Лицензия и условия использования

По состоянию на **2026-11-19**:

| Документ | Результат проверки |
|----------|-------------------|
| Terms of Use / Terms of Service | Страница `https://designspells.com/terms` — **404** (отдельных условий использования контента сайта не найдено) |
| Privacy Policy | `https://designspells.com/privacy` — есть (действует с 27.04.2024): сбор email для newsletter, Google Analytics |
| `llms.txt` | Рекомендует **ссылаться на spell** при цитировании; сайт read-only, без API |

**Вывод для репозитория:**

- Записи в `shared/design-references/` — **описания и ссылки**, не копии видео с `cdn.designspells.com`.
- Реализацию на сайте создавать **собственным кодом** проекта; не встраивать чужие ролики и не копировать ассеты продуктов из записей Design Spells.
- Показанные в spell интерфейсы принадлежат **третьим сторонам** (Perplexity, Linear, Supabase и т.д.); при внедрении по мотивам приёма указывать в PR/коммите ссылку на spell и при необходимости — спокойную атрибуцию «inspired by … (via Design Spells)».
- При публичном упоминании примера — ссылка на страницу spell на designspells.com (как просит `llms.txt`).

## Как агенту обновлять каталог

1. Главная с `Accept: text/markdown` или fetch через разрешённый веб-инструмент (см. `llms.txt`).
2. Страница spell: `https://designspells.com/spells/<slug>` — метаданные VideoObject (JSON-LD), теги, spell #.
3. Sitemap: в `llms.txt` заявлен; при запросе `https://designspells.com/sitemap.xml` **2026-11-19** вернул **500** — до восстановления sitemap полагаться на главную и поиск по slug.
4. Новые примеры — в `legal-site-curated/design-spells-curated.md` + `index.json` + дата `last_verified` в этом файле.