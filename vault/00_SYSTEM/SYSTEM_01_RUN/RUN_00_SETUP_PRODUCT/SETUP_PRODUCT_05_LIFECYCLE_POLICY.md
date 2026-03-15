---
id: SETUP_PRODUCT_05_LIFECYCLE_POLICY
type: SETUP_PRODUCT
title: SetupProductLifecyclePolicy
version: v1.4
status: FROZEN
created: 13-03-2026
updated: 15-03-2026
tags: [system, multi-product, lifecycle, policy]
depends_on: [SETUP_PRODUCT_00_INDEX, SETUP_PRODUCT_04_DESTINATION_POLICY, DISCIPLINE_01_GEL_RULES, CHECKLIST_03_READY_TO_FREEZE, WORKFLOW_06_VAULT_HEALTH_CHECK, WORKFLOW_07_TESTS_LLM, WORKFLOW_08_TESTS_CODEX]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_05 - Lifecycle Policy

## Objet
Definir les etats d un product et les criteres de passage.

## Frontiere avec `WORKFLOW`
- ce document definit **quand** un product change d etat.
- il ne remplace ni les checks operatoires ni les runbooks de preuve.
- la preparation des preuves et des reruns releve du noyau `WORKFLOW`.

## Etats
- `BOOTSTRAP`
- `ACTIVE`
- `READY_TO_FREEZE`
- `FROZEN`
- `MERGED`
- `EXTRACTED`
- `SAMPLE_PERSISTENT` pour `PRODUCT_00`

## Regles d entree / sortie
- aucun passage implicite
- chaque etat exige des preconditions, des preuves et un owner
- `READY_TO_FREEZE` et `FROZEN` exigent un seuil minimal de preuve

## Garde-fous d integration
- passage `ACTIVE -> READY_TO_FREEZE` seulement si les reruns applicables sont a jour
- passage `READY_TO_FREEZE -> FROZEN` seulement si les preuves restent coherentes apres `WORKFLOW_06`, `WORKFLOW_07` et `WORKFLOW_08` quand ils s appliquent
- un incident traite via `WORKFLOW_05_INCIDENT` peut faire revenir un product a un etat precedent

## Regle de rollback
- si une gate redevient `KO`, suspendre le gel
- documenter le rollback et relancer les reruns requis

## Next step unique
- formaliser le protocole de merge-out et d extraction.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.4 (15-03-2026) : passage en FROZEN de la politique de cycle de vie produit.
- v1.3 (13-03-2026) : rehoste le protocole sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.2 (13-03-2026) : clarifie la frontiere lifecycle vs execution `WORKFLOW` et ajoute les garde-fous de rerun.
- v1.1 (13-03-2026) : renommage `MP_05_LIFECYCLE_POLICY` -> `SETUP_PRODUCT_05_LIFECYCLE_POLICY`.
