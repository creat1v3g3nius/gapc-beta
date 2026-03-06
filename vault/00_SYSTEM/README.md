---
id: README
type: SYSTEM
title: Readme00System
version: v1.2
status: FROZEN
created: 02-03-2026
updated: 02-03-2026
tags: [system, readme, entrypoint]
depends_on: [INDEX_05_GLOSSARY]
arc: SYSTEM
scope: vault/00_SYSTEM
---

# 00_SYSTEM — README

## Rôle du dossier
`00_SYSTEM/` contient les **procédures opérateur** : comment exécuter le framework (sessions, configuration, runbooks, incidents), **sans** porter la “vérité” des règles.

- **SYSTEM = procédures** (comment faire)
- **CORE = règles transversales** (source of truth)
- **PACKAGE = règles métier** (CORE transposé)
- **PRODUCT = espace de travail** (preuves, DoD, exécution locale)

> Règle : si une règle est “transversale”, elle vit en **CORE**. SYSTEM pointe vers CORE, il ne redéfinit pas.

## Entrées essentielles (P0)
- **Glossaire** : `INDEX_05_GLOSSARY`
- **Démarrer une session** : checklists/pipelines (CORE) + actifs fixés
- **Fin de session / gel / incident** : runbooks (SYSTEM) + gates (CORE)

## Conventions non négociables
### Frontmatter (YAML)
- `id == filename`
- champs : `created`, `updated`, `depends_on`, `arc`, `scope`
- `scope` = chemin logique (pas juste `vault`)

### Exécution
- diff-first, no auto-commit, 1 intention = 1 commit
- no-secrets / no-PII

### Mentor / RAG (si utilisé)
- sources obligatoires (IDs) ; sinon `NON TROUVÉ`
- actifs uniques : 1 package actif (+ 1 product actif si contexte product)
- pas de mélange multi-package/product

## Workflow recommandé (P0)
1) Fixer actifs (package/product)
2) Fixer intention (1 objectif)
3) Choisir cible (DRAFT → READY_TO_FREEZE → FROZEN)
4) Produire (TPL/PIPELINE)
5) Valider (DocQG/CodeQG/RagQG)
6) Tracer (Risk Register + ADR-lite si décision structurante)

## Modifier un document FROZEN
Patch ciblé + validation + version bump + changelog (amendements contrôlés).

## Où mettre quoi
- Procédure → SYSTEM
- Règle transverse → CORE
- Overlay métier → PACKAGE
- Preuves/DoD/logs → PRODUCT

## Changelog
- v1.2 (02-03-2026) : rédaction complète README 00_SYSTEM.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
