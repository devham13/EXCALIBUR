# Promotion checklist — B06 chat-bot-dlya-biznesa-rag

Дата публикации: 2026-06-21  
Live URL: https://mayai.ru/blog/chat-bot-dlya-biznesa-rag/

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
Рейтинги «лучших конструкторов» не учат собирать рабочего ИИ-бота — без RAG модель выдумывает цены, без эскалации один ответ сжигает доверие.

Главное из гайда:
• MVP за 7–14 дней: один канал (Telegram / webhook / MAX) + Vector Store + handoff в CRM
• n8n vs Make: self-host и глубокий RAG против быстрого no-code старта
• Перед рекламой — 50–100 тест-кейсов, FCR 60–80%, fallback ниже 20%

Пошаговый workflow с чеклистом:
Читать: https://mayai.ru/blog/chat-bot-dlya-biznesa-rag/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Interlinker (2026-06-21): 0 авто-ссылок — writer уже добавил outbound links на n8n и MCP; hub-and-spoke keywords других статей не совпали с контекстом B06.
