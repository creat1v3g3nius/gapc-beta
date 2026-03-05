---
id: INDEX_01_ARCHITECTURE
type: INDEX
title: ArchitectureFrameworkGAPC
version: v1.2
status: FROZEN
created: 27-02-2026
updated: 02-03-2026
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

------------------------------------------------------------------------

## 1. Structure Générale du Repository

repo/ docs/ scripts/ vault/

Le Vault constitue la base de données.

------------------------------------------------------------------------

## 2. Arcs du Système

Le système est structuré en 5 arcs principaux :

00_SYSTEM/ 01_CORE/ 02_PACKAGE/ 03_PRODUCT/ 99_CACHE/

Chaque arc contient uniquement les familles nécessaires à sa fonction.

------------------------------------------------------------------------

## 3. 00_SYSTEM

Familles autorisées :

-   INDEX
-   RUN
-   GIT
-   SCRIPT
-   LLM
-   BACKLOG
-   PATCH

Rôle : Documentation d'usage, procédures d'exécution, configuration Git,
scripts de validation, protocole RAG.

Aucune règle produit ne doit exister dans cet arc.

------------------------------------------------------------------------

## 4. 01_CORE

Familles autorisées :

-   META
-   DISCIPLINE
-   CONSTRAINT
-   TOOLING

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

------------------------------------------------------------------------

## 5. 02_PACKAGE

Rôle : Extension métier d'un domaine spécifique.

Familles possibles : - RUBRIC - SOT - REF - TPL - PIPELINE - CHECKLIST

Un package peut : - Étendre le classifier générique (FIELD -> RUBRIC) - Ajouter des règles
de priorisation spécifiques (SOT) - Adapter les templates (TPL) - Ajouter des références de connaissances (REF)

Il ne peut modifier le CORE sans ADR.

Un seul package actif par produit.

------------------------------------------------------------------------

## 6. 03_PRODUCT

Rôle : Exécution concrète.

Structure type :

PRODUCT_X/ PRODUCT_X\_DOD/ PRODUCT_X\_CO_000/ PRODUCT_X\_CO_001/

1 CO = 1 intention = 1 commit.

Chaque fichier PRODUCT doit respecter : - Naming - Frontmatter -
FIELD générique - FIELD spécifique si package actif

------------------------------------------------------------------------

## 7. 04_CACHE

Rôle : Stockage temporaire non conventionnel.

Ne contient aucune source de vérité.

------------------------------------------------------------------------

## 8. Règles de Cohérence Globale

1.  CORE prime sur PACKAGE.
2.  PACKAGE actif prime sur PRODUCT.
3.  SYSTEM documente, ne décide pas.
4.  Toute modification structurelle nécessite ADR + passage en DRAFT.
5.  Tout fichier doit respecter :
    -   NamingRules
    -   Frontmatter YAML obligatoire
    -   Alignement id = nom de fichier
    -   Discipline des formats

------------------------------------------------------------------------

## 9. Statut

Cette architecture constitue la base stable du framework GAPC pour la
phase Beta.

Toute évolution ultérieure nécessite : - Audit - ADR - Mise à jour de
version.

------------------------------------------------------------------------

## 10. Changelog

- v1.0 (27-02-2026) : structure minimale du framework pour Beta.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.1 : READY_TO_FREEZE.
