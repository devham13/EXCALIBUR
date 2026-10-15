# Blog topics — Excalibur BLOG

Формат карточек. **Utility-only:** см. `shared/editorial-utility-only.md`.

**Разрешённые `search_intent`:** `how_to`, `checklist`, `comparison`, `troubleshooting`, `workflow`, `parent_guide`  
`**article_mode`:** только **B** (гайд/инструкция). Режим A (новости) — не публикуем.

Перед research:

```bash
python scripts/excalibur_blog_utility_gate.py --topic-id <ID>
```

---

## B01 — Пример темы

- **priority:** P0
- **slug:** primer-seo-stati
- **h1:** Как писать SEO-статьи, которые читают люди
- **primary_query:** как писать seo статьи
- **secondary_queries:** seo текст для блога, geo оптимизация статьи
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Зачем SEO и GEO в одной статье
  2. Структура longread
  3. FAQ и schema
  4. Чеклист перед публикацией
- **faq_hints:** сколько символов в seo статье; что такое geo в seo
- **internal_links:** /
- **cover_scene_hint:** редактор за ноутбуком, блокнот, тёплый свет

---

## B02 — Автоматизация процессов на n8n

- **priority:** P0
- **slug:** avtomatizaciya-n8n-ai-agents
- **h1:** Как настроить ИИ-агентов в n8n: пошаговое руководство по автоматизации бизнеса
- **primary_query:** автоматизация n8n
- **secondary_queries:** автоматизация ии n8n, примеры автоматизации n8n, ии агенты и автоматизация с n8n, автоматизация бизнеса n8n
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Почему n8n стал лидером автоматизации с ИИ в 2026 году
  2. Пошаговая настройка первого ИИ-агента в ноде AI Agent
  3. Подключение памяти и векторных баз данных (RAG) без кода
  4. Реальные примеры автоматизации n8n для бизнеса
  5. Сравнение n8n self-hosted и Make: что выбрать в 2026 году
- **faq_hints:** как устроен ai agent node в n8n; чем отличается n8n от make в 2026; как подключить базу знаний к ии в n8n
- **internal_links:** /services/
- **cover_scene_hint:** робот собирает конструктор из кубиков-интеграций (нод), яркие розовые стикеры с надписями "LangChain" и "AI Agent", неоновый свет, diy коллаж

---

## B03 — Подключение MCP в Cursor

- **priority:** P0
- **slug:** podklyuchenie-mcp-cursor
- **h1:** Как подключить MCP-серверы в Cursor: пошаговая инструкция для автоматизации
- **primary_query:** cursor mcp
- **secondary_queries:** mcp сервер для cursor, как подключить mcp к cursor, cursor ai mcp, настройка mcp сервера
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Что такое MCP и зачем подключать серверы в Cursor в 2026 году
  2. Где лежит конфиг: ~/.cursor/mcp.json и .cursor/mcp.json в проекте
  3. Пошаговое подключение stdio-сервера через npx (пример mcp.json)
  4. Проверка в Settings → Tools & MCP и настройка безопасности (auto-run, allowlist)
  5. Топ MCP-серверов для автоматизации: браузер, Wordstat, WordPress, Figma
  6. Troubleshooting: красный статус, spawn ENOENT, ошибки JSON и логи Output
- **faq_hints:** как подключить mcp к cursor; какие mcp серверы лучше для cursor; почему mcp сервер не подключается в cursor
- **internal_links:** /avtomatizaciya-n8n-ai-agents/
- **cover_scene_hint:** ноутбук с IDE Cursor, вокруг экрана «кубики-плагины» MCP-серверов, стикеры Browser/WordPress/Wordstat, неоновый diy-коллаж

---

## B04 — GEO-оптимизация сайта под нейросети

