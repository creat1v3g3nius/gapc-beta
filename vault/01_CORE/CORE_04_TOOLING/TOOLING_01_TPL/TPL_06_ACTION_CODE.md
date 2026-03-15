---
id: TPL_06_ACTION_CODE
type: TOOLING
title: ActionCode
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, action-code, core]
depends_on:
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - DISCIPLINE_07_RISK_REGISTER
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - DISCIPLINE_03_DOC_QG
  - DISCIPLINE_04_CODE_QG
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_06 - Action Code (CORE)

## But

Standardiser une action engineering (diff-first) :

- fichiers touchés
- patch minimal
- commit message
- validations (smoke/validator)

---

## Format

- Fichier(s) : `<path(s) repo>`
- Intention (1 phrase) :
- Patch (diff) :
- Commit message : `type(scope): action`
- Validations (P0) :
  - smoke
  - validator (si vault touché)
- Risques (max 3) :
- Backout plan :
- Next step unique :

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
