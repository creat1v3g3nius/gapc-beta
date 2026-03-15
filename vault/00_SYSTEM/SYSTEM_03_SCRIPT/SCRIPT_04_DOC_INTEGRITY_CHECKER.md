---
id: SCRIPT_04_DOC_INTEGRITY_CHECKER
type: SCRIPTS
title: DocIntegrityCheckerProcess
version: v1.1
status: FROZEN
created: 09-03-2026
updated: 15-03-2026
tags: [system, script, doc, integrity, validator, process]
depends_on:
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - META_05_FRONTMATTER
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_03_DOC_QG
  - FRAMEWORK_00_AMELIORATION_PIPELINE
arc: SYSTEM
scope: vault/00_SYSTEM/03_SCRIPT
---

# SCRIPT_04 - DOC_INTEGRITY_CHECKER

## Objet

Définir le **process de création** du script `DocIntegrityChecker` dans
`00_SYSTEM/03_SCRIPT/`.

Ce script a pour rôle de contrôler la **cohérence documentaire transverse** sur
un périmètre donné du vault.

Contrôles ciblés :

- cohérence `id == filename`
- unicité globale des `id`
- validité des `depends_on`
- harmonie `filename / id / naming`
- classification des écarts en `P0 / P1 / P2`

Ce document décrit **les règles**, **le process**, **les gates documentaires**
et **les sorties attendues**.
Il ne contient aucun secret, aucune donnée sensible, aucune procédure de
déploiement.

## Scope

Inclus :

- script de contrôle documentaire
- règles de sévérité
- contrat d’entrée / sortie
- intégration avec runner de smoke
- critères READY_TO_FREEZE

Exclus :

- logique produit
- règles métier PACKAGE / PRODUCT
- correction automatique du corpus
- stockage de secrets
- arbitrage d’architecture transverse non tracé

## Règles sources

Le script doit respecter les invariants suivants :

- `id == filename`
- `depends_on` contient uniquement des IDs
- chaque ID doit être unique sur le périmètre analysé
- chaque dépendance référencée doit exister
- le document doit rester exploitable sans oral
- aucune fuite de secret / PII
- les sorties doivent être actionnables et classées

## Classification P0 / P1 / P2

### P0 — Bloquant

Un écart est `P0` s’il casse une règle structurelle ou bloque un gel.

Cas `P0` :

- frontmatter absent ou illisible
- champ `id` absent
- `id` différent du nom de fichier
- `id` dupliqué sur le périmètre
- `depends_on` absent si requis par le schéma retenu
- `depends_on` contenant des chemins au lieu d’IDs
- `depends_on` pointant vers un ID fantôme
- `arc` invalide
- document hors convention minimale empêchant READY_TO_FREEZE
- présence de secret ou donnée sensible détectable dans les métadonnées ou
  sorties

Effet :

- verdict global `FAIL`
- blocage READY_TO_FREEZE
- blocage FROZEN

### P1 — Majeur non bloquant immédiat

Un écart est `P1` s’il n’invalide pas la structure minimale, mais crée une
dérive ou une dette de gouvernance.

Cas `P1` :

- `title` non harmonisé avec la convention attendue
- incohérence de famille entre nom de fichier et préfixe d’`id`
- variation de naming rendant la navigation ambiguë
- dépendance valide mais non cohérente avec le scope logique
- naming partiellement hérité nécessitant normalisation

Effet :

- verdict global `WARN`
- correction requise avant gel complet du périmètre critique

### P2 — Mineur

Un écart est `P2` s’il n’impacte ni la structure ni la traçabilité centrale,
mais dégrade la qualité documentaire.

Cas `P2` :

- tags bruités ou peu homogènes
- libellé peu clair mais non ambigu
- ordre non critique de champs
- légères variations de style sans impact sur la validation

Effet :

- verdict global `INFO`
- correction opportuniste

## Entrées du script

Entrées minimales :

- chemin racine à analyser
- liste de fichiers `.md` ou pattern
- mode de sortie : `text | json`
- niveau de sévérité minimum à afficher : `P0 | P1 | P2`

Entrées optionnelles :

- allowlist temporaire de fichiers hérités
- mode strict
- export rapport

Interdits :

- secrets
- tokens
- accès réseau
- dépendance à un service externe pour valider le corpus

## Sorties attendues

Le script doit produire :

### 1. Verdict global

Valeurs autorisées :

- `PASS`
- `WARN`
- `FAIL`

Règle :

- `FAIL` si au moins un `P0`
- `WARN` si aucun `P0` mais au moins un `P1`
- `PASS` si aucun `P0` et aucun `P1`

### 2. Rapport lisible

Le rapport humain doit contenir :

- périmètre analysé
- nombre de fichiers analysés
- total des écarts par niveau `P0 / P1 / P2`
- liste des écarts avec fichier, règle, message, correction attendue
- synthèse finale

### 3. Rapport machine-readable

Le rapport JSON doit contenir au minimum :

- `status`
- `scope`
- `files_scanned`
- `issues`
- `counts`
- `generated_at`

