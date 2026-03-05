---
id: PIPELINE_05_RELEASE_FREEZE
type: TOOLING
title: ReleaseFreeze
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, pipeline, freeze, release, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_02_PIPELINE
---

# PIPELINE_05 - Release / Freeze (CORE)

## Objet
Pipeline générique de gel :
- passer READY_TO_FREEZE
- passer FROZEN
- produire un artefact “release note” minimal

CORE strict : pas de commandes (SYSTEM décrit le comment).

---

## 1) READY_TO_FREEZE (P0)
Conditions minimales :
- conformité doc/code/rag selon gates applicables,
- no-secrets,
- risques critiques mitigés.

Output :
- statut READY_TO_FREEZE
- rapport (gates + risques)
- release note si nécessaire (`TPL_10_RELEASE_NOTE`)

---

## 2) FROZEN (P0)
Conditions minimales :
- READY_TO_FREEZE PASS,
- amendements contrôlés,
- reproductibilité (via procédure SYSTEM associée),
- zéro P0 ouvert.

Output :
- statut FROZEN
- changelog / release note à jour

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

---

### Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : création pipeline gel/release CORE.

## Changelog
- v1.2 (02-03-2026) : normalisation frontmatter.
- v1.3 (04-03-2026) : correction heading.
