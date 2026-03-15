---
id: WORKFLOW_00_PIPELINE
type: WORKFLOW
title: PipelineExecutionWorkflow
version: v1.3
status: FROZEN
created: 27-02-2026
updated: 13-03-2026
tags: [workflow, pipeline-execution, run, system]
depends_on: []
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# WORKFLOW_00 - Pipeline Execution Workflow

Règles opérationnelles minimales pour exécuter le workflow :
**Obsidian (Vault) → VS Code + Git (+ Copilot/Codex) → AnythingLLM
(Mentor/RAG)**,
avec traçabilité, reproductibilité, et discipline **Doc + Code**.

---

## 1. Principes

1. **Doc et/ou Code** : toute évolution technique produit :

- une action documentaire (Vault)
- une action code (repo + commit + tests)

1. **Tooling-first** : dès qu’un livrable correspond à un TOOLING

   (TPL/CHECKLIST//KNOWLEDGE/PIPELINE/EXTENSION), utiliser le modèle.

1. **Patch explicite** : pas de suggestions vagues.

- soit fichier complet,
- soit bloc START/END REPLACE,
- soit diff/patch Git.

1. **No secrets** : aucune clé/token/PII en clair.

- `.env` ignoré, `.env.example` commit.

## 1.1 Doctrine `WORKFLOW` vs `SETUP_PRODUCT`

- `WORKFLOW_*` porte l execution quotidienne : lancer une session, produire

  un patch, rerun les controles, clore, gerer un incident.

- `SETUP_PRODUCT_*` porte la composition d un product : bootstrap, profil,

  routine de maintien, cycle de vie, merge-out, gouvernance.

- `WORKFLOW_*` ne decide pas de la structure cible d un product.
- `SETUP_PRODUCT_*` ne detaille pas les gestes operatoires pas-a-pas de la

  session.

- si une tache demande `quoi maintenir` ou `quand revalider`, regarder

  `SETUP_PRODUCT_*`.

- si une tache demande `quoi executer maintenant`, regarder `WORKFLOW_*`.

---

## 2. Source of truth

- Vérité stable : Vault (META/FIELD/RESTRAINT)
- Vérité secondaire (TOOLING/PACKAGE) : fichiers KNOWLEDGE ET SOT
- Exécution : repo Git (VS Code + Git)
- Aide au raisonnement : AnythingLLM (lecture/extraction), jamais décision

  autonome

---

## 3. Règles VS Code + Copilot/Codex (in-IDE)

- **Diff-first** : demander un diff avant application.
- **No auto-commit** : tu valides le diff, puis tu commits.
- **Scope atomique** : 1 patch = 1 intention = 1 composant (CO) (autant que

  possible).

- **Élements actifs** : 1 product actif = 1 package actif.
- **Tests minimum** : smoke runner obligatoire sur toute modif non-triviale.
- Si changement structurant → ADR-lite.

---

## 4  Règles AnythingLLM

- Démarrer small corpus (RulesOnly).
- Exiger sources : citations si possible, sinon fichiers.
- Si info absente → répondre “NON TROUVÉ”.
- Check package et product actif.
- Étendre par couches + tests après chaque ingestion.

---

## 5. Contrôle qualité minimal

Avant merge/main :

- smoke OK
- validator OK
- diff relu
- pas de secrets

## 5.1 Frontiere d integration

- `WORKFLOW_03_START_SESSION`, `WORKFLOW_04_END_SESSION`,

  `WORKFLOW_05_INCIDENT`, `WORKFLOW_06_VAULT_HEALTH_CHECK`,
  `WORKFLOW_07_TESTS_LLM`, `WORKFLOW_08_TESTS_CODEX` et
  `WORKFLOW_10_COMMANDES` sont les points d entree operatoires.

- `SETUP_PRODUCT_03_ROUTINE_OPERATIONS` declare les reruns obligatoires,

  mais delegue leur execution a `WORKFLOW_06`, `WORKFLOW_07` et
  `WORKFLOW_08`.

- `SETUP_PRODUCT_05_LIFECYCLE_POLICY` declare les etats et gates, mais

  delegue la preparation des preuves et des checks au noyau `WORKFLOW`.

- `SETUP_PRODUCT_07_GOVERNANCE_RULES` declare les obligations de

  revalidation et d isolation, mais ne remplace pas les runbooks quotidiens.

## 6. Changelog

- v1.0 (27-02-2026) : pipeline workflow gapc générique.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (13-03-2026) : ajoute la doctrine `WORKFLOW` vs `SETUP_PRODUCT` et

  verrouille la frontiere d integration.

- v1.2 (04-03-2026) : correction frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 (27-02-2026) : version initiale READY_TO_FREEZE.
