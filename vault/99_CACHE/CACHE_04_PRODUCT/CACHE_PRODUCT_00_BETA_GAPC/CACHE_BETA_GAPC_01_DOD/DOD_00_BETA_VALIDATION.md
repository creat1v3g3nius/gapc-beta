---
id: DOD_00_BETA_VALIDATION
type: DOD
title: GapcBetaValidation
version: v1.2
status: DEPRECATED
created: 01-03-2026
updated: 09-03-2026
tags: [product, gapcbeta, dod, validation, product-ready]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_01_RAG_SCOPE_POLICY, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE, GAPC_TOOLING_PIPELINE_00_PACKAGE, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_02_RAG_QG]
arc: CACHE
scope: vault/99_CACHE/CACHE_04_PRODUCT/CACHE_PRODUCT_00_BETA_GAPC/CACHE_BETA_GAPC_01_DOD
---

# GAPCBETA DoD — 00 Beta Validation — v1.0 (P0)

## Objet
Valider que **PRODUCT_00_GAPCBETA** prouve que le package **GAPC** est utilisable pour produire un premier product :
- conformité SYSTEM+CORE,
- application des rubrics GAPC,
- exécution d’un cycle minimal (thin slice),
- gel GAPC (READY_TO_FREEZE / FROZEN) côté package.

> Le package reste la vérité de base. Ce product contient les **preuves** (evidence).

---

## 1) Pré-conditions (P0)
- Actifs : package = `PACKAGE_00_GAPC`, product = `PRODUCT_00_GAPCBETA`
- No-secrets / no-PII
- 1 intention = 1 CO

---

## 2) Checks P0 (PASS/FAIL)

### 2.1 Conformité docs (P0)
PASS si :
- frontmatter conforme sur artefacts utilisés,
- `id==filename`,
- `scope` cohérent,
- pas de duplication “source of truth”.

### 2.2 Gates qualité (P0)
PASS si gates applicables passent :
- DocQG
- CodeQG (si scripts/outillage)
- RagQG (si mentor utilisé)

### 2.3 Preuve thin slice (P0)
PASS si un **thin slice** complet existe (cf. `DOD_01_PRODUCT_THIN_SLICE`) :
- PRD → CO → Spec/ADR → Action Doc/Code → Smoke → Review.

### 2.4 Risques (P0)
PASS si :
- aucun risque critique (score 6–9) Open sans mitigation + owner,
- signaux GAPC pris en compte.

### 2.5 Gel (P0)
PASS si :
- GAPC_READY_TO_FREEZE applicable (rubric package),
- et conditions pour GAPC_FROZEN sont atteintes si gel demandé.

---

## 3) Output attendu
```txt
Verdict: OK|KO
P0 fails:
Evidence IDs:
Risks:
Next step unique:
```

## 4) Trace issue R-0001
- Consolidation des fichiers touches archivee dans `vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE/EVIDENCE_04_R0001_TOUCHED_FILES.md`.

---

## Changelog
- v1.0 (01-03-2026) : création DoD beta validation (product workspace).
- v1.1 (09-03-2026) : ajout de la tracabilite centralisee R-0001.
- v1.2 (09-03-2026) : retrait de la dependance active vers `EVIDENCE_04` (archive CACHE/DEPRECATED).
