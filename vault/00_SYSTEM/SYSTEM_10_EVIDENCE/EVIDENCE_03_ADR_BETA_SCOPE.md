---
id: EVIDENCE_03_ADR_BETA_SCOPE
type: EVIDENCE
title: AdrBetaScope
version: v1.8
status: FROZEN
created: 06-03-2026
updated: 09-03-2026
tags: [system, evidence, adr, beta, scope]
depends_on: [OPS_02_SPEC_DOD, TPL_02_ADR_LITE, RUN_06_VAULT_HEALTH_CHECK, EVIDENCE_02_RISK_REGISTER, SCRIPT_04_DOC_INTEGRITY_CHECKER, SCRIPT_05_SEMANTIC_NOISE_CHECKER, SCRIPT_06_FRONTMATTER_UTILS]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE
---

# EVIDENCE_03 - ADR Beta Scope

## Statut
- Status: ACCEPTED
- Date: 06-03-2026
- Owner: product-owner-beta-gapc
- Liens: `OPS_01_PRD_DOD`, `OPS_02_SPEC_DOD`

## Contexte
- Le besoin de validation a ete releve: le DocQG PASS doit couvrir tout `vault/`.
- Le lot evidence doit donc tracer une execution globale et non plus limitee au product.

## Options
### Option A
- Description: corriger tout le vault avant de rejouer la validation beta globale.
- Pros: homogeneite globale immediate.
- Cons: effort initial plus large.
- Risques: augmentation du temps de traitement.

### Option B
- Description: corriger strict sur `PRODUCT_00_BETA_GAPC` + evidence thin-slice complete.
- Pros: delivre une preuve rapide.
- Cons: ne repond pas a l'exigence de DocQG global.
- Risques: verdict beta incomplet.

## Decision
- Option A retenue: validation beta globale avec DocQG strict sur l'ensemble du vault.
- Decision confirmee: la preuve est maintenue en chaines canoniques `OPS_* -> BETA_* -> EVIDENCE_*` avec references d'ID et sans duplication locale.

## Consequences
- Positives: verdict de conformite coherent avec l'exigence globale.
- Negatives: lot de correction plus large.
- Dette creee: aucune sur le scope DocQG global.
- Backout plan: revert du lot evidence + correction globale associee.

## Mise en oeuvre
- RUN_07 execute sur tout le vault avec PASS structurel (naming/frontmatter/depends_on coherents).
- Relocalisation des preuves validee dans `SYSTEM_10_EVIDENCE`.
- Validator global et Smoke runner executes avec PASS.
- DocIntegrityChecker implemente et integre au SmokeRunner avec PASS (`P0=0`, `P1=0`).
- SemanticNoiseChecker implemente avec PASS (`P0=0`, `P1=0`).
- Parsing frontmatter factorise via `frontmatter_utils` pour alignement des checks.
- Tracabilite R-0001 consolidee dans l'archive cache/deprecated `vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE/EVIDENCE_04_R0001_TOUCHED_FILES.md`.
- Registre de risques consolide et renomme en `EVIDENCE_02_RISK_REGISTER` (R-0011 clos).

## Next Step Unique
- Maintenir un rerun `RUN_06_VAULT_HEALTH_CHECK` a chaque lot et conserver la coherence ADR <-> Risk Register.

## Changelog
- v1.1 (06-03-2026) : decision de scope mise a jour vers DocQG global `vault/`.
- v1.2 (09-03-2026) : confirmation de l'execution globale (RUN_07) et formalisation de la chaine canonique `OPS_* -> BETA_* -> EVIDENCE_*`.
- v1.3 (09-03-2026) : ajoute la reference consolidee des fichiers touches par R-0001.
- v1.4 (09-03-2026) : aligne l'ADR avec le registre de risques consolide (`EVIDENCE_02_RISK_REGISTER`) et la cloture de R-0011.
- v1.5 (09-03-2026) : retire la dependance active a `EVIDENCE_04` et conserve la trace via archive CACHE/DEPRECATED.
- v1.6 (09-03-2026) : retire la dependance active a `RUN_07_OPTIMIZATION_PROCESS` (deprecated).
- v1.7 (09-03-2026) : ajoute la decision d'integration `DocIntegrityChecker` et confirme PASS en orchestration smoke.
- v1.8 (09-03-2026) : passage en FROZEN + integration `SemanticNoiseChecker` et `frontmatter_utils`.
