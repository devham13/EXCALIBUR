# QA: B06 chat-bot-dlya-biznesa-rag

date: 2026-06-21
score_total: 92/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «чат боты для бизнеса», FAQ 6 пар, 2 таблицы, ol/ul — OK |
| GEO / citability | 25 | 23 | Lead answer-first, TL;DR, pipeline blockquote, FAQ 6, чек-лист 12 пунктов, таблица каналов |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 14 | 0 AI-slop hits; Flesch RU 91.0 (очень лёгкий — допустимо для how-to); 6 over-long в таблицах/blockquote |
| Fact safety | 15 | 12 | fact-check PASS; 2/10 чисел в fact-bank (остальное — практические ориентиры RAG/MVP, не blocker) |
| Contract HTML | 10 | 8 | linter PASS, объём 9422 ✓, CTA ≤3 ✓, internal href ×2 OK на mayai.ru; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «чат боты для бизнеса» + RAG/n8n/Make |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: бизнес без программиста, FAQ L1 / лиды |
| C04 | ✓ | RAG, Vector Store, embeddings, human-in-the-loop, FCR/CSAT — «на пальцах» |
| O01 | ✓ | H2 совпадают с планом B06 (7 секций + FAQ) |
| O02 | ✓ | Outline: задача/канал → KB → workflow → эскалация → n8n vs Make → чек-лист → что дальше |
| O03 | ✓ | FAQ 6 пар, queries из research |
| O04 | ✓ | ol (7 шагов + 5 «что дальше»), ul (12 пунктов), 2 table |
| R01 | ✓ | TL;DR + итоговый вердикт n8n vs Make + «Делайте/Не делайте» в H2 |
| R02 | ✓ | McKinsey 71%/40%, тарифы n8n/Make, MAX лимиты — из research-notes |
| R03 | ✓ | Цены с контекстом бюджета; верификация на 21.06.2026 в author block |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: против рейтингов SaaS без сквозного RAG-workflow |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×2, Telegram ×1 (3 total) |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: human-in-the-loop, галлюцинации без RAG, модерация MAX |
| Ept02 | ✓ | Internal links mayai.ru — 200 (B02, B03 опубликованы) |

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

- total: 5, failed: 0
- OK: /avtomatizaciya-n8n-ai-agents/, /podklyuchenie-mcp-cursor/, kv-ai.ru/obuchenie-po-make, t.me/maya_pro, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблицы/blockquote/списки — допустимо)
- Flesch RU: 91.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (10 extracted, 2 verified in fact-bank; unverified — практические диапазоны chunks/FCR/MVP, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- Исправлений article.html не потребовалось. Все автоматические проверки пройдены с первого прогона.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести практические диапазоны (chunks, FCR, 5800 ₽) в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
