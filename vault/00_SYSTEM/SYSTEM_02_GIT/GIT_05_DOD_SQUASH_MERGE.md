---
id: GIT_05_DOD_SQUASH_MERGE
type: GIT
title: GitSquashMergeProcedure
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 08-03-2026
tags: [git, dod, merge, squash, system]
depends_on: [GIT_02_BRANCH_POLICY, GIT_03_PATCH_COMMIT]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_02_GIT
---

# GIT_05 - DoD Squash Merge

Objectif : formaliser la DoD de merge vers `main` et une procédure squash merge reproductible.

## DoD merge vers main
- Validator `./scripts/ValidateFrontmatter.py` : PASS
- Smoke `./scripts/SmokeRunner.py` : PASS
- `git status` clean avant merge
- No-secrets : `.env`/clés absents du stage/diff
- Intention cohérente : 1 lot de changements maîtrisé

## Procédure squash merge (locale)
```bash
git switch main
git pull --rebase
git merge --squash work/<topic>
git commit -m "docs(product): squash merge work/<topic>"
git push
```

## Vérifications post-merge
```bash
git status
git log --oneline -n 5
./scripts/ValidateFrontmatter.py
./scripts/SmokeRunner.py
```

## Notes d'usage
- Garder `main` stable et lisible (1 intention = 1 commit squash).
- Faire la revue diff avant commit final (`git diff --cached`).
- En cas de conflit : résoudre proprement, sinon abort et reprendre.
