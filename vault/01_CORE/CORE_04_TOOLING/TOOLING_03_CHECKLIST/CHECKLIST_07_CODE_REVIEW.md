---
id: CHECKLIST_07_CODE_REVIEW
type: TOOLING
title: CodeReview
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, checklist, review, code, core]
depends_on:
  - CONSTRAINT_03_SECRETS_POLICY
  - DISCIPLINE_04_CODE_QG
  - PIPELINE_00_PRODUCT
  - TPL_09_REVIEW_CHECK
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_03_CHECKLIST
---

# CHECKLIST_07 - Code Review Checklist (CORE)

- [ ] Intention atomique (pas de mélange)
- [ ] Contrôles requis définis en SYSTEM : PASS
- [ ] No-secrets / no-PII
- [ ] Traçabilité (commit message + ADR si décision)
- [ ] Backout plan possible
- [ ] Pas de refactor massif non demandé

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
