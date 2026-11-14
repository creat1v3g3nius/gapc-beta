---
id: STUDIO_TOOLING_TPL_02_BACKLOG_CO_ADDON
type: TOOLING
title: StudioBacklogCoAddon
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, tpl, backlog, co]
depends_on: 
  - TPL_03_BACKLOG_CO
  - PIPELINE_03_BACKLOG_COMPOSANTS
  - STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER
  - EXTENSION_06_COST_LIMITS
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_01_TPL
---

# STUDIO_TOOLING_TPL_02 - Backlog CO Addon

## Objet

Add-on de `TPL_03_BACKLOG_CO` : champs studio a ajouter a chaque CO.

## Champs a ajouter (copiable)

```txt
Livrable (ref brief):
Type: livrable | declinaison | correction | exploration
Round: R0 (initial) | R1..Rn
Spec DA (version):
Outil / protocole:
Budget (temps / credits):
Evidence pack requis: OUI | NON
Rights check: PASS | FAIL | A VERIFIER
Decision scope (classifier): NOW | NEXT | LATER | REJECT
```

## Regles P0

- 1 CO = 1 livrable ou 1 correction coherente,
- un CO qui touche plus de 5 fichiers texte est decoupe

  (`PIPELINE_03_BACKLOG_COMPOSANTS`).

## Changelog

- v1.0 (14-11-2026) : creation de l add-on backlog CO studio.
