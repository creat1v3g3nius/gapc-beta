---
id: GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS
type: TOOLING
title: GapcAllowedTools
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, knowledge, allowlist, p1]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, DISCIPLINE_06_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_01_GEL_RULES, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, EXTENSION_00_INDEX, KNOWLEDGE_01_AI_CODING_LIST, KNOWLEDGE_03_LLM_PLATFORM_LIST]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_00_KNOWLEDGE
---

# GAPC_TOOLING_KNOWLEDGE_00 - Allowed Tools

## Objet
Définir une **allowlist** d’outils autorisés/recommandés pour exécuter GAPC (réduction du bruit + conformité).

## A) Coding (exécution repo)
### Autorisés (par défaut)
- VS Code
- Git (CLI)
- Cursor (si workflow diff-first)

### Interdits (par défaut)
- auto-commit / auto-push
- outils qui imposent l’écriture automatique dans le repo

## B) Mentor / RAG
### Autorisés (selon contexte)
- AnythingLLM (workspaces séparés, read-only)

### Interdits (par défaut)
- ingestion “all vault”
- workspaces multi-packages

## C) Générateurs média
- Autorisés : uniquement via protocoles EXTENSION + Evidence Pack
- Interdits : usage PII/visages réels sans consentement

## Règles
- Toute exception doit être tracée (ADR-lite) si structurante.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
