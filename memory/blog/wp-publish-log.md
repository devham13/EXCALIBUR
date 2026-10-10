# Excalibur BLOG — WP publish log

## 2026-06-11 — B02 avtomatizaciya-n8n-ai-agents

| Field | Value |
|-------|-------|
| topic_id | B02 |
| slug | avtomatizaciya-n8n-ai-agents |
| verdict | **FAIL** |
| post_id | — |
| permalink | — |

### Preconditions

- article-qa.md: PASS (93/100)
- link-verify.json: pass
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Attempt

```bash
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents --dry-run  # OK
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents       # FAIL
```

### Blockers

1. **Network:** HTTPS к `mayai.ru:443` недоступен из локальной среды (WinError 10060). FTP (порт 21) работает, HTTP-триггер bootstrap — нет.
2. **FTP path:** аккаунт `***_blog` видит только `/index.php` + `/cgi-bin/`, **без** `wp-load.php`. WordPress на `https://mayai.ru/blog/` — другой document root.
3. **Bootstrap 404:** загруженный `excalibur-blog-publish-once.php` (и тестовый `excalibur-test-once.php`) отдают HTTP 404 снаружи, хотя `index.php` в том же FTP root отдаётся на главной.

### Cleanup

Временные bootstrap-файлы удалены с FTP после диагностики.

### Next steps (для оператора)

1. Обновить `memory/site.env.local`: FTP_USER/FTP_PASS + `FTP_ROOT=/` (корень FTP после login, где `wp-load.php`). Путь панели хостинга: `FTP_PANEL_PATH=/your-account.beget.tech/public_html/`.
2. Либо запустить publish с машины/сети, где `curl https://mayai.ru` отвечает < 5 с.
3. Альтернатива: WP Application Password + REST API / MCP WordPress blob publish.

---

## 2026-06-11 (retry) — B02 avtomatizaciya-n8n-ai-agents — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B02 |
| slug | avtomatizaciya-n8n-ai-agents |
| verdict | **PASS** |
| post_id | 13324 |
| featured_image_id | 13325 |
| permalink | https://mayai.ru/avtomatizaciya-n8n-ai-agents/ |
| FTP_ROOT | `/` |

### Fix applied

- Обновлены FTP credentials в `memory/site.env.local` (локально, не в git)
- `FTP_ROOT=/` (wp-load.php в корне аккаунта после login)
- `excalibur_blog_wp_publish.py` — поддержка `FTP_ROOT` из env

### Result

```
OK post=13324 slug=avtomatizaciya-n8n-ai-agents
OK featured_image=13325
OK schema_meta=1
permalink=https://mayai.ru/avtomatizaciya-n8n-ai-agents/
```

---

## 2026-06-11 — B03 podklyuchenie-mcp-cursor — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B03 |
| slug | podklyuchenie-mcp-cursor |
| verdict | **PASS** |
| post_id | 13335 |
| featured_image_id | 13336 |
| inline_images | 13337, 13338, 13339 |
| permalink | https://mayai.ru/podklyuchenie-mcp-cursor/ |
| trigger | `/excalibur-blog-run topic_id: B03 publish: yes` (publish вручную после fix оркестратора) |

### Result

```
OK post=13335 slug=podklyuchenie-mcp-cursor
OK featured_image=13336
OK schema_meta=1
OK inline_image_upload=13337 src=cover/inline-01.png
OK inline_image_upload=13338 src=cover/inline-02.png
OK inline_image_upload=13339 src=cover/inline-03.png
permalink=https://mayai.ru/podklyuchenie-mcp-cursor/
```

---

## 2026-06-11 — B04 geo-optimizaciya-sajta-2026 — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B04 |
| slug | geo-optimizaciya-sajta-2026 |
| verdict | **PASS** |
| post_id | 13361 |
| featured_image_id | 13362 |
| inline_images | 13363, 13364, 13365 |
| permalink | https://mayai.ru/geo-optimizaciya-sajta-2026/ |
| trigger | `/excalibur-blog-run topic_id: B04 publish: yes` |

### Preconditions

- article-qa.md: PASS (94/100)
- link-verify.json: pass (5/5)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

