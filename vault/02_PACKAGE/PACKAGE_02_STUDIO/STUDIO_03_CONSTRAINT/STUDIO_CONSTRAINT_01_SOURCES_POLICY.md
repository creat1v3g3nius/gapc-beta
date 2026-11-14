---
id: STUDIO_CONSTRAINT_01_SOURCES_POLICY
type: CONSTRAINT
title: StudioSourcesPolicy
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, constraint, sources]
depends_on: 
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - STUDIO_DISCIPLINE_00_RAG_PROFILE
  - STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_03_CONSTRAINT
---

# STUDIO_CONSTRAINT_01 - Sources Policy

## Objet

Definir quelles sources font foi dans un projet studio et le statut des
references visuelles externes.

---

## 1) Sources qui font foi (P0)

Ordre : celui de `STUDIO_DISCIPLINE_00_RAG_PROFILE`. Dans un projet :

- **brief creatif** : seule source des faits client (livrables, delais,

  rounds, cession),

- **spec DA** : seule source des regles visuelles du projet,
- **journal de revue** : seule source des retours et decisions client.

Une information client absente de ces trois documents est `NON TROUVE`.

## 2) References visuelles externes

- elles servent a l **inspiration** (moodboard, territoires) et ne sont

  jamais integrees telles quelles dans un livrable,

- chaque reference est listee avec sa provenance (site, auteur si connu),
- une reference fournie par le client est notee comme telle,
- la reutilisation d un element externe dans un livrable releve de

  `STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY`.

## 3) Citation

- le mentor cite les IDs des documents utilises,
- une regle repetee dans un product renvoie a sa source package

  (reference > copie).

## Changelog

- v1.0 (14-11-2026) : creation de la politique de sources studio.
