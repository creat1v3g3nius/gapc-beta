---
id: PIPELINE_01_RUNBOOK_PRODUCT
type: TOOLING
title: RunbookProduct
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, pipeline, runbook, product, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE, PIPELINE_00_PRODUCT]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_02_PIPELINE
---

# PIPELINE_01 - Runbook Product (CORE)

## Objet
Définir le **cadre opérateur** d’une session de production product, sans détailler les commandes :
- démarrer
- produire
- clôturer
- gérer un incident

CORE strict : renvoie vers SYSTEM pour “comment faire”.

---

## 1) Start (P0)
- Fixer actifs (package/product).
- Fixer l’intention (1 CO).
- Sélectionner les sources (RulesOnly → couches) selon `CONSTRAINT_01_RAG_SCOPE_POLICY`.
- Choisir le livrable (PRD/Spec/ADR/Doc/Code).

**Output** : CO actif + plan.

---

## 2) During (P0)
- Exécuter selon `PIPELINE_00_PRODUCT`.
- Appliquer guardrails : no-secrets, non-duplication, non-invention, actifs uniques.

**Output** : artefacts + patchs.

---

## 3) End (P0)
- Valider les gates applicables (DocQG/CodeQG/RagQG).
- Mettre à jour risques (Risk Register) si nécessaire.
- Produire next step unique.

**Output** : rapport de session.

---

## 4) Incident (P0)
Si dérive / contradiction / fuite / mélange :
- Stop.
- Isoler actifs / réduire corpus.
- Tracer le risque et la mitigation.
- Reprendre seulement après correction.

(SYSTEM contient la checklist concrète.)

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

---

### Changelog
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : création runbook product CORE (cadre).

## Changelog
- v1.3 (04-03-2026) : correction heading.
- v1.2 (02-03-2026) : normalisation frontmatter.
