---
id: ASSO_CONSTRAINT_01_LEGAL_BASELINE_1901
type: CONSTRAINT
title: AssoLegalBaseline1901
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, constraint, legal, 1901, p0]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, ASSO_META_01_DOMAIN_DEFINITIONS]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_01 - Baseline (1901)

## Principes
- statuts + objet clair
- gouvernance définie
- conventions écrites si nécessaire
- traçabilité décisions structurantes

## Red flags
- confusion association/personne/privé
- collecte PII sans cadre
- engagement financier sans validation gouvernance

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : baseline légale ASSO.

