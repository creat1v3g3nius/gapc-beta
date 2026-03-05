---
id: GAPC_INDEX_04_TOOLING
type: INDEX
title: GAPCPackageToolingIndex
version: v1.3
status: FROZEN
created: 05-03-2026
updated: 05-03-2026
tags: [gapc, package, tooling, index]
depends_on: []
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_00_INDEX
---
# GAPC_INDEX_04 — TOOLING

## Objet

Index des **outils** (templates / checklists / knowledge / extensions / pipeline) du PACKAGE_00_GAPC.

---

## Familles

### KNOWLEDGE
Outils de connaissance : référentiels d’usage, priorités, listes autorisées.

[[GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS]] : liste des outils autorisés (et conditions) pour le PACKAGE.
[[GAPC_TOOLING_KNOWLEDGE_01_SOURCES_PRIORITY]] : ordre de priorité des sources et règles de sélection.

### TPL
Templates prêts à copier pour produire des livrables conformes.

[[GAPC_TOOLING_TPL_00_BACKLOG_CO_ADDON]] : modèle “Backlog CO” atomisé (P0/P1/P2) pour le PACKAGE.
[[GAPC_TOOLING_TPL_01_RELEASE_NOTE_ADDON]] :  modèle de release note lors d’un gel / livraison.
[[GAPC_TOOLING_TPL_02_BETA_EVIDENCE_PACK]] : pack d’évidence (DoD) pour validations / beta.
[[GAPC_TOOLING_TPL_03_RAG_SESSION_LOG]] : log standard d’une session RAG (inputs, décisions, contrôles).

### PIPELINE
Règles d’exécution et composants de pipeline (workspace / runbook).

[[GAPC_TOOLING_PIPELINE_00_PACKAGE]] : pipeline du package (génération/structure attendue).
[[GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES]] : règles du workspace (preuves, structure, conventions) pour exécution.

### CHECKLIST
Checklists opérationnelles pour cadrer la session et la qualité.

[[GAPC_TOOLING_CHECKLIST_00_START_SESSION_ADDON]]: checklist de démarrage (intake, contraintes, scope, outputs).
[[GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON]] : checklist de passage READY_TO_FREEZE (DocQG/CodeQG/risques).

### EXTENSION
Extensions / add-ons de protocole (intégrations et exigences).

[[GAPC_TOOLING_EXTENSION_00_ALLOW_LIST]] : extension de l’allowlist (cas métier / toolchain).
[[GAPC_TOOLING_EXTENSION_01_EVIDENCE_REQUIREMENTS]] : exigences d’évidence (preuves minimales) pour validation.

---

## Amendements (FROZEN)
Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (05-03-2026) : passage en FROZEN.
- v1.2 (05-03-2026) : ajout descriptions + chemins complets par famille.
- v1.1 (05-03-2026) : ajout des chemins complets par famille (tooling).
- v1.0 (05-03-2026) : création index TOOLING du PACKAGE_00_GAPC.