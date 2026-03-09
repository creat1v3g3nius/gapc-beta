---
id: OPS_01_PRD_DOD
type: PRD
title: GapcBetaPrdDodRemediation
version: v1.2
status: READY_TO_FREEZE
created: 06-03-2026
updated: 09-03-2026
tags: [product, gapcbeta, prd, dod, remediation, p0]
depends_on: [TPL_00_PROD_ONE_PAGER, OPS_00_COMPOSANTS_BACKLOG, RUN_06_VAULT_HEALTH_CHECK, EVIDENCE_02_RISK_REGISTER]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_OPS
---

# OPS_01_PRD_DOD

## Contexte
- Le DoD de validation beta doit maintenant prouver un DocQG strict sur l'ensemble du vault.
- Le pipeline P0->P2 composants est deja operationnel sur Git/validator/smoke.

## Objectif
- Passer le DoD `DOD_00_BETA_VALIDATION` avec conformite DocQG sur tout `vault/`.

## Hypothese centrale
- Si les artefacts thin-slice minimaux sont instancies et si la conformite stricte est corrigee sur l'ensemble du vault, le verdict DoD peut passer a OK.

## Perimetre
### IN (P0)
- Correction stricte des documents du vault (`id==filename`, `title` UpperCamelCase, arc/scope coherents).
- Production du pack evidence: CO, Spec, ADR, ActionDoc, TestPlanSmoke, ReviewCheck, ReleaseNote, RiskRegister.
- Execution `ValidateFrontmatter --strict --enforce-unique-ids` sur `vault/`.
- Execution `SmokeRunner`.

### OUT (P0)
- Refonte fonctionnelle des contenus metier.
- Modification de la politique CORE hors besoin de correction DocQG.

## KPI / criteres de succes
- `ValidateFrontmatter --strict --enforce-unique-ids --vault vault` == PASS.
- `./scripts/SmokeRunner.py` == PASS.
- Evidence thin-slice complete et traçable dans `BETA_GAPC_03_EVIDENCE`.

## Next Step Unique
- Executer le CO `OPS_05_CO_DOD`.

## Changelog
- v1.1 (06-03-2026) : aligne le PRD sur un objectif DocQG global `vault/`.
- v1.2 (09-03-2026) : retire la dependance active vers `DOD_00_BETA_VALIDATION` (deprecated) et corrige le scope OPS.
