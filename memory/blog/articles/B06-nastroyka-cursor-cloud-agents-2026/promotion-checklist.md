# Promotion checklist — B06 nastroyka-cursor-cloud-agents-2026

Дата публикации: 2026-09-13  
Live URL: https://mayai.ru/nastroyka-cursor-cloud-agents-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```text
Build красный — Cloud Agent мёртв. Или environment.json пустой?

Cursor Cloud Agents клонируют repo, ставят зависимости и открывают PR, пока ноутбук свободен. Настройка чаще всего ломается на GitHub без read-write, failed Build и secrets не в dashboard.

Главное из гайда:
• Цикл за 30–60 минут: GitHub read-write → environment → Build Success → agent run → PR.
• .cursor/environment.json: install на Build, dev-серверы в start/terminals; secrets только в dashboard.
• Troubleshooting: failed Build не меняет active snapshot; для terminals — поле "start": "true".

Пошаговая инструкция с чеклистом и FAQ:
Читать: https://mayai.ru/nastroyka-cursor-cloud-agents-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Interlinker (2026-09-13): 0 новых ссылок — ключевые anchor уже покрыты writer/GEO QA (B03 MCP, cursor rules). B06 добавлен в memory/blog/llms.txt и llms-full.txt.
