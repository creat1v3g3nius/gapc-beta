---
id: LLM_00_RAG_PRINCIPES
type: LLM
title: RagPrincipes
version: v1.4
status: FROZEN
created: 28-02-2026
updated: 13-03-2026
tags: [agent, rag-principes, llm, system, mentor, anythingllm, codex]
depends_on: []
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_04_LLM
---

# LLM_00 - RAG Principes (Mentor AnythingLLM)

Permet de définir les **principes opérationnels** du dispositif LLM documentaire
GAPC, aligné avec l’architecture cible :

- **Obsidian (Vault)** = Source of Truth documentaire
- **VS Code + Codex** = code / patch / exécution / scripts
- **AnythingLLM local** = mentor documentaire standard (lecture / extraction /
  contrôle)
- **API externe** = fallback, uniquement si le mentor local atteint une limite
  réelle

Ce document vise : **utilité maximale**, **zéro dérive**, **zéro ghost
decision**, **séparation stricte des rôles**.

---

## 1) Architecture cible (décision courante)

### 1.1) Répartition des rôles

- **Codex** traite :
  - code
  - patchs
  - scripts
  - exécution
  - aides de mise en oeuvre
- **AnythingLLM local** traite :
  - lecture documentaire
  - extraction de règles
  - navigation dans le corpus
  - synthèses et checklists documentaires
  - contrôle documentaire standard
- **API externe** traite :
  - cas complexes en fallback
  - corpus volumineux ou réponses locales instables
  - analyses documentaires nécessitant plus de robustesse

### 1.2) Principe directeur

Le mentor documentaire n’est **pas** le moteur principal d’exécution.
Le moteur principal d’exécution est **Codex**.

AnythingLLM local reste utile comme couche :

- de lecture
- de rappel des règles
- de contrôle documentaire
- de consultation standard

L’API externe n’est pas le mode nominal.
Elle est déclenchée **seulement** si le mode local ne tient plus le niveau
attendu.

---

## 2) Contrat du mentor documentaire

### 2.1) Ce que le mentor DOIT faire

- retrouver où est la vérité documentaire
- lister les fichiers utilisés
- rappeler l’arc concerné : SYSTEM / CORE / PACKAGE / PRODUCT
- extraire des outputs actionnables à partir du corpus
- produire des checklists, étapes, critères, mappings règle → action
- dire **NON TROUVÉ** si l’information n’existe pas
- respecter le package actif et le product actif
- si un product actif expose une checklist de gel explicite, l utiliser comme
  checklist product de reference
- rester en lecture seule

### 2.2) Ce que le mentor NE DOIT PAS faire

- patcher le code
- exécuter des scripts
- décider une architecture sans source
- inventer des règles
- se substituer à Codex sur les tâches d’implémentation
- se substituer à une ADR-lite si décision structurante

---

## 3) Hiérarchie d’autorité

Le mentor applique l’ordre suivant en cas de contradiction :

1. **CORE**
2. **PACKAGE actif**
3. **PRODUCT actif**
4. **SYSTEM**
5. **CACHE**

Règle :

- si contradiction non résolue → **NON TROUVÉ**
- proposer correction de la doc source ou ADR-lite selon le cas

---

## 4) Stratégie d’usage recommandée

### 4.1) Mode nominal

Utiliser :

- **Codex** pour produire / patcher / exécuter
- **AnythingLLM local** pour lire / extraire / contrôler la documentation

### 4.2) Mode fallback

Passer à une **API externe** uniquement si au moins un des signaux suivants
apparaît :

- réponses locales instables sur une même demande
- échec répété sur contradictions documentaires complexes
- incapacité à tenir un long contexte utile
- qualité insuffisante sur un audit documentaire important
- difficulté à restituer proprement hiérarchie / scope / files utilisés

### 4.3) Règle de coût / complexité

Le fallback API doit rester :

- ciblé
- explicite
- justifié
- limité aux cas où le local ne suffit pas

---

## 5) Anti-hallucination (non négociable)

### 5.1) Small corpus first

Toujours démarrer avec un corpus minimal :

- CORE
- SYSTEM essentiels

### 5.2) Extension par couches

Ajouter progressivement :

1. règles utiles
2. package actif
3. product actif

### 5.3) Sortie attendue

Le mentor documentaire doit répondre avec :

1. checklist actionnable
2. fichiers utilisés
3. next step unique
4. hypothèses si nécessaire

---

## 6) Interdits centraux

### 6.1) No ghost decisions

Le mentor ne décide pas :

- pas de stack imposée
- pas de règle inventée
- pas d’architecture imposée sans source

### 6.2) No-secrets

Le mentor ne doit jamais :

- demander de clés ou tokens
- proposer de stocker des secrets dans repo / vault / logs
- produire de secrets réels

### 6.3) No scope mixing

Interdit de :

- mélanger plusieurs packages
- mélanger plusieurs products
- utiliser CACHE comme vérité
- contredire CORE

---

## 7) Red flags

Considérer le mentor KO si :

- réponse générique sans fichiers utilisés
- réponse inventée
- mélange de scopes
- refus de dire NON TROUVÉ
- dérive vers des tâches de code / patch / exécution
- proposition d’usage d’un secret dans le repo

Action corrective :

- réduire le corpus
- corriger la doc source
- repasser par Codex pour l’exécution
- utiliser l’API externe seulement si la limite locale est confirmée

---

## 8) Synthèse d’architecture

La cible GAPC est :

- **Codex** = code / patch / exécution
- **AnythingLLM local** = mentor documentaire standard
- **API externe** = fallback

Ce découpage est le mode nominal du système LLM documentaire.

---

## Amendements (FROZEN)

- v1.2 : séparation explicite des rôles Codex / AnythingLLM local / API externe
  fallback.
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (13-03-2026) : remplace la reference explicite a `PRODUCT_00_BETA_GAPC`
  par une regle generique compatible avec le sample actif.
- v1.3 (10-03-2026) : ajoute la reference explicite a
  `OPS_06_READY_TO_FREEZE_CHECKLIST` pour `PRODUCT_00_BETA_GAPC`.
- v1.2 (10-03-2026) : alignement sur la nouvelle architecture LLM cible.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 (28-02-2026) : READY_TO_FREEZE.