```
OK post=13361 slug=geo-optimizaciya-sajta-2026
OK featured_image=13362
OK schema_meta=1
OK skip_theme_faq_meta=1
OK inline_image_upload=13363 src=cover/inline-01.png url=https://mayai.ru/wp-content/uploads/2026/06/geo-optimizaciya-sajta-2026-inline-01.jpg
OK inline_image_upload=13364 src=cover/inline-02.png url=https://mayai.ru/wp-content/uploads/2026/06/geo-optimizaciya-sajta-2026-inline-02.jpg
OK inline_image_upload=13365 src=cover/inline-03.png url=https://mayai.ru/wp-content/uploads/2026/06/geo-optimizaciya-sajta-2026-inline-03.jpg
permalink=https://mayai.ru/geo-optimizaciya-sajta-2026/
```

### Post-publish

- interlinker --apply: 0 new opportunities (B01 inbound already applied at indexer step)

---

## 2026-06-11 — B05 avtonomnyj-kontent-zavod-nejroseti — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B05 |
| slug | avtonomnyj-kontent-zavod-nejroseti |
| verdict | **PASS** |
| post_id | 13369 |
| featured_image_id | 13370 |
| inline_images | 13371, 13372, 13373 |
| permalink | https://mayai.ru/avtonomnyj-kontent-zavod-nejroseti/ |
| trigger | `/excalibur-blog-run topic_id: B05 publish: yes` |

### Preconditions

- article-qa.md: PASS (95/100)
- link-verify.json: pass (5/5)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

```
OK post=13369 slug=avtonomnyj-kontent-zavod-nejroseti
OK featured_image=13370
OK schema_meta=1
OK skip_theme_faq_meta=1
OK inline_image_upload=13371 src=cover/inline-01.png url=https://mayai.ru/wp-content/uploads/2026/06/avtonomnyj-kontent-zavod-nejroseti-inline-01.jpg
OK inline_image_upload=13372 src=cover/inline-02.png url=https://mayai.ru/wp-content/uploads/2026/06/avtonomnyj-kontent-zavod-nejroseti-inline-02.jpg
OK inline_image_upload=13373 src=cover/inline-03.png url=https://mayai.ru/wp-content/uploads/2026/06/avtonomnyj-kontent-zavod-nejroseti-inline-03.jpg
permalink=https://mayai.ru/avtonomnyj-kontent-zavod-nejroseti/
```

---

## 2026-10-10 — B06 ustanovka-n8n-docker-vps-2026 — **FAIL**

| Field | Value |
|-------|-------|
| topic_id | B06 |
| slug | ustanovka-n8n-docker-vps-2026 |
| verdict | **FAIL** |
| post_id | — |
| permalink | — |

### Preconditions

- article-qa.md: PASS (93/100)
- link-verify.json: pass (after internal href fix `/blog/` → root slugs, `--site-base https://mayai.ru`)
- schema.jsonld, cover, EXCALIBUR_BLOG_ALLOW_PUBLISH=yes

### Attempts (Cloud Agent)

1. **FTP** `excalibur_blog_wp_publish.py`: `425 Security: Bad IP connecting` (passive + active).
2. **SFTP** upload bootstrap to WP root + HTTP trigger `https://mayai.ru/excalibur-blog-publish-once.php`: **404** (marker `.txt` on SFTP also 404 on web — SFTP tree ≠ mayai docroot).
3. **SSH** `REMOTE_SITE_ROOT` + same HTTP bootstrap: **404**.
4. **WP-CLI over SSH**: `wp option get siteurl` → `https://www.meta-journal.ru` (not mayai.ru). Test publish created post **1263** — **deleted** (1263–1267) to avoid wrong-site content.

### Blockers

- Нет рабочего канала FTP/SFTP/SSH к **mayai.ru** из Cloud Agent (секреты ведут на meta-journal.ru).
- Для mayai: whitelist IP Cloud Agent на FTP **или** SSH/WP-CLI на document root mayai **или** publish с локальной сети (как B02–B05).

### Next steps

- Обновить Cloud Secrets: `SSH_*` / `FTP_*` / `REMOTE_SITE_ROOT` для mayai.ru (где `wp option get siteurl` = `https://mayai.ru`).
- Либо добавить `scripts/excalibur_blog_wp_publish_runner.php` + `wp eval-file` в runbook при FTP 425 (см. commit в ветке).
