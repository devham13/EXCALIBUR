# Promotion checklist — B06 claude-code-n8n-mcp-nastrojka-2026

Дата публикации: 2026-06-22  
Live URL: https://mayai.ru/2026/06/22/claude-code-n8n-mcp-nastrojka-2026/

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
Claude Code без n8n-mcp не создаст workflow в вашем n8n — агент не видит ноды и API инстанса.

• claude mcp add за 20–40 минут: doc-only → full mode с N8N_API_KEY
• Таблица n8n-mcp vs Instance MCP + чеклист 12 пунктов
• Первый webhook workflow из текстового промпта и тест POST без ручного JSON
• Troubleshooting Cloud vs self-hosted и MCP_TIMEOUT

Читать: https://mayai.ru/claude-code-n8n-mcp-nastrojka-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B02 (n8n-агенты) → link to B06 на упоминании «claude code» / «n8n-mcp»
- [ ] Обновить B03 (Cursor MCP) → link to B06 в блоке «IDE vs terminal» / «связка с n8n»

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code n8n» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 — длинные фразы, не встречаются в B01–B05; slug B06 отсутствует в inbound-текстах). B06 уже содержит outbound на B02 и B03. llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B02/B03.
