---
id: WORKFLOW_01_COMPOSANTS
type: WORKFLOW
title: WorkflowProductComposantsRules
version: v1.4
status: DEPRECATED
created: 27-02-2026
updated: 13-03-2026
tags: [workflow, composants-rules, cache, deprecated]
depends_on:
  - BACKLOG_01_SYSTEM_RUN_SETUP_PRODUCT
  - PIPELINE_00_PRODUCT
  - PIPELINE_03_BACKLOG_COMPOSANTS
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_01_RUN
---

# WORKFLOW_01 - Workflow Product Composants (Legacy)

## Statut

- `DEPRECATED`
- annexe historique, hors noyau `WORKFLOW`
- ne plus utiliser ce document comme source canonique pour piloter les CO

## Redirection canonique

- cadrage pipeline produit : `PIPELINE_00_PRODUCT`
- standard backlog composants : `PIPELINE_03_BACKLOG_COMPOSANTS`
- pilotage de la migration `WORKFLOW` : `BACKLOG_01_SYSTEM_RUN_SETUP_PRODUCT`

## Rappels qui restent valides

- `1 CO = 1 intention`
- `1 CO = 1 livrable principal`
- si `> 5 fichiers` sont touches, il faut scinder
- une decision structurante appelle une `ADR-lite`

## Ce qui change

- le pilotage backlog ne vit plus dans `SYSTEM_01_RUN`
- les CO doivent etre decrits et qualifies dans les pipelines et templates du
  `CORE`
- les runbooks `WORKFLOW_*` coeur consomment les CO, mais ne definissent plus
  leur standard documentaire

## Next step unique

- utiliser `PIPELINE_03_BACKLOG_COMPOSANTS` pour tout nouveau CO et ne plus
  etendre `WORKFLOW_01`.

## Amendements (DEPRECATED)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (13-03-2026) : archive en `CACHE_SYSTEM_01_RUN` pour sortir du scope
  SYSTEM actif.
- v1.3 (13-03-2026) : passe en `DEPRECATED` et redirige vers
  `PIPELINE_00_PRODUCT` et `PIPELINE_03_BACKLOG_COMPOSANTS`.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
