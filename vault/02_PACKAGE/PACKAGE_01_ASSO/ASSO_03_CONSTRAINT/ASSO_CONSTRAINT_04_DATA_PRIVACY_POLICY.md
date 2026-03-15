---
id: ASSO_CONSTRAINT_04_DATA_PRIVACY_POLICY
type: CONSTRAINT
title: AssoDataPrivacyPolicy
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, constraint, privacy, pii, p1, no-secrets]
depends_on:
  - CONSTRAINT_03_SECRETS_POLICY
  - ASSO_CONSTRAINT_01_LEGAL_BASELINE_1901
  - CONSTRAINT_00_GUARD_RAILS
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_04 - Data Privacy Policy

## Objet

Encadrer les données (adhérents/contacts/partenaires) sans dérive.

## Règles P0

- minimisation (collecte minimale)
- pas de PII dans docs publics ni exemples
- pas de secrets/tokens dans vault/repo
- owner + durée de conservation définis (opérationnel en PRODUCT)

## Red flags

- listes contacts en clair dans vault
- emails/téléphones versionnés publiquement
- exports non tracés

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation
  frontmatter/id/depends_on.
- v1.0 (01-03-2026) : creation policy données & privacy (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
