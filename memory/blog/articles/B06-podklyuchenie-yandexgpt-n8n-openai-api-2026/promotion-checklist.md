# Promotion checklist — B06 podklyuchenie-yandexgpt-n8n-openai-api-2026

Дата публикации: 2026-10-14  
Live URL: https://mayai.ru/blog/podklyuchenie-yandexgpt-n8n-openai-api-2026/ (проверить после publish)

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
- [ ] Проверить internal links из статьи (200): `/avtomatizaciya-n8n-ai-agents/`, `/podklyuchenie-mcp-cursor/`
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
n8n ждёт OpenAI — а у вас YandexGPT? Подключите через тот же credential: ключ Yandex Cloud + Base URL до /v1.

• Чеклист IAM: SA, scope yc.ai.languageModels.execute, роль ai.languageModels.user
• Два Base URL: llm.api и запасной ai.api — таблица 401/404
• AI Agent + yandexgpt-lite/latest и workflow с approve перед CRM

Читать: https://mayai.ru/blog/podklyuchenie-yandexgpt-n8n-openai-api-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «подключить yandexgpt к n8n» (ручная проверка / Wordstat)

## Notes

Indexer (2026-10-14): `excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles --site-base https://mayai.ru` — 0 новых автоссылок (6 статей; пересечений anchor_variants в телах других статей нет). В B06 уже есть ручные internal на B02 и B03. `memory/blog/llms.txt` и `llms-full.txt` — 6 статей, B06 добавлен.
