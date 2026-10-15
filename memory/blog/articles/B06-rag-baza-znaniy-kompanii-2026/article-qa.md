# QA: B06 rag-baza-znaniy-kompanii-2026

date: 2026-09-11
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | 8 H2, primary query «rag база знаний», FAQ 7, чеклист 12 + 8 шагов пилота — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, схема pipeline, таблица стека, prompt blockquote, FAQ 7 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial tone |
| Fact safety | 15 | 13 | fact-check PASS; 1/8 чисел в fact-bank (Wordstat/пороги из research-notes) |
| Contract HTML | 10 | 8 | linter PASS, объём 8601 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «rag база знаний» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: владельцы/IT-lead, пилот без команды dev |
| C04 | ✓ | RAG, ACL, BM25, RRF, RAGAS — «на пальцах» |
| O01 | ✓ | 8 H2 совпадают с research action_outline |
| O02 | ✓ | Outline: аудит → chunking → hybrid → промпт → eval → стек → пилот → next |
| O03 | ✓ | FAQ 7 пар, queries из research/Wordstat |
| O04 | ✓ | ol (12+8+5), 1 table, 5 blockquote |
| R01 | ✓ | TL;DR + схема pipeline + prompt template + Fact Check blockquote |
| R02 | ✓ | Novacom 70%, Cloud.ru, May AI, Liu et al. TACL 2024 — с research-notes |
| R03 | ✓ | Wordstat 419 — «вторичные данные, июнь 2026» |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: 8 шагов пилота + таблица Chroma/Qdrant/pgvector/Dify |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, t.me ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat вторичный, 152-ФЗ/on-prem, managed OCR limits |
| Ept02 | ✗ | Internal links → absolute published URL (relative href 404 на site-base env) |

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
- OK: B02 n8n-agents, B04 geo-2026, kv-ai.ru/obuchenie-po-make, t.me/maya_pro, kv-ai.ru/artur-horosheff, cloud.ru, novacom.ru, May AI RAG guide
- fix applied (cycle 1):
  - relative `/avtomatizaciya-n8n-ai-agents/` → absolute published URL (404 на relative + site-base env)
  - relative `/geo-optimizaciya-sajta-2026/` → absolute published URL (404 на relative + site-base env)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (схема/blockquote/таблица — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 1 verified in fact-bank, 7 unverified — пороги chunking/Wordstat из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 25`, `h2_sections: 8`, `faq_h3: 7`, `tables: 1`, `blockquotes: 5`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` prompt → blockquote (html-linter); relative internal href → absolute mayai.ru (link-verify)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Wordstat-цифры и Novacom % в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (8 pilot steps) | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
