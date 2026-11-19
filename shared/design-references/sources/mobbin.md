# Mobbin — экраны, компоненты и пользовательские сценарии

| Поле | Значение |
|------|----------|
| URL | https://mobbin.com/ |
| Назначение | Библиотека **600 000+** скриншотов и **flows** реальных mobile/web продуктов: компоненты, паттерны, пошаговые сценарии |
| Дата проверки | **2026-11-19** |
| Издатель | Mobbin Pte. Ltd. (support@mobbin.com) |
| Документация MCP | https://mobbin.com/mcp · https://docs.mobbin.com/mcp/clients/cursor.md |

## Доступ и планы (проверено 2026-11-19)

| Режим | Что доступно |
|-------|----------------|
| **Бесплатный аккаунт** | Ограниченный просмотр на mobbin.com (категории Explore, отдельные screen-страницы **без** полноценного Save/Copy — редирект на `/signup/modal`) |
| **Pro / Team** | Полная библиотека, flows, **Mobbin MCP** (входит в платный план; отдельной платы за MCP на странице `/mcp` не указано) |
| **Mobbin MCP** | Только **Pro & Team**; на free — browse сайта, **без** MCP |

Публичные **explore/screens/&lt;uuid&gt;** отдают **200** и превью скрина; **многошаговые flows** и детальный список экранов в flow **не верифицированы** без входа.

## MCP в Cursor (статус репозитория)

| Шаг | Статус |
|-----|--------|
| HTTP endpoint | `https://api.mobbin.com/mcp` добавлен в [`.cursor/mcp.json`](../../../.cursor/mcp.json) |
| Без токена | **401** JSON: `Missing or invalid Authorization header`; заголовок `WWW-Authenticate: Bearer resource_metadata="https://api.mobbin.com/.well-known/oauth-protected-resource/mcp"` |
| **Список tools** | **Не проверен** (нет OAuth владельца) |
| Рекомендуемый путь (официально) | [Cursor Marketplace — Mobbin](https://cursor.com/marketplace/mobbin) → Add to Cursor → Customize → Installed → Mobbin → **Authenticate** (Pro/Team) |
| Альтернатива | HTTP MCP в любом клиенте: [other.md](https://docs.mobbin.com/mcp/clients/other.md) — URL `https://api.mobbin.com/mcp`, OAuth при первом запросе |

**Следующий шаг для владельца:** оформить Mobbin Pro/Team → Authenticate в Cursor → зафиксировать список tools в `ecosystem.md` → дополнить [`mobbin-curated.md`](../legal-site-curated/mobbin-curated.md) конкретными flow ID из MCP.

## Что это даёт проекту

Mobbin закрывает **уровень сценария** (не hero — Supahero; не tokens — Refero; не motion — Design Spells):

- карточки услуг → заявка → подтверждение;
- сравнение пакетов / «от … руб.»;
- long-read блога;
- empty/error/success в формах.

Курировка: [`../legal-site-curated/mobbin-curated.md`](../legal-site-curated/mobbin-curated.md).

## Лицензия и использование

| Источник | Результат 2026-11-19 |
|----------|----------------------|
| Terms на mobbin.com | **Не извлекались** автоматически (SPA); см. https://mobbin.com/pricing |
| Скриншоты третьих продуктов | Принадлежат авторам приложений; в репо — **только ссылки и текстовый разбор** |
| Продакшен «Лирейт» | Не встраивать изображения Mobbin; реализация своим кодом + `DESIGN.md` |

## Связка с другими источниками

| Слой | Источник |
|------|----------|
| User flows / screens | Mobbin (этот файл) |
| Hero | Supahero |
| Design system | Refero Styles |
| Motion | Design Spells |
| Блоки | Jiro MCP (OAuth; tools не верифицированы) |