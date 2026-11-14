---
id: STUDIO_TOOLING_TPL_01_ART_DIRECTION_SPEC
type: TOOLING
title: StudioArtDirectionSpec
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, tpl, art-direction]
depends_on: 
  - TPL_01_SPEC_TECH
  - TPL_08_AI_IMAGE_PROMPT_MODEL
  - STUDIO_TOOLING_TPL_00_CREATIVE_BRIEF
  - STUDIO_CONSTRAINT_01_SOURCES_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_01_TPL
---

# STUDIO_TOOLING_TPL_01 - Art Direction Spec

## Objet

Add-on de `TPL_01_SPEC_TECH` : specification de la direction artistique d un
projet. Elle est la seule reference visuelle du projet une fois validee.

## Champs (copiable)

```txt
Territoire retenu:
Intention (2-3 phrases):
Palette (valeurs + roles):
Typographies (familles + licences):
Composition / cadrage:
Lumiere / ambiance:
Matieres / textures:
Do (5 max):
Don't (5 max):
References (provenance, statut inspiration):
Ancre de style IA (prompt de base, sans nom d artiste vivant):
Parametres IA figes (outil, ratio, style, seed si utile):
Matrice de declinaisons (livrable x format):
Validation DA client: date + round
```

## Regles P0

- toute modification apres validation passe par un CO et une nouvelle

  version de la spec,

- les prompts des CO reprennent l ancre de style et les parametres figes.

## Changelog

- v1.0 (14-11-2026) : creation du template spec DA.
