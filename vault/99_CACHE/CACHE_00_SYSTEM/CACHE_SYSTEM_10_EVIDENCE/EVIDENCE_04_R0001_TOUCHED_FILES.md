---
id: EVIDENCE_04_R0001_TOUCHED_FILES
type: EVIDENCE
title: R0001TouchedFilesIndex
version: v1.2
status: DEPRECATED
created: 09-03-2026
updated: 09-03-2026
tags: [cache, evidence, risk, r0001, index]
depends_on: [EVIDENCE_02_RISK_REGISTER, EVIDENCE_03_ADR_FRAMEWORK_SCOPE, DOD_00_BETA_VALIDATION, OPS_SAMPLE_04_ACTION_DOC_DOD, OPS_SAMPLE_05_CO_DOD]
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE
---

# EVIDENCE_04 - R-0001 Touched Files

## Objectif
Rassembler en un point unique les fichiers touches par la mitigation du risque `R-0001` (`FrontmatterStrictNonConforme`) sur le vault.

## Fichiers touches (canonique)
- `vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_OPS/OPS_SAMPLE_05_CO_DOD.md`
- `vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_OPS/OPS_SAMPLE_04_ACTION_DOC_DOD.md`
- `vault/99_CACHE/CACHE_04_PRODUCT/CACHE_PRODUCT_00_BETA_GAPC/CACHE_BETA_GAPC_01_DOD/DOD_00_BETA_VALIDATION.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_01_REVIEW_FRAMEWORK.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_00_RELEASE_NOTE_FRAMEWORK_VALIDATION.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_02_RISK_REGISTER.md`
- `vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_03_ADR_FRAMEWORK_SCOPE.md`

## Source de consolidation
- Commit de cloture risques : `50dfd1a` (`chore(evidence): rerun beta global and close risks`)
- Register de risque : `EVIDENCE_02_RISK_REGISTER`

## Usage
- Utiliser ce fichier comme index de preuve pour toute revue R-0001.
- Mettre a jour la liste si une nouvelle mitigation touche d'autres fichiers.

## Next Step Unique
- Conserver cet index synchronise avec `EVIDENCE_02_RISK_REGISTER`.

## Changelog
- v1.0 (09-03-2026) : creation de l'index consolide des fichiers touches par R-0001.
- v1.1 (09-03-2026) : deplacement en CACHE et passage en DEPRECATED.
- v1.2 (09-03-2026) : met a jour les chemins de fichiers deprecies relocalises en CACHE.
