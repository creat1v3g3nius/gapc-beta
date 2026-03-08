---
id: EVIDENCE_03_ADR_DOD_SCOPE
type: EVIDENCE
title: AdrDodScope
version: v1.3
status: READY_TO_FREEZE
created: 06-03-2026
updated: 09-03-2026
tags: [system, evidence, adr, dod, scope]
depends_on: [OPS_02_SPEC_DOD, TPL_02_ADR_LITE, RUN_06_VAULT_HEALTH_CHECK, RUN_07_OPTIMIZATION_PROCESS, EVIDENCE_04_R0001_TOUCHED_FILES]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE
---

# EVIDENCE_03 - ADR DoD Scope

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
- Decision confirmee: la preuve est maintenue en chaines canoniques `OPS_* -> DOD_* -> EVIDENCE_*` avec references d'ID et sans duplication locale.

## Consequences
- Positives: verdict de conformite coherent avec l'exigence globale.
- Negatives: lot de correction plus large.
- Dette creee: aucune sur le scope DocQG global.
- Backout plan: revert du lot evidence + correction globale associee.

## Mise en oeuvre
- RUN_07 execute sur tout le vault avec PASS structurel (naming/frontmatter/depends_on coherents).
- Relocalisation des preuves validee dans `SYSTEM_10_EVIDENCE`.
- Validator global et Smoke runner executes avec PASS.
- Tracabilite R-0001 consolidee dans `EVIDENCE_04_R0001_TOUCHED_FILES`.

## Next Step Unique
- Pousser le commit de normalisation et rerun `RUN_06_VAULT_HEALTH_CHECK`.

## Changelog
- v1.1 (06-03-2026) : decision de scope mise a jour vers DocQG global `vault/`.
- v1.2 (09-03-2026) : confirmation de l'execution globale (RUN_07) et formalisation de la chaine canonique `OPS_* -> DOD_* -> EVIDENCE_*`.
- v1.3 (09-03-2026) : ajoute la reference consolidee des fichiers touches par R-0001.
