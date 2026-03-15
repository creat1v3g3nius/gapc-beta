---
id: TPL_04_TEST_PLAN_SMOKE
type: TOOLING
title: TestPlanSmoke
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, smoke, test, core]
depends_on:
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - DISCIPLINE_07_RISK_REGISTER
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - DISCIPLINE_03_DOC_QG
  - DISCIPLINE_04_CODE_QG
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_04 - Test Plan Smoke (CORE)

## But

Définir un **smoke test** P0 reproductible :

- parcours minimal
- données minimales
- critères PASS/FAIL
- backout si FAIL

---

## 1) Périmètre

- Artefact/CO :
- Environnement :
- Pré-requis :

## 2) Scénarios P0

### S1 — <Nom>

- Steps :

  1.
  2.

- Expected :
- PASS/FAIL :

### S2 — <Nom>

- ...

## 3) Données de test

- Dataset :
- Contraintes no-PII :

## 4) Observabilité minimale

- Signaux PASS :
- Signaux FAIL :

## 5) Backout plan

- Revert/rollback :

## 6) Next step unique

- ...

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
