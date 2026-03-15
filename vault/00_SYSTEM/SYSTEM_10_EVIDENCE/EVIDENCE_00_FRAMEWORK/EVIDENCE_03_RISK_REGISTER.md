---
id: EVIDENCE_03_RISK_REGISTER
type: EVIDENCE
title: RiskRegisterFramework
version: v1.18
status: FROZEN
created: 06-03-2026
updated: 13-03-2026
tags: [system, evidence, risk, register, framework, p0]
depends_on: [GAPC_DISCIPLINE_04_RISK_REGISTER, OPS_SAMPLE_05_CO_DOD, WORKFLOW_06_VAULT_HEALTH_CHECK, EVIDENCE_04_ADR_FRAMEWORK_SCOPE, SCRIPT_04_DOC_INTEGRITY_CHECKER, SCRIPT_05_SEMANTIC_NOISE_CHECKER, SCRIPT_06_FRONTMATTER_UTILS, LLM_00_RAG_PRINCIPES, LLM_01_INGESTION_PROTOCOL, LLM_02_PERMISSION_SECURITY, LLM_03_MENTOR_UTILITES, SCRIPT_03_INSTRUCTIONS_CODEX]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_00_FRAMEWORK
---

# EVIDENCE_03 - Risk Register

## Regles
- Max 3 risques actifs.
- Chaque risque inclut mitigation, signal, owner, statut, liens.
- Risque critique (score 6-9) interdit en Open sans mitigation + owner.

## Etat Global (13-03-2026)
- Risques suivis: 4
- Risques Open: 0
- Risques Closed: 4
- Risques critiques Open (score 6-9): 0
- Verdict registre: STABLE

## Trace Lot 13-03-2026
- convergence `WORKFLOW + SETUP_PRODUCT` executee en `CO_001` a `CO_005`
- noyau `WORKFLOW` stabilise et annexes `WORKFLOW_01` / `WORKFLOW_02` declasses
- famille `SETUP_PRODUCT_00..07` active
- index SYSTEM raccordes
- `WORKFLOW_07_TESTS_LLM` et `WORKFLOW_08_TESTS_CODEX` confirmes raccordes au cadre final

## Trace Lot 10-03-2026
- Setup operationnel mis a jour avec references SYSTEM_04_LLM:
  - `LLM_00_RAG_PRINCIPES`
  - `LLM_01_INGESTION_PROTOCOL`
  - `LLM_02_PERMISSION_SECURITY`
  - `LLM_03_MENTOR_UTILITES`
- Instructions verite Codex IDE creees via `SCRIPT_03_INSTRUCTIONS_CODEX`.
- Conversion `SCRIPT_03` en skill + creation des 3 fichiers:
  - `skills/codex-ide-instructions/SKILL.md`
  - `skills/codex-ide-instructions/agents/openai.yaml`
  - `skills/codex-ide-instructions/references/codex_ide_baseline.md`
- Clarification SOT:
  - `CORE/PACKAGE/PRODUCT` = SOT de fond
  - `SCRIPT_03_INSTRUCTIONS_CODEX` = SOT procedurale Codex
  - `skills/codex-ide-instructions/SKILL.md` = projection executable
- Hygiene repo:
  - `.gitignore` mis a jour pour ignorer `skills/`
  - retrait `vault/00_SYSTEM/SYSTEM_03_SCRIPT/SCRIPT_03_GIT_BOOTSTRAP_AGENT.md` du scope actif

## Risques Suivis

### R-0001
- Titre: FrontmatterStrictNonConforme
- Categorie: Governance
- Description: non-conformite `id/title` bloquante pour la validation framework canon stricte globale.
- P: P2
- I: I3
- Score: 6
- Mitigation: patchs cibles multi-arcs + re-run validator strict global + consolidation dans l'archive cache/deprecated `EVIDENCE_04_R0001_TOUCHED_FILES`.
- Signal: S1 Frontmatter KO
- Owner: repo-maintainer
- Statut: Closed
- Date revue: 09-03-2026
- Date cloture: 06-03-2026
- Liens: `OPS_SAMPLE_05_CO_DOD`, `OPS_SAMPLE_04_ACTION_DOC_DOD`, `vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE/EVIDENCE_04_R0001_TOUCHED_FILES.md`

### R-0005
- Titre: EvidenceThinSliceIncomplete
- Categorie: Delivery
- Description: absence d'artefacts PRD/Spec/ADR/TestPlan/Review/Release.
- P: P2
- I: I2
- Score: 4
- Mitigation: creation du pack canonique `OPS_*` + `EVIDENCE_*`.
- Signal: S6 Derive CO
- Owner: framework-owner
- Statut: Closed
- Date revue: 09-03-2026
- Date cloture: 06-03-2026
- Liens: `OPS_SAMPLE_01_PRD_DOD`, `EVIDENCE_02_REVIEW_FRAMEWORK`, `EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION`

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
- Liens: `PIPELINE_05_RELEASE_FREEZE`, `EVIDENCE_02_REVIEW_FRAMEWORK`, `EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION`, `EVIDENCE_04_ADR_FRAMEWORK_SCOPE`

### R-0011
- Titre: BranchAheadOriginPendingSync
- Categorie: Delivery
- Description: branche locale en avance sur `origin/main` et working tree non clean pendant le lot R-0001; risque leve apres commit/push + rerun checks.
- P: P1
- I: I1
- Score: 2
- Mitigation: commit du lot evidence, push vers `origin/main`, puis rerun `WORKFLOW_06_VAULT_HEALTH_CHECK`.
- Signal: S6 Derive CO
- Owner: repo-maintainer
- Statut: Closed
- Date revue: 09-03-2026
- Date cloture: 09-03-2026
- Liens: `WORKFLOW_06_VAULT_HEALTH_CHECK`, `EVIDENCE_04_ADR_FRAMEWORK_SCOPE`, `EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION`

## Next Step Unique
- Maintenir un rerun `WORKFLOW_06_VAULT_HEALTH_CHECK` + `DocIntegrityChecker` + `SemanticNoiseChecker` a chaque lot documentaire et revalider ce registre a chaque fermeture de risque.

## Changelog
- v1.18 (13-03-2026) : rehost dans `EVIDENCE_00_FRAMEWORK` et renumerotation `EVIDENCE_02 -> EVIDENCE_03`.
- v1.17 (13-03-2026) : ajoute la trace du lot final `WORKFLOW + SETUP_PRODUCT` sans ouverture de nouveau risque.
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
- v1.13 (09-03-2026) : passage en FROZEN + ajout des controles `SemanticNoiseChecker` et `frontmatter_utils`.
- v1.14 (09-03-2026) : bascule semantique EVIDENCE vers FRAMEWORK canon + alignement des liens.
- v1.15 (10-03-2026) : trace lot setup SYSTEM_04_LLM + creation instructions verite Codex IDE + conversion `SCRIPT_03` en skill avec projection executable.
- v1.16 (10-03-2026) : ajoute la trace hygiene repo (`.gitignore` -> `skills/`) et le retrait de `SCRIPT_03_GIT_BOOTSTRAP_AGENT.md`.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
