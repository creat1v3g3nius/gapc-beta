---
id: KNOWLEDGE_00_INDEX
type: TOOLING
title: KnowledgeIndex
version: v1.2
status: DEPRECATED
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, knowledge, index, core]
depends_on: []
arc: CACHE
scope: vault/99_CACHE/CACHE_02_CORE/CACHE_CORE_04_TOOLING/
---

# KNOWLEDGE_00 - Index (CORE)

## Objet

Index des listes “KNOWLEDGE” (référentiels) destinées au mentor et à la
production.

- format : listes courtes, catégorisées, RAG-friendly
- pas de procédures opérateur
- no-secrets / no-PII

---

## 1) Listes

- [[KNOWLEDGE_01_AI_CODING_LIST]] — outils et patterns de dev assisté IA
- [[KNOWLEDGE_02_AI_GENERATOR_LIST]] — générateurs (image/vidéo/audio/3D/docs)
- [[KNOWLEDGE_03_LLM_PLATFORM_LIST]] — plateformes LLM/RAG (workspaces,
  ingestion)
- [[KNOWLEDGE_04_DATA_SOURCE_LIST]] — sources d’ingestion + typologies
- [[KNOWLEDGE_05_MOVIE_FESTIVAL_LIST]] — festivals (typologie)
- [[KNOWLEDGE_06_STARTUP_STACK_LIST]] — stack produit (par catégories)
- [[KNOWLEDGE_07_NO_CODE_TOOLS_LIST]] — no-code/low-code (familles)
- [[KNOWLEDGE_08_SECURITY_BASELINE]] — baseline sécurité (référentiel)

## 2) Convention de contenu

Chaque liste contient :

- **Catégories**
- **Items** (10–30 max) avec “note d’usage” 1 ligne
- **Red flags** (3–7)
- **Extensions** (ce qu’un PACKAGE/PRODUCT peut ajouter)

### Changelog

- v1.0 (01-03-2026) : création index KNOWLEDGE (P0+P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.2 (04-03-2026) : correction heading + `depends_on` du frontmatter +
  déplacement du fichier dans CACHE.
