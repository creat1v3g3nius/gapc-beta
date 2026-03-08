---
id: EVIDENCE_04_R0001_TOUCHED_FILES
type: EVIDENCE
title: R0001TouchedFilesIndex
version: v1.0
status: READY_TO_FREEZE
created: 09-03-2026
updated: 09-03-2026
tags: [system, evidence, risk, r0001, index]
depends_on: [EVIDENCE_02_RISK_REGISTER_PRODUCT, EVIDENCE_03_ADR_DOD_SCOPE, DOD_00_BETA_VALIDATION, OPS_04_ACTION_DOC_DOD, OPS_05_CO_DOD]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE
---

# EVIDENCE_04 - R-0001 Touched Files

## Objectif
Rassembler en un point unique les fichiers touches par la mitigation du risque `R-0001` (`FrontmatterStrictNonConforme`) sur le vault.

## Fichiers touches (canonique)
- `vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_OPS/OPS_05_CO_DOD.md`
- `vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_OPS/OPS_04_ACTION_DOC_DOD.md`
- `vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_01_DOD/DOD_00_BETA_VALIDATION.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_01_REVIEW_DOD.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_00_RELEASE_NOTE_BETA_VALIDATION.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_02_RISK_REGISTER_PRODUCT.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_03_ADR_DOD_SCOPE.md`

## Source de consolidation
- Commit de cloture risques : `50dfd1a` (`chore(evidence): rerun DOD_00 global and close risks`)
- Register de risque produit : `EVIDENCE_02_RISK_REGISTER_PRODUCT`

## Usage
- Utiliser ce fichier comme index de preuve pour toute revue R-0001.
- Mettre a jour la liste si une nouvelle mitigation touche d'autres fichiers.

## Next Step Unique
- Conserver cet index synchronise avec `EVIDENCE_02_RISK_REGISTER_PRODUCT`.

## Changelog
- v1.0 (09-03-2026) : creation de l'index consolide des fichiers touches par R-0001.
