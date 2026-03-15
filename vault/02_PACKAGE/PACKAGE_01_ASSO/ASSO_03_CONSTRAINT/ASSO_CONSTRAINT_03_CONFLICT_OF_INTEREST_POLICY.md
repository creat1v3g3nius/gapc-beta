---
id: ASSO_CONSTRAINT_03_CONFLICT_OF_INTEREST_POLICY
type: CONSTRAINT
title: AssoConflictOfInterestPolicy
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, constraint, governance, conflict-of-interest, p1]
depends_on:
  - ASSO_CONSTRAINT_01_LEGAL_BASELINE_1901
  - CONSTRAINT_04_DECISION_TRACEABILITY_POLICY
  - TPL_02_ADR_LITE
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_03 - Conflict Of Interest Policy

## Objet

Limiter les risques de confusion et de conflit d’intérêt (association ↔ intérêts
privés).

## Règles P0

- décision potentiellement conflictuelle → ADR-lite obligatoire
- séparer décisions association / privées
- formaliser les conventions quand nécessaire

## Red flags

- décision financière sans trace/owner
- communication qui confond asso et activité privée
- usage de ressources non cadré

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation
  frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création policy conflit d’intérêt (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
