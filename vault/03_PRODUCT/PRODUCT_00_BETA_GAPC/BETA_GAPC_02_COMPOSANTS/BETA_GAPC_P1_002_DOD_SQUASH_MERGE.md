---
id: BETA_GAPC_P1_002_DOD_SQUASH_MERGE
type: DOD
title: DodSquashMergeProcedure
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [beta, p1, dod, merge, squash, git]
depends_on: [GIT_02_BRANCH_POLICY, BETA_GAPC_COMPOSANTS_BACKLOG]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_02_COMPOSANTS
---

# BETA_GAPC_P1_002_DOD_SQUASH_MERGE

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
