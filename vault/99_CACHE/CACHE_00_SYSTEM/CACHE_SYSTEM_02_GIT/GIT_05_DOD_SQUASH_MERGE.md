---
id: GIT_05_DOD_SQUASH_MERGE
type: GIT
title: GitSquashMergeProcedure
version: v1.2
status: DEPRECATED
created: 06-03-2026
updated: 13-03-2026
tags: [git, dod, merge, squash, cache, deprecated]
depends_on: [GIT_02_BRANCH_POLICY, GIT_03_PATCH_COMMIT]
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_02_GIT
---

# GIT_05 - DoD Squash Merge

## Statut
- `DEPRECATED`
- source active remplacee par `GIT_03_PATCH_COMMIT`

Objectif historique : formaliser la DoD de merge vers `main` et une procédure squash merge reproductible.

## Raison de dépréciation
- la DoD de merge et la procédure squash merge vivent maintenant dans `GIT_03_PATCH_COMMIT`,
- maintenir deux fichiers actifs sur le meme sujet creait un doublon de doctrine.

## Action
- lire `GIT_03_PATCH_COMMIT`
- ne plus maintenir `GIT_05`

## Changelog
- v1.2 (13-03-2026) : archive en `CACHE_SYSTEM_02_GIT` apres fusion de la source active dans `GIT_03_PATCH_COMMIT`.
- v1.1 (13-03-2026) : fichier deprecate ; contenu fusionne dans `GIT_03_PATCH_COMMIT`.
