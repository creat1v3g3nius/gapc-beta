---
id: ASSO_META_00_PACKAGE_PROFILE
type: META
title: AssoPackageProfile
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, meta, profile, p0, product-ready]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_01_META
---

# ASSO_META_00 - Package Profile

## Objet

Profil de `PACKAGE_01_ASSO` : rôle, périmètre, règles d’extension, invariants
P0.

## Rôle

Vérité métier “association 1901” : gouvernance, conformité, communication,
lexique.

## IN / OUT

**IN** : rubrics + constraints + knowledge + templates métier.
**OUT** : procédures (SYSTEM), preuves (PRODUCT), duplication des règles CORE.

## Invariants P0 (hérités CORE)

- no-secrets/no-PII
- `NON TROUVÉ` si absence de source
- référence > copie
- actifs uniques (package/product) quand exécution

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN (v1.2) + mise à jour metadata.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : création profile package ASSO.
