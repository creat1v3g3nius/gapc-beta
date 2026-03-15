---
id: EVIDENCE_04_ADR_FRAMEWORK_SCOPE
type: EVIDENCE
title: AdrFrameworkScope
version: v1.14
status: FROZEN
created: 06-03-2026
updated: 13-03-2026
tags: [system, evidence, adr, framework, scope]
depends_on: [OPS_SAMPLE_02_SPEC_DOD, TPL_02_ADR_LITE, WORKFLOW_06_VAULT_HEALTH_CHECK, EVIDENCE_03_RISK_REGISTER, SCRIPT_04_DOC_INTEGRITY_CHECKER, SCRIPT_05_SEMANTIC_NOISE_CHECKER, SCRIPT_06_FRONTMATTER_UTILS, LLM_00_RAG_PRINCIPES, LLM_01_INGESTION_PROTOCOL, LLM_02_PERMISSION_SECURITY, LLM_03_MENTOR_UTILITES, SCRIPT_03_INSTRUCTIONS_CODEX]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_00_FRAMEWORK
---

# EVIDENCE_04 - ADR Framework Scope

## Statut
- Status: ACCEPTED
- Date: 06-03-2026
- Owner: framework-owner
- Liens: `OPS_SAMPLE_01_PRD_DOD`, `OPS_SAMPLE_02_SPEC_DOD`

## Contexte
- Le besoin de validation a ete releve: le DocQG PASS doit couvrir tout `vault/`.
- Le lot evidence doit donc tracer une execution globale et non plus limitee au product.
- Le setup operationnel a ete mis a jour avec les documents SYSTEM_04_LLM.
- Les instructions verite Codex IDE ont ete formalisees via `SCRIPT_03_INSTRUCTIONS_CODEX`.

## Options
### Option A
- Description: corriger tout le vault avant de rejouer la validation framework canon globale.
- Pros: homogeneite globale immediate.
- Cons: effort initial plus large.
- Risques: augmentation du temps de traitement.

### Option B
- Description: corriger strict sur le scope produit + evidence thin-slice complete.
- Pros: delivre une preuve rapide.
- Cons: ne repond pas a l'exigence de DocQG global.
- Risques: verdict framework canon incomplet.

## Decision
- Option A retenue: validation framework canon globale avec DocQG strict sur l'ensemble du vault.
- Decision confirmee: la preuve est maintenue en chaines canoniques `OPS_* -> FRAMEWORK_* -> EVIDENCE_*` avec references d'ID et sans duplication locale.
- Decision complementaire: clarifier la chaine SOT Codex IDE:
  - `CORE/PACKAGE/PRODUCT` = SOT de fond
  - `SCRIPT_03_INSTRUCTIONS_CODEX` = SOT procedurale Codex
  - `skills/codex-ide-instructions/SKILL.md` = projection executable
- Decision complementaire: aligner l hygiene repo sur ce cadre:
  - ignorer `skills/` via `.gitignore`
  - retirer `SCRIPT_03_GIT_BOOTSTRAP_AGENT.md` du scope actif
- Decision complementaire: converger `SYSTEM` vers :
  - `WORKFLOW_*` pour l execution quotidienne
  - `SETUP_PRODUCT_*` pour bootstrap, maintien, cycle de vie et gouvernance
- Decision complementaire: stabiliser le host SYSTEM de cette convergence en :
  - `SYSTEM_01_RUN` comme famille SYSTEM canonique
  - `RUN_00_WORKFLOW` comme sous-lot d execution quotidienne
  - `RUN_01_SETUP_PRODUCT` comme sous-lot de composition produit
  - `CACHE_SYSTEM_01_RUN` pour les annexes legacy sorties du scope actif

## Consequences
- Positives: verdict de conformite coherent avec l'exigence globale.
- Negatives: lot de correction plus large.
- Dette creee: aucune sur le scope DocQG global.
- Backout plan: revert du lot evidence + correction globale associee.

