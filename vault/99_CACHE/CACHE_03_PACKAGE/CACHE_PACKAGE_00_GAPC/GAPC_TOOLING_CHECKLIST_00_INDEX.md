---
id: GAPC_TOOLING_CHECKLIST_00_INDEX
type: TOOLING
title: GapcChecklistIndex
version: v1.2
status: DEPRECATED
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, checklist, index, p1]
depends_on: [CHECKLIST_00_INDEX, PIPELINE_00_PRODUCT, GAPC_TOOLING_PIPELINE_01_PACKAGE]
arc: CACHE
scope: vault/99_CACHE/CACHE_03_PACKAGE/CACHE_PACKAGE_00_GAPC/
---

# GAPC_TOOLING_CHECKLIST_00 - Index

## Objet
Index des **checklists GAPC (PACKAGE)** : uniquement des **add-ons** qui complètent les checklists CORE.
Les checklists d’exécution détaillées restent dans CORE/SYSTEM/PRODUCT.

## Add-ons GAPC
- [[GAPC_TOOLING_CHECKLIST_01_START_SESSION_ADDON]]
- [[GAPC_TOOLING_CHECKLIST_02_READY_TO_FREEZE_ADDON]]

## Références CORE
- `CHECKLIST_01_START_SESSION`
- `CHECKLIST_03_READY_TO_FREEZE`
- `CHECKLIST_05_INCIDENT`

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter + déplacement dans CACHE.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création index checklists GAPC (add-on).

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
