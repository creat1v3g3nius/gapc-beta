---
id: PIPELINE_04_OPTIMIZATION_PROTOCOL
type: TOOLING
title: OptimizationProtocol
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, pipeline, optimization, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_02_PIPELINE
---

# PIPELINE_04 - Optimization Protocol

## Objet
Éviter l’optimisation prématurée et encadrer l’optimisation quand elle est justifiée.

---

## 1) Règle CORE
On n’optimise que si :
- un problème est observé (signal),
- l’impact est mesurable,
- le coût est maîtrisé.

Sinon : NEXT/LATER.

---

## 2) Déclencheurs (P0)
Optimisation autorisée si :
- un gate échoue à cause de perf/stabilité,
- un risque critique est ouvert (score 6–9) lié à perf/ops,
- une contrainte explicite de product le requiert (dans PRODUCT, pas ici).

---

## 3) Format d’optimisation (P0)
Tout travail d’optimisation doit déclarer :
- Signal (mesure)
- Hypothèse (cause probable)
- Option(s)
- Plan minimal
- PASS/FAIL attendu
- Backout plan

---

## 4) Stop conditions
- optimisation “pour faire propre”
- refactor massif sans demande
- métriques absentes

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

---

### Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : création protocole d’optimisation CORE.

## Changelog
- v1.3 (04-03-2026) : correction heading.
- v1.2 (02-03-2026) : normalisation frontmatter.
