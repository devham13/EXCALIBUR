# Promotion checklist — B06 nastroyka-cursor-automations-2026

Дата публикации: 2026-10-15  
Live URL: https://mayai.ru/blog/nastroyka-cursor-automations-2026/ (заполнить после publish)

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

```
Cursor Automations за 45 минут — или cron в 3 ночи по вашему «локальному»?

• Cron в UTC + forum workarounds; webhook только после Save
• GitHub PR, billing ~$2 headroom, Run History
• 7 шагов: от триггера до чеклиста secrets

Читать: https://mayai.ru/blog/nastroyka-cursor-automations-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (B03 MCP, B05 контент-завод — по смыслу)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor automations настройка» (ручная проверка / Wordstat)

## Notes

Indexer: 0 автоматических interlink (anchor_variants B06 не совпали в телах других статей в `memory/blog/articles`). В `article.html` уже есть ручные internal: mayai.ru/podklyuchenie-mcp-cursor/ (×2), cursor setup docs. После publish — перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru` при появлении пересечений с B07+ и обновить старые посты ссылкой на B06. `memory/blog/llms.txt` и `llms-full.txt`: 6 статей, B06 в индексе.
