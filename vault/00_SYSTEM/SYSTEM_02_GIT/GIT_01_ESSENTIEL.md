---
id: GIT_01_ESSENTIEL
type: GIT
title: GitEssentiel
version: v1.3
status: FROZEN
created: 28-02-2026
updated: 13-03-2026
tags: [boostrap, commandes, git, system]
depends_on: [INDEX_01_ARCHITECTURE, GIT_03_PATCH_COMMIT]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_02_GIT
---

# GIT_01 - Liste des commandes minimales du Git

Permettre d’utiliser Git **sans théorie inutile**, dans le
framework GAPC (Vault → Repo), en appliquant :

- **1 intention = 1 commit**
- **diff-first** (tu lis avant d’agir)
- **no-secrets** (aucun token/clé/PII versionné)
- workflow compatible avec l’architecture :

  `00_SYSTEM/01_CORE/02_PACKAGE/03_PRODUCT/04_CACHE`.

> Règle : travailler toujours depuis la racine repo
> (dossier contenant `.git/`).
> Obsidian lit/écrit dans `repo/vault/`, VS Code opère dans `repo/`.

---

## 1) Les 7 concepts à connaître (ultra court)

- **Repo** : dossier versionné (contient `.git/`).
- **Commit** : photo d’un changement intentionnel.
- **Diff** : ce qui change (à lire avant commit).
- **Stage** : sélection exacte de ce qui part dans le commit.
- **Branch** : ligne de travail (`main`, `work/*`).
- **Remote** : repo distant (ex: GitHub) = `origin`.
- **Rebase/Merge** : méthodes pour intégrer/aligner

  (débutant : suivre la policy du framework).

---

## 2) Commandes P0 (survie)

```bash
git status                 # où j’en suis ?
git diff                   # qu’est-ce qui a changé ?
git add <file>             # stage ciblé (recommandé)
git add -p                 # stage interactif (top pour 1 intention)
git commit -m "type(scope): action"
git pull --rebase          # récupérer + aligner proprement (si policy rebase)
git push                   # envoyer sur le remote
```

**Stop condition**

- Si `git status` montre “detached HEAD” ou “merge in progress”

  → ne pas continuer sans lire §6.

---

## 3) Workflow standard (safe) — 1 intention

### 3.1) Mini-cycle (le plus fréquent)

1) Vérifier :

```bash
git status
git diff
```

2) Stage **ciblé** :

```bash
git add path/to/file
# ou
git add -p
```

3) (Option) lancer validator/smoke si le framework l’impose :

```bash
python scripts/ValidateFrontmatter.py
# python scripts/SmokeRunner.py
```

4) Commit :

```bash
git commit -m "docs(system): update quickstart runbook"
```

5) Push :

```bash
git push
```

### 3.2) Messages de commit (convention)

Format :
`type(scope): action`

Types recommandés :

- `docs` (vault/system/core/package/product)
- `chore` (scripts/outillage/config)
- `feat|fix|refactor|test`

Scopes courants :

- `system`, `core`, `package-asso`, `package-gapc`, `product`, `scripts`, `git`

Exemples :

- `docs(core): tighten frontmatter rules`
- `chore(scripts): enforce frontmatter validation`
- `docs(product): add CO_002 backlog`

---

## 4) Branches (règle simple)

### 4.1) Policy

- `main` = stable
- `work/<topic>` = travail (une intention ou un petit lot cohérent)

Créer une branche :

```bash
git switch -c work/frontmatter-validator
```

Mettre à jour ta branche :

```bash
git pull --rebase
```

Finir :

```bash
git push -u origin work/frontmatter-validator
```

> Solo : tu peux merger vers `main` après validate/smoke.
> En équipe : PR obligatoire.

---

## 5) Dépannage (scénarios fréquents)

### 5.1) “Repo non détecté”

Symptôme :

- `git status` renvoie “not a git repository”.

Fix :

- ouvrir dans VS Code le dossier qui contient `.git/` (racine repo).

### 5.2) “Push rejected / non-fast-forward”

Fix safe (si policy rebase) :

```bash
git pull --rebase
git push
```

### 5.3) “J’ai stage un fichier sensible (.env)”

Fix :

```bash
git restore --staged .env
```

Puis :

- ajouter `.env` à `.gitignore`
- si déjà tracké :

```bash
git rm --cached .env
```

### 5.4) “Je dois annuler des changements”

Annuler changements **non committés** :

```bash
git restore .
```

Retirer du stage sans perdre les modifs :

```bash
git restore --staged <file>
```

---

## 6) Les 2 cas “danger” (ne pas improviser)

## 6.1) Detached HEAD

Symptôme :

- `git status` indique “HEAD detached”.

Fix safe :

```bash
git switch -c work/recover-detached
```

### 6.2) Merge/Rebase en cours

Symptôme :

- “You have unmerged paths” ou “rebase in progress”.

Règles :

- soit tu **termines** correctement,
- soit tu **aborts**.

Abort :

```bash
git merge --abort
git rebase --abort
```

---

## 7) Check fin de session (30 secondes)

- [ ] `git status` = clean
- [ ] push fait (ou noté pourquoi)
- [ ] aucun secret dans le diff
- [ ] 1 commit = 1 intention

---

## 8) Dépannage rapide (top 6)

### 8.1) Repo non détecté

Symptôme :

- `fatal: not a git repository`

Fix safe :

```bash
git rev-parse --show-toplevel
```

Si erreur :

- ouvrir le bon dossier repo dans VS Code
- relancer `git status`

### 8.2) Push rejected / non-fast-forward

Fix safe :

```bash
git pull --rebase
git push
```

### 8.3) Fichier sensible stage par erreur

Fix safe :

```bash
git restore --staged .env
# si déjà tracké:
git rm --cached .env
```

Puis compléter `.gitignore`.

### 8.4) Annuler des changements locaux

Fix safe :

```bash
git restore <file>
# ou pour tout le working tree:
git restore .
```

### 8.5) Detached HEAD

Fix safe :

```bash
git switch -c work/recover-detached
```

### 8.6) Merge/Rebase en cours

Fix safe :

```bash
git rebase --continue
# ou abort si nécessaire:
git merge --abort
git rebase --abort
```

### STOP conditions

- `detached HEAD` non résolu
- `merge/rebase in progress` non compris
- fichier sensible détecté dans le diff/stage
- changement touche plusieurs arcs sans intention claire

---

## 9) Changelog

- v1.0 (28-02-2026) : liste essentiel des commandes git

  dans VsCode pour la v1.0 du Gapc.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (13-03-2026) : fusionne le top 6 de depannage

  de `GIT_04_DEPANNAGE_CHECKLIST`.

- v1.2 (13-03-2026) : retire la dependance au bootstrap

  `GIT_00_CONFIG` devenu deprecated.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
