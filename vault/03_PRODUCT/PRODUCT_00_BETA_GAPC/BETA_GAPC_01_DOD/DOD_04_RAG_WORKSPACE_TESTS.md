---
id: DOD_04_RAG_WORKSPACE_TESTS
type: DOD
title: GapcBetaRagWorkspaceTests
version: v1.0
status: DEPRECATED
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, rag, tests, p1]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_01_RAG_SCOPE_POLICY, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE, GAPC_TOOLING_PIPELINE_00_PACKAGE, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_02_RAG_QG, DISCIPLINE_00_RAG_PROFILE]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_01_DOD
---

# GAPCBETA DoD — 04 RAG Workspace Tests — v1.0 (P1)

## Objet
Définir un set minimal de tests “workspace mentor” :
- citations/sources,
- `NON TROUVÉ`,
- actifs uniques,
- pas de mélange packages/products.

---

## Tests (P1)
- T1 : question sans source → réponse `NON TROUVÉ`
- T2 : question product → sources product + GAPC, pas d’autre package
- T3 : question CORE → CORE cité, pas de “plausible”
- T4 : mélange actif → refus + demande isolation

---

## Output attendu
- logs/réponses exemplaires (texte) + verdict OK/KO

---

## Changelog
- v1.0 (01-03-2026) : création DoD tests RAG.
