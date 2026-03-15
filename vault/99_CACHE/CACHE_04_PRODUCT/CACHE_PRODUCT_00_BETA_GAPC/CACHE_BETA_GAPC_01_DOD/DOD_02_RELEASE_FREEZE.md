---
id: DOD_02_RELEASE_FREEZE
type: DOD
title: GapcBetaReleaseFreeze
version: v1.0
status: DEPRECATED
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, freeze, release, p0]
depends_on:
  - PIPELINE_00_PRODUCT
  - PIPELINE_05_RELEASE_FREEZE
  - DISCIPLINE_03_DOC_QG
  - DISCIPLINE_04_CODE_QG
  - DISCIPLINE_02_RAG_QG
  - DISCIPLINE_01_GEL_RULES
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - TPL_00_PROD_ONE_PAGER
  - TPL_01_SPEC_TECH
  - TPL_02_ADR_LITE
  - TPL_03_BACKLOG_CO
  - TPL_04_TEST_PLAN_SMOKE
  - TPL_05_ACTION_DOC
  - TPL_06_ACTION_CODE
  - TPL_09_REVIEW_CHECK
  - TPL_10_RELEASE_NOTE
  - GAPC_TOOLING_PIPELINE_00_PACKAGE
  - GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
  - GAPC_DISCIPLINE_01_GEL_RULES
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_04_RISK_REGISTER
  - GAPC_DISCIPLINE_00_RAG_PROFILE
  - GAPC_DISCIPLINE_02_RAG_QG
  - DOD_00_BETA_VALIDATION
  - DOD_01_BETA_PRODUCT_THIN_SLICE
arc: CACHE
scope: vault/99_CACHE/CACHE_04_PRODUCT/CACHE_PRODUCT_00_BETA_GAPC/CACHE_BETA_GAPC_01_DOD
---

# DOD_02 - RELEASE_FREEZE

## Objet

Définir la DoD “gel” appliquée dans le workspace product :

- déclarer READY_TO_FREEZE
- produire la preuve de reproductibilité
- passer en FROZEN si requis

---

## 1) READY_TO_FREEZE (P0)

PASS si :

- thin slice PASS,
- gates applicables PASS,
- risques critiques mitigés,
- evidence pack disponible (IDs + liens).

Output : verdict + release note (si applicable).

---

## 2) FROZEN (P0)

PASS si :

- READY_TO_FREEZE PASS,
- amendements contrôlés (patch + version bump),
- reproductibilité démontrable via procédures SYSTEM,
- zéro P0 ouvert.

Output : statut FROZEN + release note à jour.

---

## Changelog

- v1.0 (01-03-2026) : création DoD release/freeze (workspace).
