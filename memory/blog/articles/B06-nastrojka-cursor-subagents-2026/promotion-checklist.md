# Promotion checklist — B06 nastrojka-cursor-subagents-2026

Дата публикации: 2026-06-22  
Live URL: https://neurinix.com/2026/06/22/nastrojka-cursor-subagents-2026/

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
Cursor subagents за 20–30 минут: reviewer + test-runner параллельно, без enterprise-оркестратора.

• 7 шагов: .cursor/agents/, YAML frontmatter, /name и автоделегирование
• 2 готовых subagent-файла (code-reviewer readonly, test-runner)
• Таблица frontmatter + сравнение subagents vs MCP vs Background Agents
• Чеклист из 12 пунктов перед git commit

Читать: https://neurinix.com/2026/06/22/nastrojka-cursor-subagents-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP) → link to B06 на упоминании subagents / parallel Task
- [ ] Обновить B02 (n8n) → link to B06 на связке IDE + автоматизация 24/7

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor subagents» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 3× internal: B03 MCP ×2, B02 n8n ×1). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt` (--site-base https://mayai.ru). После publish — перезапустить interlinker для inbound из B03/B02.
