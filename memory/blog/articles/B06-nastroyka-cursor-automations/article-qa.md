# QA: B06 nastroyka-cursor-automations

date: 2026-09-11
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2×8, primary query «cursor automations», FAQ 7, 2 таблицы, 3 ol — OK; −1 за отсутствие Wordstat-цифр в meta |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы (режимы/triggers), FAQ 7, чек-лист 12 пунктов |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 4 unverified duration/number в fact-check (не blocker) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический how-to тон, Flesch RU 100 (короткие предложения) |
| Fact safety | 15 | 13 | fact-check PASS; 1/5 verified in fact-bank; цены Pro $20 и дата 05.03.2026 из research-notes/docs |
| Contract HTML | 10 | 8 | linter PASS, объём 9099 ✓, CTA ≤3 ✓, internal href ×4; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «cursor automations» / «настройка cursor automations» |
| C02 | ✓ | Lead — direct answer (30–45 мин, cron/webhook), без «в этой статье» |
| C03 | ✓ | Аудитория: маркетолог, автоматизатор, бизнес без Senior-разработчика |
| C04 | ✓ | MCP, cron, webhook, on-demand, spend limit — «на пальцах» |
| O01 | ✓ | H2 совпадают с планом B06 (8 секций + FAQ) |
| O02 | ✓ | Outline: сравнение режимов → billing → создание → cron → webhook → MCP → чек-лист → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research (repo, cron MSK, цена, webhook key, GitHub, Projects) |
| O04 | ✓ | ol (3 блока, 15 шагов), ul (12 пунктов чек-листа), 2 table |
| R01 | ✓ | TL;DR + workflow blockquote + рекомендации «Делайте/Не делайте» в H2 |
| R02 | ✓ | Дата релиза 05.03.2026, Pro $20, CRON_TZ — с research-notes + cursor.com/docs |
| R03 | ✓ | Цены с контекстом billing; Wordstat отсутствует — явный disclaimer в blockquote эксперта |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый RU how-to (cron + webhook + Make/n8n), не фрагментированные EN tutorials |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×2, @maya_pro ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case «я настроил за выходные» |
| Exp02 | ✓ | Тон research/brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: on-demand, fork PR, региональный доступ, spend limit |
| Ept02 | ✗ | Internal links B03/B05 — 200 на live site ✓; −1 за отсутствие третьей internal из карточки (B02 не вставлен) |

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

- total: 7, failed: 0
- OK: /podklyuchenie-mcp-cursor/, /avtonomnyj-kontent-zavod-nejroseti/, cursor.com/automate, cursor.com/docs/cloud-agent/automations, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, t.me/maya_pro

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/списки — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 1 verified in fact-bank, 4 unverified — durations/400 words/cron expr, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` ×3 → `<blockquote>` (html-linter FAIL → PASS); cannibalization — корректный вызов `--blog-dir` + `-o`

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Pro $20 и дату релиза Automations в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