- **priority:** P0
- **slug:** geo-optimizaciya-sajta-2026
- **h1:** Как настроить GEO-оптимизацию сайта: чек-лист для попадания в ответы нейросетей
- **primary_query:** geo оптимизация
- **secondary_queries:** geo оптимизация сайта, geo seo оптимизация, с чего начать geo оптимизацию, geo оптимизация контента
- **search_intent:** checklist
- **article_mode:** B
- **h2_outline:**
  1. GEO vs SEO: что меняется в 2026 и зачем оптимизировать под ChatGPT, Алису и Perplexity
  2. Аудит текущего присутствия: как проверить, цитирует ли вас нейровыдача
  3. Структура контента под извлечение ИИ: блоки 40–80 слов, FAQ, таблицы и заголовки
  4. Schema.org и технический доступ: FAQPage, Article, robots.txt для GPTBot и PerplexityBot
  5. Чек-лист GEO-оптимизации: 30+ пунктов с приоритетами (критично / важно / бонус)
  6. Мониторинг AI Share of Voice: как отслеживать цитирование и обновлять контент
- **faq_hints:** с чего начать geo оптимизацию; чем geo отличается от seo; как попасть в ответы яндекс нейро; нужна ли schema для geo
- **internal_links:** /primer-seo-stati/
- **cover_scene_hint:** экран сайта в центре, вокруг «пузыри-ответы» ChatGPT/Алиса/Perplexity со стрелками-цитатами, чек-лист на стикерах, блоки FAQ и schema, тёплый неоновый diy-коллаж

---

## B05 — Контент-завод на нейросетях

- **priority:** P0
- **slug:** avtonomnyj-kontent-zavod-nejroseti
- **h1:** Как создать автономный контент-завод на нейросетях: пошаговое руководство по автоматизации
- **primary_query:** контент завод
- **secondary_queries:** контент завод ии, автоматизация создания контента, как создать контент завод, контент завод для бизнеса
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Что такое контент-завод на нейросетях и почему ручной промптинг умер в 2026 году
  2. Архитектура автономного конвейера: связка Make.com, n8n и ИИ-агентов
  3. Настройка ИИ-сотрудников: роли исследователя, копирайтера и редактора (Newsroom)
  4. Автоматическая дистрибуция: автопостинг в Telegram, WordPress и социальные сети
  5. Экономика и ROI контент-завода: как снизить стоимость производства на 85%
- **faq_hints:** как создать контент завод; какие нейросети использовать для контент завода; сколько стоит запуск контент завода для бизнеса
- **internal_links:** /avtomatizaciya-n8n-ai-agents/
- **cover_scene_hint:** футуристический конвейер (завод), на ленте которого вместо деталей собираются светящиеся 3D-иконки постов, логотипы Telegram и WordPress, робот-манипулятор с кистью наносит неоновые надписи "AI Content", яркий diy-коллаж

---

## B06 — n8n MCP для Cursor

- **priority:** P0
- **slug:** n8n-mcp-server-cursor-podklyuchenie
- **h1:** Как подключить n8n к Cursor через MCP: пошаговая настройка Server Trigger и instance-level MCP
- **primary_query:** n8n mcp server
- **secondary_queries:** mcp server trigger n8n, n8n mcp cursor, подключить n8n к cursor mcp
- **search_intent:** how_to
- **article_mode:** B
- **wordstat_status:** недоступен (MCP `user-mcp-kv` / `wordstat_get_top_requests` отсутствует в Cloud run 2026-10-10; спрос подтверждён WebSearch + официальная документация n8n 2.33+ и тренд MCP Server Trigger в 2026)
- **h2_outline:**
  1. MCP Server Trigger vs instance-level MCP в n8n: что выбрать под Cursor
  2. Workflow с MCP Server Trigger: tool-ноды, Bearer-auth, test vs production URL
  3. Instance-level MCP: Enable workflows, OAuth/one-click setup для Cursor (Settings → Connect a client)
  4. Подключение в Cursor: `.cursor/mcp.json`, лимит tools и allowlist серверов
  5. Custom n8n Workflow Tool: как отдать готовый сценарий одним MCP-tool
  6. Troubleshooting: 401, пустой список tools, Claude Desktop через mcp-remote vs Cursor напрямую
- **faq_hints:** чем отличается mcp server trigger от instance mcp в n8n; какой url давать cursor production или test; можно ли подключить self-hosted n8n к cursor mcp
- **internal_links:** /podklyuchenie-mcp-cursor/, /avtomatizaciya-n8n-ai-agents/
- **cover_scene_hint:** n8n-нода «MCP Server» как розетка, от неё неоновые кабели к логотипам Cursor и Claude, стикеры Production URL / Bearer token, diy-коллаж на тёмном фоне

---

