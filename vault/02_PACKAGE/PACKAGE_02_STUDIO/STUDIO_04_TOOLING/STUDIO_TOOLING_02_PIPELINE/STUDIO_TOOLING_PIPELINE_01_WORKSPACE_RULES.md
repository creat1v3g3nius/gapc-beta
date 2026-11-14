---
id: STUDIO_TOOLING_PIPELINE_01_WORKSPACE_RULES
type: TOOLING
title: StudioWorkspaceRules
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, pipeline, workspace]
depends_on: 
  - SETUP_PRODUCT_01_BOOTSTRAP
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
  - STUDIO_TOOLING_EXTENSION_02_ASSET_NAMING_ADDON
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_02_PIPELINE
---

# STUDIO_TOOLING_PIPELINE_01 - Workspace Rules

## Objet

Definir la structure d un projet studio dans `03_PRODUCT` et sa frontiere
avec le stockage externe des fichiers.

---

## 1) Ouverture

- via `SETUP_PRODUCT_01_BOOTSTRAP`, avec `active-package: PACKAGE_02_STUDIO`,
- nom du product : `PRODUCT_NN_<CODE>` ; `<CODE>` court, sans nom de client

  (ex : `PRODUCT_03_CLIENT05_LAUNCH`).

## 2) Arborescence dans le repo

```txt
03_PRODUCT/PRODUCT_NN_<CODE>/
  <CODE>_00_DOD/       brief, spec DA, criteres de BAT
  <CODE>_01_OPS/       backlog CO, journal de revue, ADR-lite
  <CODE>_02_EVIDENCE/  evidence packs, note de livraison
```

Le repo ne contient que des fichiers texte.

## 3) Stockage externe (hors repo)

```txt
CLIENT_NN/PRODUCT_NN/
  inputs/    fichiers fournis par le client
  work/      masters et fichiers de travail
  exports/   livrables
```

- les documents du vault referencent ces dossiers par chemin logique,
- nommage des fichiers : `STUDIO_TOOLING_EXTENSION_02_ASSET_NAMING_ADDON`.

## 4) Fermeture

- apres livraison : merge-out puis retrait du product du repo

  (`SETUP_PRODUCT_04_DESTINATION_POLICY`).

## Changelog

- v1.0 (14-11-2026) : creation des regles de workspace projet studio.
