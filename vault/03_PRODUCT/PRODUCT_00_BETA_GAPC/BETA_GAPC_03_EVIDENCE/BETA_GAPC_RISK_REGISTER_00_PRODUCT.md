---
id: BETA_GAPC_RISK_REGISTER_00_PRODUCT
type: DISCIPLINE
title: GapcBetaRiskRegisterProduct
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, risk, register, dod, p0]
depends_on: [GAPC_DISCIPLINE_04_RISK_REGISTER, BETA_GAPC_CO_00_DOD]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# BETA_GAPC_RISK_REGISTER_00_PRODUCT

## Regles
- Max 3 risques actifs.
- Chaque risque inclut mitigation, signal, owner, statut, liens.
- Risque critique (score 6-9) interdit en Open sans mitigation + owner.

## Risques Actifs

### R-0001
- Titre: FrontmatterStrictNonConforme
- Categorie: Governance
- Description: non-conformite `id/title` bloquante pour DoD strict product.
- P: P2
- I: I3
- Score: 6
- Mitigation: patch cible backlog + re-run validator strict.
- Signal: S1 Frontmatter KO
- Owner: repo-maintainer
- Statut: Mitigating
- Date revue: 06-03-2026
- Liens: `BETA_GAPC_CO_00_DOD`, `BETA_GAPC_ACTION_DOC_00_DOD`

### R-0005
- Titre: EvidenceThinSliceIncomplete
- Categorie: Delivery
- Description: absence d'artefacts PRD/Spec/ADR/TestPlan/Review/Release.
- P: P2
- I: I2
- Score: 4
- Mitigation: creation du pack `BETA_GAPC_03_EVIDENCE`.
- Signal: S6 Derive CO
- Owner: product-owner-beta-gapc
- Statut: Mitigating
- Date revue: 06-03-2026
- Liens: `BETA_GAPC_PRD_00_DOD`, `BETA_GAPC_RELEASE_NOTE_00_BETA_VALIDATION`

### R-0009
- Titre: DocqgGlobalVaultNotInScope
- Categorie: Governance
- Description: des erreurs strictes persistent hors perimetre product.
- P: P2
- I: I2
- Score: 4
- Mitigation: ouvrir un CO dedie multi-arc apres validation beta.
- Signal: S1 Frontmatter KO
- Owner: framework-owner
- Statut: Open
- Date revue: 06-03-2026
- Liens: `BETA_GAPC_DOD_00_BETA_VALIDATION`

## Next Step Unique
- Clore R-0001 et R-0005 apres rerun DoD_00 scope product.
