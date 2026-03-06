---
id: BETA_GAPC_ADR_00_DOD_SCOPE
type: ADR
title: GapcBetaAdrDodScope
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, adr, dod, scope]
depends_on: [BETA_GAPC_SPEC_00_DOD, TPL_02_ADR_LITE]
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
- Le strict global `vault/` est KO pour des raisons hors perimetre product beta.
- Le DoD_00 demande une preuve executable sur le product, pas une remise a niveau complete du vault.

## Options
### Option A
- Description: corriger tout le vault avant de rejouer DoD_00.
- Pros: homogeneite globale immediate.
- Cons: effort massif hors scope.
- Risques: blocage delivery P0 product.

### Option B
- Description: corriger strict sur `PRODUCT_00_BETA_GAPC` + evidence thin-slice complete.
- Pros: respecte le scope product, delivre une preuve rapide.
- Cons: dette restante hors product.
- Risques: confusion possible si scope non explicite.

## Decision
- Option B retenue: validation DoD_00 sur perimetre product cible.

## Consequences
- Positives: execution rapide et traçable.
- Negatives: strict global non traite.
- Dette creee: chantier global DocQG a planifier separément.
- Backout plan: revert des fichiers `BETA_GAPC_03_EVIDENCE` et retour au state precedent.

## Next Step Unique
- Executer `BETA_GAPC_ACTION_DOC_00_DOD`.
