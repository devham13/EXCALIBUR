# База референсов дизайна (EXCALIBUR / сайт «Лирейт»)

Канонический каталог **визуальной системы** (Refero Styles), **микровзаимодействий** (Design Spells) и связки с **Jiro MCP** для публичного сайта юридической компании «Лирейт» (`PUBLIC_SITE_URL`, см. `.env.example`) и связанных визуальных работ в репозитории.

Черновик проектных tokens и страниц: [`DESIGN.md`](../../DESIGN.md) в корне репозитория.

Это **не** библиотека ассетов и **не** исходный код чужих продуктов. Агент использует записи как ориентиры и оформляет реализацию средствами проекта.

## Структура

| Путь | Назначение |
|------|------------|
| [`index.json`](index.json) | Машиночитаемый реестр источников и курируемых подборок |
| [`sources/`](sources/) | Карточки внешних источников (ссылка, дата проверки, лицензия/ограничения) |
| [`legal-site-curated/`](legal-site-curated/) | Подборки примеров для корпоративного юридического сайта |

## Связанные инструкции

- Карта экосистемы: [`ecosystem.md`](ecosystem.md) (Refero ↔ Design Spells ↔ Jiro)
- Правило визуальной системы: [`rules/design-pages-visual-system.mdc`](../../rules/design-pages-visual-system.mdc)
- Правило motion: [`.cursor/rules/design-micro-interactions.mdc`](../../.cursor/rules/design-micro-interactions.mdc) (исходник — [`rules/design-micro-interactions.mdc`](../../rules/design-micro-interactions.mdc))
- Визуальные MCP-ассеты (обложки, hero): [`shared/visual-assets-mcp-policy.md`](../visual-assets-mcp-policy.md)
- Cloud-агенты: краткая отсылка в [`AGENTS.md`](../../AGENTS.md) (раздел «Референсы микровзаимодействий»)

## Как добавлять источник

1. Создайте `sources/<slug>.md` по образцу [`sources/design-spells.md`](sources/design-spells.md).
2. При необходимости — курируемую подборку в `legal-site-curated/` или другом каталоге проекта.
3. Обновите [`index.json`](index.json).
4. Не копируйте видео, скринкасты и код с референс-сайтов; указывайте прямые ссылки и атрибуцию.