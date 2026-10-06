# Promotion checklist — B06 n8n-agents-self-hosted-bez-queue-mode-2026

Дата публикации: YYYY-MM-DD  
Live URL: https://mayai.ru/blog/n8n-agents-self-hosted-bez-queue-mode-2026/ (заполнить после publish)

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

```
Queue mode для workflow, а вкладка Agents не появилась? Self-hosted n8n Agents — это не AI Agent node на canvas, а отдельный продукт с publish и каналами.

• N8N_ENABLED_MODULES=agents, regular mode, версия ≥2.32.3
• Production: queue-инстанс + второй Docker без queue для Agents
• Публичный N8N_WEBHOOK_URL для Telegram/Slack и smoke после publish

Читать: https://mayai.ru/blog/n8n-agents-self-hosted-bez-queue-mode-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «n8n агенты на своем сервере» (ручная проверка / Wordstat)

## Notes

Indexer (06.10.2026): 0 interlink changes — hub-and-spoke не нашёл совпадений anchor_variants в телах других статей (6 статей в индексе). После publish перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru`. llms: `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (6 статей).
