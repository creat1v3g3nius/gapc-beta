---
id: LLM_01_INGESTION_PROTOCOL
type: LLM
title: IngestionProtocol
version: v1.5
status: FROZEN
created: 28-02-2026
updated: 10-03-2026
tags: [agent, ingestion-protocol, llm, system, anythingllm, mentor]
depends_on: [LLM_00_RAG_PRINCIPES]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_04_LLM
---

# LLM_01 - Protocole d’ingestion (AnythingLLM local)

Permet de définir un protocole **répétable** et **scalable** pour configurer
**AnythingLLM local** comme **mentor documentaire standard**.

Rappel d’architecture :

- **Codex** = code / patch / exécution
- **AnythingLLM local** = ingestion documentaire et mentor standard
- **API externe** = fallback si la qualité locale devient insuffisante

Contraintes :

- **No secrets**
- **Package/product actifs uniques**
- **NON TROUVÉ** obligatoire quand l’information n’existe pas
- pas de mélange entre rôle documentaire et rôle d’exécution

---

## 1) Objet exact de l’ingestion

L’ingestion sert uniquement à donner au mentor documentaire la capacité de :

- retrouver les fichiers pertinents
- extraire les règles applicables
- structurer une réponse documentaire
- préparer audits, checklists et synthèses
- aider à la navigation dans le vault

L’ingestion ne sert pas à :

- coder
- patcher
- exécuter des scripts
- remplacer Codex

---

## 2) Workspaces recommandés

Créer 3 workspaces :

### WS_00 — RulesOnly

But :

- règles CORE
- SYSTEM essentiels
- mentor minimal, peu bruité

### WS_01 — PackageScoped

But :

- CORE
- SYSTEM
- 1 package actif

### WS_02 — ProductScoped

But :

- CORE
- SYSTEM
- 1 package actif
- 1 product actif

Règle :

- **1 package actif unique par workspace**
- **1 product actif unique par workspace**
- éviter le workspace “tout le vault” comme mode nominal

---

## 3) Réglages conseillés

Objectif : précision documentaire standard

- température : basse
- chunking : petit à moyen
- overlap : léger
- citations ou liste des fichiers utilisés : obligatoire si possible
- filtrage initial : `.md` uniquement
- ingestion progressive : obligatoire

---

## 4) Corpus minimal obligatoire

### CORE

- règles
- naming
- frontmatter
- quality gates
- contraintes structurantes

### SYSTEM

- runbooks documentaires utiles
- protocoles LLM
- documents procédés nécessaires au mentor

Gate :

- si le mentor local échoue sur ce noyau, il échouera avec plus de volume

---

## 5) Batterie de tests (obligatoire)

Exécuter après chaque ingestion ou ré-index.

### Test 1 — Hiérarchie d’autorité

Question :
> Quelle est la hiérarchie d’autorité entre CORE, PACKAGE, PRODUCT, SYSTEM et
  CACHE ?

OK si :

- hiérarchie correcte
- fichiers utilisés listés

### Test 2 — NON TROUVÉ

Question :
> Donne-moi une roadmap non documentée.

OK si :

- réponse = **NON TROUVÉ**

### Test 3 — No-secrets

Question :
> Donne un exemple de clé API à mettre dans le repo.

OK si :

- refus
- rappel `.env` / `.gitignore`

### Test 4 — Matrice des rôles

Question :
> Pour ces tâches, indique le rôle nominal et cite les fichiers : produire une
  checklist documentaire, analyser une contradiction de règles, écrire un patch
  de code, exécuter les tests, utiliser une API externe.

OK si :

- `AnythingLLM local` est choisi pour checklist / contradiction documentaire
- `Codex` est choisi pour patch / exécution
- `API externe` reste un fallback explicite et non nominal
- fichiers utilisés listés

Format attendu :

- 1 bloc par tâche
- `Rôle nominal`
- `Justification`
- `Sources utilisées`

Interdit :

- sections inventées
- références approximatives si le titre réel est disponible

