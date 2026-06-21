# Promotion checklist — B07 wordpress-mcp-ai-agenty

Дата публикации: YYYY-MM-DD  
Live URL: $EXCALIBUR_PUBLIC_SITE_URL/wordpress-mcp-ai-agenty/

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
Черновик в WordPress всё ещё копируете из Cursor руками? Official MCP Adapter переводит abilities сайта в tools агента — с проверкой человеком, без auto-publish.

• 10 шагов: mcp-adapter, отдельный user, Application Password, .cursor/mcp.json
• Discover → read-only → draft: human-in-the-loop на каждом write-tool
• Связка с базовым гайдом MCP в Cursor и GEO-чеклистом перед публикацией

Читать: $EXCALIBUR_PUBLIC_SITE_URL/wordpress-mcp-ai-agenty/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] B03 уже получил inbound: «WordPress MCP» → /wordpress-mcp-ai-agenty/ (interlinker --apply)
- [ ] Рассмотреть ручную ссылку из B04 (GEO) при упоминании WordPress MCP workflow

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «wordpress mcp» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 1 auto-injected link (B03 → B07, anchor «WordPress MCP»). B07 writer уже содержит 5× B03, 3× B04. llms.txt обновлён: 7 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker для inbound из B02/B05 при появлении anchor matches.
