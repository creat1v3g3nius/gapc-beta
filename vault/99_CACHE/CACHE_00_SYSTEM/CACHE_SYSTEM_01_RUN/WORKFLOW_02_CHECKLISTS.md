---
id: WORKFLOW_02_CHECKLISTS
type: WORKFLOW
title: IndexChecklistsExecution
version: v1.3
status: DEPRECATED
created: 27-02-2026
updated: 13-03-2026
tags: [workflow, checklists, cache, deprecated]
depends_on:
  - BACKLOG_01_SYSTEM_RUN_SETUP_PRODUCT
  - CHECKLIST_01_START_SESSION
  - CHECKLIST_02_END_SESSION
  - CHECKLIST_03_READY_TO_FREEZE
  - CHECKLIST_04_FROZEN_AMENDMENT
  - CHECKLIST_05_INCIDENT
  - CHECKLIST_06_DOC_REVIEW
  - CHECKLIST_07_CODE_REVIEW
  - CHECKLIST_08_RAG_SESSION
  - CHECKLIST_09_OPTIMIZATION
  - CHECKLIST_10_RELEASE_NOTE
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_01_RUN
---

# WORKFLOW_02 - Index Checklist Execution (Legacy)

## Statut

- `DEPRECATED`
- index legacy, hors noyau `WORKFLOW`
- ne plus maintenir ce document comme catalogue actif des checklists

## Redirection canonique

- demarrage de session : `CHECKLIST_01_START_SESSION`
- cloture de session : `CHECKLIST_02_END_SESSION`
- ready to freeze : `CHECKLIST_03_READY_TO_FREEZE`
- amendement FROZEN : `CHECKLIST_04_FROZEN_AMENDMENT`
- incident : `CHECKLIST_05_INCIDENT`
- revue doc : `CHECKLIST_06_DOC_REVIEW`
- revue code : `CHECKLIST_07_CODE_REVIEW`
- session RAG : `CHECKLIST_08_RAG_SESSION`
- optimisation : `CHECKLIST_09_OPTIMIZATION`
- release note : `CHECKLIST_10_RELEASE_NOTE`

## Note de migration

- la mention historique `CHECKLIST_00_INDEX` n est plus une source canonique

  exploitable dans l etat courant

- les checklists actives vivent dans

  `vault/01_CORE/CORE_04_TOOLING/TOOLING_03_CHECKLIST/`

- quand une checklist devient un protocole operatoire durable, la logique

  detaillee doit vivre dans `SYSTEM_01_RUN`

## Next step unique

- utiliser directement les `CHECKLIST_*` du `CORE` et ne plus etendre

  `WORKFLOW_02`.

## Amendements (DEPRECATED)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (13-03-2026) : archive en `CACHE_SYSTEM_01_RUN` pour sortir du scope

  SYSTEM actif.

- v1.2 (13-03-2026) : passe en `DEPRECATED` et redirige vers les `CHECKLIST_*`

  du `CORE`.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