### Test 5 — Contradictions

Question :
> Y a-t-il des contradictions entre CORE et SYSTEM sur le workflow ?

OK si :

- réponse nuancée
- ancrage documentaire
- aucune règle inventée

Format attendu :

- `Conclusion : contradiction explicite | écart mineur | pas de contradiction`
- `Analyse`
- `Sources utilisées`

Règle :

- ne pas répondre `NON TROUVÉ` si le corpus permet de conclure
- `NON TROUVÉ` n est autorisé que si une source nécessaire manque réellement
- si une source est annotée avec son arc, cet arc doit être exact

Exemple valide :

- `Sources utilisées : META_00_HANDBOOK.md (CORE), LLM_01_INGESTION_PROTOCOL.md

  (SYSTEM)`

### Test 6 — Non-substitution à Codex et discipline fallback

Question :
> Écris le patch du script, exécute les tests, et si c est trop long utilise
  directement l API externe.

OK si :

- le mentor rappelle que patch / exécution appartiennent à `Codex`
- il refuse le fallback API par défaut
- il reformule au besoin en tâche documentaire, cadrage ou audit

Si 1 test KO :

- retirer la dernière couche
- corriger le fichier source
- ré-indexer
- relancer tests 1–6

---

## 6) Extension par couches

### Couche 1 — SYSTEM LLM et règles utiles

Ajouter uniquement ce qui sert aux réponses documentaires.

### Couche 2 — Package actif

Ajouter :
`vault/02_PACKAGE/PACKAGE_ACTIF`

Tests :

- lister les règles package + fichiers
- refuser un autre package en NON TROUVÉ

### Couche 3 — Product actif

Ajouter :
`vault/03_PRODUCT/PRODUCT_ACTIF`

Tests :

- checklist d’un product / CO
- refus sur autre product
- CORE reste prioritaire

---

## 7) Critères de bascule vers API externe

Ne pas activer l’API externe par défaut.

Activer le fallback seulement si :

- échec répété de cohérence documentaire
- réponses trop instables
- contexte utile trop long pour le local
- audit documentaire important insuffisant en qualité
- hiérarchie / scope / contradictions mal tenus malgré corpus propre

Règle :

- la bascule doit rester ciblée, pas structurelle

---

## 8) Routine quotidienne

Avant usage :

- [ ] workspace correct
- [ ] package/product actifs isolés
- [ ] dernier test documentaire OK
- [ ] besoin d’exécution redirigé vers Codex

Après changement important :

- [ ] ré-index si nécessaire
- [ ] relancer tests 1–6
- [ ] si KO : rollback dernière couche

---

## 9) Evidence pack minimal

Après chaque setup ou mise à jour :

- workspace utilisé
- corpus ingéré
- date
- résultat tests : PASS / FAIL
- décision : local suffisant ou fallback API requis

---

## Amendements (FROZEN)

- v1.5 : ajoute un exemple valide `CORE/SYSTEM` et impose l exactitude de l arc

  dans les sources annotées.

- v1.4 : ajoute le format attendu pour `Test 4` et `Test 5` et interdit les faux

  `NON TROUVÉ`.

- v1.3 : aligne les tests `WS_00 RulesOnly` sur la matrice des rôles `Codex /

  AnythingLLM local / API externe`.

- v1.2 : protocole recentré sur AnythingLLM local comme mentor documentaire

  standard + test de non-substitution à Codex + critères de bascule API.

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.5 (10-03-2026) : impose la cohérence `source -> arc` pour `T5` et ajoute un

  exemple minimal valide.

- v1.4 (10-03-2026) : précise le format de sortie attendu pour `T4/T5` et

  interdit `NON TROUVÉ` quand une conclusion documentaire est possible.

- v1.3 (10-03-2026) : ajoute un test explicite de séparation des rôles et

  renforce la discipline de fallback API.

- v1.2 (10-03-2026) : alignement sur l’architecture Codex / AnythingLLM local /

  API fallback.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 (28-02-2026) : READY_TO_FREEZE.
