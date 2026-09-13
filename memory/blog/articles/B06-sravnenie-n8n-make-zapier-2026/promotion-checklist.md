# Promotion checklist — B06 sravnenie-n8n-make-zapier-2026

Дата публикации: 2026-09-13  
Live URL: https://mayai.ru/blog/sravnenie-n8n-make-zapier-2026/

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
Один ИИ-сценарий — 5 шагов, 2000 прогонов/мес: Zapier съест ~10 000 tasks, Make — 10 000 credits, n8n — всего 2 000 executions. Пересчитайте свой объём до оплаты.

• Таблица 15 параметров: n8n vs Make vs Zapier
• Матрица 6 сценариев для ИИ-автоматизации
• Чеклист из 12 пунктов перед подпиской + TCO с LLM API

Читать: https://mayai.ru/blog/sravnenie-n8n-make-zapier-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B02 (n8n) → link to B06 на «Сравнение n8n vs Make» (anchor «сравнение n8n make zapier»)
- [ ] Обновить B05 (контент-завод) → link to B06 на «n8n или Make.com» (anchor «n8n или make»)
- [ ] B06 уже содержит outbound на B02 (`/avtomatizaciya-n8n-ai-agents/`)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «сравнение n8n make zapier» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются дословно в B01–B05; B06 уже содержит 2× outbound на B02 по slug `avtomatizaciya-n8n-ai-agents`). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B02/B05.
