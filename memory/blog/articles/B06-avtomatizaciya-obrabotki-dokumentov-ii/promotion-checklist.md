# Promotion checklist — B06 avtomatizaciya-obrabotki-dokumentov-ii

Дата публикации: YYYY-MM-DD  
Live URL: https://mayai.ru/avtomatizaciya-obrabotki-dokumentov-ii/ (заполнить после publish)

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
Счёт из почты в CRM за 2 недели — или снова копипаст ИНН?

• 8 шагов: intake → OCR → LLM(JSON) → валидация ИНН → approve → amoCRM/Bitrix24
• Таблица n8n vs Make + JSON-schema для счетов
• KPI пилота: ≥90% верных полей на 30–50 документах
• Human-in-the-loop обязателен — автономные ИИ закрывают <2,5% сложных задач без человека

Читать: https://mayai.ru/avtomatizaciya-obrabotki-dokumentov-ii/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «автоматизация обработки документов» (ручная проверка / Wordstat)

## Notes

Indexer (2026-06-21): interlinker `--apply` — 0 новых ссылок (6 статей загружены; anchor_variants B06 не встречаются в текстах B01–B05 без уже существующих slug-ссылок). В B06 уже есть internal link на B02 (`/avtomatizaciya-n8n-ai-agents/`). После publish — перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru`. llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt`.
