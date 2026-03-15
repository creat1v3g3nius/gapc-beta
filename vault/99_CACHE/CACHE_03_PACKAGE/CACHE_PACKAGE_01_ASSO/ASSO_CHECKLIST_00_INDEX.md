---
id: ASSO_CHECKLIST_00_INDEX
type: TOOLING
title: AssoChecklistIndex
version: v1.3
status: DEPRECATED
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, tooling, checklist, index, p1]
depends_on:
  - CHECKLIST_00_INDEX
  - ASSO_CHECKLIST_01_READY_TO_FREEZE_ADDON
  - ASSO_DISCIPLINE_01_GEL_RULES
arc: CACHE
scope: vault/99_CACHE/CACHE_03_PACKAGE/CACHE_PACKAGE_01_GAPC/
---

# ASSO_CHECKLIST_00 - Index

## Objet

Index des checklists **add-on** métier ASSO. Les checklists génériques vivent en
CORE.

## Add-ons ASSO

- [[ASSO_CHECKLIST_01_READY_TO_FREEZE_ADDON]]

## Références CORE

- CHECKLIST_01_START_SESSION
- CHECKLIST_03_READY_TO_FREEZE
- CHECKLIST_05_INCIDENT

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter + déplacement dans

  CACHE.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation metadata.
- v1.0 (01-03-2026) : création index checklist ASSO (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
