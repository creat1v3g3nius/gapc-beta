---
id: GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
type: TOOLING
title: GapcWorkspaceRules
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, pipeline, workspace, rag]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_01_RUNBOOK_PRODUCT, PIPELINE_02_BACKLOG_PRODUCT, PIPELINE_03_BACKLOG_COMPOSANT, PIPELINE_04_OPTIMIZATION_PROTOCOL, PIPELINE_05_RELEASE_FREEZE, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_02_RAG_QG, GAPC_TOOLING_PIPELINE_00_INDEX]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_02_PIPELINE
---

# GAPC_TOOLING_PIPELINE_01 - Workspace Rules (actifs + sources + RAG)

## Objet
Règles PACKAGE qui encadrent l’usage du workspace (PRODUCT) quand GAPC est actif :
- actifs uniques,
- profils de scope,
- priorités de sources GAPC-only,
- non-invention (`NON TROUVÉ`).

---

## 1) Actifs (P0)
- package actif : `PACKAGE_00_GAPC`
- product actif : `PRODUCT_XX` (si contexte product)

Interdit : multi-products ou multi-packages dans une réponse/exécution.

---

## 2) Profils (P0)
- **RulesOnly** : CORE + discipline GAPC (pas de product)
- **GAPC+Product** : CORE + GAPC + product actif

Règle : commencer petit (RulesOnly) puis étendre.

---

## 3) Priorités de sources (P0)
1) GAPC discipline (scope/risk/gel/rag)
2) autres docs package GAPC
3) CORE transverse
4) PRODUCT actif
5) SYSTEM (procédures)

Interdit : sources d’un autre package “actif”.

---

## 4) Qualité réponse/exécution (P0)
- sources obligatoires (IDs) ou `NON TROUVÉ`
- no-secrets/no-PII
- > 3 actions → backlog CO (pas liste vague)
- décision structurante → ADR-lite

---

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création règles workspace GAPC (P1).

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
