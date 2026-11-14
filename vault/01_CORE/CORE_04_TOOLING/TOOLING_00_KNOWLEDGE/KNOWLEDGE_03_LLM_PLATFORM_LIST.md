---
id: KNOWLEDGE_03_LLM_PLATFORM_LIST
type: TOOLING
title: LlmPlatformList
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 14-11-2026
tags: [tooling, knowledge, llm-plateform, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_03 — LLM Platform List (RAG / Mentor) (CORE)

## Objet

Typologie des plateformes LLM utiles à GAPC (mentor RAG, workspaces, ingestion),
sans procédure.

---

## 1) Plateformes “Mentor RAG”

- **AnythingLLM** — workspaces + ingestion, mentor “corpus-first”.
- **RAG custom** — pipeline maison (plus flexible, plus coûteux).

## 2) Agents intégrés IDE

- **Copilot Chat / Agents** — in-editor, rapides pour patchs.
- **Codex / assistants VS Code** — à cadrer via prompt system.
- **Claude Code** — agent IDE/CLI qui lit le repo et peut l exécuter ; cadré
  par un fichier d instructions à la racine et un mode lecture seule (plan).

## 3) Critères de choix (P0)

- **Workspaces / scopes** : RulesOnly vs PackageScoped vs ProductScoped (par
  ingestion, ou par périmètre de lecture déclaré pour un agent IDE).
- **Citations / sources** : capacité à montrer “d’où vient la réponse”.
- **Contrôle** : mode lecture seule disponible, pas d’actions non demandées.
- **Hébergement** : local ou service externe (impact confidentialité).
- **Sécurité** : gestion des permissions, logs, no-secrets.
- **Export** : possibilité de tracer (notes, prompts, résultats).

## 4) Risques récurrents

- hallucination (absence de `NON TROUVÉ`)
- mélange multi-package/product
- ingestion “tout le vault” → bruit
- logs sensibles

### Extensions PACKAGE/PRODUCT

- Ajouter “plateformes autorisées” + exigences légales (si besoin).
- Ajouter critères de performance (latence/coût) pour un product.

---

## Historique initial

- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (14-11-2026) : ajoute Claude Code et les criteres perimetre de lecture /

  hebergement.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
