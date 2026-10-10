# QA: B06 ustanovka-n8n-docker-vps-2026

date: 2026-10-10
score_total: 93/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2×5, FAQ 7, таблица VPS vs Cloud, 10 шагов + чеклист 12 — OK; −1 нет `<img>` с alt |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица, FAQ 7, blockquote-сниппеты .env/compose/Caddy |
| CORE-EEAT lite | 15 | 13 | 18/20 (см. ниже); −2 за временное снятие internal href (404 на kv-ai до publish B02/B03) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический how-to, Flesch RU 100 (упрощённый из-за списков/команд) |
| Fact safety | 15 | 14 | fact-check PASS; 3/8 чисел в fact-bank, остальное из docs/research (порты, Wordstat B02) |
| Contract HTML | 10 | 10 | linter PASS, объём 9559 ✓, CTA ≤3 ✓, whitelist tags ✓ |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title: установка n8n на VPS, Docker, HTTPS |
| C02 | ✓ | Lead — direct answer (webhook/HTTPS, стек) |
| C03 | ✓ | Аудитория: self-host без cloud-лимитов, DevOps-ready |
| C04 | ✓ | webhook, Compose, reverse proxy, runners — в тексте |
| O01 | ✓ | H2 = план B06 (VPS → Docker → compose → proxy → prod) |
| O02 | ✓ | 10 нумерованных шагов + финальный чеклист |
| O03 | ✓ | FAQ 7 пар по VPS/RAM/HTTPS/SQLite/runners/backup/update |
| O04 | ✓ | ol×2, ul чеклист, table, blockquote config |
| R01 | ✓ | TL;DR, FAQ, таблица, blockquote workflow |
| R02 | ✓ | 2.42.6, 4 GB RAM, 20 € Cloud — research/docs + дата 10.10.2026 |
| R03 | ✓ | Цены/версии с контекстом, без выдуманных % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: production-стек RU VPS + runners + N8N_PROXY_HOPS |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | OOM, DNS, encryption key, major Postgres upgrade |
| Ept02 | ✗ | Internal href B02/B03 сняты (HTTP 404 на EXCALIBUR_PUBLIC_SITE_URL); текст-заглушка до publish |

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

- site-base: EXCALIBUR_PUBLIC_SITE_URL (kv-ai.ru)
- total: 3, failed: 0
- OK: github n8n-hosting compose, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- **Перед publish:** вернуть href `/avtomatizaciya-n8n-ai-agents/` и `/podklyuchenie-mcp-cursor/` после публикации B02/B03 на kv-ai.ru

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 3 verified in fact-bank, 5 unverified — порты/Wordstat из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle (cycle 1)

1. **html-linter:** три блока `<pre><code>` → `<blockquote>` с `<br>` (whitelist tags).
2. **link-verify:** четыре относительных internal link → plain text «B02/B03, href после публикации на kv-ai.ru» (404 на production base; mayai.ru в href не использовался).

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- восстановить internal href после publish B02/B03 на kv-ai.ru

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
