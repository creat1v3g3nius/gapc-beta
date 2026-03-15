---
id: PIPELINE_02_BACKLOG_PRODUCT
type: TOOLING
title: BacklogProduct
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, pipeline, backlog, product, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_02_PIPELINE
---

# PIPELINE_02 - Backlog Product (CORE)

## Objet
Définir le standard de backlog au niveau product :
- structurer la demande
- relier aux CO atomiques
- prioriser sans dérive

CORE strict : pas d’outil imposé (GitHub/Jira/etc).

---

## 1) Structure minimale (P0)
Un backlog product contient :
- Vision / objectif (référence PRD)
- Liste de CO (unités atomiques)
- Décisions (ADR) liées
- Risques (liens vers Risk Register)
- Statut global (DRAFT/READY_TO_FREEZE/FROZEN si applicable)

---

## 2) Règles P0
- 1 intention = 1 CO.
- Chaque CO a : output, PASS/FAIL, scope (NOW/NEXT/LATER/REJECT).
- Toute décision structurante → ADR.
- Toute dérive multi-arc → découpage.

---

## 3) Mapping recommandé
- PRD → ensemble de CO.
- CO → Spec (si nécessaire) → Action Doc/Code → TestPlan.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

---

### Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : création standard backlog product CORE.

## Changelog
- v1.3 (04-03-2026) : correction heading.
- v1.2 (02-03-2026) : normalisation frontmatter.
