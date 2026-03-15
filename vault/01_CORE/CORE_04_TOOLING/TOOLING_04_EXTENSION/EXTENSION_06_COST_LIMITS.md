---
id: EXTENSION_06_COST_LIMITS
type: TOOLING
title: CostLimits
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, cost, limits, core, minimal]
depends_on: [DISCIPLINE_06_SCOPE_CLASSIFIER, CONSTRAINT_00_GUARD_RAILS]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_04_EXTENSION
---

# EXTENSION_06 - Cost Limits (minimal) (CORE)

## Objet

Garde-fou minimal pour éviter la dérive coûts/temps sur outils externes.

- Définir un budget/temps maximal par CO (dans PRODUCT/PACKAGE).
- Si dépassement : reclassifier (NOW→NEXT/LATER) via ScopeClassifier.
- Stop si aucune mesure d’impact n’est définie.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : FROZEN + depends_on minimisé et dédupliqué + corection

  heading.

- v1.1 (01-03-2026) : correction erreurs.
- v1.0 (01-03-2026) : version initiale.
