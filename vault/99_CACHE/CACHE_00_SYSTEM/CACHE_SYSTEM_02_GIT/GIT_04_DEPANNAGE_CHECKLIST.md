---
id: GIT_04_DEPANNAGE_CHECKLIST
type: GIT
title: DepannageGitChecklist
version: v1.1
status: DEPRECATED
created: 06-03-2026
updated: 13-03-2026
tags: [git, depannage, checklist, cache, deprecated]
depends_on: [GIT_01_ESSENTIEL, GIT_02_BRANCH_POLICY]
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_02_GIT
---

# GIT_04 - Checklist Depannage Git

But : checklist operateur consolidee "top 6" (symptome -> cause probable -> fix
safe).

Références consolidées :

- `GIT_01_ESSENTIEL`
- `GIT_02_BRANCH_POLICY`

## Scénario 1 — Repo non détecté

Symptôme : `fatal: not a git repository`
Cause probable : terminal ouvert hors racine contenant `.git/`
Fix safe :

```bash
git rev-parse --show-toplevel
# si erreur: ouvrir le bon dossier repo/ dans VS Code
```

Vérif : `git status` fonctionne.

## Scénario 2 — Push rejected (non-fast-forward)

Symptôme : `rejected` / `non-fast-forward`
Cause probable : branche distante en avance
Fix safe :

```bash
git pull --rebase
git push
```

Vérif : push OK sans conflit restant.

## Scénario 3 — Fichier sensible stage par erreur

Symptôme : `.env`/clé apparaît dans `git status` (staged)
Cause probable : `.gitignore` incomplet ou ajout accidentel
Fix safe :

```bash
git restore --staged .env
# si déjà tracké:
git rm --cached .env
```

Puis compléter `.gitignore`.
Vérif : `.env` n’apparaît plus dans les fichiers versionnés.

## Scénario 4 — Annuler des changements locaux

Symptôme : modifications locales à annuler
Cause probable : patch erroné ou mauvais scope
Fix safe :

```bash
git restore <file>
# ou pour tout le working tree:
git restore .
```

Vérif : `git status` revient à l’état attendu.

## Scénario 5 — Detached HEAD

Symptôme : `HEAD detached`
Cause probable : checkout d’un commit/tag sans branche
Fix safe :

```bash
git switch -c work/recover-detached
```

Vérif : `git branch --show-current` renvoie `work/recover-detached` (ou branche
cible).

## Scénario 6 — Merge/Rebase in progress

Symptôme : `unmerged paths` / `rebase in progress`
Cause probable : conflit non résolu
Fix safe :

```bash
# terminer proprement (résolution + add + continue)
git rebase --continue
# ou abort si nécessaire:
git merge --abort
git rebase --abort
```

Vérif : `git status` ne mentionne plus merge/rebase en cours.

## STOP Conditions (ne pas improviser)

- `detached HEAD` non résolu
- `merge/rebase in progress` non compris
- fichier sensible détecté dans le diff/stage
- changement touche plusieurs arcs sans intention claire

## Utilisation

- Exécuter cette checklist avant escalade incident.
- Si un cas sort du cadre, ouvrir incident P1 avec symptômes + commandes déjà
  tentées.

## Statut d archivage

- contenu utile fusionne dans `GIT_01_ESSENTIEL`
- ne plus maintenir ce fichier comme source active

## Changelog

- v1.1 (13-03-2026) : fusionne le contenu utile dans `GIT_01_ESSENTIEL` puis
  archive en `CACHE_SYSTEM_02_GIT`.
