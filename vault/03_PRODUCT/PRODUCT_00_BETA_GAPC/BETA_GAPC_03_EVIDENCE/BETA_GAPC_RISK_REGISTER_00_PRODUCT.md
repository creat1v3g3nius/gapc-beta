---
id: BETA_GAPC_RISK_REGISTER_00_PRODUCT
type: DISCIPLINE
title: GapcBetaRiskRegisterProduct
version: v1.2
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, risk, register, dod, p0]
depends_on: [GAPC_DISCIPLINE_04_RISK_REGISTER, BETA_GAPC_CO_00_DOD, GAPC_VAULT_HEALTH_CHECK]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# BETA_GAPC_RISK_REGISTER_00_PRODUCT

## Regles
- Max 3 risques actifs.
- Chaque risque inclut mitigation, signal, owner, statut, liens.
- Risque critique (score 6-9) interdit en Open sans mitigation + owner.

## Risques Suivis

### R-0001
- Titre: FrontmatterStrictNonConforme
- Categorie: Governance
- Description: non-conformite `id/title` bloquante pour DoD strict global.
- P: P2
- I: I3
- Score: 6
- Mitigation: patchs cibles multi-arcs + re-run validator strict global.
- Signal: S1 Frontmatter KO
- Owner: repo-maintainer
- Statut: Closed
- Date revue: 06-03-2026
- Date cloture: 06-03-2026
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
- Statut: Closed
- Date revue: 06-03-2026
- Date cloture: 06-03-2026
- Liens: `BETA_GAPC_PRD_00_DOD`, `BETA_GAPC_RELEASE_NOTE_00_BETA_VALIDATION`

### R-0009
- Titre: DocqgGlobalVaultCoverage
- Categorie: Governance
- Description: risque de non-couverture DocQG globale si le controle reste limite au product.
- P: P2
- I: I2
- Score: 4
- Mitigation: integrer DocQG global dans CO/PRD/SPEC/ADR/TestPlan/Review/Release + health check.
- Signal: S1 Frontmatter KO
- Owner: framework-owner
- Statut: Closed
- Date revue: 06-03-2026
- Date cloture: 06-03-2026
- Liens: `BETA_GAPC_DOD_00_BETA_VALIDATION`

## Next Step Unique
- Maintenir un rerun health check + validator strict global a chaque lot documentaire.

## Changelog
- v1.1 (06-03-2026) : aligne le registre risques sur la cible DocQG globale.
- v1.2 (06-03-2026) : cloture R-0001, R-0005 et R-0009 apres PASS DOCQG global.
