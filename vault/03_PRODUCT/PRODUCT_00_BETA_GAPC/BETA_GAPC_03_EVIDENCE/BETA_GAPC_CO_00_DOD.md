---
id: BETA_GAPC_CO_00_DOD
type: BACKLOG_CO
title: GapcBetaCoDodRemediation
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, co, dod, remediation, p0]
depends_on: [BETA_GAPC_PRD_00_DOD, TPL_03_BACKLOG_CO]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# BETA_GAPC_CO_00_DOD

### CO_001 - DocQG strict perimetre product
- Arc principal: PRODUCT
- Goal: rendre tous les docs `PRODUCT_00_BETA_GAPC` conformes strict.
- Output attendu: validator strict PASS sur le perimetre product.
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

### CO_003 - Risques product
- Arc principal: PRODUCT
- Goal: instancier un registre risques avec owners/mitigations/statuts.
- Output attendu: risk register product traceable.
- Critere PASS/FAIL: PASS si aucun risque critique Open sans mitigation + owner.
- Scope: NOW
- Priorite: P0
- Risque: R-0001

## Next Step Unique
- Executer le spec `BETA_GAPC_SPEC_00_DOD`.
