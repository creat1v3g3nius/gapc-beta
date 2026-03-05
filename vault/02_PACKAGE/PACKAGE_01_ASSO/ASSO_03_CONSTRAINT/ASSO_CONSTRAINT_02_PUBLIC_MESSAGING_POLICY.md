---
id: ASSO_CONSTRAINT_02_PUBLIC_MESSAGING_POLICY
type: CONSTRAINT
title: AssoPublicMessagingPolicy
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, constraint, messaging, p0]
depends_on: [ASSO_DISCIPLINE_03_LEXICAL_QG, CONSTRAINT_00_GUARD_RAILS]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_02 - Public Messaging Policy
## Règles P0
- pas d’absolus non vérifiables
- séparer objectifs / moyens / résultats
- expliciter limites/incertitudes si besoin
- pas de PII

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : policy messaging ASSO.

