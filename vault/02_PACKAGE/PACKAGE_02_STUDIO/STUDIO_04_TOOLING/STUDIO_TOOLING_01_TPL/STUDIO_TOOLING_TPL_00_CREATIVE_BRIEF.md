---
id: STUDIO_TOOLING_TPL_00_CREATIVE_BRIEF
type: TOOLING
title: StudioCreativeBrief
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, tpl, brief]
depends_on: 
  - TPL_00_PROD_ONE_PAGER
  - STUDIO_META_01_DOMAIN_DEFINITIONS
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
  - STUDIO_TOOLING_KNOWLEDGE_01_DELIVERABLE_FORMATS
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_01_TPL
---

# STUDIO_TOOLING_TPL_00 - Creative Brief

## Objet

Add-on de `TPL_00_PROD_ONE_PAGER` : champs studio a ajouter au PRD d un
projet. Le brief est la seule source des faits client du projet.

## Champs a ajouter (copiable)

```txt
Client: CLIENT_NN
Projet: PRODUCT_NN_<CODE>
Objectif (1 phrase):
Cible:
Message cle:
Livrables (liste: type, format, ratio, nb declinaisons):
Charte existante (OUI/NON + reference):
References fournies par le client:
Contraintes (mentions, interdits, accessibilite):
Rounds de retours inclus: N
Budget (temps / credits de generation):
Echeances (presentation DA, BAT, livraison):
Validation (role qui valide):
Cession attendue (supports, territoire, duree):
Droits sur elements fournis par le client: garantis OUI/NON
Hors scope explicite:
```

## Regles P0

- aucun nom ou contact client : code `CLIENT_NN` et role uniquement,
- un champ inconnu reste vide et devient une question au client, jamais une

  hypothese.

## Changelog

- v1.0 (14-11-2026) : creation du template brief creatif.
