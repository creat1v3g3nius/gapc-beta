---
id: ASSO_DISCIPLINE_01_GEL_RULES
type: DISCIPLINE
title: AssoGelRules
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, discipline, gel, p0, product-ready]
depends_on:
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_03_DOC_QG
  - CONSTRAINT_00_GUARD_RAILS
  - ASSO_DISCIPLINE_05_RISK_REGISTER
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_02_DISCIPLINE
---

# ASSO_DISCIPLINE_01 - Gel Rules

## ASSO_READY_TO_FREEZE (P0)

PASS si :

- DocQG PASS
- legal baseline OK
- messaging policy OK (si public)
- risques critiques mitigés
- no-secrets/no-PII

## ASSO_FROZEN (P0)

READY_TO_FREEZE PASS + amendements contrôlés + version bump + changelog +
reproductibilité “sans oral”.

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (02-03-2026) : passage en FROZEN v1.2 + correction depends_on.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : gel métier ASSO.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
