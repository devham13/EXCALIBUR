# Research notes — B06 «Как установить n8n на VPS: Docker Compose, PostgreSQL, домен и HTTPS»

**topic_id:** B06  
**slug:** ustanovka-n8n-docker-vps-2026  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-10-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.10.2026 (Europe/Moscow).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [docs.n8n.io — Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose) | Официальный deploy | Postgres 18 + `PGDATA`, healthcheck, task runners, минимум 4 GB / 2 vCPU | Traefik-стек не для всех; мало про РФ-VPS и nginx/Caddy | Сухой перевод без чеклиста «перед продом» |
| 2 | [forestsnet.cloud — n8n self-hosted](https://forestsnet.cloud/ru/wiki/development/n8n-self-hosted) | RU wiki (сент. 2026) | Полный стек: Postgres 18, external runners, `N8N_PROXY_HOPS`, бэкапы | Привязка к хостингу ForestsNet | Копировать compose 1:1 без пояснения переменных |
| 3 | [virtua.cloud — Docker Compose VPS](https://www.virtua.cloud/learn/ru/tutorials/ustanovka-n8n-docker-compose-vps) | RU tutorial | Фиксированные версии, healthcheck, localhost bind 5678 | SSL/reverse proxy вынесен в другую статью | Обещание «15 минут» без учёта DNS/LE |
| 4 | [promtbaza.com — установка n8n](https://promtbaza.com/voprosy/ustanovka-n8n-na-vps) | RU how-to (2026) | One-liner, цены VPS, Community edition | Смешение версий/маркeting («n8n 3.0 октябрь» — перепроверить writer) | Непроверенные прайсы VPS без даты |
| 5 | [meta-journal.ru — n8n docker VPS](https://www.meta-journal.ru/2026/10/05/ustanovka-n8n-docker-vps/) | RU свежий (окт 2026) | PostgreSQL, HTTPS, webhook, типовые ошибки 502/cookie | Пересекается с другими материалами meta-journal | Дублировать серию «agents/queue» (отдельные темы) |
| 6 | [easylinklife.com — n8n 2.0 VPS](https://easylinklife.com/blog/kak-razvernut-n8n-2-0-na-vps-secure-by-default-avtomatizacziya-2026/) | RU longread | Secure-by-default, docker-compose, обновления | Affiliate-хостинг | Структура 1:1 |
| 7 | [unihost.com — Traefik + Postgres](https://unihost.com/help/ru/deploying-n8n-with-postgresql-and-traefik-automatic-https-via-lets-encrypt/) | FAQ хостера | Traefik v3 + Let's Encrypt HTTP challenge | Postgres 16, не 18; `latest` tag | `n8nio/n8n:latest` в проде без pin |
| 8 | [ssdnodes.com — Docker HTTPS (RU)](https://www.ssdnodes.com/learn/lang/ru/self-host-n8n-vps-docker-https) | RU guide | A-запись, порты 80/443, `127.0.0.1:5678`, `N8N_PROXY_HOPS` | Англоязычный первоисточник, RU-локализация | Жёстко зашитый домен в примере |

**Паттерн SERP:** доминируют пошаговые RU-гайды «Docker Compose + PostgreSQL + HTTPS за 30–40 мин» (октябрь 2026). Официальная документация задаёт канон по **Postgres 18**, **external task runners** и **4 GB RAM**. Отдельный кластер — self-hosted для РФ (оплата, данные на VPS). Видео (Rutube) и обзоры «n8n + LLM» не закрывают production-чеклист.

**Intent:** `how_to` — развернуть **рабочий** self-hosted n8n с HTTPS и PostgreSQL на VPS, чтобы вебхуки (Telegram, CRM, MCP) работали стабильно. Вторичный intent: runners после n8n 2.x, бэкап `.env` + БД, обновление без потери credentials.

**Пробел для блога «Ковчег»:** связка **VPS в РФ / данные у себя** → **готовая база под ИИ-агентов** (internal link B02, B03), честный чеклист prod (encryption key, webhook URL, не открывать 5678), без пересказа «что такое n8n».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** namespace `user-mcp-kv` / `wordstat_get_top_requests` **недоступен** в Cloud run 2026-10-10. Точные показы по `primary_query` «установка n8n на vps» **не получены** — цифры ниже не выдумываются.

**SERP-fallback (косвенный спрос, research B02 от 11.06.2026 — только LSI, не заменяет Wordstat по primary):**

| Фраза (смежная) | Показы/мес | Источник |
|-----------------|------------|----------|
| n8n | 37 115 | B02 research-notes, Wordstat 11.06.2026 |
| n8n docker | 498 | B02 research-notes |
| n8n установка | 364 | B02 research-notes |
| n8n self hosted | (в топе SERP, без цифры) | WebSearch 10.10.2026 |

**LSI для writer (SERP + docs, без выдуманных частот):**

- установка n8n на vps, n8n docker compose postgresql  
- n8n self hosted россия, vps россия данные  
- n8n ssl домен webhook, `N8N_WEBHOOK_URL`, Let's Encrypt  
- n8n task runners docker, `n8nio/runners`, external mode  
- reverse proxy nginx caddy traefik, `N8N_PROXY_HOPS`  
- `N8N_ENCRYPTION_KEY`, бэкап postgres, обновление docker compose  

**SEO-стратегия:** primary «установка n8n на vps» в H1/lead; head «n8n docker» / «n8n установка» через H2; secondary из карточки темы + LSI выше.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Рекомендуемый способ self-host: **Docker Compose** (plain `docker run` помечен outdated) | [Install with Docker](https://docs.n8n.io/hosting/installation/docker/) | 10.10.2026 | да |
| Текущий **stable** образ n8n: **2.42.6**; **beta**: 2.43.3 | [Install with Docker](https://docs.n8n.io/hosting/installation/docker/) | 10.10.2026 | да |
| Для Docker Compose: минимум **4 GB RAM** и **2 vCPU** (sandbox/runners — больше headroom) | [Install using Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose) | 10.10.2026 | да |
| Официальный пример **Postgres 18** + `PGDATA=/var/lib/postgresql/data` для стабильного volume | [n8n-hosting withPostgres](https://github.com/n8n-io/n8n-hosting/blob/main/docker-compose/withPostgres/docker-compose.yml) | 10.10.2026 | да |
| Major upgrade Postgres 18 на существующих данных требует **pg_dumpall** / миграции, иначе incompatible data dir | [Install using Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose) | 10.10.2026 | да |
| Production БД: `DB_TYPE=postgresdb` + host/port/user/password; SQLite по умолчанию только для dev | [Install with Docker](https://docs.n8n.io/hosting/installation/docker/) | 10.10.2026 | да |
| Том `/home/node/.n8n` нужен даже с Postgres (ключи шифрования, логи, SC assets) | [Install with Docker](https://docs.n8n.io/hosting/installation/docker/) | 10.10.2026 | да |
| `N8N_ENCRYPTION_KEY` — custom key для credentials; в queue mode **одинаковый на всех workers** | [Set a custom encryption key](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key) | 10.10.2026 | да |
| За reverse proxy: `N8N_WEBHOOK_URL=https://домен/` + `N8N_PROXY_HOPS=1` + X-Forwarded-* на прокси | [Configure webhook URLs with reverse proxy](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy) | 10.10.2026 | да |
| `WEBHOOK_URL` deprecated с **n8n 2.35.0** → использовать `N8N_WEBHOOK_URL` | [Endpoints env](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints) | 10.10.2026 | да |
| n8n **2.0**: task runners **включены по умолчанию**; `N8N_RUNNERS_ENABLED` deprecated | [v2.0 Breaking changes](https://docs.n8n.io/changelog/v20-breaking-changes) | 10.10.2026 | да |
| С **n8n 2.0** runner для external mode — отдельный образ **`n8nio/runners`**, версия = версии n8n | [v2.0 Breaking changes](https://docs.n8n.io/changelog/v20-breaking-changes) | 10.10.2026 | да |
| External mode: `N8N_RUNNERS_MODE=external`, `N8N_RUNNERS_AUTH_TOKEN`, broker `0.0.0.0`, sidecar `N8N_RUNNERS_TASK_BROKER_URI=http://n8n:5679` | [Set up task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners) | 10.10.2026 | да |
| Образ registry: `docker.n8n.io/n8nio/n8n:${N8N_VERSION}` в официальном compose | [n8n-hosting withPostgres](https://github.com/n8n-io/n8n-hosting/blob/main/docker-compose/withPostgres/docker-compose.yml) | 10.10.2026 | да |
| Официальный cloud VPS stack: **Traefik** + TLS + `N8N_HOST`, `N8N_PROTOCOL=https`, `N8N_WEBHOOK_URL` | [Use Docker Compose (cloud provider)](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose) | 10.10.2026 | да |
| Self-hosted **Community edition** — бесплатно, «almost complete feature set», без cloud execution limits | [Choose how to use n8n](https://docs.n8n.io/choose-how-to-use-n8n) | 10.10.2026 | да |
| Регистрация CE по email (бесплатно) unlock: folders, debug in editor, custom execution data | [Compare editions](https://docs.n8n.io/deploy/host-n8n/community-edition-features) | 10.10.2026 | да |
| n8n Cloud Starter от **20 €/мес** (2 500 executions) — для comparison «своё vs облако» | [n8n.io/pricing](https://n8n.io/pricing/) | 10.10.2026 | да |
| **npm install deprecated с n8n 3.0** (self-host через Docker) | [Host n8n](https://docs.n8n.io/deploy/host-n8n) | 10.10.2026 | да |
| OOM на self-host: увеличить RAM или `NODE_OPTIONS=--max-old-space-size` | [Fix memory issues](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues) | 10.10.2026 | да |
| Порт UI по умолчанию **5678**; в prod bind **127.0.0.1:5678** + прокси 443 | [ssdnodes RU guide](https://www.ssdnodes.com/learn/lang/ru/self-host-n8n-vps-docker-https) | 10.10.2026 | да (практика + согласуется с docs proxy) |
| Virtua tutorial: минимум **4 GB RAM**, Ubuntu 24.04 / Debian 12, плагин `docker compose` | [virtua.cloud tutorial](https://www.virtua.cloud/learn/ru/tutorials/ustanovka-n8n-docker-compose-vps) | 10.10.2026 | да |

**Не использовать без перепроверки на дату публикации:** «n8n 3.0 только Docker в октябре 2026» (promtbaza/meta-journal) — сверить с [Host n8n](https://docs.n8n.io/deploy/host-n8n) и changelog; конкретные ₽/мес VPS из affiliate-статей.

**Fact-bank (mayai.ru):** self-hosted n8n vs SaaS — снижение накладных на медиа, маржа контент-производства до 35% ([mayai.ru comparison](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/)) — только как контекст «зачем VPS», не как технический шаг установки.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** читатель за один проход поднимает **production-ready** стек на VPS: Docker Compose, **PostgreSQL 18**, **external task runners**, reverse proxy (**Nginx или Caddy** — writer выбирает один путь), **HTTPS**, корректные **`N8N_WEBHOOK_URL` / `N8N_PROXY_HOPS`**, сохранённые секреты и план бэкапа.

**Отличие от конкурентов:**
- Явный **чеклист перед продом** (ключ шифрования, не публиковать 5678, pin версии образов).
- Контекст **РФ**: VPS в РФ, данные workflows/credentials на своём железе, мост к **ИИ-агентам** (B02) и **MCP** (B03) — без повторения настройки агентов.
- Опора на **официальный n8n-hosting/withPostgres** + docs 2.42.x, а не только affiliate-compose.

**Tone:** инструкция для админа/техничного фрилансера; термины webhook, reverse proxy, volume — с коротким «на пальцах» в lead или FAQ.

**H2-каркас (из карточки + research):**
1. Требования VPS (4 GB+, Ubuntu 24.04, домен A→IP, порты 80/443)
2. Docker + каталог `/opt/n8n`, `.env`, генерация `N8N_ENCRYPTION_KEY` и пароля Postgres
3. `docker-compose.yml`: Postgres 18, n8n pin version, healthcheck, external runners
4. Reverse proxy + Let's Encrypt, env для HTTPS и webhooks
5. Чеклист prod: бэкап, обновление `docker compose pull`, типовые ошибки (502, secure cookie)

**Internal links (карточка):** `/avtomatizaciya-n8n-ai-agents/`, `/podklyuchenie-mcp-cursor/`

**Cannibalization:** не дублировать B02 (AI Agent node), B03 (MCP Cursor), отдельные материалы про n8n agents-only / queue mode deep-dive — только упоминание runners как обязательной части 2.x install.

---

## 5. FAQ-кандидаты (5–7)

1. **Сколько RAM нужно для n8n на VPS?** — от 4 GB / 2 vCPU по docs; при Code node и runners — мониторить OOM, масштабировать RAM.
2. **Можно ли n8n бесплатно на своём VPS?** — да, Community edition; платите только хостинг и API внешних сервисов.
3. **Почему вебхуки не работают без HTTPS?** — внешние сервисы требуют публичный HTTPS URL; задайте `N8N_WEBHOOK_URL` и прокси.
4. **SQLite или PostgreSQL?** — Postgres для prod; SQLite только для тестов.
5. **Зачем отдельный контейнер `n8nio/runners`?** — с 2.0 изоляция Code node; версия runner = версии n8n.
6. **Что обязательно бэкапить?** — `.env` (encryption key), volume Postgres, volume `/home/node/.n8n`.
7. **Как обновить без потери данных?** — `docker compose pull`, `down`, `up -d`; не менять `N8N_ENCRYPTION_KEY`; миграции Postgres major — по docs.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение self-hosted n8n 40–60 слов | Lead | «Self-hosted n8n — …» |
| Workflow-схема | H2-4 | DNS → proxy:443 → n8n:5678 → Postgres + runners |
| Чеклист prod 10+ пунктов | H2-5 | Маркированный список действий |
| FAQ 5–7 | Конец | Короткие ответы-действия |
| Таблица «VPS vs n8n Cloud» (3–4 строки) | Опционально H2-1 | Сравнение без water |

**Целевые формулировки:** «установка n8n на vps», «n8n docker compose postgresql», «n8n webhook https», «n8n task runners docker».

---

## 7. Риски для writer

- Pin **версию** образа (`2.42.6` или актуальный stable на дату publish), не `latest` в prod.
- Все секреты — из `.env`, не в article.html в открытом виде (плейсхолдеры).
- Объём и quality: `shared/quality-blog.md`; min **5 нумерованных шагов** + **чеклист 10+** (utility gate статьи).
- Не обещать «30 минут», если включены DNS propagation и LE.
- CTA на услуги «Ковчег» ≤ 3, не подменяют инструкцию.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель развернёт на VPS self-hosted n8n с Docker Compose, PostgreSQL, HTTPS и корректными webhook URL, сохранит ключ шифрования и бэкапы — и сможет перейти к настройке ИИ-агентов и интеграций без облачных лимитов n8n Cloud.

**action_outline (для writer):**

1. **Выбрать VPS** (≥4 GB RAM, 2 vCPU, Ubuntu 24.04), привязать домен A-записью, открыть 80/443, закрыть публичный 5678.
2. **Установить Docker Engine + Compose plugin** (`docker compose version`).
3. **Создать `/opt/n8n`**, сгенерировать `.env`: Postgres credentials, `N8N_ENCRYPTION_KEY`, `N8N_RUNNERS_AUTH_TOKEN`, `N8N_VERSION`, timezone, домен.
4. **Написать `docker-compose.yml`** по официальному withPostgres: Postgres 18 + healthcheck, n8n с `DB_*`, external runners sidecar, named volumes.
5. **Запустить** `docker compose up -d`, проверить health (`pg_isready`, UI на localhost:5678).
6. **Настроить reverse proxy** (Caddy или Nginx) + Let's Encrypt; выставить `N8N_HOST`, `N8N_PROTOCOL=https`, `N8N_WEBHOOK_URL`, `N8N_PROXY_HOPS=1`.
7. **Создать owner-пользователя**, зарегистрировать CE (Settings → Usage) при необходимости folders/debug.
8. **Smoke-test webhook:** test URL → production URL, триггер с внешнего сервиса (Telegram/HTTP).
9. **Зафиксировать бэкап-ритуал:** `.env` offsite, `pg_dump` cron, документировать версию образа перед `compose pull`.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (SERP + B02 LSI) |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
