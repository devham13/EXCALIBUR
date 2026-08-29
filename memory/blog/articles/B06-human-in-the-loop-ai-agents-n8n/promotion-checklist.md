# Promotion checklist — B06 human-in-the-loop-ai-agents-n8n

Дата публикации: 2026-08-29  
Live URL: /2026/08/29/human-in-the-loop-ai-agents-n8n/ (production host — см. EXCALIBUR_PUBLIC_SITE_URL)

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
ИИ-агент списал деньги — вы не нажимали Approve?

HITL — пауза перед опасным tool call: Approve выполняет, Deny отменяет.

• Карта рисков: финансы, email, CRM delete, deploy
• n8n 2.6+ native human review (9 каналов: Slack, Telegram…)
• Make: native HITL только Enterprise; иначе webhook split
• Cursor Cloud Agents: branch protection + PR review вместо per-action approve
• Чек-лист 27 пунктов перед prod + EU AI Act Art. 14

Читать: /2026/08/29/human-in-the-loop-ai-agents-n8n/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B02 (n8n AI Agents) → link to B06 на упоминании Human-in-the-Loop (anchor «human in the loop n8n»)
- [ ] Обновить B05 (контент-завод) → link to B06 на Human-in-the-loop 2.0 (anchor «human review tool calls»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «human in the loop n8n» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не совпали с текстами B01–B05; B06 уже содержит outbound на B02 `/avtomatizaciya-n8n-ai-agents/` и Cursor Automations). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru` для inbound из B02/B05.
