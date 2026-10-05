# Research notes — B06 «Как установить n8n в Docker: пошаговая инструкция с PostgreSQL, доменом и HTTPS»

**topic_id:** B06  
**slug:** ustanovka-n8n-docker-vps  
**article_mode:** B (how-to)  
**research_date:** 2026-10-05  
**disclaimer:** Все даты, версии и статистика проверены на 05.10.2026.

---

## 1. SERP-обзор (WebSearch, приоритет; research-serp.json — дополнение)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [docs.n8n.io — Install with Docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | Официальная docs | Канон: `docker run`, PostgreSQL env, volume `/home/node/.n8n`, обновление compose | Минимум production (нет полного prod-стека в одном месте) | Копировать сырой `docker run` без Postgres для «прода» |
| 2 | [docs.n8n.io — Docker Compose + Traefik](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose) | Официальный tutorial | Traefik + TLS, `.env`, `docker compose up -d` | Только Traefik; мало troubleshooting | Структура 1:1 без адаптации под nginx/Caddy |
| 3 | [github.com/n8n-io/n8n-hosting](https://github.com/n8n-io/n8n-hosting) | Официальные шаблоны | `withPostgres`, queue mode, PostgreSQL 18, матрица зависимостей | Нужна сборка из шаблонов | Пин `latest` в проде |
| 4 | [virtua.cloud — n8n Docker Compose VPS 2026](https://www.virtua.cloud/learn/en/tutorials/install-n8n-docker-compose-vps) | Практический гайд | Postgres с healthcheck, pin версий, `127.0.0.1:5678`, лимиты RAM | SSL вынесен в отдельную статью | Жёсткие версии без пояснения «как обновить pin» |
| 5 | [rafftechnologies.com — self-host n8n Docker](https://rafftechnologies.com/learn/tutorials/self-host-n8n-docker) | Tutorial Ubuntu 24.04 | `N8N_WEBHOOK_URL`, `N8N_PROXY_HOPS=1`, deprecation `WEBHOOK_URL` | Фокус на nginx отдельно | Устаревший `WEBHOOK_URL` |
| 6 | [jacar.es — n8n self-hosted Docker](https://jacar.es/en/how-to-install-n8n-self-hosted-with-docker/) | Deep-dive compose | Postgres 18, external task runners, healthchecks | EN, узкая аудитория | Перегруз runners для MVP |
| 7 | [lumadock.com — nginx reverse proxy](https://lumadock.com/tutorials/n8n-nginx-reverse-proxy) | HTTPS/nginx | Bind localhost, forwarded headers, webhook vars | Без Postgres в статье | Публиковать 5678 на `0.0.0.0` |
| 8 | [purpleschool.ru — n8n Docker](https://purpleschool.ru/knowledge-base/docker/deploy/n8n) | RU база знаний | Русский язык, контекст self-host vs Cloud | Меньше prod-checklist | Дублировать без своих шагов |

**Паттерн SERP:** доминируют англоязычные «Complete 2026 Guide» (Docker Compose + Postgres + HTTPS). Официальные docs и `n8n-hosting` — эталон для версий БД и env. Русскоязычный слой тоньше; пробел — **один связный RU-гайд**: подготовка VPS → минимальный compose → prod (Postgres + proxy + webhook) → бэкап/обновление → чеклист, без «homelab-мемов».

**Intent:** `how_to` — развернуть self-hosted n8n на VPS через Docker Compose с PostgreSQL, вывести на домен с HTTPS, не потерять credentials при миграции/обновлении.

**Пробел для «Ковчег»:** практик no-code/DevOps-light: готовые фрагменты `.env` + `compose`, акцент на `N8N_ENCRYPTION_KEY` и бэкап, timezone `Europe/Moscow`, опционально AI Starter Kit — без ухода в «что такое n8n».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud run (namespace not found). Инструмент `wordstat_get_top_requests` не вызывался. **Точные показы на 05.10.2026 не получены — не выдумывать цифры в статье.**

Семантика для writer (из карточки B06 + secondary_queries, без объёмов):

| Фраза (приоритет) | Назначение в тексте |
|-------------------|---------------------|
| n8n docker | primary, H1/H2 |
| n8n docker compose | блок compose + команды |
| n8n установка | lead, подготовка VPS |
| n8n self hosted | сравнение с Cloud, мотивация |

**LSI (SERP + docs):** `N8N_ENCRYPTION_KEY`, `N8N_WEBHOOK_URL`, `N8N_PROXY_HOPS`, `docker compose`, `postgresdb`, Traefik/Caddy/nginx, `127.0.0.1:5678`, healthcheck, `export:entities`, self-hosted AI starter kit, Ollama, Qdrant.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n рекомендует Docker для большинства self-host сценариев | [docs.n8n.io/install-with-docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | 05.10.2026 | да |
| По умолчанию n8n в Docker использует SQLite; для prod — PostgreSQL через `DB_TYPE=postgresdb` и `DB_POSTGRESDB_*` | [docs.n8n.io/install-with-docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | 05.10.2026 | да |
| Volume `/home/node/.n8n` нужен даже с PostgreSQL (ключи шифрования, логи, SC assets) | [docs.n8n.io/install-with-docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | 05.10.2026 | да |
| Обновление compose: `docker compose pull` → `down` → `up -d` | [docs.n8n.io/install-with-docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | 05.10.2026 | да |
| `N8N_RUNNERS_ENABLED` deprecated с n8n 2.0 | [docs.n8n.io/install-with-docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | 05.10.2026 | да |
| MySQL/MariaDB как backend n8n deprecated с 1.0, удалены в 2.0 — только PostgreSQL (или SQLite) | [github.com/n8n-io/n8n-docs database.md](https://github.com/n8n-io/n8n-docs/blob/main/docs/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database.md) | 05.10.2026 | да |
| Официальные шаблоны: PostgreSQL **17 или 18**, **16** для совместимости; в templates — **18** | [github.com/n8n-io/n8n-hosting](https://github.com/n8n-io/n8n-hosting) | 05.10.2026 | да |
| Каталог compose: `withPostgres`, `withPostgresAndWorker`, `subfolderWithSSL`, `docker-caddy` | [github.com/n8n-io/n8n-hosting](https://github.com/n8n-io/n8n-hosting) | 05.10.2026 | да |
| Перед `docker compose up -d` в шаблоне withPostgres — сменить пароли в `.env` | [n8n-hosting/withPostgres README](https://github.com/n8n-io/n8n-hosting/blob/main/docker-compose/withPostgres/README.md) | 05.10.2026 | да |
| UI n8n по умолчанию на порту **5678** | [docs.n8n.io/install-using-docker-compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose) | 05.10.2026 | да |
| За reverse proxy: `N8N_WEBHOOK_URL` (заменяет deprecated `WEBHOOK_URL`), `N8N_PROXY_HOPS=1`, заголовки X-Forwarded-* на последнем proxy | [docs.n8n.io/webhook reverse proxy](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy) | 05.10.2026 | да |
| `N8N_ENCRYPTION_KEY` — шифрование credentials; смена/потеря ключа делает сохранённые credentials нечитаемыми | [selfhosted.study env reference](https://selfhosted.study/n8n/environment-variables/) | 05.10.2026 | да |
| Рекомендация генерировать ключ: `openssl rand -base64 32` | [selfhosted.study env reference](https://selfhosted.study/n8n/environment-variables/) | 05.10.2026 | да |
| Production-практика: bind `127.0.0.1:5678:5678`, HTTPS снаружи через nginx/Caddy/Traefik | [lumadock nginx tutorial](https://lumadock.com/tutorials/n8n-nginx-reverse-proxy) | 05.10.2026 | да |
| VPS для prod-стека n8n+Postgres: часто указывают **≥4 GB RAM** (virtua.cloud tutorial) | [virtua.cloud install n8n](https://www.virtua.cloud/learn/en/tutorials/install-n8n-docker-compose-vps) | 05.10.2026 | да (как рекомендация провайдера, не официальный минимум n8n) |
| Self-hosted AI Starter Kit: n8n + PostgreSQL + Ollama + Qdrant; CPU profile `docker compose --profile cpu up` | [github.com/n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) | 05.10.2026 | да |
| Starter Kit: n8n editor `localhost:5678`, Ollama `11434`, Qdrant `6333` | [self-hosted-ai-starter-kit README](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md) | 05.10.2026 | да |
| Self-hosted n8n снижает накладные расходы на медиа vs SaaS (контекст «Ковчег») | [mayai.ru n8n vs Make](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) + fact-bank | 2026-06-11 | да (контекст, не инструкция) |

**Не использовать без pin на дату релиза:** конкретные теги образов из сторонних гайдов (2.12.3, 2.38.5, 2.39.6) — в статье писать «pin актуальный stable-тег с Docker Hub / `docker.n8n.io` на дату деплоя», пример через переменную `N8N_VERSION`.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** с нуля поднять **production-ready** n8n на VPS: Docker Compose v2, PostgreSQL, persistent volumes, `.env` с секретами, reverse proxy + HTTPS, корректные webhook URL — и пройти **чеклист** перед открытием редактора в интернет.

**Отличие от конкурентов:** один RU-трек «сделай сам» с официальными env-именами (2.x webhook vars), явным блоком «не потерять encryption key», timezone Москва, опциональный AI Starter Kit без смешения с базовой установкой.

**H2-каркас (карточка B06 + SERP):**
1. Что подготовить (VPS, Docker Compose v2, домен, `N8N_ENCRYPTION_KEY`)
2. Минимальный compose: n8n + volume, первый запуск на localhost:5678
3. Production: PostgreSQL, healthchecks, pin версий
4. Домен и HTTPS (Traefik/Caddy/nginx — выбор + env)
5. Self-Hosted AI Starter Kit (опционально)
6. Обновление, бэкап `/home/node/.n8n` + Postgres, типовые ошибки
7. Чеклист перед продом

**Internal / conversion:** мягкая отсылка — если self-host не нужен, Cloud trial / Make (из fact-bank и editorial), без подмены how-to.

---

## 5. FAQ-кандидаты (5–7)

1. **Можно ли n8n только на SQLite в Docker?** — да для теста; для prod и нескольких пользователей — PostgreSQL с первого дня.
2. **Что будет, если не задать `N8N_ENCRYPTION_KEY`?** — ключ может сгенерироваться в volume; при пересоздании контейнера без volume/credentials — риск потери расшифровки; задайте ключ в `.env` и сохраните offline.
3. **Почему webhook приходят на http://localhost?** — не заданы `N8N_WEBHOOK_URL`, `N8N_HOST`, `N8N_PROTOCOL=https`, `N8N_PROXY_HOPS=1` за proxy.
4. **Как обновить n8n в compose?** — backup → `pull` → `down` → `up -d` → проверка `/healthz`.
5. **Нужен ли Redis?** — только для queue mode (`withPostgresAndWorker`); базовый single-instance — Postgres + n8n.
6. **MySQL в compose из старых гайдов?** — не использовать для n8n 2.x backend.
7. **Минимальный VPS?** — ориентир 2 vCPU / 4 GB для n8n+Postgres; AI Starter Kit — отдельно больше RAM/GPU.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «self-hosted n8n в Docker» 40–60 слов | Lead | Практический итог |
| Таблица env-переменных prod | H2 HTTPS | Имя / зачем / пример |
| Workflow подготовки | H2-1 | VPS → secrets → compose → proxy → check |
| Чеклист 10+ пунктов | Финал | utility gate статьи |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | schema agent | BlogPosting + FAQPage |

---

## 7. Риски для writer

- Не публиковать порт 5678 на `0.0.0.0` без proxy в prod-инструкции.
- Не использовать `WEBHOOK_URL` как primary — только `N8N_WEBHOOK_URL` (2.x).
- Версии образов — pin через `.env`, не `latest` в проде.
- Wordstat-цифры не писать до восстановления MCP.
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).
- Объём и стиль: `shared/quality-blog.md`, без эмодзи.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель на своём VPS поднимет n8n в Docker Compose с PostgreSQL, сохранит секреты и volumes, настроит домен с HTTPS и корректные webhook URL, выполнит бэкап и безопасное обновление — и пройдёт финальный чеклист перед production.

**action_outline (для writer):**

1. **Подготовить VPS:** Ubuntu 24.04 / Debian 12, установить Docker Engine + Compose plugin (`docker compose version`), DNS A-record на поддомен, сгенерировать `N8N_ENCRYPTION_KEY` (`openssl rand -base64 32`) и пароль Postgres — записать в password manager.
2. **Создать каталог проекта** и `.env` (без коммита в git): `POSTGRES_*`, `N8N_ENCRYPTION_KEY`, `N8N_VERSION` (pinned tag), `GENERIC_TIMEZONE=Europe/Moscow`, `TZ=Europe/Moscow`.
3. **Написать `docker-compose.yml`:** сервис `postgres` (healthcheck), сервис `n8n` с `DB_TYPE=postgresdb`, volumes `n8n_data` + `postgres_data`, ports `127.0.0.1:5678:5678`, `depends_on` с condition healthy.
4. **Запустить и проверить локально:** `docker compose up -d`, `docker compose ps`, открыть `http://127.0.0.1:5678`, создать owner account.
5. **Настроить reverse proxy** (nginx/Caddy/Traefik): TLS на домен, proxy на `127.0.0.1:5678`, forwarded headers; в n8n env: `N8N_HOST`, `N8N_PROTOCOL=https`, `N8N_WEBHOOK_URL=https://<domain>/`, `N8N_PROXY_HOPS=1`, `N8N_SECURE_COOKIE=true`.
6. **Проверить webhooks:** создать test workflow с Webhook node, убедиться что URL в UI — `https://`, внешний POST доходит.
7. **Настроить бэкап:** архив volume `/home/node/.n8n` + `pg_dump` Postgres по cron; отдельно backup файла `.env` с encryption key.
8. **Обновление:** backup → `docker compose pull` → `docker compose down` → `docker compose up -d` → smoke test `/healthz`.
9. **Опционально AI:** отдельный compose из [self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) с profile cpu/gpu — не смешивать с минимальным prod без нужды в Ollama/Qdrant.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
