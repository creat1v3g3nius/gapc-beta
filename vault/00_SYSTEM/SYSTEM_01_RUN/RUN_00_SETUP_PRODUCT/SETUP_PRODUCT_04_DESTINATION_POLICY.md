---
id: SETUP_PRODUCT_04_DESTINATION_POLICY
type: SETUP_PRODUCT
title: SetupProductDestinationPolicy
version: v1.3
status: FROZEN
created: 13-03-2026
updated: 15-03-2026
tags: [system, multi-product, destination, policy]
depends_on: [SETUP_PRODUCT_00_INDEX, SETUP_PRODUCT_03_ROUTINE_OPERATIONS, SETUP_PRODUCT_05_LIFECYCLE_POLICY]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_04 - Destination Policy

## Objet
Definir la destination normale d un product une fois son usage operationnel termine.

## Regle centrale
- `PRODUCT` est temporaire
- seul `PRODUCT_00` peut rester comme sample durable
- tout autre product finalise est destine a etre merge puis extrait

## Destination du savoir
- transverse -> `CORE`
- operatoire -> `SYSTEM`
- specialise package -> `PACKAGE`
- preuve locale -> export / archive hors repo si non reusable

## Interdictions
- ne pas laisser vivre durablement un product framework finalise dans le repo
- ne pas utiliser `PRODUCT` comme source de verite durable des regles

## Next step unique
- formaliser les etats de cycle de vie et leurs criteres de passage.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (15-03-2026) : passage en FROZEN de la politique de destination produit.
- v1.2 (13-03-2026) : rehoste le protocole sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.1 (13-03-2026) : renommage `MP_04_PRODUCT_DESTINATION_POLICY` -> `SETUP_PRODUCT_04_DESTINATION_POLICY`.
