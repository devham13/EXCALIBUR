# Promotion checklist — B06 nastroyka-cursor-automations

Дата публикации: 2026-09-11  
Live URL: /2026/09/11/nastroyka-cursor-automations/ (prefix: EXCALIBUR_PUBLIC_SITE_URL)

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
Cursor Automations: Cloud Agent по будильнику — или снова ручной чат каждое утро?

За 30–45 минут можно запустить первую Automation: cron no-repo для брифов или webhook POST из Make/n8n.

Главное из гайда:
• Pro+ и on-demand billing — без них фоновые runs могут не стартовать после included usage
• Webhook URL и API key появляются только после Save & Activate
• CRON_TZ=Europe/Moscow для cron по Москве — сверяйте время в Run History

Читать: /2026/09/11/nastroyka-cursor-automations/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит outbound на B03 и B05). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound-ссылок из B03 (MCP) и B05 (контент-завод).
