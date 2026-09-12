# Promotion checklist — B06 nastrojka-claude-code-ci-cd-2026

Дата публикации: 2026-09-12  
Live URL: https://mayai.ru/nastrojka-claude-code-ci-cd-2026/

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
Claude Code в CI/CD обещает авто-ревью, но без схемы job падает на секретах, лишних tools или бесконечном agent loop.

Главное из гайда:
• GitHub-only → anthropics/claude-code-action@v1; multi-CI → claude --bare -p с ANTHROPIC_API_KEY
• Guardrails: --permission-mode dontAsk, --allowedTools, --max-turns, job timeout
• GitLab beta на сентябрь 2026; не запускайте agent на untrusted PR через pull_request_target

Читать: https://mayai.ru/nastrojka-claude-code-ci-cd-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Interlinker (2026-09-12): 0 auto-injected links — B06 уже содержит ручные ссылки на B03/B05; keyword-match в других статьях не найден. После publish — рассмотреть ручную перелинковку из B03 (MCP/CI) и B02 (n8n automation).
