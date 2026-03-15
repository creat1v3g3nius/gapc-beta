---
id: INDEX_01_ARCHITECTURE
type: INDEX
title: ArchitectureFrameworkGAPC
version: v1.10
status: FROZEN
created: 27-02-2026
updated: 13-03-2026
tags: [repo, framework-architecture, index, system]
depends_on: []
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_00_INDEX
---

# INDEX_01 - Architecture Framework GAPC

Ce document formalise l'architecture officielle du framework GAPC.

Il respecte strictement : - Les règles de naming (META_00) - Les règles
de frontmatter YAML (META_01) - La hiérarchie contractuelle CORE →
PACKAGE → PRODUCT.

---

## 1. Structure Générale du Repository

repo/ docs/ scripts/ vault/

Le Vault constitue la base de données.

---

## 2. Arcs du Système

Le système est structuré en 5 arcs principaux :

00_SYSTEM/ 01_CORE/ 02_PACKAGE/ 03_PRODUCT/ 99_CACHE/

Chaque arc contient uniquement les familles nécessaires à sa fonction.

---

## 3. 00_SYSTEM

Familles autorisées :

- INDEX
- WORKFLOW
- GIT
- SCRIPT
- LLM
- BACKLOG
- PATCH
- FAQ

Rôle : Documentation d'usage, procédures d'exécution, setup produit,
configuration Git, scripts de validation et protocole RAG.

Aucune règle produit ne doit exister dans cet arc.

### 3.1 WORKFLOW

`WORKFLOW_*` porte les runbooks d execution quotidienne :

- demarrage et cloture de session
- incident
- health check
- batteries de tests
- commandes operatoires

Noyau `WORKFLOW` actif :

- `WORKFLOW_00_PIPELINE`
- `WORKFLOW_03_START_SESSION`
- `WORKFLOW_04_END_SESSION`
- `WORKFLOW_05_INCIDENT`
- `WORKFLOW_06_VAULT_HEALTH_CHECK`
- `WORKFLOW_07_TESTS_LLM`
- `WORKFLOW_08_TESTS_CODEX`
- `WORKFLOW_10_COMMANDES`

Annexes legacy archivees hors scope actif :

- `WORKFLOW_01_COMPOSANTS` : deplace en `CACHE_SYSTEM_01_RUN`
- `WORKFLOW_02_CHECKLISTS` : deplace en `CACHE_SYSTEM_01_RUN`

### 3.2 RUN_01_SETUP_PRODUCT

`SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT` porte la composition multi-products :

- bootstrap
- selection de profil
- routine du product actif
- destination finale
- cycle de vie
- merge-out
- gouvernance

La nomenclature active des documents de cette famille est :

- `SETUP_PRODUCT_00_INDEX`
- `SETUP_PRODUCT_01_BOOTSTRAP`
- `SETUP_PRODUCT_02_PROFILE_SELECTION`
- `SETUP_PRODUCT_03_ROUTINE_OPERATIONS`
- `SETUP_PRODUCT_04_DESTINATION_POLICY`
- `SETUP_PRODUCT_05_LIFECYCLE_POLICY`
- `SETUP_PRODUCT_06_MERGE_OUT_POLICY`
- `SETUP_PRODUCT_07_GOVERNANCE_RULES`

Frontiere d integration :

- `WORKFLOW_*` execute la session, les checks et les reruns
- `SETUP_PRODUCT_*` declare ce qui doit etre maintenu, revalide ou promu
- `RUN_01_SETUP_PRODUCT` ne remplace pas les runbooks quotidiens

### 3.3 FAQ

`SYSTEM_99_FAQ` porte un support operatoire leger :

- formulaire de question / incident
- reponses rapides aux cas frequents
- point d entree secondaire, non canonique face aux index et runbooks

Le point d entree principal de `00_SYSTEM` reste `README.md`, puis `INDEX_01` et
`INDEX_02`.

---

## 4. 01_CORE

Familles autorisées :

- META
- DISCIPLINE
- CONSTRAINT
- TOOLING

Rôle : Définir les règles transverses universelles.

### 4.1 META

Règles système : naming, frontmatter, SOP, output protocol.

### 4.2 FIELD

Classifier générique, quality gates génériques, risk register générique.

### 4.3 RESTRAINT

RAG scope policy, garde-fous, anti-duplication.

### 4.4 TOOLING

Templates génériques, pipelines, checklists, extensions.

Aucun élément métier spécifique ne doit exister dans le CORE.

---

## 5. 02_PACKAGE

Rôle : Extension métier d'un domaine spécifique.

Familles possibles :

- RUBRIC
- SOT
- REF
- TPL
- PIPELINE
- CHECKLIST

Un package peut :

- Étendre le classifier générique (`FIELD -> RUBRIC`)
- Ajouter des règles de priorisation spécifiques (`SOT`)
- Adapter les templates (`TPL`)
- Ajouter des références de connaissances (`REF`)

Il ne peut modifier le CORE sans ADR.

Un seul package actif par produit.

---

## 6. 03_PRODUCT

Rôle : Exécution concrète.

Structure type :

PRODUCT_X/ PRODUCT_X\_DOD/ PRODUCT_X\_CO_000/ PRODUCT_X\_CO_001/

1 CO = 1 intention = 1 commit.

Chaque fichier PRODUCT doit respecter : - Naming - Frontmatter -
FIELD générique - FIELD spécifique si package actif

---

## 7. 99_CACHE

Rôle : Stockage temporaire non conventionnel.

Ne contient aucune source de vérité.

Compatibilité legacy : certains documents historiques peuvent encore mentionner
`04_CACHE`.

---

## 8. Règles de Cohérence Globale

1. CORE prime sur PACKAGE.
1. PACKAGE actif prime sur PRODUCT.
1. SYSTEM documente, ne décide pas.
1. Toute modification structurelle nécessite ADR + passage en DRAFT.
1. Tout fichier doit respecter :
    - NamingRules
    - Frontmatter YAML obligatoire
    - Alignement id = nom de fichier
    - Discipline des formats

---

## 9. Statut

Cette architecture constitue la base stable du framework GAPC (version canon).

Toute évolution ultérieure nécessite : - Audit - ADR - Mise à jour de
version.

---

## 10. Changelog

- v1.0 (27-02-2026) : structure minimale du framework pour Beta.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.10 (13-03-2026) : ajoute la famille `FAQ`, raccorde `SYSTEM_99_FAQ`

  et clarifie `README.md` comme point d entree principal de `00_SYSTEM`.

- v1.9 (13-03-2026) : retire `WORKFLOW_01` et `WORKFLOW_02` du scope

  SYSTEM actif et les archive en `CACHE`.

- v1.8 (13-03-2026) : renomme la famille documentaire `RUN_*` en

  `WORKFLOW_*` et recable l architecture SYSTEM.

- v1.7 (13-03-2026) : rehoste `SETUP_PRODUCT_*` sous

  `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT` et retire `MULTI_PRODUCT` comme
  famille separee.

- v1.6 (13-03-2026) : raccorde l architecture au cadre final `WORKFLOW`

  vs `SETUP_PRODUCT`, avec noyau `WORKFLOW` et annexes legacy explicites.

- v1.5 (13-03-2026) : applique la nomenclature active `SETUP_PRODUCT_00..07`.
- v1.4 (13-03-2026) : ajout de la famille `MULTI_PRODUCT` et doctrine `WORKFLOW`

  vs `SETUP_PRODUCT`.

- v1.3 (09-03-2026) : alignement architecture sur la version FRAMEWORK canon

  (`99_CACHE` explicite).

- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.1 : READY_TO_FREEZE.
