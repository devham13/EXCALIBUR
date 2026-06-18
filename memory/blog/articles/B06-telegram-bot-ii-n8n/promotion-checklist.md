# Promotion checklist — B06 telegram-bot-ii-n8n

Дата публикации: 2026-06-18  
Live URL: [REDACTED]/2026/06/18/telegram-bot-ii-n8n/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
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
Telegram-бот n8n за 40 минут — лиды ночью или клиент у конкурента?

Заявки в Telegram приходят вне рабочих часов, а шаблонные конструкторы не дают CRM и эскалацию. Соберите бота без кода:

• BotFather → Telegram Trigger → AI Agent + память + Send Message
• 1–2 tools: FAQ в Sheets, лид в amoCRM/Bitrix24
• Чеклист из 12 пунктов перед продакшеном (fallback, Error Workflow, telegram_id)

Читать: [REDACTED]/2026/06/18/telegram-bot-ii-n8n/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B02 (avtomatizaciya-n8n-ai-agents) → ссылка на B06 в блоке «следующий шаг» / Telegram-канал

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «telegram бот n8n» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker `--apply` — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 2× ссылку на B02 `/avtomatizaciya-n8n-ai-agents/`). После publish — вручную добавить inbound из B02 и перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru`. llms.txt обновлён: 6 статей в `memory/blog/llms.txt`.
