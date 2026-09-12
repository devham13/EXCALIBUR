# Promotion checklist — B06 nastrojka-make-ai-agents

Дата публикации: 2026-09-12  
Live URL: https://www.meta-journal.ru/2026/09/12/nastrojka-make-ai-agents/

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
Линейный сценарий Make не понимает срочность заявки? Make AI Agent (New) — «умный диспетчер» на том же canvas: сам выбирает tools по вашим правилам.

• Run an agent + Instructions + 2–3 tools за один вечер
• MCP, Call a scenario, Knowledge (RAG) без кода
• Тест в Chat/Reasoning и чеклист credits перед prod
• Open beta с 2 февраля 2026; Make's AI Provider на всех тарифах

Читать: https://mayai.ru/blog/nastrojka-make-ai-agents/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «make ai agents настройка» (ручная проверка / Wordstat)

## Notes

Indexer: 0 interlink changes (anchor_variants B06 не встречаются дословно в текстах B01–B05; B02 упоминает «Make AI Agents», но slug ещё не связан). После publish — перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru`. llms.txt обновлён: 6 статей в `memory/blog/llms.txt`.
