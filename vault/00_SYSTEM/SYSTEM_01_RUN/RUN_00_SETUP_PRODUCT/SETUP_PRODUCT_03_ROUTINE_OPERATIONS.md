---
id: SETUP_PRODUCT_03_ROUTINE_OPERATIONS
type: SETUP_PRODUCT
title: SetupProductRoutineOperations
version: v1.4
status: FROZEN
created: 13-03-2026
updated: 15-03-2026
tags: [system, multi-product, routine, operations]
depends_on:
  - SETUP_PRODUCT_00_INDEX
  - SETUP_PRODUCT_02_PROFILE_SELECTION
  - WORKFLOW_00_PIPELINE
  - WORKFLOW_06_VAULT_HEALTH_CHECK
  - WORKFLOW_07_TESTS_LLM
  - WORKFLOW_08_TESTS_CODEX
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_03 - Routine Operations

## Objet

Definir la routine d exploitation d un product actif.

## Frontiere avec `WORKFLOW`

- ce document definit **ce qui doit rester maintenu** pour un product actif.
- il ne decrit pas le pas-a-pas de session.
- l execution quotidienne releve de `WORKFLOW_03_START_SESSION`,

  `WORKFLOW_04_END_SESSION` et `WORKFLOW_10_COMMANDES`.

- les reruns requis sont executes via `WORKFLOW_06_VAULT_HEALTH_CHECK`,

  `WORKFLOW_07_TESTS_LLM` et `WORKFLOW_08_TESTS_CODEX`.

## Routine minimale

- verifier package et product actifs
- maintenir `DOD`, `OPS`, `EVIDENCE`
- re-run des batteries applicables apres tout changement majeur
- backfill des preuves avant tout freeze

## Evenements qui imposent un rerun

- changement de prompt system
- changement de corpus `CORE`, `SYSTEM` ou `PACKAGE`
- changement de workflow mentor ou Codex
- changement de gates DOD/OPS/EVIDENCE

## Resultat attendu

- verdict documente sans oral
- etat du product cohérent avec ses preuves

## Sorties attendues

- liste de reruns applicables
- etat du product : stable ou a revalider
- besoin explicite de passage de cycle de vie si les preuves sont suffisantes

## Next step unique

- cadrer la destination finale des products une fois finalises.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (15-03-2026) : passage en FROZEN du protocole de routine produit.
- v1.3 (13-03-2026) : rehoste le protocole sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.2 (13-03-2026) : clarifie la frontiere entre routine produit et runbooks `WORKFLOW`.
- v1.1 (13-03-2026) : renommage `MP_03_ROUTINE_OPERATIONS` -> `SETUP_PRODUCT_03_ROUTINE_OPERATIONS`.