## Mise en oeuvre
- WORKFLOW_07 execute sur tout le vault avec PASS structurel (naming/frontmatter/depends_on coherents).
- Relocalisation des preuves validee dans `SYSTEM_10_EVIDENCE/EVIDENCE_00_FRAMEWORK`.
- Validator global et Smoke runner executes avec PASS.
- DocIntegrityChecker implemente et integre au SmokeRunner avec PASS (`P0=0`, `P1=0`).
- SemanticNoiseChecker implemente avec PASS (`P0=0`, `P1=0`).
- Parsing frontmatter factorise via `frontmatter_utils` pour alignement des checks.
- Tracabilite R-0001 consolidee dans l'archive cache/deprecated `vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE/EVIDENCE_04_R0001_TOUCHED_FILES.md`.
- Registre de risques consolide et renomme en `EVIDENCE_03_RISK_REGISTER` (R-0011 clos).
- Setup operationnel aligne avec SYSTEM_04_LLM:
  - `LLM_00_RAG_PRINCIPES`
  - `LLM_01_INGESTION_PROTOCOL`
  - `LLM_02_PERMISSION_SECURITY`
  - `LLM_03_MENTOR_UTILITES`
- Conversion de `SCRIPT_03_INSTRUCTIONS_CODEX` en skill `codex-ide-instructions` avec creation des 3 fichiers:
  - `skills/codex-ide-instructions/SKILL.md`
  - `skills/codex-ide-instructions/agents/openai.yaml`
  - `skills/codex-ide-instructions/references/codex_ide_baseline.md`
- Hygiene repo appliquee:
  - `.gitignore` inclut `skills/`
  - `vault/00_SYSTEM/SYSTEM_03_SCRIPT/SCRIPT_03_GIT_BOOTSTRAP_AGENT.md` retire
- Migration `WORKFLOW + SETUP_PRODUCT` executee:
  - `SYSTEM_01_RUN` retabli comme host canonique
  - `RUN_00_WORKFLOW` reserve la couche operatoire `WORKFLOW_*`
  - `RUN_01_SETUP_PRODUCT` porte la famille `SETUP_PRODUCT_*`
  - `WORKFLOW_01` et `WORKFLOW_02` declasses puis archives en `CACHE_SYSTEM_01_RUN`
  - `SETUP_PRODUCT_00..07` actives
  - doctrine `WORKFLOW` vs `SETUP_PRODUCT` explicitee dans `WORKFLOW_00_PIPELINE`
  - index SYSTEM raccordes au cadre final

## Next Step Unique
- Maintenir un rerun `WORKFLOW_06_VAULT_HEALTH_CHECK` a chaque lot et conserver la coherence ADR <-> Risk Register.

## Changelog
- v1.14 (13-03-2026) : rehost dans `EVIDENCE_00_FRAMEWORK` et renumerotation `EVIDENCE_03 -> EVIDENCE_04`.
- v1.13 (13-03-2026) : ajoute la stabilisation finale de la famille `SYSTEM_01_RUN` avec `RUN_00_WORKFLOW`, `RUN_01_SETUP_PRODUCT` et archivage legacy en `CACHE_SYSTEM_01_RUN`.
- v1.12 (13-03-2026) : ajoute la decision complementaire de convergence `WORKFLOW + SETUP_PRODUCT` et sa mise en oeuvre.
- v1.1 (06-03-2026) : decision de scope mise a jour vers DocQG global `vault/`.
- v1.2 (09-03-2026) : confirmation de l'execution globale (WORKFLOW_07) et formalisation de la chaine canonique `OPS_* -> FRAMEWORK_* -> EVIDENCE_*`.
- v1.3 (09-03-2026) : ajoute la reference consolidee des fichiers touches par R-0001.
- v1.4 (09-03-2026) : aligne l'ADR avec le registre de risques consolide (`EVIDENCE_03_RISK_REGISTER`) et la cloture de R-0011.
- v1.5 (09-03-2026) : retire la dependance active a `EVIDENCE_04` et conserve la trace via archive CACHE/DEPRECATED.
- v1.6 (09-03-2026) : retire la dependance active a `RUN_07_OPTIMIZATION_PROCESS` (deprecated).
- v1.7 (09-03-2026) : ajoute la decision d'integration `DocIntegrityChecker` et confirme PASS en orchestration smoke.
- v1.8 (09-03-2026) : passage en FROZEN + integration `SemanticNoiseChecker` et `frontmatter_utils`.
- v1.9 (09-03-2026) : bascule de naming/ID ADR vers la version FRAMEWORK canon.
- v1.10 (10-03-2026) : ajoute la decision SOT Codex IDE, la reference setup SYSTEM_04_LLM et la conversion `SCRIPT_03` en skill (3 fichiers `skills/`).
- v1.11 (10-03-2026) : ajoute la decision hygiene repo (`.gitignore` -> `skills/`) et la trace du retrait `SCRIPT_03_GIT_BOOTSTRAP_AGENT.md`.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
