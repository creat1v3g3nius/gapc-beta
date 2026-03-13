---
id: SETUP_PRODUCT_00_INDEX
type: SETUP_PRODUCT
title: SetupProductIndex
version: v1.3
status: DRAFT
created: 13-03-2026
updated: 13-03-2026
tags: [system, multi-product, composition, index]
depends_on: [INDEX_01_ARCHITECTURE, INDEX_02_REPOSITORY, SETUP_PRODUCT_01_BOOTSTRAP, SETUP_PRODUCT_02_PROFILE_SELECTION, SETUP_PRODUCT_03_ROUTINE_OPERATIONS, SETUP_PRODUCT_04_DESTINATION_POLICY, SETUP_PRODUCT_05_LIFECYCLE_POLICY, SETUP_PRODUCT_06_MERGE_OUT_POLICY, SETUP_PRODUCT_07_GOVERNANCE_RULES]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_00 - Index

## Objet
Cadrer la gestion multi-products dans GAPC sans dupliquer `CORE`, `SYSTEM`, `PACKAGE` ou `PRODUCT`.

## Positionnement
- `CORE` definit les invariants durables.
- `SYSTEM` porte les protocoles operatoires et la composition.
- `PACKAGE` adapte les regles utiles a un domaine.
- `PRODUCT` instancie les outils de production et les preuves pendant la phase active.

## Principe directeur
- `CORE` definit.
- `PACKAGE` adapte.
- `PRODUCT` execute et prouve.
- le sous-lot `RUN_01_SETUP_PRODUCT` orchestre la chaine.

## Fichiers du lot
- `SETUP_PRODUCT_01_BOOTSTRAP`
- `SETUP_PRODUCT_02_PROFILE_SELECTION`
- `SETUP_PRODUCT_03_ROUTINE_OPERATIONS`
- `SETUP_PRODUCT_04_DESTINATION_POLICY`
- `SETUP_PRODUCT_05_LIFECYCLE_POLICY`
- `SETUP_PRODUCT_06_MERGE_OUT_POLICY`
- `SETUP_PRODUCT_07_GOVERNANCE_RULES`

## Arbitrage de numerotation
- `SETUP_PRODUCT_00_INDEX` reserve l entree de famille
- `SETUP_PRODUCT_01..07` portent les protocoles operatoires
- le conflit historique entre index et bootstrap est clos

## Regles transverses
- un package actif
- un product actif
- un `PRODUCT` hors `PRODUCT_00` est temporaire
- tout savoir stable remonte vers `CORE`, `SYSTEM` ou `PACKAGE`

## Next step unique
- formaliser la doctrine d integration `WORKFLOW` vs `SETUP_PRODUCT`.

## Changelog
- v1.3 (13-03-2026) : rehoste la famille sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.2 (13-03-2026) : renommage effectif de la famille en `SETUP_PRODUCT_*` avec arbitrage `00_INDEX`.
- v1.1 (13-03-2026) : cartographie de transition `MP_* -> SETUP_PRODUCT_*` ajoutee sans renommage effectif.
