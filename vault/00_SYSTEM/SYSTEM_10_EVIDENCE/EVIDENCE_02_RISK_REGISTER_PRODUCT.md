---
id: EVIDENCE_02_RISK_REGISTER_PRODUCT
type: EVIDENCE
title: RiskRegisterProduct
version: v1.2
status: READY_TO_FREEZE
created: 06-03-2026
updated: 08-03-2026
tags: [system, evidence, risk, register, dod, p0]
depends_on: [GAPC_DISCIPLINE_04_RISK_REGISTER, OPS_05_CO_DOD, RUN_06_VAULT_HEALTH_CHECK]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE
---

# EVIDENCE_02 - Risk Register Product

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
- Liens: `OPS_05_CO_DOD`, `OPS_04_ACTION_DOC_DOD`

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
- Liens: `OPS_01_PRD_DOD`, `EVIDENCE_00_RELEASE_NOTE_BETA_VALIDATION`

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
- Liens: `DOD_00_BETA_VALIDATION`

## Next Step Unique
- Maintenir un rerun health check + validator strict global a chaque lot documentaire.

## Changelog
- v1.1 (06-03-2026) : aligne le registre risques sur la cible DocQG globale.
- v1.2 (06-03-2026) : cloture R-0001, R-0005 et R-0009 apres PASS DOCQG global.
