# Promotion checklist — B06 nastroyka-cursor-rules-mdc

Дата публикации: YYYY-MM-DD  
Live URL: https://mayai.ru/blog/nastroyka-cursor-rules-mdc/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
- [ ] Проверить internal links из статьи (200): 3× `/podklyuchenie-mcp-cursor/`
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Agent снова переписал файл — а rules вы так и не настроили? За 20–40 минут соберите .cursor/rules/*.mdc и проверьте Active Rules.

• 7 шагов: alwaysApply, globs, YAML frontmatter, git commit
• Таблица Project / User / Team / AGENTS.md + миграция .cursorrules за 5 минут
• Чеклист troubleshooting: silent YAML, Tab vs Agent, дубли legacy
• Связка с MCP: rules — «как думать», MCP — доступ к сервисам (гайд B03)

Читать: https://mayai.ru/blog/nastroyka-cursor-rules-mdc/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP) → link to B06 на упоминании rules/Agent (anchor «cursor rules» / «настройка rules»)
- [ ] Обновить B05 (контент-завод) → link to B06, если в тексте есть Cursor/Agent без rules

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor rules» (ручная проверка / Wordstat; 248 показов/мес, июнь 2026)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 — длинные фразы; «cursor rules» встречается только в B06; B06 уже содержит 3× outbound на B03). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B03/B05.
