---
id: GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS
type: TOOLING
title: GapcAllowedTools
version: v1.4
status: FROZEN
created: 01-03-2026
updated: 14-11-2026
tags: [package, gapc, tooling, knowledge, allowlist, p1]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_04_RISK_REGISTER
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_01_GEL_RULES
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - EXTENSION_04_EVIDENCE_PACK
  - KNOWLEDGE_01_AI_CODING_LIST
  - KNOWLEDGE_03_LLM_PLATFORM_LIST
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_00_KNOWLEDGE
---

# GAPC_TOOLING_KNOWLEDGE_00 - Allowed Tools

## Objet

Définir une **allowlist** d’outils autorisés/recommandés pour exécuter GAPC
(réduction du bruit + conformité).

## A) Coding (exécution repo)

### Autorisés (par défaut)

- VS Code
- Git (CLI)
- Claude Code en mode EXECUTION (diff-first, approbations actives)

### Interdits RAG (par défaut)

- auto-commit / auto-push
- outils qui imposent l’écriture automatique dans le repo

## B) Agent LLM (mode MENTOR)

### Autorisés (selon contexte)

- Claude Code en Plan mode (read-only), perimetre declare

### Interdits (par défaut)

- lecture de plusieurs packages dans une session
- acceptation automatique des modifications

## C) Générateurs média

- Autorisés : uniquement via protocoles EXTENSION + Evidence Pack
- Interdits : usage PII/visages réels sans consentement

## Règles

- Toute exception doit être tracée (ADR-lite) si structurante.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (14-11-2026) : roles realignes sur l agent Claude (`Agent MENTOR / Agent

  EXECUTION / Humain`), references AnythingLLM / Codex / API fallback retirees.

- v1.3 (09-03-2026) : remplace la dependance deprecated `EXTENSION_00_INDEX` par

  `EXTENSION_04_EVIDENCE_PACK`.

- v1.2 (04-03-2026) : correction `scope` du frontmatter
- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
