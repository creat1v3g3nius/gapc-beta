---
id: TPL_01_SPEC_TECH
type: TOOLING
title: SpecTech
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, spec-tech, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, TPL_00_PROD_ONE_PAGER, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_01 — Spec Tech (CORE)

## But
Traduire le PRD en une **spécification exécutable** :
- architecture minimale
- contrats (API, data)
- limites / non-objectifs
- plan de tests (smoke) + validations

---

## 0) Références
- PRD : <ID doc PRD réel>
- ADR (si existantes) : ...

## 1) Scope technique
- Inclus :
- Exclu :

## 2) Architecture (minimal)
- Modules / composants :
- Flux principaux :
- Dépendances :

## 3) Data / Modèle (si applicable)
- Entités :
- Schémas :
- Contraintes :
- Migration / compat :

## 4) Interfaces / Contrats
- Entrées / sorties :
- Erreurs :
- Auth / permissions (si applicable) :

## 5) Non-fonctionnel
- Performance :
- Observabilité :
- Sécurité (no-secrets, permissions) :

## 6) Plan d’implémentation (CO)
- CO_001 :
- CO_002 :

## 7) Plan de test (smoke)
- Parcours P0 :
- Données de test :
- Critères PASS/FAIL :

## 8) Risques & mitigations (top 3)
- ...

## 9) Next step unique
- ...

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
