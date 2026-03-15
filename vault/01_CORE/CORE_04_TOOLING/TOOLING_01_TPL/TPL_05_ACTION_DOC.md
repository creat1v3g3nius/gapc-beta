---
id: TPL_05_ACTION_DOC
type: TOOLING
title: ActionDoc
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, action-doc, core]
depends_on:
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - DISCIPLINE_07_RISK_REGISTER
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - DISCIPLINE_05_DOC_COMPLIANCE
  - DISCIPLINE_03_DOC_QG
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_05 - Action Doc (CORE)

## But

Standardiser une action documentaire (diff-first) :

- fichier
- section
- patch attendu
- validations

---

## Format

- Fichier : `<path dans vault>`
- ID : `<id frontmatter>`
- Section : `<H2/H3>`
- Intention (1 phrase) :
- Patch :
    - `--- START REPLACE ---`
    - ...
    - `--- END REPLACE ---`
- Validation (P0) :
    - frontmatter conforme
    - cohérence hiérarchique CORE→PACKAGE→PRODUCT→SYSTEM
- Next step unique :

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
