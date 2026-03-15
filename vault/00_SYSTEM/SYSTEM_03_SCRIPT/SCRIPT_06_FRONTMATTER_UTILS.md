---
id: SCRIPT_06_FRONTMATTER_UTILS
type: SCRIPTS
title: FrontmatterUtilsProcess
version: v1.1
status: FROZEN
created: 09-03-2026
updated: 09-03-2026
tags: [system, script, frontmatter, utils, parser, process]
depends_on:
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - META_05_FRONTMATTER
  - DISCIPLINE_03_DOC_QG
  - SCRIPT_00_VALIDATOR
  - SCRIPT_04_DOC_INTEGRITY_CHECKER
  - FRAMEWORK_00_AMELIORATION_PIPELINE
arc: SYSTEM
scope: vault/00_SYSTEM/03_SCRIPT
---

# SCRIPT_06 - FRONTMATTER_UTILS

## Objet

Definir le **process de creation** du module utilitaire `frontmatter_utils` dans
`00_SYSTEM/03_SCRIPT/`.

Ce module unifie le parsing frontmatter utilise par :

- `ValidateFrontmatter`
- `DocIntegrityChecker`
- `SemanticNoiseChecker`
- `SmokeRunner` (lecture statut)

Le but est de reduire la duplication, stabiliser les erreurs et garder un
comportement deterministe.

## Scope

Inclus :

- contrat API de parsing frontmatter
- format de retour standardise
- regles d'erreur homogenes
- integration multi-scripts
- criteres READY_TO_FREEZE

Exclus :

- validation metier des champs
- regles de qualite semantique
- auto-correction documentaire
- acces reseau

## Regles sources

Le module doit respecter les invariants suivants :

- parsing local, sans effet de bord
- meme resultat pour une meme entree
- position de ligne exploitable dans les rapports
- erreurs explicites (`missing_opening`, `missing_closing`)
- compatibilite ASCII/UTF-8 sans crash

## Classification P0 / P1 / P2

### P0 - Bloquant

Un ecart est `P0` s'il casse la fiabilite du parsing partage.

Cas `P0` :

- faux negatif sur frontmatter manquant
- frontmatter invalide non detecte
- metadata parsee de maniere incoherente entre scripts
- erreur bloquante non remontee

Effet :

- verdict global `FAIL`
- blocage READY_TO_FREEZE
- blocage FROZEN

### P1 - Majeur non bloquant immediat

Un ecart est `P1` s'il cree une dette de maintenance.

Cas `P1` :

- divergence de regex cle/valeur
- differences de comportement selon script appelant
- ligne d'erreur imprécise mais exploitable

Effet :

- verdict global `WARN`
- correction requise avant gel complet

### P2 - Mineur

Un ecart est `P2` s'il n'impacte pas la fiabilite.

Cas `P2` :

- nommage interne perfectible
- commentaire manquant non critique

Effet :

- verdict global `INFO`
- correction opportuniste

## Entrees du module

Entrees minimales :

- `path` fichier Markdown
- regex cle/valeur optionnelle

Sortie attendue :

- `metadata`
- `line_map`
- `raw`
- `error_code`
- `error_line`
- `error_message`

Interdits :

- secret
- token
- I/O reseau

## Sorties attendues

Le module doit produire un objet resultat standard.

### 1. Cas nominal

- `error_code = None`
- `metadata` peuple
- `line_map` coherent
- `raw` exploitable

### 2. Cas erreur opening

- `error_code = missing_opening`
- `error_message` explicite

### 3. Cas erreur closing

- `error_code = missing_closing`
- `error_message` explicite

## Contrat fonctionnel

Le module `frontmatter_utils` doit executer les etapes suivantes :

### Etape 1 - Ouverture

- ouvrir le fichier en mode lecture robuste (`utf-8`, `errors=replace`)

### Etape 2 - Verification delimiters

- verifier `---` d'ouverture
- parcourir jusqu'au `---` de fermeture

### Etape 3 - Extraction

- extraire le bloc frontmatter brut
- parser les couples cle/valeur reconnus

### Etape 4 - Mapping lignes

- enregistrer la ligne d'origine de chaque cle

### Etape 5 - Resultat

- retourner une structure unique pour tous les appelants

## Process de creation du module

### 1. Cadrage

- confirmer l'arc : `SYSTEM`
- confirmer le scope : `vault/00_SYSTEM/03_SCRIPT`
- confirmer l'objectif : utilitaire commun, pas validateur complet

### 2. Specification

- figer la structure `FrontmatterResult`
- figer les codes d'erreur
- figer le contrat de compatibilite appelants

### 3. Implementation

- parser en streaming leger
- gerer erreurs opening/closing
- exposer une fonction unique `parse_frontmatter_file`

### 4. Validation locale

- fichier valide
- fichier sans opening delimiter
- fichier sans closing delimiter
- fichier avec lignes non parseables

### 5. Integration

- brancher dans `ValidateFrontmatter`
- brancher dans `DocIntegrityChecker`
- brancher dans `SemanticNoiseChecker`
- brancher dans `SmokeRunner`

### 6. Documentation

- documenter API, structure de retour, limites
- tracer la non-duplication des parseurs

## Contrat de non-duplication

Le module ne doit pas :

- decider les regles metier des validateurs
- imposer un policy de severite
- corriger les documents

Le module doit :

- centraliser le parsing frontmatter
- garantir un comportement homogene
- reduire la dette de maintenance

## Doc QG

### Gate READY_TO_FREEZE - PASS/FAIL

PASS si :

- contrat API explicite
- erreurs opening/closing formalisees
- integration multi-scripts definie
- aucun secret

FAIL sinon.

### Gate FROZEN - PASS/FAIL

FROZEN = READY_TO_FREEZE + :

- module utilise par les scripts cibles
- amendements controles
- version bump
- zero `P0` ouvert sur le parsing partage

## Tests smoke attendus

### Cas PASS

- frontmatter valide parse uniformement par tous les scripts

### Cas FAIL P0

- frontmatter absent non detecte
- frontmatter non ferme non detecte

### Cas WARN P1

- ecart mineur de mapping ligne sans casse fonctionnelle

## Code de retour recommande

Le module n'expose pas de code retour direct.
Les scripts appelants conservent :

- `0` : PASS
- `1` : FAIL
- `2` : WARN

## Message de commit recommande

`refactor(system): add shared frontmatter utils process for validators`

## Risques & controles

### Risques

- regression transverse sur tous les validateurs
- ambiguite du contrat retour
- couplage excessif

### Controles

- tests de non-regression sur chaque script
- contrat de structure stable
- responsabilites separees (utils vs rules)

## Criteres de reussite

Le process est reussi si :

- le parsing est unique et stable
- les scripts appeles retournent les memes verdicts qu'avant
- la maintenance est simplifiee

## Next step unique

Creer la **Spec Tech** de `frontmatter_utils` avec exemples d'entree/sortie et
cas limites.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (09-03-2026) : passage en FROZEN.
- v1.0 (09-03-2026) : creation du process.
