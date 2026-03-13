---
id: SETUP_PRODUCT_06_MERGE_OUT_POLICY
type: SETUP_PRODUCT
title: SetupProductMergeOutPolicy
version: v1.2
status: DRAFT
created: 13-03-2026
updated: 13-03-2026
tags: [system, multi-product, merge-out, extraction]
depends_on: [SETUP_PRODUCT_00_INDEX, SETUP_PRODUCT_04_DESTINATION_POLICY, SETUP_PRODUCT_05_LIFECYCLE_POLICY]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_06 - Merge-Out Policy

## Objet
Definir comment un product finalise sort du framework.

## Decisions possibles
- merge vers `CORE`
- merge vers `SYSTEM`
- merge vers `PACKAGE`
- extraction sans merge durable
- merge puis extraction

## Criteres de decision
- reusable multi-package -> `CORE` ou `SYSTEM`
- specialise domaine -> `PACKAGE`
- pure preuve locale -> extraction/archivage

## Protocole d extraction
- identifier le savoir durable
- merger les canons utiles
- exporter ou archiver le residuel local
- retirer le product du repo, sauf exception `PRODUCT_00`

## Next step unique
- cadrer la gouvernance multi-products pour eviter les collisions d usage.

## Changelog
- v1.2 (13-03-2026) : rehoste le protocole sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.1 (13-03-2026) : renommage `MP_06_MERGE_OUT_POLICY` -> `SETUP_PRODUCT_06_MERGE_OUT_POLICY`.
