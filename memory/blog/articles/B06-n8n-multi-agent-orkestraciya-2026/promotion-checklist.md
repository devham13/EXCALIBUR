# Promotion checklist — B06 n8n-multi-agent-orkestraciya-2026

Дата публикации: 2026-06-22  
Live URL: https://mayai.ru/blog/n8n-multi-agent-orkestraciya-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
- [ ] Проверить internal links из статьи (200): B02 prerequisite, inbound из B02
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Один AI Agent в n8n захлебнулся в 10 tools? Соберите orchestrator + 2–3 specialists.

• 8 шагов сборки: Supervisor/Router, AI Agent Tool vs sub-workflow
• Таблица паттернов + чеклист 16 пунктов перед prod
• Честно про ~15× tokens vs single-agent (Anthropic/n8n)
• Prerequisite: single agent из B02

Читать: https://mayai.ru/blog/n8n-multi-agent-orkestraciya-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] B03 (MCP) → link to B06 на упоминании n8n-агентов / фоновой автоматизации
- [ ] B05 (контент-завод) → link to B06 на multi-agent / Newsroom (anchor «n8n агенты» или «multi-agent»)
- [ ] После publish B06 — перезапустить interlinker для inbound из B03/B05 и href B02→B06 на live URL

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «n8n агенты» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 1 автоматическая вставка (B02 → B06, anchor «n8n агенты»). B06 outbound: prerequisite на B02 (`/avtomatizaciya-n8n-ai-agents/`). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для дополнительных inbound и проверки slug B02 в B06.
