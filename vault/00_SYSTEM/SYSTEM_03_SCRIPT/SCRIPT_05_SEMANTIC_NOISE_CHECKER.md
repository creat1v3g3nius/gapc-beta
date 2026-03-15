---
id: SCRIPT_05_SEMANTIC_NOISE_CHECKER
type: SCRIPTS
title: SemanticNoiseCheckerProcess
version: v1.1
status: FROZEN
created: 09-03-2026
updated: 09-03-2026
tags: [system, script, semantic, noise, checker, process]
depends_on:
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - META_05_FRONTMATTER
  - DISCIPLINE_03_DOC_QG
  - SCRIPT_04_DOC_INTEGRITY_CHECKER
  - FRAMEWORK_00_AMELIORATION_PIPELINE
arc: SYSTEM
scope: vault/00_SYSTEM/03_SCRIPT
---

# SCRIPT_05 - SEMANTIC_NOISE_CHECKER

## Objet

Definir le **process de creation** du script `SemanticNoiseChecker` dans
`00_SYSTEM/03_SCRIPT/`.

Ce script controle le **bruit semantique** du corpus documentaire.

Controles cibles :

- variations lexicales d'IDs (`GUARDRAILS` vs `GUARD_RAILS`, `COMPOSANT` vs

  `COMPOSANTS`)

- references `depends_on` inconnues mais proches d'un ID canonique
- references `depends_on` fantomes ou de type chemin
- collisions semantiques sur les `title`
- classification des ecarts en `P0 / P1 / P2`

Ce document decrit **les regles**, **le process**, **les gates documentaires**
et **les sorties attendues**.
Il ne contient aucun secret, aucune donnee sensible, aucune procedure de
deploiement.

## Scope

Inclus :

- script de detection du bruit semantique
- regles de severite
- contrat d'entree / sortie
- articulation avec `DocIntegrityChecker`
- criteres READY_TO_FREEZE

Exclus :

- correction automatique du corpus
- arbitrage metier PACKAGE / PRODUCT
- logique de deploiement
- stockage de secrets

## Regles sources

Le script doit respecter les invariants suivants :

- les references `depends_on` restent des IDs, pas des chemins
- les variantes lexicales sont detectees de maniere explicable
- les suggestions restent deterministes et reproductibles
- le rapport est actionnable fichier par fichier
- aucune fuite de secret / PII

## Classification P0 / P1 / P2

### P0 - Bloquant

Un ecart est `P0` s'il casse une regle structurelle.

Cas `P0` :

- frontmatter absent ou illisible
- `depends_on` au format invalide
- `depends_on` contenant un chemin
- `depends_on` pointant vers un ID inexistant sans suggestion fiable

Effet :

- verdict global `FAIL`
- blocage READY_TO_FREEZE
- blocage FROZEN

### P1 - Majeur non bloquant immediat

Un ecart est `P1` s'il n'empeche pas la structure minimale, mais introduit une
derive.

Cas `P1` :

- ID inconnu avec suggestions proches plausibles
- groupe de variantes lexicales d'IDs a normaliser
- incoherence semantique detectee entre documents relies

Effet :

- verdict global `WARN`
- correction requise avant gel complet du perimetre critique

### P2 - Mineur

Un ecart est `P2` s'il degrade la lisibilite sans risque structurel.

Cas `P2` :

- overlap semantique de `title` sans ambiguite bloquante
- variation de style non critique

Effet :

- verdict global `INFO`
- correction opportuniste

## Entrees du script

Entrees minimales :

- chemin racine a analyser
- pattern de fichiers Markdown
- mode de sortie : `text | json`
- niveau minimum a afficher : `P0 | P1 | P2`

Entrees optionnelles :

- limite de suggestions
- export rapport

Interdits :

- secrets
- tokens
- acces reseau
- dependance a un service externe

## Sorties attendues

Le script doit produire :

### 1. Verdict global

Valeurs autorisees :

- `PASS`
- `WARN`
- `FAIL`

Regle :

- `FAIL` si au moins un `P0`
- `WARN` si aucun `P0` mais au moins un `P1`
- `PASS` si aucun `P0` et aucun `P1`

### 2. Rapport lisible

Le rapport humain doit contenir :

