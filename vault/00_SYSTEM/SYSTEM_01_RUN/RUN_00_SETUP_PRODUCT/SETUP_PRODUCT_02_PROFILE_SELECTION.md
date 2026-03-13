---
id: SETUP_PRODUCT_02_PROFILE_SELECTION
type: SETUP_PRODUCT
title: SetupProductProfileSelection
version: v1.2
status: DRAFT
created: 13-03-2026
updated: 13-03-2026
tags: [system, multi-product, profile, selection]
depends_on: [SETUP_PRODUCT_00_INDEX, SETUP_PRODUCT_01_BOOTSTRAP, DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_00_RAG_PROFILE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_02 - Profile Selection

## Objet
Choisir le profil operatoire d un product a partir du package et du type de produit.

## Principe
- le package filtre ce qui descend de `CORE`
- le product ne recoit que les briques necessaires a son profil

## Matrice minimale
- `mentor_doc_only` : evidence et DOD legers, ops minimaux
- `mentor_rag_validated` : DOD workspace, ops smoke, evidence qualif
- `hybrid_doc_code` : evidence, ops et redirection stricte vers Codex
- `ops_heavy_product` : ops dominants, preuves d execution et runbooks renforces

## Regle de sortie
Pour chaque profil, documenter :
- briques requises
- briques optionnelles
- briques interdites

## Interdictions
- ne pas deduire un profil uniquement depuis le product
- ne pas contourner le package pour specialiser depuis `CORE`

## Next step unique
- formaliser la routine de maintenance d un product actif.

## Changelog
- v1.2 (13-03-2026) : rehoste le protocole sous `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.1 (13-03-2026) : renommage `MP_02_PROFILE_SELECTION` -> `SETUP_PRODUCT_02_PROFILE_SELECTION`.
