---
id: GAPC_CONSTRAINT_02_EXCEPTION_POLICY
type: CONSTRAINT
title: GapcExceptionPolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, constraint, exception, p2, minimal]
depends_on: [CONSTRAINT_04_DECISION_TRACEABILITY_POLICY, TPL_02_ADR_LITE, GAPC_CONSTRAINT_00_ALLOW_LIST]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_03_CONSTRAINT
---

# GAPC_CONSTRAINT_02 - Exception Policy (P2 minimal)

## Objet
Définir comment une **exception** aux contraintes GAPC peut être acceptée sans dérive.

## Règle
Une exception est acceptable seulement si :
- tracée (ADR-lite),
- bornée (périmètre + durée),
- owner explicite,
- backout plan.

Sans ADR-lite : **KO**.

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création policy d’exception minimale.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
