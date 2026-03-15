---
id: WORKFLOW_09_MARKDOWN_LINT_CHECK
type: WORKFLOW
title: MarkdownLintCheck
version: v1.6
status: FROZEN
created: 15-03-2026
updated: 15-03-2026
tags: [workflow, markdownlint, markdown, vscode, lint, run, system]
depends_on:
  - WORKFLOW_00_PIPELINE
  - WORKFLOW_06_VAULT_HEALTH_CHECK
  - WORKFLOW_10_COMMANDES
  - META_04_WRITING_RULES
  - META_05_FRONTMATTER
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# WORKFLOW_09 - Markdown Lint Check

## Objectif

Définir le runbook local pour lancer un contrôle `markdownlint` dans VS Code
sur les fichiers Markdown du repo, lire les diagnostics et rerun le check
jusqu à retour propre.

Ce workflow couvre le **lint local via l extension VS Code**.
Il ne suppose pas la présence d un binaire `markdownlint` dans le repo.

Le contrôle doit être réalisé sur le **socle complet des règles `MD001` à
`MD060`**, avec exceptions repo-wide documentées dans `.markdownlint.json`.

## Portée

Le workflow s applique à :

- un fichier Markdown unique
- un sous-dossier du vault
- tout le workspace

Le point de vérité de configuration est :

- `.markdownlint.json`

La baseline attendue est :

- toutes les règles natives `MD001` à `MD060` activées
- avec paramétrage local uniquement quand GAPC l exige

Exceptions repo-wide actuellement admises :

- `MD013` désactivée
- `MD046` désactivée

## Préconditions

- workspace Git GAPC ouvert dans VS Code
- extension `markdownlint` installée et active
- fichier de config workspace présent : `.markdownlint.json`
- panneau `Problems` disponible

## Commandes VS Code à utiliser

### 1. Lancer le lint du workspace

Depuis la palette de commandes :

- `Markdownlint: Lint all Markdown files in the workspace`

Commande interne associée :

- `markdownlint.lintWorkspace`

### 2. Corriger automatiquement les règles supportées

Sur le fichier ouvert :

- `Markdownlint: Fix all supported markdownlint violations in the document`

Commande interne associée :

- `markdownlint.fixAll`

### 3. Ouvrir ou créer la configuration

- `Markdownlint: Create or open the markdownlint configuration file for the workspace`

Commande interne associée :

- `markdownlint.openConfigFile`

## Boucle opératoire locale

### Étape 1 — Cibler le scope

Choisir explicitement le niveau de contrôle :

- fichier unique si patch local
- dossier si lot homogène
- workspace si bilan global avant commit

### Étape 2 — Lancer le check

Exécuter :

- `Markdownlint: Lint all Markdown files in the workspace`

Puis ouvrir :

- `View: Problems`

### Étape 3 — Lire les diagnostics

Le check doit couvrir **tout le périmètre `MD001` à `MD060`**,
hors règles explicitement désactivées dans la config workspace.

Traiter ensuite les diagnostics par familles de règles :

- `MD004` : style des listes non ordonnées
- `MD007` : indentation des listes non ordonnées
- `MD022` : lignes vides autour des headings
- `MD024` : headings dupliqués
- `MD029` : préfixes des listes ordonnées
- `MD030` : espaces après les marqueurs de liste
- `MD031` : lignes vides autour des blocs de code
- `MD032` : lignes vides autour des listes
- `MD033` : HTML inline
- `MD035` : style des séparateurs horizontaux
- `MD036` : emphase utilisée à la place d un heading
- `MD047` : fin de fichier
- `MD055` : style des pipes de tableau
- `MD056` : nombre de colonnes de tableau
- `MD060` : style des colonnes de tableau

Règle locale déjà configurée dans ce repo :

- `default = true`
- `MD007.indent = 4`
- `MD013 = false`
- `MD046 = false`
- `MD025.front_matter_title = ""`

Cela évite de compter `title:` du frontmatter comme un faux `H1`.

Règles effectivement observées dans `00_SYSTEM` lors des contrôles locaux :

- `MD004`
- `MD007`
- `MD024`
- `MD029`
- `MD030`
- `MD032`
- `MD033`
- `MD035`
- `MD036`
- `MD046`
- `MD055`
- `MD056`
- `MD060`

### Étape 4 — Corriger

Ordre recommandé :

1. appliquer `Fix all` quand la règle est supportée
1. corriger ensuite manuellement les cas restants
1. rerun le lint

### Étape 5 — Valider le lot

Le lot est `PASS` si :

- plus aucun diagnostic `markdownlint` ne remonte sur le scope choisi
- le frontmatter reste intact
- le document reste conforme aux règles GAPC

## Règles de prudence

- ne pas dégrader le frontmatter pour faire taire le lint
- ne pas casser `depends_on`, `scope`, `arc` ou `id`
- ne pas réécrire massivement un document si quelques lignes suffisent
- préserver les blocs de code et les exemples exacts

## Cas particuliers GAPC

### Frontmatter

Le repo utilise à la fois :

- un champ `title:` YAML métier
- un `H1` canonique dans le body

La config `.markdownlint.json` doit donc conserver :

```json
{
  "default": true,
  "MD007": {
    "indent": 4
  },
  "MD013": false,
  "MD046": false,
  "MD025": {
    "front_matter_title": ""
  }
}
```

### Pas de CLI repo

Le repo ne porte pas de binaire `markdownlint` exécutable par défaut.
Le contrôle local standard passe donc par l extension VS Code.

## Sortie attendue

Pour un lot contrôlé, produire au minimum :

- scope vérifié
- règles `MDxxx` rencontrées
- patch appliqué si nécessaire
- verdict final `PASS` ou `KO`

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.6 (15-03-2026) : desactive `MD013` et `MD046` au niveau repo et aligne
  le runbook sur ces exceptions globales.
- v1.5 (15-03-2026) : ajoute `MD046` parmi les regles observees dans
  `00_SYSTEM`.
- v1.4 (15-03-2026) : ajoute `MD035` parmi les regles observees dans
  `00_SYSTEM`.
- v1.3 (15-03-2026) : ajoute les règles observees en plus sur `00_SYSTEM`
  (`MD007`, `MD024`, `MD032`, `MD033`, `MD055`, `MD056`) et documente
  `MD007.indent = 4`.
- v1.2 (15-03-2026) : ajoute les règles observees dans `00_SYSTEM`
  (`MD004`, `MD029`, `MD030`, `MD036`, `MD060`) au runbook.
- v1.1 (15-03-2026) : explicite le contrôle sur tout le socle `MD001` à
  `MD060` et aligne la config workspace.
- v1.0 (15-03-2026) : création du runbook local pour le check `markdownlint`
  via l extension VS Code.
