# QA: B01 primer-seo-stati

date: 2026-10-08
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | TL;DR answer-first, таблица SEO vs GEO, 8 шагов ol, 7 FAQ, workflow blockquote |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 84.6 |
| Fact safety | 15 | 13 | fact-check PASS; 2/9 в fact-bank; ориентиры объёма/lead — допустимо |
| Contract HTML | 10 | 7 | linter PASS, объём 9307 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (cover на publish) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Ковчег |
| C04 | ✓ | SEO, GEO, JSON-LD, llms.txt — при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline how-to |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (8 шагов), ul (чеклист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Princeton GEO-bench, Wordstat/Webmaster — с research-notes |
| R03 | ✓ | +40% с оговоркой «эксперименты»; нет выдуманных цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo пайплайна |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×1, бренд Maya AI уместен |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat без API, объём по SERP |
| Ept02 | ✓ | B04 mayai.ru ×2, главная блога, kv-ai.ru |

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

- total: 6, failed: 0
- OK: mayai.ru/geo-optimizaciya-sajta-2026/ (×2), wordstat.yandex.ru, webmaster.yandex.ru, internal `/`, kv-ai.ru (×2)
- fix applied (cycle 1): relative `/geo-optimizaciya-sajta-2026/` → absolute `https://mayai.ru/...` (404 на PUBLIC_SITE staging)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3
- Flesch RU: 84.6 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (9 extracted, 2 verified in fact-bank, 7 unverified — ориентиры, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 8`, `h2_sections: 5`, `faq_h3: 7`, `tables: 1`, `blockquotes: 4`)
- WARN: water phrase «в этой статье вы узнаете» — только в антипримере в ol (не blocker)

## Fix cycle

- cycle 1 (GEO QA): H2 «Настройте FAQ…» → «Настройте schema…» (duplicate FAQ linter); `<pre><code>` → blockquote; B04 links → mayai.ru absolute

## Optional (не blocker)

- `<img>` с alt после cover-агента
- занести Princeton 2023 / 2,5% в fact-bank при следующем research refresh

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
