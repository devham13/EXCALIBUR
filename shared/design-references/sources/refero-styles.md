# Refero Styles — источник визуальных систем (DESIGN.md)

| Поле | Значение |
|------|----------|
| URL | https://styles.refero.design/ |
| Назначение | Каталог **визуальных систем** реальных сайтов: палитра, типографика, сетка, отступы, компоненты и встроенный **DESIGN.md** для агентов |
| Дата проверки | **2026-11-19** |
| Издатель | [Refero](https://refero.design/) (Refero Styles — отдельный продукт на поддомене) |
| Связанный MCP | [refero.design/mcp](https://refero.design/mcp?utm_source=refero_styles) (отдельно от Jiro; OAuth / подключение в IDE) |

## Что это даёт проекту

Refero Styles описывает **макро-уровень** (layout, tokens, компоненты). Для **микровзаимодействий** используйте [Design Spells](design-spells.md) и [`legal-site-curated/design-spells-curated.md`](../legal-site-curated/design-spells-curated.md).

Курируемая подборка для юридического сайта «Лирейт»: [`../legal-site-curated/refero-styles-curated.md`](../legal-site-curated/refero-styles-curated.md).

Проектный черновик айдентики: [`DESIGN.md`](../../../DESIGN.md) в корне репозитория.

## Как читать DESIGN.md

По состоянию на **2026-11-19**:

| Способ | Результат |
|--------|-----------|
| Страница стиля `https://styles.refero.design/style/<uuid>` | **200** — вкладки Preview / DESIGN.md / Tailwind / tokens (контент DESIGN.md встроен в страницу) |
| Прямой URL `.../style/<uuid>/DESIGN.md` | **404** — отдельного raw-файла нет |
| `https://styles.refero.design/llms.txt` | **404** |
| Экспорт «Copy .md» на странице стиля | Заявлен на UI; для агентов достаточно markdown-вкладки после fetch |

Токены в карточках Refero — **нормализованные измерения** исходного сайта; подпись на странице: *«Source measurements are normalized; roles and recommendations are interpreted.»*

## Лицензия и условия использования

| Документ | Результат проверки 2026-11-19 |
|----------|------------------------------|
| `https://styles.refero.design/terms` | **404** |
| `https://refero.design/terms` | HTML загружается, но **текст условий в fetch не извлечён** (пустой markdown; возможна SPA) |
| `https://refero.design/privacy` | Аналогично — **текст не извлечён** в автоматическом fetch |

**Вывод для репозитория:**

- Использовать Refero как **справочник идей и токенов**, не копировать скриншоты `images.refero.design` как продакшен-ассеты без права.
- Шрифты из карточек (Wise Sans, Roobert, SuisseIntl, lausanne и т.д.) часто **коммерческие**; в проекте — только **замены с проверенной лицензией и кириллицей** (см. [`DESIGN.md`](../../../DESIGN.md)).
- Исходные сайты (wise.com, column.com, …) принадлежат третьим сторонам; при публичном упоминании — ссылка на страницу стиля Refero и на оригинальный продукт.

## Связка с другими источниками

| Слой | Источник | Путь в репо |
|------|----------|-------------|
| Визуальная система | Refero Styles | этот файл + `legal-site-curated/refero-styles-curated.md` |
| Motion / micro-UX | Design Spells | `sources/design-spells.md` |
| Готовые React/Tailwind блоки | Jiro MCP (`https://mcp.jiro.build`) | `.cursor/mcp.json` — **OAuth-вход обязателен**; список tools в этой среде **не проверялся** (см. [`ecosystem.md`](../ecosystem.md)) |