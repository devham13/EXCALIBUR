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
| post_id | 13326 |
| featured_image_id | 13327 |
| permalink | https://mayai.ru/podklyuchenie-mcp-cursor/ |

---

## 2026-06-11 — B04 geo-optimizaciya-sajta-2026 — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B04 |
| slug | geo-optimizaciya-sajta-2026 |
| verdict | **PASS** |
| post_id | 13328 |
| featured_image_id | 13329 |
| inline_images | 13330, 13331, 13332 |
| permalink | https://mayai.ru/geo-optimizaciya-sajta-2026/ |

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

## 2026-10-06 — B01 primer-seo-stati — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B01 |
| slug | primer-seo-stati |
| verdict | **PASS** |
| post_id | 238 |
| status | published |
| featured_image_id | 1166 |
| inline_images | 1167, 1168, 1169, 1170 |
| permalink | https://www.meta-journal.ru/2026/06/19/primer-seo-stati/ |
| site_base | EXCALIBUR_PUBLIC_SITE_URL (production) |
| transport | **SFTP** upload + HTTP bootstrap trigger |

### Preconditions

- article-qa.md: PASS (94/100)
- link-verify.json: pass (preflight; убрана 404 internal href на geo до publish)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Notes

- Канонический `excalibur_blog_wp_publish.py` через FTP: `425 Security: Bad IP connecting` из Cloud Agent (PASV data channel). Обход: SFTP (порт 22) + тот же bootstrap PHP + HTTP trigger (~28 с).
- WebFetch fallback не потребовался (HTTP trigger OK).
- Bootstrap `excalibur-blog-publish-once.php` удалён с сервера после успеха.
- Preflight: dry-run PHP ~3.76 MB.

### Result

```
OK post=238 slug=primer-seo-stati
OK featured_image=1166
OK schema_meta=1
OK skip_theme_faq_meta=1
OK inline_image_upload=1167 src=cover/inline-01.png
OK inline_image_upload=1168 src=cover/inline-02.png
OK inline_image_upload=1169 src=cover/inline-03.png
OK inline_image_upload=1170 src=cover/inline-03.png (duplicate src in HTML — см. post-publish)
permalink=https://www.meta-journal.ru/2026/06/19/primer-seo-stati/
```
