---
id: CHECKLIST_00_INDEX
type: TOOLING
title: ChecklistIndex
version: v1.2
status: DEPRECATED
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, checklist, index, core]
depends_on: []
arc: CACHE
scope: vault/99_CACHE/CACHE_02_CORE/CACHE_CORE_04_TOOLING/
---

# CHECKLIST_00 - Index (CORE)

## Objet
Index des checklists opérateur (CORE) : **courtes**, **binaires**, sans procédures détaillées.

## P0 (product-ready)
- [[CHECKLIST_01_START_SESSION]] — démarrer une session
- [[CHECKLIST_02_END_SESSION]] — clôturer une session
- [[CHECKLIST_03_READY_TO_FREEZE]] — checklist pré-gel (READY_TO_FREEZE)
- [[CHECKLIST_04_FROZEN_AMENDMENT]] — amendement contrôlé (FROZEN)
- [[CHECKLIST_05_INCIDENT]] — incident / dérive

## P1 (product-ready)
- [[CHECKLIST_06_DOC_REVIEW]] — review doc
- [[CHECKLIST_07_CODE_REVIEW]] — review code
- [[CHECKLIST_08_RAG_SESSION]] — session mentor RAG

## P2 (minimales)
- [[CHECKLIST_09_OPTIMIZATION]] — optimisation (garde-fou)
- [[CHECKLIST_10_RELEASE_NOTE]] — release note (garde-fou)

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : déplacement fichier dans CACHE.
- v1.1 (01-03-2026) : passage en FROZEN.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.