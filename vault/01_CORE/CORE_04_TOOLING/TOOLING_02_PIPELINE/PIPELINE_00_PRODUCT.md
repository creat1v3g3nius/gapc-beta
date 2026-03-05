---
id: PIPELINE_00_PRODUCT
type: TOOLING
title: PipelineProduct
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, pipeline, product, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_02_PIPELINE
---

# PIPELINE_00 - Pipeline Product (CORE)

## Objet
Pipeline **générique** pour produire un product de façon reproductible :
- anti-dérive (scope / actifs uniques)
- traçabilité (ADR)
- qualité (gates doc/code/RAG)
- gel (READY_TO_FREEZE → FROZEN)

CORE strict : aucune commande opérateur. Les procédures vivent dans SYSTEM.  
Les exigences métier vivent dans PACKAGE/PRODUCT.

---

## 0) Pré-conditions (P0)
- Actifs : 1 package actif (ou NA), 1 product actif (si contexte product).
- No-secrets / no-PII.
- 1 intention = 1 CO = 1 commit (ou squash).

---

## 1) Phase A — Cadrage (PRD)
**Input** : idée / besoin  
**Output** : PRD 1-page

- Produire un PRD via `TPL_00_PRDONEPAGER`.
- Classifier les items majeurs via `DISCIPLINE_06_SCOPECLASSIFIER` (NOW/NEXT/LATER/REJECT).
- Si décision structurante détectée → ADR via `TPL_02_ADRLITE`.

**Gate** : DocQG READY_TO_FREEZE (sur le PRD).

---

## 2) Phase B — Découpage (Backlog Product → CO)
**Output** : Backlog product + CO atomiques

- Construire backlog product (voir `PIPELINE_02_BACKLOG_PRODUCT`).
- Produire CO atomiques via `TPL_03_BACKLOGCO` (1 intention).
- Pour chaque CO : définir output + PASS/FAIL + risques.

**Gate** : cohérence scope (pas de multi-arcs sans découpage).

---

## 3) Phase C — Spécification (Spec Tech)
**Output** : Spec Tech + décisions

- Produire spec via `TPL_01_SPECTECH`.
- Tracer décisions structurantes via `TPL_02_ADRLITE`.
- Définir smoke plan via `TPL_04_TESTPLANSMOKE` (si exécution).

**Gate** : DocQG READY_TO_FREEZE (Spec + ADR).

---

## 4) Phase D — Exécution (Action Doc / Action Code)
**Output** : patches doc/code, commits, validation

- Action Doc : `TPL_05_ACTIONDOC` (diff-first).
- Action Code : `TPL_06_ACTIONCODE` (diff-first).
- Review : `TPL_09_REVIEWCHECK`.

**Gates** :
- CodeQG MERGE (si code/scripts touchés).
- DocQG READY_TO_FREEZE (si docs touchés).
- RAGQG READY_TO_FREEZE (si le mentor est utilisé comme exécution).

---

## 5) Phase E — Gel / Release
**Output** : état READY_TO_FREEZE puis FROZEN

- Déclarer READY_TO_FREEZE via `DISCIPLINE_01_GELRULES`.
- Produire Release Note via `TPL_10_RELEASENOTE` si gel/release.
- Passer FROZEN si critères de gel satisfaits (amendements contrôlés, reproductibilité, zéro P0 ouvert).

---

## 6) Sortie standard (rapport)
- Ce qui a été livré (IDs)
- Gates PASS/FAIL
- Risques ouverts (avec mitigations)
- Next step unique

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

---

### Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : création pipeline product CORE (P0).

## Changelog
- v1.2 (02-03-2026) : normalisation frontmatter.
- v1.3 (04-03-2026) : corrections des ids `depends_on` + heading.
