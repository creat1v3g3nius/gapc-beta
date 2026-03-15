---
id: KNOWLEDGE_01_AI_CODING_LIST
type: TOOLING
title: AiCodingList
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, ai-coding, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_01 — AI Coding List (CORE)

## Objet

Référentiel d’outils et de patterns pour coder avec assistance IA en respectant
:

- diff-first
- no auto-commit
- 1 intention = 1 commit
- no-secrets

---

## 1) Éditeurs / IDE (assistés IA)

- **VS Code** — standard extensible (tasks, git, extensions).
- **Cursor** — IDE orienté “AI pair programming”.
- **JetBrains + AI** — workflow IDE lourd mais solide (refactors, inspections).

## 2) Assistants IA (in-editor)

- **GitHub Copilot / Copilot Chat** — complétion + chat contextuel.
- **OpenAI/Codex (agent)** — génération patch/diff (à cadrer strictement).
- **Continue / Tabby** — alternatives self-host / open-source (selon contexte).

## 3) Qualité & lint (à coupler avec IA)

- **Ruff** (Python) — lint+format rapide.
- **Black** (Python) — format standard.
- **ESLint** (JS/TS) — lint.
- **Prettier** (JS/TS/MD) — format.
- **EditorConfig** — cohérence whitespace.

## 4) Tests & exécution rapide

- **pytest** (Python) — tests unitaires.
- **jest / vitest** (JS/TS) — tests.
- **smoke runner** (GAPC) — happy-path en 1 commande.

## 5) Patterns “AI-safe” (à appliquer)

- **Patch minimal** : “ne modifie que X fichiers”.
- **Explain-before-apply** : demander 3 bullets (quoi/pourquoi/risque).
- **Stage sélectif** : `git add -p`.
- **Refactor interdit sans demande** : pas de “cleanup” gratuit.
- **Rollback plan** : revert/switch branch.

## 6) Red flags (STOP)

- L’IA propose un commit automatique.
- Le diff touche 2 intentions ou 2 arcs (CORE + PRODUCT…).
- Ajout de dépendances lourdes sans ADR.
- Apparition de secrets/PII dans le diff.
- “Gros refactor” sans tests.

### Extensions PACKAGE/PRODUCT

- Ajouter une “stack list” locale (langage/libs).
- Ajouter des conventions de tests propres au product.

---

## Historique initial

- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
