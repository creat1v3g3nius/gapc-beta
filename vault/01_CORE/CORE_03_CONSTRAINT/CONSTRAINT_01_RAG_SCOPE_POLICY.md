---
id: CONSTRAINT_01_RAG_SCOPE_POLICY
type: CONSTRAINT
title: RagScopePolicy
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 09-03-2026
tags: [limites, rag-scope-policy, llm, discipline, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_01 - RAG Scope Policy (contraintes transversales)

## Objet
Fixer les contraintes CORE qui gouvernent le **scope de corpus RAG** :
- réduire le bruit,
- empêcher le mélange multi-package/product,
- garantir la non-invention,
- permettre des profils scalables (RulesOnly → PackageScoped → ProductScoped).

CORE strict : aucune procédure d’ingestion/tests ici (SYSTEM/LLM).

---

## 1) Règles P0 (bloquantes)

### 1.1 Small-first
Le corpus doit démarrer en **RulesOnly** (profil R0) avant toute extension.

### 1.2 Extension par couches
Toute extension du corpus doit être faite par **couches explicites** :
- CORE/SYSTEM minimal → + PACKAGE actif → + PRODUCT actif.

Interdit : ingérer “tout le vault” comme mode nominal.

### 1.3 Actifs uniques
Un corpus scoped doit être associé à :
- 1 package actif unique (si PackageScoped/plus),
- 1 product actif unique (si ProductScoped).

### 1.4 Séparation des profils
Un profil ne doit pas répondre sur un scope hors profil :
- RulesOnly ne répond pas “métier produit”,
- PackageScoped ne répond pas sur un autre package,
- ProductScoped ne répond pas sur un autre product.

### 1.5 NON TROUVÉ
Si l’information n’est pas dans le corpus ingéré : `NON TROUVÉ` (jamais de complétion plausible).

---

## 2) Règles P1 (renforcement)
- Minimiser la duplication de sources (référencer).
- Préférer des workspaces dédiés par profil plutôt qu’un workspace “global”.

---

## 3) Contrat d’extension
PACKAGE/PRODUCT peuvent :
- renforcer les contraintes (tests plus stricts, règles de sélection internes),
- définir des priorités **internes** (dans leur périmètre).

Ils ne peuvent pas :
- autoriser multi-packages/products,
- assouplir `NON TROUVÉ`,
- supprimer le principe “small-first”.

---

## Changelog
- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.0 (01-03-2026) : création des contraintes CORE de scope RAG.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
