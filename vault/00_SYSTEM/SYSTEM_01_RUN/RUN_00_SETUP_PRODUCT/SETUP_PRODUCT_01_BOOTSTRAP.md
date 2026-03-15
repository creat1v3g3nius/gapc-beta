---
id: SETUP_PRODUCT_01_BOOTSTRAP
type: SETUP_PRODUCT
title: SetupProductBootstrap
version: v1.3
status: FROZEN
created: 13-03-2026
updated: 15-03-2026
tags: [system, multi-product, bootstrap, product]
depends_on: [SETUP_PRODUCT_00_INDEX, SETUP_PRODUCT_02_PROFILE_SELECTION, SETUP_PRODUCT_07_GOVERNANCE_RULES, META_03_NAMING_CONVENTIONS, META_05_FRONTMATTER]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_01 - Bootstrap

## Objet
Definir l ouverture d un nouveau product dans le repo.

## Regles de creation
- aucun nouveau `PRODUCT` sans package actif ou package dedie
- si le package dedie manque, il est derive depuis `CORE` puis specialise
- le `PRODUCT` n est cree qu apres selection du profil package/product

## Contrat minimum a l ouverture
- `active-package` explicite
- `active-product` explicite
- owner explicite
- lot `DOD`
- lot `OPS`
- lot `EVIDENCE`
- plan de tests applicable

## Arborescence minimale
- `*_00_DOD`
- `*_01_OPS`
- `*_02_EVIDENCE`

## Interdictions
- ne pas creer un `PRODUCT` autonome sans chaine `CORE -> PACKAGE`
- ne pas dupliquer integralement des canons sans justification

## Next step unique
- selectionner le profil de composition avant toute instanciation documentaire.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (15-03-2026) : passage en FROZEN du protocole bootstrap produit.
- v1.2 (13-03-2026) : rehoste le protocole sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.1 (13-03-2026) : renommage `MP_01_PRODUCT_BOOTSTRAP` -> `SETUP_PRODUCT_01_BOOTSTRAP`.
