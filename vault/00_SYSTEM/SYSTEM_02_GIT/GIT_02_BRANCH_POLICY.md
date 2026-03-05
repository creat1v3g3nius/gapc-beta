---
id: GIT_02_BRANCH_POLICY
type: GIT
title: BranchPolicy
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [boostrap, branch-policy, git, system]
depends_on: [GIT_00_CONFIG, GIT_01_ESSENTIEL]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_02_GIT
---

# GIT_02 - Branch Policy (main/work + merge + tags)

Permet de définir une gouvernance Git **simple, safe, scalable** pour le framework GAPC, alignée avec l’architecture :
`00_SYSTEM/01_CORE/02_PACKAGE/03_PRODUCT/04_CACHE`.

Principes :
- `main` = état stable (présentable / gelable)
- `work/*` = branches de travail (1 intention, 1 CO ou 1 lot cohérent)
- merges = contrôlés (validator + smoke)
- tags = jalons reproductibles (freeze)

Contraintes :
- **No secrets**
- **1 intention = 1 commit** (ou squash merge sur `main`)
- pas de commit direct sur `main` (sauf hotfix)

---

## 1) Règles (P0)

### 1.1) main (stable)
- Interdit : commit direct (sauf **hotfix** documenté).
- Doit rester “green” :
  - validator frontmatter/naming OK
  - smoke runner OK (si applicable)
- Sert de base pour toutes les branches `work/*`.

### 1.2) work/* (branches de travail)
- Toute modification se fait dans une branche `work/<topic>`.
- `topic` = intention courte (ex : `work/frontmatter-validator`, `work/runbooks-update`).
- Une branche = idéalement **1 CO** (ou une intention claire).
- Tu peux faire plusieurs commits sur `work/*`, tant que l’intention reste unique.

### 1.3) Un seul package/product actifs par session
Si ton travail touche un package ou un product, note :
- package actif
- product actif
dans le CO / note de session.
But : éviter les mélanges (RAG + docs).

---

## 2) Mise en place (repo neuf)

```bash
git init
git branch -M main
git remote add origin <URL_DU_REMOTE>
git push -u origin main
```

Créer ta première branche :
```bash
git switch -c work/bootstrap
git push -u origin work/bootstrap
```

---

## 3) Cycle de travail standard

### 3.1) Démarrer une intention
```bash
git switch main
git pull --rebase
git switch -c work/<topic>
```

### 3.2) Travailler (commits sur work)
- Lire diff → stage sélectif → (validator/smoke) → commit → push

```bash
git status
git diff
git add -p
python scripts/ValidateFrontmatter.py   # si présent
# python scripts/SmokeRunner.py         # si présent
git commit -m "docs(system): update runbook"
git push -u origin work/<topic>
```

### 3.3) Intégrer dans main (safe)

#### Option recommandée : squash merge
Objectif : garder `main` propre (1 intention = 1 commit).

Checklist avant merge :
- [ ] diff relu
- [ ] validator OK
- [ ] smoke OK (si applicable)
- [ ] pas de secrets (check `.env` / `.gitignore`)

Merge (selon ton environnement) :
- via PR GitHub (recommandé, même solo)
- ou local :

```bash
git switch main
git pull --rebase
git merge --squash work/<topic>
git commit -m "docs(system): update runbook"
git push
```

#### Nettoyage (option)
```bash
git branch -d work/<topic>
git push origin --delete work/<topic>
```

---

## 4) Hotfix (exception)

Quand `main` est cassée (P0) :
- créer une branche dédiée :
```bash
git switch -c work/hotfix-<topic>
```
- appliquer fix minimal + validator/smoke
- squash merge dans `main`
- tag si nécessaire

---

## 5) Tags (jalons “freeze”)

### 5.1) Quand tagger
Tagger quand :
- `main` est stable et reproductible
- l’architecture ou une release est “READY_TO_FREEZE/FROZEN”

### 5.2) Format recommandé
- `v0.1`, `v0.2`, `v1.0` (jalons framework)
- option : suffixe `-beta` si besoin

```bash
git tag -a v0.1 -m "v0.1 freeze framework"
git push origin v0.1
```

Règle : **1 tag = 1 état reproductible**.

---

## 6) Cas fréquents / erreurs

### 6.1) Mauvaise branche
```bash
git branch --show-current
git switch work/<topic>
```

### 6.2) Detached HEAD
```bash
git switch -c work/recover-detached
```

### 6.3) Merge/Rebase bloqué
Abort (si nécessaire) :
```bash
git merge --abort
git rebase --abort
```

---

## 7) DoD (Definition of Done) d’un merge

Un merge vers `main` est acceptable si :
- [ ] 1 intention (ou squash)
- [ ] validator OK
- [ ] smoke OK (si applicable)
- [ ] doc mise à jour (si doc change)
- [ ] aucun secret

---

## 8) Changelog
- v1.0 (28-02-2026) : version multi-branch work/*, squash merge, tags freeze.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