## Contrat fonctionnel

Le `DocIntegrityChecker` doit exécuter les étapes suivantes dans l’ordre :

### Étape 1 — Collecte

- lister les fichiers Markdown du périmètre
- exclure les répertoires non documentaires si la politique locale l’exige
- figer la liste de travail

### Étape 2 — Lecture frontmatter

- détecter la présence du frontmatter YAML
- parser les champs requis
- remonter un `P0` si le parsing échoue

### Étape 3 — Index des IDs

- construire un index global `id -> fichier`
- détecter les doublons
- détecter les IDs manquants

### Étape 4 — Contrôle filename / id

- comparer le nom de fichier sans extension avec la valeur `id`
- classer en `P0` toute divergence

### Étape 5 — Contrôle depends_on

- vérifier que `depends_on` est une liste d’IDs
- vérifier que chaque ID existe dans l’index ou dans une allowlist explicite
- détecter les références fantômes

### Étape 6 — Contrôle harmonie naming

- vérifier la cohérence de famille : ex. `META_`, `DISCIPLINE_`, `CONSTRAINT_`,
  `SCRIPT_`
- vérifier la cohérence entre préfixe, type, arc et scope
- classer les écarts selon impact réel

### Étape 7 — Agrégation

- consolider les écarts
- calculer le verdict global
- préparer les sorties texte et JSON

## Process de création du script

### 1. Cadrage

- confirmer l’arc : `SYSTEM`
- confirmer le scope : `vault/00_SYSTEM/03_SCRIPT`
- confirmer que le script complète le validator YAML et le smoke runner sans
  dupliquer leur rôle

### 2. Spécification

- figer la liste des règles `P0 / P1 / P2`
- figer le contrat CLI
- figer le format du rapport

### 3. Implémentation

- parser les fichiers Markdown
- extraire frontmatter
- construire l’index global
- exécuter les règles dans l’ordre défini
- produire un exit code compatible CI locale

### 4. Validation locale

- tester un corpus `PASS`
- tester un cas `id` dupliqué
- tester un cas `depends_on` fantôme
- tester un cas `id != filename`
- tester un cas `P1` de naming
- vérifier la stabilité de la sortie JSON

### 5. Intégration

- brancher le script au `SmokeRunner`
- conserver la séparation des rôles :
  - `ValidatorYaml` = schéma local
  - `DocIntegrityChecker` = cohérence transverse
  - `SmokeRunner` = orchestration

### 6. Documentation

- documenter commande, options, codes retour, exemples de sortie
- relier le script au process d’amélioration framework
- préparer le passage `READY_TO_FREEZE`

## Contrat de non-duplication

Le script ne doit pas :

- réécrire toute la validation YAML si elle existe déjà
- décider à la place des documents CORE
- corriger automatiquement les fichiers sans procédure dédiée
- masquer des erreurs `P0`

Le script doit :

- compléter le validator existant
- centraliser les écarts de cohérence transverse
- produire un diagnostic reproductible

## Doc QG

### Gate READY_TO_FREEZE — PASS/FAIL

PASS si :

- frontmatter conforme
- objectif clair
- sections courtes et lisibles
- règles actionnables
- classification `P0 / P1 / P2` explicite
- aucun secret
- process exécutable sans oral

FAIL sinon.

### Gate FROZEN — PASS/FAIL

FROZEN = READY_TO_FREEZE + :

- intégration réelle au pipeline SYSTEM
- amendements contrôlés
- version bump
- zéro `P0` ouvert sur le périmètre gelé

## Tests smoke attendus

### Cas PASS

- corpus avec frontmatters valides
- IDs uniques
- `depends_on` valides
- nom de fichier aligné avec `id`

### Cas FAIL P0

- document sans frontmatter
- duplication d’ID
- `depends_on` fantôme
- `id != filename`

### Cas WARN P1

- incohérence d’harmonie naming sans casse structurelle

## Code de retour recommandé

- `0` : PASS
- `1` : FAIL avec au moins un `P0`
- `2` : WARN avec au moins un `P1` et aucun `P0`

## Message de commit recommandé

`feat(system): add doc integrity checker process and validation contract`

## Risques & contrôles

### Risques

- duplication de responsabilité avec `ValidatorYaml`
- faux positifs sur corpus hérité
- règles de naming trop floues
- dérive si allowlist non contrôlée

### Contrôles

- séparer schéma local et cohérence transverse
- documenter chaque règle et sa sévérité
- limiter les exceptions temporaires
- exiger un rapport explicite à chaque exécution

## Critères de réussite

Le process est réussi si :

- le script est spécifié sans ambiguïté
- les règles P0/P1/P2 sont stables
- la sortie est exploitable par humain et runner
- l’intégration smoke est possible sans secret ni service externe

## Next step unique

Créer la **Spec Tech** du binaire/CLI `DocIntegrityChecker` à partir de ce
process avant toute implémentation.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (15-03-2026) : passage en FROZEN apres implementation et validation du
  checker dans le repo.
- v1.0 (09-03-2026) : creation du process `DocIntegrityChecker`.
