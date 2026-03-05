---
id: BETA_GAPC_DOD_02_RELEASE_FREEZE
type: DOD
title: GapcBetaReleaseFreeze
version: v1.0
status: READY_TO_FREEZE
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, freeze, release, p0]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOCQG, DISCIPLINE_04_CODEQG, DISCIPLINE_02_RAGQG, DISCIPLINE_01_GELRULES, CONSTRAINT_00_GUARDRAILS, CONSTRAINT_03_SECRETSPOLICY, CONSTRAINT_01_RAGSCOPEPOLICY, TPL_00_PRDONEPAGER, TPL_01_SPECTECH, TPL_02_ADRLITE, TPL_03_BACKLOGCO, TPL_04_TESTPLANSMOKE, TPL_05_ACTIONDOC, TPL_06_ACTIONCODE, TPL_09_REVIEWCHECK, TPL_10_RELEASENOTE, GAPC_PIPELINE_00_PACKAGE, GAPC_PIPELINE_01_WORKSPACE_RULES, GAPC_DISCIPLINE_02_GELRULES, MVP_SCOPE_CLASSIFIER, GAPC_01_RISKREGISTER, GAPC_DISCIPLINE_00_RAGPROFILE, GAPC_DISCIPLINE_02_RAGQG, GAPCBETA_DOD_00_BETA_VALIDATION, GAPCBETA_DOD_01_PRODUCT_THIN_SLICE]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_01_DOD
---

# GAPCBETA DoD — 02 Release / Freeze — v1.0 (P0)

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
