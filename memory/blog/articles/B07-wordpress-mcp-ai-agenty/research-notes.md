# Research notes — B07 «Как подключить WordPress MCP Adapter: пошаговая инструкция для управления сайтом через AI»

**topic_id:** B07  
**slug:** wordpress-mcp-ai-agenty  
**article_mode:** B (how-to)  
**research_date:** 2026-06-21  
**disclaimer:** Все даты, версии и статистика проверены на 21.06.2026.

---

## 1. SERP-обзор (WebSearch, 21.06.2026, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | Официальный dev-blog (EN) | Канон: Abilities API, default-server, STDIO/HTTP, mcp.json для Cursor/Claude, security | Английский; для разработчиков плагинов; мало «бизнес без кода» | Сухой перевод без RU-сценариев для владельца сайта |
| 2 | [smartwp.com/wordpress-mcp/](https://smartwp.com/wordpress-mcp/) | Практический гайд 2026 (EN) | Пошаговый HTTP-setup, Application Password, security least-privilege, FAQ | EN; Pressable bias; нет связки с Cursor на русском | Коммерческий уклон managed host как «единственный путь» |
| 3 | [plugins.miniorange.com/ru/connect-wordpress-with-cursor-mcp-guide](https://plugins.miniorange.com/ru/connect-wordpress-with-cursor-mcp-guide) | RU how-to + Cursor | Единственный заметный RU-гайд «WordPress + Cursor»; готовый JSON для `@automattic/mcp-wordpress-remote` | Продаёт miniOrange; смешивает свой плагин и official adapter | Плагин miniOrange как обязательный шаг |
| 4 | [github.com/WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) | Официальный репозиторий | Releases v0.5.0, endpoint `/wp-json/mcp/mcp-adapter-default-server`, `meta.mcp.public` | README для dev; нет бизнес-кейсов | Техдок 1:1 без «на пальцах» |
| 5 | [wordpress.com/support/mcp/](https://wordpress.com/support/mcp/) | Док WordPress.com | OAuth 2.1, read/write toggles, role-based access, human confirmation на write | Только WordPress.com (Personal+); не self-hosted | Путать OAuth WordPress.com с Application Password на своём хостинге |
| 6 | [instawp.com/how-to-connect-ai-agents-to-wordpress-using-mcp/](https://instawp.com/how-to-connect-ai-agents-to-wordpress-using-mcp/) | Step-by-step EN | Cursor + Claude Code CLI + Gemini CLI в одном материале | Продаёт InstaWP sandbox; abilities provider как black box | Sandbox-only workflow без prod security |
| 7 | [zerotowp.com/connect-ai-agents-to-wordpress-mcp-setup](https://zerotowp.com/connect-ai-agents-to-wordpress-mcp-setup) | EN setup 2026 | Чётко: 6.9+, `meta.mcp.public`, STDIO vs HTTP, gotchas | EN; узкий dev-аудитория | Копировать структуру без RU и без human-in-the-loop |
| 8 | [mayai.ru/sajt-na-wordpress-nastrojka-mcp-dlya-avtomatizaczii-kontent-zavodov/](https://mayai.ru/sajt-na-wordpress-nastrojka-mcp-dlya-avtomatizacziya-kontent-zavodov/) | RU «контент-завод» | RU intent «подключить mcp к wordpress» | Общие слова про MCP; мало official adapter; риск устаревших команд | Контент-завод hype без security checklist |

**Паттерн SERP:** топ — официальный WordPress Developer Blog + EN-гайды 2026 (smartwp, zerotowp, instawp) + один RU-конкурент (miniOrange). Запрос «подключить mcp к wordpress» на русском почти не закрыт **официальным** how-to для **self-hosted** сайта с фокусом на **бизнес-задачи** (черновики, аудит контента, human-in-the-loop), а не на разработку плагинов.

**Intent:** how_to — владелец/маркетолог хочет **подключить** WordPress MCP Adapter, создать Application Password, прописать `.cursor/mcp.json`, увидеть tools в Cursor/Claude и **безопасно** дать агенту первые команды (discover abilities → черновик → проверка человеком). Вторичный intent: чем Abilities API отличается от «просто REST API» и что нужно для WordPress 6.9+.

**Пробел для Excalibur:** RU how-to для **B2B без бэкграунда разработчика**: официальный MCP Adapter + `@automattic/mcp-wordpress-remote` + Cursor; отдельный пользователь с минимальными правами; read-only на старте; связка с B03 (общий MCP в Cursor) и B04 (GEO-структура черновиков). Без kv-ai.ru, без курса Make как CTA.

**internal_links (карточка):**
- `/podklyuchenie-mcp-cursor/` — базовая настройка MCP в Cursor (B03); B07 = следующий шаг «подключить именно WordPress»
- `/geo-optimizaciya-sajta-2026/` — когда агент готовит черновик поста, применить GEO-чеклист перед публикацией

---

## 2. Яндекс Wordstat (user-mcp-kv, 21.06.2026)

⚠️ **WORDSTAT AUTH WARNING:** Токен Wordstat устарел / MCP `user-mcp-kv` недоступен в среде research (нет `YANDEX_WORDSTAT_TOKEN`). Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Точные объёмы спроса не получены.** Ниже — экспертная семантика по SERP, смежной теме B03 (`cursor mcp` = 630 показов/мес на 11.06.2026) и англоязычному intent; writer использует как LSI, **не как цифры в тексте**.

### Оценка семантики (не Wordstat)

| Фраза | Оценка спроса | Комментарий |
|-------|---------------|-------------|
| wordpress mcp | низкий / niche | EN-запрос; растёт с релизом 6.9 и dev-blog Feb 2026 |
| mcp adapter wordpress | очень низкий | Dev-intent, long-tail |
| подключить mcp к wordpress | низкий | RU how-to; мало качественных RU-страниц в топе |
| wordpress abilities api | очень низкий | Технический EN/RU mix |
| управление wordpress через ai | средний (широкий) | Конкуренция с обзорами AI-плагинов, не с MCP Adapter |
| cursor mcp wordpress | низкий | Пересечение с B03; B07 закрывает CMS-ветку |

### LSI для writer (SERP + official docs + B03)

- wordpress mcp adapter, abilities api, mcp-adapter-default-server  
- application password wordpress, `@automattic/mcp-wordpress-remote`, WP_API_URL  
- `.cursor/mcp.json`, Tools & MCP, npx, HTTPS  
- discover-abilities, execute-ability, meta.mcp.public  
- human-in-the-loop, read-only abilities, least-privilege user  
- черновик поста wordpress через ai, аудит контента, загрузка медиа  
- wordpress 6.9, wordpress 7.0 ai infrastructure  

**SEO-стратегия:** primary «wordpress mcp» + «mcp adapter wordpress» в H1/lead; RU «подключить mcp к wordpress» — в H2 и FAQ; «управление wordpress через ai» — в блок бизнес-сценариев, не в title целиком (риск каннибализации с обзорами плагинов).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Model Context Protocol (MCP) — открытый стандарт Anthropic для подключения AI к внешним системам | [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol) | 25.11.2024 | да |
| MCP анонсирован 25 ноября 2024 как open-source спецификация + SDK | [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol) | 25.11.2024 | да |
| WordPress 6.9 «Gene» выпущен **2 декабря 2025**; в core входит **Abilities API** | [wordpress.org/news/2025/12/gene](https://wordpress.org/news/2025/12/gene) | 02.12.2025 | да |
| Abilities API доступен только для **WordPress 6.9+** | [developer.wordpress.org/apis/abilities-api/](https://developer.wordpress.org/apis/abilities-api/) | 03.12.2025 | да |
| Abilities API: REST endpoints под namespace `wp-abilities/v1` (categories, abilities, run) | [make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/](https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/) | 10.11.2025 | да |
| WordPress 6.9 ships **3 core abilities**: `core/get-site-info`, `core/get-user-info`, `core/get-environment-info` | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| WordPress MCP Adapter — официальный пакет инициативы **AI Building Blocks for WordPress** | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| После активации adapter регистрирует default server **`mcp-adapter-default-server`** | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| HTTP endpoint default server: **`/wp-json/mcp/mcp-adapter-default-server`** | [github.com/WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) | 21.06.2026 | да |
| Adapter добавляет 3 meta-abilities: `discover-abilities`, `get-ability-info`, `execute-ability` | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| Abilities видны через MCP default server только при **`meta.mcp.public => true`** в `wp_register_ability()` | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| Для remote HTTP self-hosted: proxy **`@automattic/mcp-wordpress-remote`** + Application Password | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| Для local dev: STDIO через **WP-CLI** `wp mcp-adapter serve --server=mcp-adapter-default-server` | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| MCP Adapter **v0.5.0** — latest release (protocol DTO, spec 2025-11-25) | [github.com/WordPress/mcp-adapter/releases/tag/v0.5.0](https://github.com/WordPress/mcp-adapter/releases/tag/v0.5.0) | 15.04.2026 | да |
| Composer install: `composer require wordpress/abilities-api wordpress/mcp-adapter`; plugin path: clone в `wp-content/plugins/mcp-adapter` | [github.com/WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) | 21.06.2026 | да |
| Минимум для adapter (plugin docs): **PHP >= 7.4**, **WordPress >= 6.8**; Abilities API in core — **6.9+** | [github.com/WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) | 21.06.2026 | да |
| SmartWP: минимум **WordPress 6.9+** для Abilities API + MCP Adapter | [smartwp.com/wordpress-mcp/](https://smartwp.com/wordpress-mcp/) | 06.06.2026 | да |
| Application Password создаётся в **Users → Profile → Application Passwords**; показывается один раз | [smartwp.com/wordpress-mcp/](https://smartwp.com/wordpress-mcp/) | 06.06.2026 | да |
| Пароль Application Password вставлять **с пробелами**, как выдал WordPress | [github.com/Automattic/mcp-wordpress-remote](https://github.com/Automattic/mcp-wordpress-remote) | 21.06.2026 | да |
| WordPress.com MCP: feature на планах **Personal, Premium, Business, Commerce**; OAuth endpoint `https://public-api.wordpress.com/wpcom/v2/mcp/v1` | [wordpress.com/support/mcp/](https://wordpress.com/support/mcp/) | 20.05.2026 | да |
| WordPress.com: write-операции запрашивают **подтверждение**; удалённые посты в trash восстанавливаются **30 дней** | [wordpress.com/support/mcp/](https://wordpress.com/support/mcp/) | 20.05.2026 | да |
| Self-hosted: OAuth для MCP **пока нет**; auth через Application Passwords или JWT (Automattic remote) | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) (комментарий автора, Feb 2026) | 12.02.2026 | да (как community/author signal) |
| Security best practice: dedicated MCP user, minimum capability, read-only на старте, HTTPS only | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| MCP clients = logged-in WordPress users; каждый ability должен проверять `permission_callback` | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| Cursor: конфиг MCP в **Tools & MCP → Add Custom MCP** → `mcp.json`; формат как Claude Desktop | [developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/](https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/) | 04.02.2026 | да |
| Automattic `wordpress-mcp` plugin **сводится** к official `WordPress/mcp-adapter` (fresh install 2026 — official) | [smartwp.com/wordpress-mcp/](https://smartwp.com/wordpress-mcp/) | 06.06.2026 | да |
| Автономные ИИ-системы завершают **< 2,5%** сложных неструктурированных задач без человека; human-in-the-loop — стандарт | fact-bank / [REDACTED]/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/ | 11.06.2026 | да |

**fact-bank.md:** прямых строк про WordPress MCP нет; human-in-the-loop (< 2,5%) — из fact-bank. Остальные цифры — только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B, RU how-to для бизнеса)

**Главный угол:** за **30–60 минут** на **self-hosted WordPress 6.9+** установить official MCP Adapter, создать **отдельного пользователя** с Application Password, подключить сайт к **Cursor** через `@automattic/mcp-wordpress-remote`, выполнить первый цикл **discover → read-only audit → черновик поста → ручное одобрение** без публикации «в один клик».

**Почему отличается от конкурентов:**
- Official dev-blog — канон для разработчиков плагинов, не для маркетолога/владельца бизнеса.
- miniOrange RU — продаёт свой продукт; official adapter не выделен как единственный безопасный путь.
- smartwp/instawp — EN, без связки с уже опубликованным B03 (Cursor MCP) и B04 (GEO черновиков).
- Excalibur: **операционная безопасность** (отдельный user, read-only старт, human-in-the-loop) + **3 бизнес-сценария**: черновик из брифа, аудит старых постов, подготовка медиа/мета — не «новость про WordPress 7.0».

**Tone:** Abilities = «что сайт умеет делать, описанное для машины»; MCP Adapter = «переводчик между WordPress и AI-клиентом»; Application Password = «отдельный ключ, который можно отозвать, не меняя пароль входа».

**H2-каркас (карточка B07 + research):**
1. WordPress MCP в 2026: Abilities API, MCP Adapter, сценарии для бизнеса  
2. Требования: WP 6.9+, PHP 8.0+ (prod), HTTPS, Node.js/npx для remote bridge  
3. Подготовка: отдельный пользователь (Editor/Author), Application Password  
4. Установка MCP Adapter (plugin zip / Composer) + проверка endpoint  
5. Подключение Cursor: `.cursor/mcp.json` + `@automattic/mcp-wordpress-remote`  
6. Первые команды: discover abilities, get-site-info, черновик (draft only)  
7. Безопасность и troubleshooting: 401/403, security plugins, whitelist REST/MCP  
8. FAQ + чеклист перед prod  

**Conversion:** мягкий CTA AI-аудит / внедрение агентов (conversion-map); **не** kv-ai.ru; **не** курс Make. Internal: B03, B04.

---

## 5. Бизнес-сценарии (черновик для writer)

| Сценарий | Что просит агент | Роль user | Human-in-the-loop |
|----------|------------------|-----------|-------------------|
| Черновик из брифа | «Создай черновик поста по тезисам X, H2 как в брифе, статус draft» | Author или Editor | Человек правит текст + [GEO-чеклист](/geo-optimizaciya-sajta-2026/) перед publish |
| Аудит контента | «Покажи 10 самых старых постов в рубрике Y + title + дата» | Editor (read) | Человек решает, что обновлять |
| Мета и медиа | «Предложи alt-тексты для вложений в черновик Z» | Editor | Человек загружает/публикует медиа вручную на первом этапе |

**Важно writer:** на старте многие write-abilities **не exposed** без `meta.mcp.public` у плагинов; реалистичный MVP — **discover + core read abilities + черновик**, если установлен abilities provider (упомянуть без выдуманных имён плагинов; «проверьте список abilities после discover»).

---

## 6. Пример конфигурации (для writer, канон из official docs)

```json
{
  "mcpServers": {
    "wordpress-mcp-server": {
      "command": "npx",
      "args": ["-y", "@automattic/mcp-wordpress-remote@latest"],
      "env": {
        "WP_API_URL": "https://your-site.com/wp-json/mcp/mcp-adapter-default-server",
        "WP_API_USERNAME": "mcp-editor",
        "WP_API_PASSWORD": "xxxx xxxx xxxx xxxx xxxx xxxx"
      }
    }
  }
}
```

Перед prod: заменить placeholder URL; user не admin; HTTPS; после правки — **полный перезапуск Cursor** (см. miniOrange RU guide + B03).

---

## 7. FAQ-кандидаты (5–7)

1. **Что такое WordPress MCP Adapter?** — Official bridge между Abilities API и MCP; default server на `/wp-json/mcp/mcp-adapter-default-server`.  
2. **Какие версии WordPress нужны?** — Минимум **6.9** (Abilities API in core); adapter docs также упоминают WP 6.8+ с отдельным abilities-api plugin — writer: рекомендовать 6.9+.  
3. **Как подключить WordPress MCP к Cursor?** — Установить adapter → Application Password → блок в `.cursor/mcp.json` → Tools & MCP; детали базового MCP — [B03](/podklyuchenie-mcp-cursor/).  
4. **Чем MCP отличается от REST API?** — MCP описывает **discoverable tools** для AI-агента; REST — ручные HTTP-вызовы из кода.  
5. **Безопасно ли давать AI write-доступ?** — Только dedicated user, least privilege, draft + ручное одобрение; WordPress.com требует confirm на write.  
6. **Почему tools пустые / 401?** — Неверный Application Password, HTTP вместо HTTPS, security plugin блокирует `/wp-json/`, abilities без `meta.mcp.public`.  
7. **WordPress.com vs self-hosted?** — .com: OAuth + account MCP settings; self-hosted: Application Password + mcp-adapter plugin.

---

## 8. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение WordPress MCP 40–60 слов | Lead после H1 | «WordPress MCP — …» |
| Таблица STDIO vs HTTP | H2 transport | Когда local dev vs prod remote |
| Workflow A→B→C | H2 setup | Install adapter → password → mcp.json → discover → draft → human review |
| Таблица бизнес-сценариев | H2 use cases | Раздел 5 |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage + HowTo steps |

**Целевые формулировки:** «wordpress mcp», «mcp adapter wordpress», «подключить mcp к wordpress», «управление wordpress через ai».

---

## 9. Риски для writer

- Не выдумывать версии adapter/npx — на дату статьи: **v0.5.0** latest на GitHub.  
- Не обещать auto-publish: human-in-the-loop + fact-bank (< 2,5% автономности).  
- Не ссылаться на kv-ai.ru / mcp-kv.ru.  
- Не делать Make/n8n главным CTA (можно 1 абзац «фоновая автоматизация 24/7 — другой слой», без курса).  
- Различать **WordPress.com MCP** (OAuth) и **self-hosted** (Application Password) — отдельный callout.  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Каннибализация B03: B03 = общий MCP Cursor; B07 = только WordPress Adapter, со ссылкой «если MCP в Cursor ещё не настроен — начните с B03».

---

## 10. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель на self-hosted WordPress 6.9+ установит MCP Adapter, создаст отдельного пользователя с Application Password, пропишет `@automattic/mcp-wordpress-remote` в Cursor, увидит WordPress tools в Tools & MCP, выполнит discover abilities и безопасно получит черновик или аудит контента с обязательным ручным одобрением перед публикацией.

**action_outline (для writer):**

1. **Проверить версию WordPress** (6.9+) и HTTPS; убедиться, что REST API доступен (`/wp-json/` не блокируется firewall/security plugin).  
2. **Создать dedicated user** (Editor для контента или Author для своих черновиков); **не** использовать главный admin.  
3. **Сгенерировать Application Password** (Users → Profile → Application Passwords); сохранить пароль с пробелами; имя «Cursor MCP».  
4. **Установить MCP Adapter:** скачать release с GitHub или `composer require wordpress/mcp-adapter`; активировать; при необходимости `composer install` в папке плагина.  
5. **Проверить endpoint:** браузер/curl на `https://site/wp-json/mcp/mcp-adapter-default-server` (ожидаем auth challenge или JSON — не 404).  
6. **Настроить Cursor:** `.cursor/mcp.json` с `@automattic/mcp-wordpress-remote@latest`, `WP_API_URL`, `WP_API_USERNAME`, `WP_API_PASSWORD`; перезапуск Cursor; зелёный статус в Tools & MCP (см. [B03](/podklyuchenie-mcp-cursor/) при проблемах с MCP).  
7. **Первый read-only тест:** prompt «discover abilities» / «get site info»; убедиться, что агент вызывает MCP tools с подтверждением.  
8. **Первый write-тест (draft):** попросить черновик поста **без publish**; проверить в wp-admin; применить [GEO-чеклист](/geo-optimizaciya-sajta-2026/) перед публикацией.  
9. **Зафиксировать политику безопасности:** whitelist только нужных abilities; отозвать Application Password при компрометации; логи MCP/security plugins; read-only режим на первую неделю.

---

## 11. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ AUTH (семантика + LSI) |
| Таблица фактов с URL | ✅ (26 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| internal_links | ✅ `/podklyuchenie-mcp-cursor/`, `/geo-optimizaciya-sajta-2026/` |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B07 + `site-brief.md` + `conversion-map.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B07
article_dir: memory/blog/articles/B07-wordpress-mcp-ai-agenty
status: ✅ PASS
utility_verdict: PASS
wordstat: ⚠️ AUTH WARNING (семантика в §2; точные показы не получены)
summary: SERP — 8 конкурентов. Угол — RU how-to self-hosted WordPress 6.9+ + MCP Adapter + Cursor; 26 фактов, 9 шагов action_outline, 7 FAQ. internal_links: /podklyuchenie-mcp-cursor/, /geo-optimizaciya-sajta-2026/. Готов к writer.
===
