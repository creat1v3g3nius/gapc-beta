---
id: OPS_05_CO_DOD
type: BACKLOG_CO
title: GapcBetaCoDodRemediation
version: v1.2
status: READY_TO_FREEZE
created: 06-03-2026
updated: 09-03-2026
tags: [product, gapcbeta, co, dod, remediation, p0]
depends_on: [OPS_01_PRD_DOD, TPL_03_BACKLOG_CO, RUN_06_VAULT_HEALTH_CHECK, EVIDENCE_04_R0001_TOUCHED_FILES]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_OPS
---

# OPS_05_CO_DOD

### CO_001 - DocQG strict vault global
- Arc principal: PRODUCT
- Goal: rendre tous les docs du `vault/` conformes strict.
- Output attendu: validator strict PASS sur l'ensemble du vault.
- Critere PASS/FAIL: PASS si 0 erreur strict.
- Scope: NOW
- Priorite: P0
- Risque: R-0001

### CO_002 - Evidence thin-slice minimale
- Arc principal: PRODUCT
- Goal: instancier PRD->CO->Spec/ADR->ActionDoc->Smoke->Review->Release.
- Output attendu: pack evidence complet.
- Critere PASS/FAIL: PASS si les 8 artefacts existent et se referencent.
- Scope: NOW
- Priorite: P0
- Risque: R-0005

### CO_003 - Risques vault
- Arc principal: PRODUCT
- Goal: instancier un registre risques avec owners/mitigations/statuts.
- Output attendu: risk register traceable incluant couverture DocQG globale.
- Critere PASS/FAIL: PASS si aucun risque critique Open sans mitigation + owner.
- Scope: NOW
- Priorite: P0
- Risque: R-0001

## Tracabilite R-0001
- Index consolide des fichiers touches: `EVIDENCE_04_R0001_TOUCHED_FILES`.

## Next Step Unique
- Executer le spec `OPS_02_SPEC_DOD`.

## Changelog
- v1.1 (06-03-2026) : bascule CO_001 vers DocQG strict global `vault/`.
- v1.2 (09-03-2026) : ajout de la tracabilite R-0001 via index evidence dedie.
