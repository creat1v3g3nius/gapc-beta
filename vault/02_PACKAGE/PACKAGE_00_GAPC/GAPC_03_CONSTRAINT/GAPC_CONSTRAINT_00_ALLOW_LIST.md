---
id: GAPC_CONSTRAINT_00_ALLOW_LIST
type: CONSTRAINT
title: GapcAllowlist
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 14-11-2026
tags: [package, gapc, constraint, allowlist, p1, no-secrets]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - GAPC_TOOLING_EXTENSION_00_ALLOW_LIST
  - GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_03_CONSTRAINT
---

# GAPC_CONSTRAINT_00 - Allowlist

## Objet

Fixer, au niveau PACKAGE GAPC, une **contrainte** : ce qui est autorisé/interdit
pour exécuter GAPC.
But : réduire le bruit et éviter les usages non gouvernés.

---

## 1) Autorisés (par défaut)

- Outils de dev : VS Code, Git CLI
- Agent LLM : Claude Code (`LLM_04_AGENT_CLAUDE`), mode MENTOR en Plan mode
  (read-only), mode EXECUTION diff-first
- Extensions : uniquement celles présentes dans CORE/EXTENSION et autorisées par

  `GAPC_TOOLING_EXTENSION_00_ALLOW_LIST`

## 2) Interdits (par défaut) — P0

- auto-commit / auto-push
- session sans package actif declare pour une question package
- multi-packages ou multi-products simultanément
- toute extension non documentée dans CORE
- PII/visages réels sans consentement

## 3) Règle P0

Toute exception est **KO** sans `GAPC_CONSTRAINT_02_EXCEPTION_POLICY`.

---

## Changelog

- v1.3 (14-11-2026) : roles realignes sur l agent Claude (`Agent MENTOR / Agent

  EXECUTION / Humain`), references AnythingLLM / Codex / API fallback retirees.

- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : création allowlist GAPC (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
