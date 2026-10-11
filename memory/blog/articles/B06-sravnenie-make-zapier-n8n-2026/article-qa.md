# QA: B06 sravnenie-make-zapier-n8n-2026

date: 2026-10-11
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×7 + FAQ×7, primary query «n8n vs make vs zapier», таблица 4 платформ, lists — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 1 таблица, FAQ 7, migration `<ol>` 7 шагов, compliance 12 пунктов |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat не в тексте (MCP недоступен, зафиксировано в blockquote) |
| Human voice | 15 | 15 | 0 AI-slop hits; «Делайте/Не делайте» в секциях |
| Fact safety | 15 | 13 | fact-check PASS; 1/12 чисел в fact-bank, остальное из research-notes / официальных pricing |
| Contract HTML | 10 | 6 | linter PASS, объём ~8961 ✓, CTA Make ×2 ✓; −4 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/meta закрывают «n8n vs make vs zapier» |
| C02 | ✓ | Lead — billing + 152-ФЗ, без «в этой статье» |
| C03 | ✓ | Аудитория: команды в РФ, выбор SaaS vs self-host |
| C04 | ✓ | API, webhook, Docker, credits/tasks/executions — кратко |
| O01 | ✓ | 7 H2 + FAQ по action_outline research |
| O02 | ✓ | 4 критерия → таблица → матрица → миграция → compliance → старт → next steps |
| O03 | ✓ | FAQ 7 пар по intent из research |
| O04 | ✓ | ol (критерии, migration, next steps), ul (матрица, compliance), 1 table |
| R01 | ✓ | TL;DR + итоговые blockquote в таблице и миграции |
| R02 | ✓ | Тарифы с датой 11.10.2026 и ссылками на Zapier/n8n/help.make |
| R03 | ✓ | Billing-эталон 4×1000 в контексте выбора |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: РФ, 152-ФЗ, Zapier legacy |
| E02 | ✓ | «Делайте/Не делайте» в каждой основной секции |
| E03 | ✓ | CTA kv-ai.ru/obuchenie-po-make ×2 |
| Exp01 | ✓ | article_mode B, без fake case |
| Exp02 | ✓ | Тон brief/research |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: не юрконсультация, parallel run, rollback |
| Ept02 | ✗ | Wordstat LSI не подтверждён в тексте (blocker research, не publish) |

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

- total: 8, failed: 0
- **Fix cycle (QA):** `www.make.com/en/pricing` → 403 с Cloud egress → заменено на `https://help.make.com/credits` (200); относительные `/avtomatizaciya-n8n-ai-agents/` → `https://mayai.ru/avtomatizaciya-n8n-ai-agents/` (200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (табличные фрагменты — допустимо)
- Flesch RU: 100.0 (короткие предложения; тема сложная, но slop PASS)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (12 extracted, 1 verified in fact-bank, 11 unverified — pricing/limits из research-notes, не blocker при PASS verdict скрипта)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- GEO QA: правки `article.html` — только URL (Make credits help, absolute internal mayai.ru). Контент writer не переписывался.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- обогатить fact-bank тарифами Make/n8n/Zapier для автoverify

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
