---
id: BETA_GAPC_DOD_04_RAG_WORKSPACE_TESTS
type: DOD
title: GapcBetaRagWorkspaceTests
version: v1.0
status: READY_TO_FREEZE
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, rag, tests, p1]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOCQG, DISCIPLINE_04_CODEQG, DISCIPLINE_02_RAGQG, DISCIPLINE_01_GELRULES, CONSTRAINT_00_GUARDRAILS, CONSTRAINT_03_SECRETSPOLICY, CONSTRAINT_01_RAGSCOPEPOLICY, TPL_00_PRDONEPAGER, TPL_01_SPECTECH, TPL_02_ADRLITE, TPL_03_BACKLOGCO, TPL_04_TESTPLANSMOKE, TPL_05_ACTIONDOC, TPL_06_ACTIONCODE, TPL_09_REVIEWCHECK, TPL_10_RELEASENOTE, GAPC_PIPELINE_00_PACKAGE, GAPC_PIPELINE_01_WORKSPACE_RULES, GAPC_DISCIPLINE_02_GELRULES, MVP_SCOPE_CLASSIFIER, GAPC_01_RISKREGISTER, GAPC_DISCIPLINE_00_RAGPROFILE, GAPC_DISCIPLINE_02_RAGQG, DISCIPLINE_00_RAGPROFILE, DISCIPLINE_08_RAGQG]
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
