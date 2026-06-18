# Promotion checklist — B06 cursor-rules-nastrojka-2026

Дата публикации: 2026-06-18  
Live URL: https://mayai.ru/cursor-rules-nastrojka-2026/

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
Agent в Cursor отвечает по-разному — пока нет cursor rules в .cursor/rules/*.mdc?

• 7 H2: миграция с .cursorrules, первый .mdc, 4 режима активации, стек для автоматизации
• Пример 00-general.mdc + чеклист 15 пунктов перед git push
• FAQ×7: rules vs MCP, globs, context gauge, troubleshooting
• Связка с B03: rules — как думать, MCP — к чему подключаться

Читать: https://mayai.ru/cursor-rules-nastrojka-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP) → link to B06 на упоминании rules / «cursor rules» (anchor «настройка cursor rules»)
- [ ] Обновить B05 (контент-завод) → link to B06 на упоминании Cursor Agent / rules в Git

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor rules» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 4× outbound на B03 `/podklyuchenie-mcp-cursor/`). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound-ссылок из B03/B05.
