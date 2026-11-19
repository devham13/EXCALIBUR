# Экосистема дизайн-референсов (сайт «Лирейт»)

Согласованная модель для агентов EXCALIBUR. Приоритет: **утверждённый** [`DESIGN.md`](../../DESIGN.md) проекта, затем база `shared/design-references/`.

## Роли источников

```text
DESIGN.md (проект)
    ↑ согласование владельцем
Mobbin ─────────→ экраны, компоненты, user flows (MCP: Pro/Team)
Supahero ───────→ композиция hero (H1, CTA, фото/mockup, trust)
Refero Styles ──→ палитра, типографика, сетка, компоненты
Design Spells ──→ микровзаимодействия, переходы, feedback
Jiro MCP ───────→ шаблоны секций (после OAuth; не подменяет DESIGN.md)
```

| Источник | Когда открывать | Что не делать |
|----------|-----------------|---------------|
| [`DESIGN.md`](../../DESIGN.md) | Новая страница, смена токенов, новый компонент | Игнорировать пометки «требует утверждения» |
| [Mobbin](sources/mobbin.md) | Новый/изменённый **сценарий** (форма, услуги, успех) | Вызывать MCP без OAuth; копировать скриншоты в продакшен |
| [Supahero](sources/supahero.md) | Проектирование **первого экрана** / hero | Копировать webp с CDN и чужие фото в продакшен |
| [Refero Styles](sources/refero-styles.md) | Нужна визуальная система / сравнение стилей | Копировать коммерческие шрифты и скриншоты Refero |
| [Design Spells](sources/design-spells.md) | Анимация, sheet, loading, CTA feedback | Встраивать MP4; hover-only без touch |
| **Jiro** (`https://mcp.jiro.build`) | Нужен готовый блок React/Tailwind **и** стек проекта это поддерживает | Считать Jiro источником истины по цветам; подключать без OAuth |
| **Mobbin MCP** (`https://api.mobbin.com/mcp`) | Поиск flows после **Authenticate** (Pro/Team) | Считать tools проверенными; бесплатный план **без** MCP |

## Mobbin MCP (проверено / не проверено)

**Проверено 2026-11-19:**

- Endpoint в [`.cursor/mcp.json`](../../.cursor/mcp.json): `https://api.mobbin.com/mcp`
- Без Authorization: **401**, `resource_metadata` в `WWW-Authenticate`
- Документация: https://mobbin.com/mcp , https://docs.mobbin.com/mcp/clients/cursor.md , Marketplace https://cursor.com/marketplace/mobbin
- MCP доступен на **Pro & Team** (не на free)

**Не проверено:** список tools, поиск flows, лимиты — нужен **Authenticate** владельцем.

**Следующий шаг владельца:** Pro/Team → Marketplace Mobbin → Authenticate → smoke «Search Mobbin for web legal services contact form» → обновить `mobbin-curated.md` и этот раздел.

## Jiro MCP (проверено / не проверено)

**Проверено 2026-11-19 (публичная документация + landing):**

- Endpoint: `https://mcp.jiro.build` (редирект на `https://jiro.build/mcp`).
- Подключение в Cursor: блок в [`.cursor/mcp.json`](../../.cursor/mcp.json).
- Аутентификация: **OAuth / sign-in** в браузере после добавления сервера (на landing: «Login JIRO → Connect MCP → Build»).
- Заявленный каталог: **1 522** секции и шаблоны (React/Tailwind), поиск из IDE.

**Не проверено в этом репозитории:**

- Список MCP tools после OAuth.
- Соответствие блоков Jiro стеку продакшен-сайта «Лирейт» (в репо в основном оркестрация блога, не фронтенд темы).
- Лимиты бесплатного аккаунта.

До проверки tools Jiro используйте только как **опциональный** источник секций; визуальные решения фиксируйте в `DESIGN.md` и Refero-подборке.

## Пайплайн агента (страницы сайта)

1. Прочитать [`DESIGN.md`](../../DESIGN.md).
2. [`index.json`](index.json) → Mobbin (MB-*), Supahero (SH-*), Refero (RS-*), Design Spells (DS-*).
3. Сценарии — правило [`rules/design-user-flows.mdc`](../../rules/design-user-flows.mdc).
4. Hero — правило [`rules/design-hero-first-screen.mdc`](../../rules/design-hero-first-screen.mdc).
5. Motion — правило [`rules/design-micro-interactions.mdc`](../../rules/design-micro-interactions.mdc).
6. Новые страницы — правило [`rules/design-pages-visual-system.mdc`](../../rules/design-pages-visual-system.mdc).
7. Jiro / Mobbin MCP — только после OAuth владельца; иначе не вызывать tools.

## Пайплайн блога EXCALIBUR

Не смешивать с Refero/Jiro для cover: [`shared/visual-assets-mcp-policy.md`](../visual-assets-mcp-policy.md), `memory/cover/`. Палитра блога в `memory/brief/site-brief.md` (**отдельно** от корпоративного сайта).