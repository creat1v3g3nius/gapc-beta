---
id: ASSO_DISCIPLINE_04_SCOPE_CLASSIFIER
type: DISCIPLINE
title: AssoScopeClassifier
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, discipline, scope, p0, product-ready]
depends_on: [DISCIPLINE_06_SCOPE_CLASSIFIER, ASSO_DISCIPLINE_05_RISK_REGISTER, ASSO_DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_02_DISCIPLINE
---

# ASSO_DISCIPLINE_04 - Scope Classifier

## Labels
NOW / NEXT / LATER / REJECT.

## NOW si (P0)
- réduit un risque critique,
- nécessaire à un gate de gel métier,
- nécessaire à conformité légale/gouvernance.

## Anti-dérive
> 3 items → backlog CO (TPL CORE).


---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + correction depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : classifier métier ASSO.
