---
id: RUN_02_CHECKLISTS
type: RUN
title: IndexChecklistsExecution
version: v1.1
status: FROZEN
created: 27-02-2026
updated: 02-03-2026
tags: [workflow, checklists, run, system]
depends_on: [RUN_00_PIPELINE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# RUN_02 - Index Checklist Execution

Ce document regroupe des checklists **copiables** pour exécuter le workflow GAPC sans dérive :
- sessions (start/end),
- doc compliance (Vault),
- patch code + commit Git,
- gel (READY_TO_FREEZE / FROZEN),
- AnythingLLM (ingestion + tests),
- serveur (backup + monitoring + DR).

---

## 1. Liste
`CHECKLIST_00_INDEX.md`
`CHECKLIST_01_START_SESSION.md`
`CHECKLIST_02_END_SESSION.md`
`CHECKLIST_03_READY_TO_FREEZE.md`
`CHECKLIST_04_FROZEN_AMENDMENT.md`
`CHECKLIST_05_INCIDENT.md`
`CHECKLIST_06_DOC_REVIEW.md`
`CHECKLIST_07_CODE_REVIEW.md`
`CHECKLIST_08_RAG_SESSION.md`
`CHECKLIST_09_OPTIMIZATION.md`
`CHECKLIST_10_RELEASE_NOTE.md`

Autres fichiers importants : documents CORE_01_DISCIPLINE et CORE_02_RESTRAINT.

---

## 2. Règle d'usage
- Une checklist doit pouvoir être exécutée en **< 10 minutes**.
- Si une checklist devient trop longue : **scinder** ou passer en “runbook” (CORE_04_TOOLING/TOOLING_02_PIPELINE).

---

## 3. Changelog
-v1.0 (27-02-2026) : Création du document regroupant les checklists utiles à l'exécution du workflow GAPC.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
