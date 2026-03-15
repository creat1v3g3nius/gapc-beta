---
id: ASSO_CONSTRAINT_05_SOURCES_POLICY
type: CONSTRAINT
title: AssoSourcesPolicy
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, constraint, sources, p0]
depends_on:
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - ASSO_META_00_PACKAGE_PROFILE
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_05 - Sources Policy

## Priorité

CORE > PACKAGE_01_ASSO > PRODUCT actif > SYSTEM > CACHE.

## Règles P0

- référence > copie
- `NON TROUVÉ` si absence de source
- pas d’autre package comme “actif” si ASSO actif

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : policy sources ASSO.
