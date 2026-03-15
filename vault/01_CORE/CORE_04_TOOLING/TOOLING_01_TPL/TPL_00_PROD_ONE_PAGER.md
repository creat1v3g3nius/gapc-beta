---
id: TPL_00_PROD_ONE_PAGER
type: TOOLING
title: PrdOnePager
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, prd-one-pager, core]
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
  - DISCIPLINE_05_DOC_COMPLIANCE
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_00 - Prod One-pager (CORE)

## But

Capturer le **besoin produit** en 1 page, sans dérive :

- 1 objectif
- 1 périmètre
- 1 hypothèse centrale
- 1 critère de succès mesurable

> Règle : si tu ne peux pas écrire cette page, tu n’es pas prêt à coder.

---

## 1) Contexte

- Problème / douleur :
- Pour qui (persona) :
- Situation actuelle :
- Pourquoi maintenant :

## 2) Objectif (1 phrase)

- Goal :

## 3) Hypothèse centrale (testable)

- Hypothesis :

## 4) Périmètre

### IN (P0)

- ...

### OUT (P0)

- ...

## 5) User journey (happy path)

1. ...
1. ...
1. ...

## 6) Exigences / contraintes

- No-secrets / no-PII :
- Read-only mentor (si applicable) :
- 1 intention = 1 commit :
- Perf / UX minima :
- Conformité (si applicable) :

## 7) KPIs / critères de succès

- KPI_1 :
- KPI_2 :
- Signal d’échec :

## 8) Risques (top 3) + mitigations

- R1 :
- R2 :
- R3 :

## 9) Décisions requises (si besoin)

- Décision A (ADR ?) :

## 10) Next step unique

- Next step :

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
