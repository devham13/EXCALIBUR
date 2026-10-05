# QA: B06 ustanovka-n8n-docker-vps

date: 2026-10-05
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «n8n docker», FAQ 7, id-якоря на секциях |
| GEO / citability | 25 | 23 | Lead answer-first, TL;DR, таблица Caddy/nginx/Traefik, 7 FAQ, ol/ul чеклисты |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 за отсутствие рабочего internal href на B02 |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100, режим B без fake case |
| Fact safety | 15 | 13 | fact-check PASS; порты/метрики из docs n8n, не из fact-bank |
| Contract HTML | 10 | 6 | linter PASS после FIX; объём 8634 ✓; −4 за замену `<pre><code>` на blockquote (whitelist QA) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «n8n docker» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: self-host на VPS без DevOps-отдела |
| C04 | ✓ | Docker, webhook, reverse proxy — коротко при первом упоминании |
| O01 | ✓ | H2 совпадают с research-каркасом (8 секций + FAQ) |
| O02 | ✓ | VPS → compose → HTTPS → backup → checklist |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (шаги), ul (12 пунктов), table, blockquote-код |
| R01 | ✓ | TL;DR + схема деплоя, standalone блоки |
| R02 | ✓ | docs.n8n.io, n8n-hosting — с явными ссылками |
| R03 | ✓ | Нет неподтверждённых цен/процентов |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: один связный prod-трек (Postgres + HTTPS + webhook) |
| E02 | ✓ | «Делайте / Не делайте» в ключевых H2 |
| E03 | ✓ | CTA Make ×1, author kv-ai ×1, docs/github — без спама |
| Exp01 | ✓ | Режим B, без fake «я поднял на проде» |
| Exp02 | ✓ | Практический тон, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | MySQL 2.x, encryption key, `down -v`, firewall |
| Ept02 | ✗ | Internal href `/avtomatizaciya-n8n-ai-agents/` → 404 (статья B02 не на сайте) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0
- OK: github n8n-hosting, self-hosted-ai-starter-kit, kv-ai (×2), docs.n8n.io
- fix applied (cycle 1):
  - `<a href="/avtomatizaciya-n8n-ai-agents/">` → plain text «ИИ-агенты в n8n» (404 на PUBLIC_SITE_URL)
- **Перед publish:** восстановить href на опубликованный slug B02, повторить link-verify

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (compose/table — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 1 verified in fact-bank, 4 unverified — порты/сроки из tech context)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass, 0 issues (blog-dir scan)
- see `cannibalization-report.json`

## HTML linter (FIX cycle 1)

- Writer использовал `<pre><code>` / inline `<code>` по writing-contract; whitelist linter — без `pre`/`code`.
- Замена: inline `<code>` → `<b>`, блоки кода → `<blockquote>` с `<br>`.
- Verdict после правки: **PASS**

## Utility gate (article)

- PASS: 8 H2, 7 FAQ, 1 table, 14 numbered steps, 32 action markers
- see `utility-gate-report.json`
