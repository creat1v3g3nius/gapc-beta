---
id: DOD_01_BETA_PRODUCT_THIN_SLICE
type: DOD
title: GapcBetaProductThinSlice
version: v1.0
status: DEPRECATED
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, thin-slice, p0]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_01_RAG_SCOPE_POLICY, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE, GAPC_TOOLING_PIPELINE_00_PACKAGE, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_02_RAG_QG, DOD_00_BETA_VALIDATION]
arc: CACHE
scope: vault/99_CACHE/CACHE_04_PRODUCT/CACHE_PRODUCT_00_BETA_GAPC/CACHE_BETA_GAPC_01_DOD
---

# DOD_01 - BETA_PRODUCT_THIN_SLICE

## Objet
Définir le **cycle minimal** qui prouve l’exécutabilité de GAPC :
PRD → CO → Spec/ADR → Action Doc/Code → TestPlan Smoke → Review → (Release Note si gel).

---

## 1) Artefacts obligatoires (P0)
- PRD (1 page) — via TPL PRD
- Backlog CO — via TPL Backlog CO
- 1 CO atomique (doc ou code)
- Spec Tech (si nécessaire) + ADR si décision
- TestPlan Smoke (si exécution)
- ReviewCheck
- ReleaseNote (si gel)

---

## 2) Règles P0
- 1 intention = 1 CO = 1 commit
- sources citées, sinon `NON TROUVÉ`
- pas de secrets/PII
- si le mentor est utilisé : actifs uniques + RagQG

---

## 3) Checklist PASS/FAIL (P0)
PASS si :
- tous les artefacts P0 existent et sont “sans oral”
- gates applicables PASS
- risques critiques mitigés
- next step unique produit

FAIL sinon.

---

## Changelog
- v1.0 (01-03-2026) : création DoD thin slice (preuve exécution).
