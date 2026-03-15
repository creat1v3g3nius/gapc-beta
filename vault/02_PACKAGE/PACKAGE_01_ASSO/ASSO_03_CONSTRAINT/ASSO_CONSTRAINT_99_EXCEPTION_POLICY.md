---
id: ASSO_CONSTRAINT_99_EXCEPTION_POLICY
type: CONSTRAINT
title: AssoExceptionPolicy
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, constraint, exception, p2, minimal]
depends_on: [CONSTRAINT_04_DECISION_TRACEABILITY_POLICY, TPL_02_ADR_LITE]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_99 - Exception Policy

## Objet

Accepter une exception sans dérive.

## Règle

Exception acceptable seulement si :

- ADR-lite tracée
- périmètre + durée + owner
- backout plan

Sans ADR-lite : KO.

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : création policy exception (P2 minimal).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
