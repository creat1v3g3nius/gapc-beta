---
id: PIPELINE_03_BACKLOG_COMPOSANT
type: TOOLING
title: BacklogComposant
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, pipeline, backlog, component, co, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_02_PIPELINE
---

# PIPELINE_03 — Backlog Composant (CO) (CORE)

## Objet
Standardiser un backlog “composant” = liste de CO atomiques, exécutable sans dérive.

---

## 1) Règles P0
- 1 CO = 1 intention.
- 1 CO = 1 livrable principal (doc OU code).
- 1 CO = 1 commit (ou squash unique).
- Si > 5 fichiers touchés : découper.

---

## 2) Champs obligatoires d’un CO (P0)
- Goal (1 phrase)
- Arc principal
- Inputs/dépendances (IDs)
- Output attendu
- PASS/FAIL
- Risques (R1/R2/R3) + mitigation si nécessaire
- Next step unique

---

## 3) Artefacts associés
- Action Doc : `TPL_05_ACTION_DOC`
- Action Code : `TPL_06_ACTION_CODE`
- Review : `TPL_09_REVIEW_CHECK`
- Tests : `TPL_04_TEST_PLAN_SMOKE` (si exécution)

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

---

### Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : création standard backlog CO CORE.

## Changelog
- v1.2 (02-03-2026) : normalisation frontmatter.
- v1.3 (04-03-2026) : correction id.
