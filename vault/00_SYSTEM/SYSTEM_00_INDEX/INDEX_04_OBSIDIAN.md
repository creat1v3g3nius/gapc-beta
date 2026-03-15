---
id: INDEX_04_OBSIDIAN
type: INDEX
title: ObsidianConfig
version: v1.2
status: FROZEN
created: 27-02-2026
updated: 13-03-2026
tags: [repo, obsidian-knowledge, index, system]
depends_on: [INDEX_01_ARCHITECTURE, INDEX_02_REPOSITORY, INDEX_03_WRITING, META_00_HANDBOOK, META_05_FRONTMATTER]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_00_INDEX
---

# INDEX_04 - Obsidian Config

## Objet
Ce document décrit **comment utiliser Obsidian** comme noyau documentaire du framework GAPC :
- navigation dans le Vault (SYSTEM/CORE/PACKAGE/PRODUCT/CACHE),
- règles de liens, tags, recherches,
- routines de session (Doc → Code → Commit),
- bonnes pratiques pour limiter le bruit RAG (AnythingLLM).

**Source of Truth** : le Vault (Obsidian).
**Exécution** : repo Git (VS Code).  
**Mentor** : AnythingLLM (lecture/extraction), jamais décision autonome.

## Pré-requis
- Obsidian installé
- Vault ouvert : `repo/vault/`
- Conventions actives :
  - Naming conventions (META_00)
  - Frontmatter YAML obligatoire (META_01)
  - Règles de rédaction (INDEX_03)

---

## 1. Vue d’ensemble du Vault

### 1.1 Arcs (macro-dossiers)
Le Vault est structuré en arcs :

- `00_SYSTEM/` : documentation d’usage et exécution (non décisionnel)
- `01_CORE/` : règles transverses (normatif)
- `02_PACKAGE/` : extensions métier (ASSO, GAPC…)
- `03_PRODUCT/` : exécution par composants (CO)
- `99_CACHE/` : stockage temporaire / archivage non contractuel

### 1.2 Règle
- Si c’est **une règle transversale** → CORE
- Si c’est **une adaptation métier** → PACKAGE
- Si c’est **une étape de production** (CO) → PRODUCT
- Si c’est **un guide d’usage / procédure** → SYSTEM
- Si c’est **temporaire** → CACHE

---

## 2. Création d’un fichier dans Obsidian

### 2.1 Choisir la famille
Chaque fichier appartient à une **famille** (INDEX/WORKFLOW/GIT/SCRIPT/LLM/BACKLOG/PATCH/FAQ/META/DISCIPLINE/RESTRAINT/TOOLING…).

La famille doit être cohérente avec le dossier parent.

### 2.2 Naming
Règles :
- Dossiers arcs : `<NUM_TITRE>/` (ex: `00_SYSTEM/`)
- Dossiers familles : `<ARC_NUM_TITRE>/` (ex: `SYSTEM_00_INDEX/`)
- Fichiers : `<FAMILLE_NUM_TITRE>.md`
- `id` YAML = `<FAMILLE_NUM>/`

Exemple :
- Fichier : `INDEX_04_OBSIDIAN_KB_DRAFT.md`
- `id: INDEX_04`

### 2.3 Frontmatter YAML (obligatoire)
Tout fichier doit commencer par un YAML frontmatter conforme (META_01).

Checklist rapide :
- [ ] `id` présent et aligné
- [ ] `type` = famille
- [ ] `title` en UpperCamelCase
- [ ] `version` + `status`
- [ ] `created` + `updated`
- [ ] `tags` + `dependances`
- [ ] `scope` + `arc`

