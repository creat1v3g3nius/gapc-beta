---
id: EVIDENCE_02_RISK_REGISTER
type: EVIDENCE
title: RiskRegisterEvidence
version: v1.12
status: READY_TO_FREEZE
created: 06-03-2026
updated: 09-03-2026
tags: [system, evidence, risk, register, beta, p0]
depends_on: [GAPC_DISCIPLINE_04_RISK_REGISTER, OPS_05_CO_DOD, RUN_06_VAULT_HEALTH_CHECK, EVIDENCE_03_ADR_BETA_SCOPE, SCRIPT_04_DOC_INTEGRITY_CHECKER]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE
---

# EVIDENCE_02 - Risk Register

## Regles
- Max 3 risques actifs.
- Chaque risque inclut mitigation, signal, owner, statut, liens.
- Risque critique (score 6-9) interdit en Open sans mitigation + owner.

## Etat Global (09-03-2026)
- Risques suivis: 4
- Risques Open: 0
- Risques Closed: 4
- Risques critiques Open (score 6-9): 0
- Verdict registre: STABLE

## Risques Suivis

### R-0001
- Titre: FrontmatterStrictNonConforme
- Categorie: Governance
- Description: non-conformite `id/title` bloquante pour la validation beta stricte globale.
- P: P2
- I: I3
- Score: 6
- Mitigation: patchs cibles multi-arcs + re-run validator strict global + consolidation dans l'archive cache/deprecated `EVIDENCE_04_R0001_TOUCHED_FILES`.
- Signal: S1 Frontmatter KO
- Owner: repo-maintainer
- Statut: Closed
- Date revue: 09-03-2026
- Date cloture: 06-03-2026
- Liens: `OPS_05_CO_DOD`, `OPS_04_ACTION_DOC_DOD`, `vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE/EVIDENCE_04_R0001_TOUCHED_FILES.md`

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
- Date revue: 09-03-2026
- Date cloture: 06-03-2026
- Liens: `OPS_01_PRD_DOD`, `EVIDENCE_01_REVIEW_BETA`, `EVIDENCE_00_RELEASE_NOTE_BETA_VALIDATION`

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
- Liens: `DOD_00_BETA_VALIDATION`, `EVIDENCE_01_REVIEW_BETA`, `EVIDENCE_00_RELEASE_NOTE_BETA_VALIDATION`, `EVIDENCE_03_ADR_BETA_SCOPE`

### R-0011
- Titre: BranchAheadOriginPendingSync
- Categorie: Delivery
- Description: branche locale en avance sur `origin/main` et working tree non clean pendant le lot R-0001; risque leve apres commit/push + rerun checks.
- P: P1
- I: I1
- Score: 2
- Mitigation: commit du lot evidence, push vers `origin/main`, puis rerun `RUN_06_VAULT_HEALTH_CHECK`.
- Signal: S6 Derive CO
- Owner: repo-maintainer
- Statut: Closed
- Date revue: 09-03-2026
- Date cloture: 09-03-2026
- Liens: `RUN_06_VAULT_HEALTH_CHECK`, `EVIDENCE_03_ADR_BETA_SCOPE`, `EVIDENCE_00_RELEASE_NOTE_BETA_VALIDATION`

## Next Step Unique
- Maintenir un rerun `RUN_06_VAULT_HEALTH_CHECK` + `DocIntegrityChecker` a chaque lot documentaire et revalider ce registre a chaque fermeture de risque.

## Changelog
- v1.1 (06-03-2026) : aligne le registre risques sur la cible DocQG globale.
- v1.2 (06-03-2026) : cloture R-0001, R-0005 et R-0009 apres PASS DOCQG global.
- v1.3 (09-03-2026) : aligne les references canonique OPS/EVIDENCE et ouvre R-0011 (sync remote en attente).
- v1.4 (09-03-2026) : ajoute la dependance explicite vers l'index consolide R-0001.
- v1.5 (09-03-2026) : confirme la mitigation R-0001 via index consolide et affine R-0011 (ahead + working tree non clean).
- v1.6 (09-03-2026) : integre la revue explicite de R-0009 (statut confirme Closed avec preuves).
- v1.7 (09-03-2026) : fermeture de R-0011 + suppression du suffixe `_PRODUCT` sur naming/id.
- v1.8 (09-03-2026) : mise a jour complete du registre (etat global, dates de revue harmonisees, preuves de cloture).
- v1.9 (09-03-2026) : retire la dependance active a `EVIDENCE_04` et conserve la reference comme archive CACHE/DEPRECATED.
- v1.10 (09-03-2026) : retire la dependance active a `RUN_07_OPTIMIZATION_PROCESS` (deprecated).
- v1.11 (09-03-2026) : ajoute `DocIntegrityChecker` comme controle transverse recurrent du registre.
- v1.12 (09-03-2026) : debruitage title pour distinguer le registre evidence du registre discipline CORE.
