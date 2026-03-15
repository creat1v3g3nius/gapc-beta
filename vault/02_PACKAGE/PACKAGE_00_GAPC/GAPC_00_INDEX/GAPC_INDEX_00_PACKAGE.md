---
id: GAPC_INDEX_00_PACKAGE
type: INDEX
title: GAPCPackageNavigationIndex
version: v1.3
status: FROZEN
created: 05-03-2026
updated: 06-03-2026
tags: [gapc, package, index, navigation]
depends_on: []
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_00_INDEX
---

# GAPC_INDEX_00 — Navigation Package

## Objet

Point d’entrée du **PACKAGE_00_GAPC** (overlay métier du framework GAPC).

Le PACKAGE contient :

- des **overlays** (règles métier spécifiques, sans duplication du CORE)
- des **add-ons** (templates, checklists, extensions) propres au métier
- des **allowlists** et politiques de sources/outils spécifiques
- des **ponts vers PRODUCT** (exigences de preuves / workspace), si applicable

Le PACKAGE ne contient pas :

- les règles transverses (CORE)
- les procédures opérateur (SYSTEM)
- les preuves et validations d’un produit (PRODUCT)

---

## GAPC_INDEX_00 - Package Navigation

### INDEX

[[GAPC_INDEX_01_META]] · [[GAPC_INDEX_02_DISCIPLINE]] ·
[[GAPC_INDEX_03_CONSTRAINT]] · [[GAPC_INDEX_04_TOOLING]]

---

### META

- [[GAPC_META_00_PACKAGE_PROFILE]] :  profil du package (périmètre, overlays,
  add-ons, règles d’intégration).

---

### DISCIPLINE

- [[GAPC_DISCIPLINE_00_RAG_PROFILE]] :  profil RAG du package (cadre d’usage et
  limites).
- [[GAPC_DISCIPLINE_01_GEL_RULES]] :  règles de gel (READY_TO_FREEZE / FROZEN)
  appliquées au package.
- [[GAPC_DISCIPLINE_02_RAG_QG]] :  quality gates RAG (contrôles P0/P1/P2).
- [[GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER]] :  classifieur de scope
  (CORE/SYSTEM/PACKAGE/PRODUCT/CACHE).
- [[GAPC_DISCIPLINE_04_RISK_REGISTER]] : registre de risques (P0-first,
  contrôles, mitigations).

---

### CONSTRAINT

- [[GAPC_CONSTRAINT_00_ALLOW_LIST]] :  allowlist spécifique (ce qui est
  explicitement autorisé dans le package).
- [[GAPC_CONSTRAINT_01_SOURCES_POLICY]] :  politique de sources (priorités,
  exclusions, contraintes).
- [[GAPC_CONSTRAINT_02_EXCEPTION_POLICY]] : gestion des exceptions (conditions,
  traçabilité, contrôles).

---

### TOOLING (navigation par famille)

> Objectif : permettre de naviguer **directement** vers chaque fichier de
  TOOLING, groupé par famille.

#### KNOWLEDGE

- [[GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS]] :  liste des outils autorisés
  (usage + limites).
- [[GAPC_TOOLING_KNOWLEDGE_01_SOURCES_PRIORITY]] :  priorisation des sources
  (règles de choix et ordre).

#### TPL

- [[GAPC_TOOLING_TPL_00_BACKLOG_CO_ADDON]] : template add-on Backlog CO (items
  atomiques).
- [[GAPC_TOOLING_TPL_01_RELEASE_NOTE_ADDON]] :  template add-on Release Note
  (gel, versions, changements).
- [[GAPC_TOOLING_TPL_02_BETA_EVIDENCE_PACK]] :  template pack de preuves (beta /
  validations).
- [[GAPC_TOOLING_TPL_03_RAG_SESSION_LOG]] :  template log de session RAG
  (traçabilité).

#### PIPELINE

- [[GAPC_TOOLING_PIPELINE_00_PACKAGE]] : pipeline du package
  (génération/structure attendue).
- [[GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES]] :  règles workspace (structure +
  contraintes d’usage).

#### CHECKLIST

- [[GAPC_TOOLING_CHECKLIST_00_START_SESSION_ADDON]] : checklist add-on démarrage
  session (P0-first).
- [[GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON]] : checklist add-on passage
  READY_TO_FREEZE.

#### EXTENSION

- [[GAPC_TOOLING_EXTENSION_00_ALLOW_LIST]] :  extension allowlist (compléments
  et cas).
- [[GAPC_TOOLING_EXTENSION_02_EVIDENCE_REQUIREMENTS]] : extension exigences de
  preuves (règles additionnelles).

---

## Amendements (FROZEN)

Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (06-03-2026) : lien extension evidence aligné vers
  `GAPC_TOOLING_EXTENSION_02_EVIDENCE_REQUIREMENTS`.
- v1.2 (05-03-2026) : passage en FROZEN.
- v1.1 (05-03-2026) : ajout navigation TOOLING par famille (liste complète +
  chemins + descriptions).
- v1.0 (05-03-2026) : création index PACKAGE du PACKAGE_00_GAPC.
