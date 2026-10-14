# Promotion checklist — B06 n8n-bitrix24-ii-agent-otkrytye-linii

Дата публикации: 2026-10-14  
Live URL: https://mayai.ru/blog/n8n-bitrix24-ii-agent-otkrytye-linii/

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
Клиент в Telegram, а CRM плодит дубли? Соберите MVP: ONIMBOTV2 → n8n → AI Agent → лид без повторов.

• Бот v2 + фильтр entityType=LINES — не CRM-webhook на onCrmLeadAdd
• Ответ в диалоге: imopenlines.bot.session.message.send
• Лимит REST 2 rps и human-in-the-loop при эскалации

Читать: https://mayai.ru/blog/n8n-bitrix24-ii-agent-otkrytye-linii/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Interlinker (2026-10-14): 0 новых hub-and-spoke вставок; отчёт `memory/blog/interlink-suggestions.json`.
- llms.txt обновлён: B06 в индексе `memory/blog/llms.txt`.
