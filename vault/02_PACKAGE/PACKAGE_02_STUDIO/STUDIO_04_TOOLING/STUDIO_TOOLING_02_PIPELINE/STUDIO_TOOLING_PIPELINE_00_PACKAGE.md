---
id: STUDIO_TOOLING_PIPELINE_00_PACKAGE
type: TOOLING
title: StudioProjectPipeline
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, pipeline]
depends_on: 
  - PIPELINE_00_PRODUCT
  - PIPELINE_05_RELEASE_FREEZE
  - STUDIO_TOOLING_TPL_00_CREATIVE_BRIEF
  - STUDIO_TOOLING_TPL_01_ART_DIRECTION_SPEC
  - STUDIO_TOOLING_TPL_03_CLIENT_REVIEW_LOG
  - STUDIO_DISCIPLINE_01_GEL_RULES
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_02_PIPELINE
---

# STUDIO_TOOLING_PIPELINE_00 - Project Pipeline

## Objet

Overlay de `PIPELINE_00_PRODUCT` pour un projet studio. Les phases et gates
CORE s appliquent ; ce document precise leur contenu metier.

---

## Phase A - Brief (= cadrage PRD)

- brief creatif (`STUDIO_TOOLING_TPL_00_CREATIVE_BRIEF`),
- **gate** : brief complet et valide par le client.

## Phase B - Exploration et DA (= spec)

- moodboard, 2-3 territoires, presentation (round R0),
- spec DA du territoire retenu (`STUDIO_TOOLING_TPL_01_ART_DIRECTION_SPEC`),
- **gate** : DA validee par le client, consignee au journal de revue.

## Phase C - Decoupage (= backlog CO)

- un CO par livrable ou declinaison (`STUDIO_TOOLING_TPL_02_BACKLOG_CO_ADDON`),
- budget temps / credits par CO.

## Phase D - Production (= execution)

- generation via protocole d extension, retouche, exports,
- evidence pack studio par asset genere, rights check par livrable.

## Phase E - Revue client (rounds)

- presentation, retours, classement, CO de correction

  (`STUDIO_TOOLING_TPL_03_CLIENT_REVIEW_LOG`).

## Phase F - Pret pour BAT (= READY_TO_FREEZE)

- `STUDIO_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON` PASS.

## Phase G - BAT et livraison (= FROZEN)

- BAT trace, note de livraison, archivage hors repo.

## Phase H - Sortie du projet

- merge-out selon `SETUP_PRODUCT_06_MERGE_OUT_POLICY` : methode, prompts de

  base ou checklists reutilisables -> `PACKAGE_02_STUDIO` ; preuves locales ->
  archive.

## Changelog

- v1.0 (14-11-2026) : creation du pipeline projet studio.
