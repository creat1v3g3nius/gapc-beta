---
id: GIT_03_PATCH_COMMIT
type: GIT
title: CodePatchCommit
version: v1.2
status: FROZEN
created: 28-02-2026
updated: 13-03-2026
tags: [boostrap, patch-commit, git, system]
depends_on: [INDEX_01_ARCHITECTURE, WORKFLOW_00_PIPELINE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_02_GIT
---

# GIT_03 - Code Patch & Commit (diff-first, tests, commit atomique)

Sécuriser l’exécution d’un **patch** (doc ou code)
jusqu’au **commit/push**, dans la nouvelle architecture GAPC :
`repo/` (Git) + `vault/` (Source of Truth) avec arcs
`00_SYSTEM/01_CORE/02_PACKAGE/03_PRODUCT/04_CACHE`.

Cette checklist est adaptée à :

- workflow `work/* → main` (squash merge recommandé),
- validations **bloquantes**

  (validator frontmatter/naming) quand on touche le Vault,

- smoke runner quand on touche scripts/outillage/config,
- discipline **no-secrets**.

> Principe : **1 intention = 1 CO = 1 commit** (ou squash unique sur `main`).

---

## 1) Inputs (avant de commencer)

- **Arc touché (1 seul)** : `SYSTEM | CORE | PACKAGE | PRODUCT`
- **Package actif** : `<PACKAGE_ID>` (si applicable)
- **Product actif** : `<PRODUCT_ID>` (si applicable)
- **CO** : `<CO_ID>` (si PRODUCT)
- **Type** : `docs | chore | feat | fix | refactor | test`
- **Scope commit** : `system | core | package-xxx | product | scripts | git`

Stop condition :

- si tu touches **2 arcs** dans le même patch → scinde en 2 patches/commits.

---

## 2) Avant patch (P0)

- [ ] **Context Pack** rempli (Goal/Constraints/Files/Expected output).
- [ ] Si assistant (Codex/Copilot) : **diff-first** demandé.
- [ ] Je comprends “ce que ça change” (≥ 70%).
- [ ] Le patch respecte **1 intention** (CO unique ou objectif unique).
- [ ] Je sais quels fichiers sont

  “Source of Truth” (Vault) vs “Exécution” (repo).

---

## 3) Application du patch (P0)

- [ ] J’applique le patch dans VS Code (pas dans un export).
- [ ] Je relis le diff :
  - VS Code Source Control **et/ou** `git diff`
- [ ] Je supprime les fichiers parasites :
  - exports, caches, logs, fichiers temporaires
- [ ] **No-secrets** :
  - pas de token/clé/PII dans le diff
  - `.env` non tracké (gitignore)

Commande utile :

```bash
git diff
```

---

## 4) Validations minimum (P0)

### 4.1) Validator (obligatoire si Vault/structure)

À lancer si tu modifies :

- un fichier sous `vault/`
- une règle naming/frontmatter
- un index / un fichier “invariant”

- [ ] Validator OK (frontmatter + naming si dispo)
- [ ] `id` = nom du fichier (sans extension)
- [ ] champs YAML requis présents :

  `type/title/version/status/creation/maj/scope/tags/dependances/arc`

### 4.2) Smoke (obligatoire si scripts/outillage)

À lancer si tu modifies :

- `scripts/`
- `.vscode/`
- règles d’exécution / runner / validator

- [ ] Smoke runner OK
- [ ] Le smoke détecte au moins 1 erreur volontaire

  (si en phase de durcissement)

---

## 5) Stage (sélectif) (P0)

- [ ] Je stage **uniquement** les fichiers liés à l’intention.
- [ ] J’utilise `git add -p` si nécessaire.

Commandes :

```bash
git status
git add -p
```

Stop condition :

- si je suis tenté de “stage tout”

  → l’intention est probablement trop large.

---

## 6) Commit atomique (P0)

- [ ] Message conforme : `type(scope): action`
- [ ] Pas de “WIP”, pas de commit fourre-tout.
- [ ] Push effectué.

Commandes :

```bash
git commit -m "type(scope): action"
git push
```

Exemples :

- `docs(system): add WORKFLOW_06 incident checklist`
- `docs(core): tighten naming rules`
- `chore(scripts): improve frontmatter validator output`
- `fix(smoke): handle missing vault folders`

---

## 7) Après commit (P0)

- [ ] CO mis à jour (Done/Blocked) + lien commit (message ou hash).
- [ ] Si un contournement a été fait

  (pas de smoke, etc.) : justification écrite.

- [ ] Next step unique noté (≤ 1 session si possible).

---

## 8) Intégration vers `main` (quand applicable)

Utilité :

- ne sert pas au patch quotidien minimal,
- sert quand un lot doit etre intégré proprement dans `main`,
- remplace la procédure séparée anciennement portée par `GIT_05`.

### 8.1) DoD merge vers `main`

- [ ] Validator : PASS
- [ ] Smoke : PASS
- [ ] `git status` clean avant merge
- [ ] no-secrets : `.env`, clés, PII absents du stage/diff
- [ ] intention cohérente : 1 lot de changements maitrisé
- [ ] `git diff --cached` relu avant commit final

### 8.2) Procédure squash merge (locale)

```bash
git switch main
git pull --rebase
git merge --squash work/<topic>
git commit -m "type(scope): action"
git push
```

### 8.3) Vérifications post-merge

```bash
git status
git log --oneline -n 5
python scripts/ValidateFrontmatter.py \
  --strict --enforce-unique-ids --vault vault
python scripts/SmokeRunner.py
```

Règle :

- garder `main` lisible et stable,
- si conflit ou doute, abort et reprendre proprement,
- cette étape complète le `diff-first`, elle ne le remplace pas.

---

## 9) Red flags (STOP)

- [ ] 2 intentions dans le même diff
- [ ] patch énorme sans validations
- [ ] incompréhension totale du changement
- [ ] présence d’un secret/token/PII
- [ ] modifications dans 2 arcs (ex: CORE + PRODUCT) sans split

---

## 10) Mini-playbooks (cas fréquents)

### 9.1) J’ai committé trop large

- [ ] Revenir en arrière (safe) : `git revert <sha>` (si déjà push)
- [ ] Refaire 2 commits atomiques

### 9.2)J’ai oublié le validator

- [ ] Revenir à l’étape 3.1
- [ ] Si correction : nouveau commit `fix(...)` ou `docs(...)`

### 9.3) J’ai accidentellement tracké un `.env`

- [ ] `git restore --staged .env`
- [ ] si déjà tracké : `git rm --cached .env`
- [ ] ajouter `.env` au `.gitignore`
- [ ] commit correctif sans secret

---

## 11) Changelog

- v1.0 (28-02-2026) : version arcs,

  package/product actifs,
  intégration validator/smoke + policy work/main.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (13-03-2026) : fusionne la DoD squash merge

  de `GIT_05` dans `GIT_03`
  et formalise l integration vers `main`.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
