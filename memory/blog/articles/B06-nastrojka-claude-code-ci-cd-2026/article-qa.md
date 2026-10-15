# QA: B06 nastrojka-claude-code-ci-cd-2026

date: 2026-09-12
score_total: 93/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×8, primary query «claude code ci cd», FAQ 7 пар, ol/ul, таблица сравнения Action vs headless |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 YAML-примера в blockquote, FAQ 7, чеклист 10+ guardrails |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, технический тон без штампов |
| Fact safety | 15 | 14 | fact-check PASS; 1/1 год 2026 верифицирован в fact-bank; beta GitLab – из docs Anthropic |
| Contract HTML | 10 | 5 | linter PASS после fix cycle; объём ~9583 (чуть выше 9500); CTA ≤3 ✓; internal href ×4; −5 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code ci cd» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: DevOps/разработчики, настраивающие CI/CD |
| C04 | ✓ | CI/CD, headless, MCP, `--bare` — расшифрованы в контексте |
| O01 | ✓ | H2 совпадают с research action_outline (8 секций + FAQ) |
| O02 | ✓ | Outline: выбор → секреты → GitHub → headless → GitLab → hardening → debug → next |
| O03 | ✓ | FAQ 7 пар, queries из research/SERP |
| O04 | ✓ | ol (5+5+5+5 шагов), ul (10 guardrails), 1 table |
| R01 | ✓ | TL;DR + workflow blockquote + YAML-примеры |
| R02 | ✓ | GitLab beta, `--max-budget-usd` v2.1.217+, install.sh — из research-notes |
| R03 | ✓ | Нет выдуманных процентов/цен; Wordstat не подставлялся |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: GitHub Action + headless + GitLab beta + security checklist в одном how-to |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: beta GitLab, pull_request_target, bot loops, budget caps |
| Ept02 | ✓ | Internal links B03, B02 (×2 каждый) — 200 на mayai.ru |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 4, failed: 0
- OK: /podklyuchenie-mcp-cursor/, /avtomatizaciya-n8n-ai-agents/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- **site-base:** `https://mayai.ru` (статьи B02/B03 опубликованы на mayai.ru; `PUBLIC_SITE_URL` kv-ai.ru даёт 404 на relative slugs)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (blockquote/YAML-блоки — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (1 extracted, 1 verified in fact-bank)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- **Cycle 1:** `<pre><code>` YAML-примеры (GitHub Actions, GitLab CI) заменены на `<blockquote>` с `<br>` — html-linter FAIL → PASS (теги `<pre>/<code>` вне whitelist контракта linter).

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- укоротить plain-text до ≤9500 символов при следующем рерайте

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