Cas spécifique (activation PACKAGE et PRODUCT) : 
- [ ] : `active_package: package_x
- [ ] : active_product: product_x

---

## 3. Liens, navigation, et index

### 3.1 Liens internes (Obsidian)
- Lien vers un fichier : `[[INDEX_01_ARCHITECTURE]]`
- Lien vers un heading : `[[INDEX_01_ARCHITECTURE#2. Arcs du Système]]`

Règle :
- Préférer le lien à la duplication de contenu.

### 3.2 Index obligatoires (SYSTEM_00_INDEX)
Utiliser les index comme “table des matières” du système :
- `INDEX_01_*` : architecture
- `INDEX_02_*` : liste fichiers / arborescence
- `INDEX_03_*` : règles de rédaction/formats
- `INDEX_04_*` : guide Obsidian (ce document)
- `INDEX_05_*` : glossaire

### 3.3 Navigation recommandée
- Démarrer par `README.md` (racine de `00_SYSTEM/`)
- Puis `INDEX_01` → `INDEX_02` → `INDEX_03` → `INDEX_04`
- Ensuite entrer dans le package actif et le product actif

---

## 4. Tags, recherche et hygiène

### 4.1 Tags (usage)
Les tags servent à :
- retrouver vite,
- filtrer dans Obsidian,
- aider le RAG (AnythingLLM) si ingéré.

Règles :
- Tags courts, sans accents, sans espaces
- 3–7 tags max
- Préférer des tags “fonction” (`workflow`, `validator`) aux tags “humeur”

### 4.2 Recherche efficace
- Recherche par `id` ou `title` via frontmatter si tu standardises
- Recherche globale : mots-clés stables (ex: `READY_TO_FREEZE`, `ADR`, `scope`)

### 4.3 Hygiène anti-bruit (RAG)
- Éviter les doublons (lien à la place)
- Garder les fichiers courts, scannables
- Mettre les brouillons instables dans `99_CACHE/` (ou legacy `04_CACHE/` si encore present), puis migrer/archiver

### 4.4 Point d entree SYSTEM
- `vault/00_SYSTEM/README.md` = point d entree de navigation rapide
- `SYSTEM_00_INDEX/*` = tables des matieres canoniques
- `SYSTEM_99_FAQ/FAQ_00_FORM.md` = support operatoire leger, secondaire

---

## 5. Workflow quotidien (session standard)

### 5.1 Règle d’or
**1 composant (CO) = 1 étape = 1 intention = 1 commit**

### 5.2 Début de session (5–10 min)
- [ ] Ouvrir l’index du product actif (`*_DOD/` + backlog composants)
- [ ] Choisir **1 CO**
- [ ] Préparer un mini “context pack” :
  - Goal
  - Constraints
  - Current state
  - Files
  - Expected output

### 5.3 Pendant la session
- Écrire/mettre à jour la doc dans Obsidian (Vault)
- Implémenter scripts/config dans VS Code si requis
- Lancer validator frontmatter (bloquant)
- Lancer smoke runner (si défini)
- Commit (1 intention)

### 5.4 Fin de session (5 min)
- [ ] Mettre à jour statut du CO (Draft/Ready/In progress/Done)
- [ ] Noter 1 risque max (si nouveau)
- [ ] Définir le **next step unique**

---

## 6. Templates, snippets, et standardisation

### 6.1 Snippets utiles à garder dans SYSTEM
- Context Pack
- Checklists de session
- Checklist incident
- Checklist ingestion RAG

### 6.2 Templates Obsidian (option)
Si tu utilises le plugin “Templates” :
- stocker les templates **dans CORE/TOOLING/TPL** (génériques),
- et les templates métier dans PACKAGE (ex: ASSO_04_TPL).

Règle : pas de duplication entre CORE et PACKAGE.

---

## 7. Intégration avec AnythingLLM (mentor)

### 7.1 Discipline d’ingestion
- Ingestion minimale d’abord (RulesOnly)
- Ajouter ensuite le package actif
- Puis le product actif
- Tester à chaque extension du corpus (batterie de prompts)

### 7.2 Ce que le mentor a le droit de faire
- extraire des règles,
- proposer des drafts de documents,
- pointer incohérences,
- suggérer next step.

Interdit :
- décider à ta place,
- inventer des faits,
- mélanger plusieurs packages actifs.

---

## 8. Dépannage Obsidian (pannes courantes)

### 8.1 Liens cassés
Causes :
- renommage sans mise à jour,
- doublons de noms.

Fix :
- renommer via Obsidian (mise à jour liens),
- éviter les noms proches (SpecTech vs SpechTech).

### 8.2 Fichier non committable
Cause fréquente :
- frontmatter invalide / manquant.

Fix :
- corriger le YAML,
- vérifier `id` aligné au nom de fichier,
- relancer validator.

---

## 9. Checklist READY_TO_FREEZE (doc)
Avant de passer un doc en READY_TO_FREEZE :
- [ ] H1 unique, sections claires
- [ ] Pas de doublon (liens plutôt)
- [ ] Frontmatter complet et correct
- [ ] Contenu utilisable “sans oral”
- [ ] Dépendances déclarées

---

## Changelog
- v1.2 (13-03-2026) : aligne la navigation Obsidian sur `99_CACHE`, `README.md` et `SYSTEM_99_FAQ`.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v0.1 (27-02-2026) : création du draft (réécriture depuis la v0, alignée naming/frontmatter).

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
