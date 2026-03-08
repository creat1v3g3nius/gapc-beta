---
id: EVIDENCE_02_RISK_REGISTER_PRODUCT
type: EVIDENCE
title: RiskRegisterProduct
version: v1.6
status: READY_TO_FREEZE
created: 06-03-2026
updated: 09-03-2026
tags: [system, evidence, risk, register, dod, p0]
depends_on: [GAPC_DISCIPLINE_04_RISK_REGISTER, OPS_05_CO_DOD, RUN_06_VAULT_HEALTH_CHECK, RUN_07_OPTIMIZATION_PROCESS, EVIDENCE_03_ADR_DOD_SCOPE, EVIDENCE_04_R0001_TOUCHED_FILES]
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
- Mitigation: patchs cibles multi-arcs + re-run validator strict global + consolidation dans `EVIDENCE_04_R0001_TOUCHED_FILES`.
- Signal: S1 Frontmatter KO
- Owner: repo-maintainer
- Statut: Closed
- Date revue: 09-03-2026
- Date cloture: 06-03-2026
- Liens: `OPS_05_CO_DOD`, `OPS_04_ACTION_DOC_DOD`, `EVIDENCE_04_R0001_TOUCHED_FILES`

### R-0005
- Titre: EvidenceThinSliceIncomplete
- Categorie: Delivery
- Description: absence d'artefacts PRD/Spec/ADR/TestPlan/Review/Release.
- P: P2
- I: I2
- Score: 4
- Mitigation: creation du pack canonique `OPS_*` + `EVIDENCE_*`.
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
- Date revue: 09-03-2026
- Date cloture: 06-03-2026
- Liens: `DOD_00_BETA_VALIDATION`, `EVIDENCE_01_REVIEW_DOD`, `EVIDENCE_00_RELEASE_NOTE_BETA_VALIDATION`, `EVIDENCE_03_ADR_DOD_SCOPE`

### R-0011
- Titre: BranchAheadOriginPendingSync
- Categorie: Delivery
- Description: branche locale en avance sur `origin/main` et working tree non clean pendant le lot R-0001; RUN_06 reste `FIX_REQUIRED` tant que commit/push/rerun ne sont pas finalises.
- P: P1
- I: I1
- Score: 2
- Mitigation: commit du lot evidence en cours, push vers `origin/main`, puis rerun `RUN_06_VAULT_HEALTH_CHECK`.
- Signal: S6 Derive CO
- Owner: repo-maintainer
- Statut: Open
- Date revue: 09-03-2026
- Date cloture: NON CLOTURE
- Liens: `RUN_06_VAULT_HEALTH_CHECK`, `EVIDENCE_03_ADR_DOD_SCOPE`

## Next Step Unique
- Committer le lot evidence R-0001, pousser `main`, puis rerun `RUN_06_VAULT_HEALTH_CHECK`.

## Changelog
- v1.1 (06-03-2026) : aligne le registre risques sur la cible DocQG globale.
- v1.2 (06-03-2026) : cloture R-0001, R-0005 et R-0009 apres PASS DOCQG global.
- v1.3 (09-03-2026) : aligne les references canonique OPS/EVIDENCE et ouvre R-0011 (sync remote en attente).
- v1.4 (09-03-2026) : ajoute la dependance explicite vers l'index consolide R-0001.
- v1.5 (09-03-2026) : confirme la mitigation R-0001 via index consolide et affine R-0011 (ahead + working tree non clean).
- v1.6 (09-03-2026) : integre la revue explicite de R-0009 (statut confirme Closed avec preuves).
