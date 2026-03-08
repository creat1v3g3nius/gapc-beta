---
id: OPS_02_SPEC_DOD
type: SPEC
title: GapcBetaSpecDodRemediation
version: v1.1
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, spec, dod, remediation, p0]
depends_on: [OPS_01_PRD_DOD, OPS_05_CO_DOD, TPL_01_SPEC_TECH, RUN_06_VAULT_HEALTH_CHECK]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# OPS_02_SPEC_DOD

## References
- PRD: `OPS_01_PRD_DOD`
- CO: `OPS_05_CO_DOD`

## Scope Technique
- Inclus: corrections frontmatter strict globales + evidence pack documentaire.
- Exclu: remediation de tous les arcs hors `PRODUCT_00_BETA_GAPC`.

## Architecture Minimale
- Composant A: backlog composants (etat execution pipeline).
- Composant B: dossier evidence thin-slice.
- Composant C: scripts quality gates (`ValidateFrontmatter.py`, `SmokeRunner.py`).

## Contrats / Validations
- Validator strict sur vault global:
  - commande: `./scripts/ValidateFrontmatter.py --strict --enforce-unique-ids --vault vault`
  - attendu: exit code 0.
- Smoke runner:
  - commande: `./scripts/SmokeRunner.py`
  - attendu: `PASS smoke runner`.

## Plan d'Implementation
- CO_001: corriger backlog strict.
- CO_002: produire le pack thin-slice.
- CO_003: produire le risk register product.

## Risques & Mitigations
- R-0001: non-conformite stricte globale => mitigation: patch cible + re-run validator.
- R-0005: evidence incomplete => mitigation: artefacts minimaux obligatoires.

## Next Step Unique
- Valider la decision de scope dans `EVIDENCE_03_ADR_DOD_SCOPE`.

## Changelog
- v1.1 (06-03-2026) : bascule les validations spec vers DocQG global `vault/`.
