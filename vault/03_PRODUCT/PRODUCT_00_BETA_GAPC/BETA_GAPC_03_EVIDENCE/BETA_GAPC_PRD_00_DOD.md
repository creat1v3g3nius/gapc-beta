---
id: BETA_GAPC_PRD_00_DOD
type: PRD
title: GapcBetaPrdDodRemediation
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, prd, dod, remediation, p0]
depends_on: [BETA_GAPC_DOD_00_BETA_VALIDATION, TPL_00_PROD_ONE_PAGER, BETA_GAPC_COMPOSANTS_BACKLOG]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# BETA_GAPC_PRD_00_DOD

## Contexte
- Le DoD de validation beta est KO sur trois axes: DocQG strict, evidence thin-slice incomplete, risques non instancies cote product.
- Le pipeline P0->P2 composants est deja operationnel sur Git/validator/smoke.

## Objectif
- Passer le DoD `BETA_GAPC_DOD_00_BETA_VALIDATION` sur le perimetre product BETA_GAPC.

## Hypothese centrale
- Si les artefacts thin-slice minimaux sont instancies et si la conformite stricte est corrigee sur le perimetre product, le verdict DoD peut passer a OK.

## Perimetre
### IN (P0)
- Correction stricte du backlog composants (`id==filename`, `title` UpperCamelCase).
- Production du pack evidence: CO, Spec, ADR, ActionDoc, TestPlanSmoke, ReviewCheck, ReleaseNote, RiskRegister.
- Execution `ValidateFrontmatter --strict --enforce-unique-ids` sur `PRODUCT_00_BETA_GAPC`.
- Execution `SmokeRunner`.

### OUT (P0)
- Remediation globale de tout `vault/`.
- Refonte des documents cache (`99_CACHE`) et autres packages.

## KPI / criteres de succes
- `ValidateFrontmatter --strict --enforce-unique-ids --vault vault/03_PRODUCT/PRODUCT_00_BETA_GAPC` == PASS.
- `./scripts/SmokeRunner.py` == PASS.
- Evidence thin-slice complete et traçable dans `BETA_GAPC_03_EVIDENCE`.

## Next Step Unique
- Executer le CO `BETA_GAPC_CO_00_DOD`.
