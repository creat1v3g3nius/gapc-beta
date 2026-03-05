---
id: RUN_00_PIPELINE
type: RUN
title: PipelineExecutionWorkflow
version: v1.2
status: FROZEN
created: 27-02-2026
updated: 04-03-2026
tags: [workflow, pipeline-execution, run, system]
depends_on: []
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# RUN_00 - Pipeline Execution Workflow

Règles opérationnelles minimales pour exécuter le workflow :
**Obsidian (Vault) → VS Code + Git (+ Copilot/Codex) → AnythingLLM (Mentor/RAG)**,
avec traçabilité, reproductibilité, et discipline **Doc + Code**.

---

## 1. Principes 
1) **Doc et/ou Code** : toute évolution technique produit :
- une action documentaire (Vault)
- une action code (repo + commit + tests)

2) **Tooling-first** : dès qu’un livrable correspond à un TOOLING (TPL/CHECKLIST//KNOWLEDGE/PIPELINE/EXTENSION → utiliser le modèle.

3) **Patch explicite** : pas de suggestions vagues.
- soit fichier complet,
- soit bloc START/END REPLACE,
- soit diff/patch Git.

4) **No secrets** : aucune clé/token/PII en clair.
- `.env` ignoré, `.env.example` commit.

---

## 2. Source of truth
- Vérité stable : Vault (META/FIELD/RESTRAINT)
- Vérité secondaire (TOOLING/PACKAGE) : fichiers KNOWLEDGE ET SOT
- Exécution : repo Git (VS Code + Git)
- Aide au raisonnement : AnythingLLM (lecture/extraction), jamais décision autonome

---

## 3. Règles VS Code + Copilot/Codex (in-IDE)
- **Diff-first** : demander un diff avant application.
- **No auto-commit** : tu valides le diff, puis tu commits.
- **Scope atomique** : 1 patch = 1 intention = 1 composant (CO) (autant que possible).
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

## 6. Changelog
- v1.0 (27-02-2026) : pipeline workflow gapc générique.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 (27-02-2026) : version initiale READY_TO_FREEZE.