- perimetre analyse
- nombre de fichiers analyses
- total des ecarts `P0 / P1 / P2`
- liste des ecarts avec fichier, regle, message, correction attendue

### 3. Rapport machine-readable

Le rapport JSON doit contenir au minimum :

- `status`
- `scope`
- `files_scanned`
- `issues`
- `counts`
- `generated_at`

## Contrat fonctionnel

Le `SemanticNoiseChecker` doit executer les etapes suivantes dans l'ordre :

### Etape 1 - Collecte

- lister les fichiers Markdown du perimetre
- figer la liste de travail

### Etape 2 - Lecture frontmatter

- parser le frontmatter de chaque fichier
- remonter un `P0` en cas d'echec

### Etape 3 - Index des IDs

- construire l'index global des IDs
- verifier l'unicite de base

### Etape 4 - Analyse `depends_on`

- valider le format liste
- rejeter les chemins
- proposer des IDs proches pour les variantes lexicales

### Etape 5 - Analyse semantique des IDs

- construire des cles semantiques normalisees
- detecter les groupes de variantes a converger

### Etape 6 - Analyse semantique des titles

- detecter les collisions semantiques de titres
- classer en `P2` sauf impact structurel

### Etape 7 - Aggregation

- consolider les ecarts
- calculer le verdict global
- produire texte + JSON

## Process de creation du script

### 1. Cadrage

- confirmer l'arc : `SYSTEM`
- confirmer le scope : `vault/00_SYSTEM/03_SCRIPT`
- confirmer le positionnement : bruit semantique, pas validation structurelle

  brute

### 2. Specification

- figer les regles `P0 / P1 / P2`
- figer le contrat CLI
- figer le format de suggestion

### 3. Implementation

- parser frontmatter
- indexer IDs et depends_on
- appliquer normalisation semantique
- produire code retour CI-compatible

### 4. Validation locale

- cas PASS
- cas depends_on fantome
- cas variante detectee avec suggestion
- cas overlap de title

### 5. Integration

- execution standalone
- execution combinee avec `SmokeRunner` et `DocIntegrityChecker`
- separation claire des responsabilites

### 6. Documentation

- documenter options CLI, codes retour et exemples
- relier au process framework

## Contrat de non-duplication

Le script ne doit pas :

- remplacer `ValidateFrontmatter`
- remplacer `DocIntegrityChecker`
- corriger automatiquement les documents

Le script doit :

- completer la detection des derives lexicales
- standardiser les signals de bruit semantique
- fournir un diagnostic reproductible

## Doc QG

### Gate READY_TO_FREEZE - PASS/FAIL

PASS si :

- objectif explicite
- regles actionnables
- severites P0/P1/P2 explicites
- sorties texte/json definies
- aucun secret

FAIL sinon.

### Gate FROZEN - PASS/FAIL

FROZEN = READY_TO_FREEZE + :

- integration stable dans le pipeline SYSTEM
- amendements controles
- version bump
- zero `P0` ouvert sur le perimetre gele

## Tests smoke attendus

### Cas PASS

- corpus coherent
- zero depends_on fantome
- zero variation semantique critique

### Cas FAIL P0

- depends_on path-like
- depends_on inconnu sans match plausible
- frontmatter manquant

### Cas WARN P1

- variantes lexicales d'IDs detectees avec suggestion

## Code de retour recommande

- `0` : PASS
- `1` : FAIL avec au moins un `P0`
- `2` : WARN avec au moins un `P1` et aucun `P0`

## Message de commit recommande

`feat(system): add semantic noise checker process and quality contract`

## Risques & controles

### Risques

- faux positifs sur corpus historique
- suggestions non pertinentes
- confusion avec les checks structurels

### Controles

- normalisation deterministe
- seuil de suggestion explicite
- separation claire avec les autres validateurs

## Criteres de reussite

Le process est reussi si :

- les variantes semantiques sont detectees sans ambiguite
- le rapport est actionnable
- l'integration pipeline est simple

## Next step unique

Creer la **Spec Tech** du CLI `SemanticNoiseChecker` avant extension des regles
semantiques.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (09-03-2026) : passage en FROZEN.
- v1.0 (09-03-2026) : creation du process.
