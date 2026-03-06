---
id: BETA_GAPC_ADR_00_DOD_SCOPE
type: ADR
title: GapcBetaAdrDodScope
version: v1.1
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, adr, dod, scope]
depends_on: [BETA_GAPC_SPEC_00_DOD, TPL_02_ADR_LITE, GAPC_VAULT_HEALTH_CHECK]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# BETA_GAPC_ADR_00_DOD_SCOPE

## Statut
- Status: ACCEPTED
- Date: 06-03-2026
- Owner: product-owner-beta-gapc
- Liens: `BETA_GAPC_PRD_00_DOD`, `BETA_GAPC_SPEC_00_DOD`

## Contexte
- Le besoin de validation a ete releve: le DocQG PASS doit couvrir tout `vault/`.
- Le lot evidence doit donc tracer une execution globale et non plus limitee au product.

## Options
### Option A
- Description: corriger tout le vault avant de rejouer DoD_00.
- Pros: homogeneite globale immediate.
- Cons: effort initial plus large.
- Risques: augmentation du temps de traitement.

### Option B
- Description: corriger strict sur `PRODUCT_00_BETA_GAPC` + evidence thin-slice complete.
- Pros: delivre une preuve rapide.
- Cons: ne repond pas a l'exigence de DocQG global.
- Risques: verdict DoD incomplet.

## Decision
- Option A retenue: validation DoD_00 avec DocQG strict sur l'ensemble du vault.

## Consequences
- Positives: verdict de conformite coherent avec l'exigence globale.
- Negatives: lot de correction plus large.
- Dette creee: aucune sur le scope DocQG global.
- Backout plan: revert du lot evidence + correction globale associee.

## Next Step Unique
- Executer `BETA_GAPC_ACTION_DOC_00_DOD`.

## Changelog
- v1.1 (06-03-2026) : decision de scope mise a jour vers DocQG global `vault/`.
