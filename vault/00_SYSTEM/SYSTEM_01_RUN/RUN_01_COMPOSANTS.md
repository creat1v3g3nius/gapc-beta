---
id: RUN_01_COMPOSANTS
type: RUN
title: WorkflowProductComposantsRules
version: v1.2
status: FROZEN
created: 27-02-2026
updated: 09-03-2026
tags: [workflow, composants-rules, run, system]
depends_on: [INDEX_01_ARCHITECTURE, RUN_00_PIPELINE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# RUN_01 - Workflow Product Composants (Rules)

Ce document permet de définir comment utiliser le backlog de composants (CO) (Change Orders) comme **pilote** du travail :
- un CO = une étape de production
- idéalement une CO = un commit,
- une CO = un livrable vérifiable.

## 1. Source de vérité
Fichier structure et fonctionnement générique du Backlog (dans le repo/Vault) :
- `PIPELINE_00_BACKLOG_PRODUCT.md`

Règle : ne jamais maintenir deux backlogs concurrents.  
Si un backlog doit être remplacé : marquer l’ancien `DEPRECATED` et pointer vers le nouveau.

## 2. Statuts (pilotage)
- Draft → Ready → In progress → Blocked → Done

## 3. Règle d’exécution
Pour chaque session :
1) Choisir **un product actif** et **un composant actif**
2) Préparer un **Context Pack**
3) Exécuter Doc et/ou Code
4) Smoke minimal
5) Commit atomique
6) Mettre à jour le statut composant

## 4. Détection de dérive
Stop si :
- une CO contient 2 intentions/étapes,
- une CO implique une décision structurante non tracée (ADR-lite),
- la CO “grandit” sans critère d’acceptation.

## 5. Quick check (gel / qualité)
Le backlog est “bon” si :
- les CO sont atomiques,
- chaque CO a acceptance criteria,
- priorité P0/P1/P2 est explicite (scopeclassifier),
- dépendances raisonnables.

## 6. Changelog
-v1.0 (27-02-2026) : Workflow et règles de production par composants pour v1.0 GAPC

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
