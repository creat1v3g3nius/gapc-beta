---
id: README
type: SYSTEM
title: Readme00System
version: v1.4
status: FROZEN
created: 02-03-2026
updated: 14-11-2026
tags: [system, readme, entrypoint]
depends_on: [INDEX_01_ARCHITECTURE, INDEX_02_REPOSITORY, INDEX_05_GLOSSARY, WORKFLOW_00_PIPELINE, SETUP_PRODUCT_00_INDEX, EVIDENCE_00_FRAMEWORK_INDEX, LLM_04_AGENT_CLAUDE, SCRIPT_07_INSTRUCTIONS_CLAUDE]
arc: SYSTEM
scope: vault/00_SYSTEM
---

# 00_SYSTEM — README

## Rôle du dossier

`00_SYSTEM/` contient les **procédures opérateur** : comment exécuter le
framework (sessions, configuration, runbooks, incidents), **sans** porter la
“vérité” des règles.

- **SYSTEM = procédures** (comment faire)
- **CORE = règles transversales** (source of truth)
- **PACKAGE = règles métier** (CORE transposé)
- **PRODUCT = espace de travail** (preuves, DoD, exécution locale)

> Règle : si une règle est “transversale”, elle vit en **CORE**. SYSTEM pointe
  vers CORE, il ne redéfinit pas.

## Entrées essentielles (P0)

- **Architecture système** : `INDEX_01_ARCHITECTURE`
- **Arborescence complète** : `INDEX_02_REPOSITORY`
- **Glossaire** : `INDEX_05_GLOSSARY`
- **Runbooks quotidiens** : `WORKFLOW_00_PIPELINE`
- **Setup produit** : `SETUP_PRODUCT_00_INDEX`
- **Preuves framework** : `EVIDENCE_00_FRAMEWORK_INDEX`
- **Agent LLM (Claude)** : `LLM_04_AGENT_CLAUDE`, instructions

  `SCRIPT_07_INSTRUCTIONS_CLAUDE` (projection `CLAUDE.md`)

## Structure actuelle (P0)

- `SYSTEM_01_RUN` porte l execution quotidienne et le setup produit.
- `RUN_00_WORKFLOW` porte `WORKFLOW_00/03/04/05/06/07/08/10`.
- `RUN_01_SETUP_PRODUCT` porte `SETUP_PRODUCT_00..07`.
- `SYSTEM_02_GIT` porte le noyau Git actif : `GIT_01`, `GIT_02`, `GIT_03`.
- `SYSTEM_03_SCRIPT` porte le noyau outillage actif : `SCRIPT_00`, `SCRIPT_01`,

  `SCRIPT_04`, `SCRIPT_05`, `SCRIPT_06`, `SCRIPT_07`.

- `SYSTEM_04_LLM` porte le dispositif agent Claude (`LLM_04`).
- `SYSTEM_10_EVIDENCE` est scinde entre `EVIDENCE_00_FRAMEWORK` et

  `EVIDENCE_01_AGENTS`.

- `99_CACHE` est une zone d archivage, jamais une source de verite.

## Conventions non négociables

### Frontmatter (YAML)

- `id == filename`
- champs : `created`, `updated`, `depends_on`, `arc`, `scope`
- `scope` = chemin logique (pas juste `vault`)

### Exécution

- diff-first, no auto-commit, 1 intention = 1 commit
- no-secrets / no-PII

### Agent LLM (modes MENTOR / EXECUTION)

- sources obligatoires (IDs) ; sinon `NON TROUVÉ`
- actifs uniques : 1 package actif (+ 1 product actif si contexte product)
- pas de mélange multi-package/product
- cadrage nominal : `LLM_04_AGENT_CLAUDE`, `SCRIPT_07_INSTRUCTIONS_CLAUDE`

## Workflow recommandé (P0)

1. Fixer actifs (package/product) et ouvrir le cadre via `WORKFLOW_00_PIPELINE`
1. Fixer intention (1 objectif)
1. Choisir cible (DRAFT → READY_TO_FREEZE → FROZEN)
1. Produire avec `WORKFLOW_03_START_SESSION`, `WORKFLOW_04_END_SESSION`,

   `WORKFLOW_05_INCIDENT`, `WORKFLOW_10_COMMANDES`

1. Valider avec `WORKFLOW_06_VAULT_HEALTH_CHECK`, puis `WORKFLOW_07_TESTS_LLM` /

   `WORKFLOW_08_TESTS_EXECUTION` si le lot le demande

1. Tracer dans `EVIDENCE_00_FRAMEWORK_INDEX` (preuves framework) ou dans le

   product qui porte la preuve

## Modifier un document FROZEN

Patch ciblé + validation + version bump + changelog (amendements contrôlés).

## Où mettre quoi

- Procédure → SYSTEM
- Règle transverse → CORE
- Overlay métier → PACKAGE
- Preuves/DoD/logs → PRODUCT

## Références rapides

- exécution quotidienne : `WORKFLOW_*`
- bootstrap / profil / cycle de vie / gouvernance produit : `SETUP_PRODUCT_*`
- preuves framework globales : `EVIDENCE_00_FRAMEWORK/*`
- preuves agents AnythingLLM / Codex (archivees) : `99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_10_EVIDENCE/CACHE_EVIDENCE_01_AGENTS/*`
- agent LLM : `SYSTEM_04_LLM/*`, `SCRIPT_07_INSTRUCTIONS_CLAUDE`
- archivage historique : `99_CACHE/*`

## Changelog

- v1.4 (14-11-2026) : realigne sur l agent Claude (modes MENTOR / EXECUTION) ;

  references AnythingLLM / Codex retirees (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- v1.3 (13-03-2026) : aligne le README sur la structure active `WORKFLOW /

  SETUP_PRODUCT / EVIDENCE_00_FRAMEWORK / EVIDENCE_01_AGENTS / SYSTEM_04_LLM`.

- v1.2 (02-03-2026) : rédaction complète README 00_SYSTEM.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
