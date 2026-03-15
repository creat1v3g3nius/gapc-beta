---
id: ASSO_CONSTRAINT_00_ALLOW_LIST
type: CONSTRAINT
title: AssoExtensionAllowlist
version: v1.4
status: FROZEN
created: 01-03-2026
updated: 09-03-2026
tags: [package, asso, tooling, extension, allowlist, p1]
depends_on:
  - EXTENSION_04_EVIDENCE_PACK
  - CONSTRAINT_03_SECRETS_POLICY
  - ASSO_CONSTRAINT_04_DATA_PRIVACY_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_03_CONSTRAINT
---

# ASSO_CONSTRAINT_00 - Extension AllowList

## Objet

Définir les outils externes autorisés pour produire des assets “asso”, avec
preuve minimale.

## Autorisés (si evidence pack)

- image/vidéo : OK sans PII/visage réel sans consentement
- texte : OK si sourcé, sobre, sans surpromesse

## Interdits (P0)

- personnes identifiables sans consentement
- PII/secrets dans prompts/logs
- outils non documentés dans CORE/EXTENSION

## Evidence

- Evidence Pack CORE obligatoire (`EXTENSION_04_EVIDENCEPACK`)

## Changelog

- v1.4 (09-03-2026) : retire la dependance deprecated `EXTENSION_00_INDEX`.
- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation ids/depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : allowlist extensions ASSO (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
