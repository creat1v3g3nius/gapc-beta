---
id: GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
type: TOOLING
title: GapcWorkspaceRules
version: v1.8
status: FROZEN
created: 01-03-2026
updated: 12-03-2026
tags: [package, gapc, tooling, pipeline, workspace, rag]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_01_RUNBOOK_PRODUCT, PIPELINE_02_BACKLOG_PRODUCT, PIPELINE_03_BACKLOG_COMPOSANTS, PIPELINE_04_OPTIMIZATION_PROTOCOL, PIPELINE_05_RELEASE_FREEZE, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_01_GEL_RULES, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_02_RAG_QG, GAPC_INDEX_04_TOOLING]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_02_PIPELINE
---

# GAPC_TOOLING_PIPELINE_01 - Workspace Rules (actifs + sources + RAG)

## Objet
Règles PACKAGE qui encadrent l’usage du workspace (PRODUCT) quand GAPC est actif :
- actifs uniques,
- profils de scope,
- priorités de sources GAPC-only,
- non-invention (`NON TROUVÉ`).

---

## 1) Actifs (P0)
- package actif : `PACKAGE_00_GAPC`
- product actif : `PRODUCT_XX` (si contexte product)

Interdit : multi-products ou multi-packages dans une réponse/exécution.

---

## 2) Profils (P0)
- **RulesOnly** : CORE + discipline GAPC (pas de product)
- **GAPC+Product** : CORE + GAPC + product actif

Règle : commencer petit (RulesOnly) puis étendre.

---

## 3) Priorités de sources (P0)
1) CORE transverse
2) GAPC discipline (scope/risk/gel/rag)
3) autres docs package GAPC
4) PRODUCT actif
5) SYSTEM (procédures)

Interdit : sources d’un autre package “actif”.

Format attendu si le mentor restitue cet ordre :
- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `PRODUCT actif`
- `SYSTEM`

Clarification de scope :
- pour `WS_01 PackageScoped`, conserver `PRODUCT actif`,
- pour `WS_02 ProductScoped`, appliquer la regle `PRODUCT` plus specifique et restituer `docs product actifs`,
- ne pas reutiliser le format `WS_01` dans un workspace produit.

Format de sortie attendu pour une question simple sur les priorités de sources :
- la liste ordonnée seule
- puis `Sources utilisées :`

Interdit :
- supprimer `PRODUCT actif` de l ordre,
- fusionner `GAPC discipline` avec tout le package,
- annoter un fichier `PACKAGE` comme `CORE` ou `SYSTEM`,
- ajouter `Matrice de rôles`, `Rôle nominal`, `Justification`, `Conclusion`, `Audit` ou `Next step unique`.

Exemple minimal valide :
- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `PRODUCT actif`
- `SYSTEM`
- `Sources utilisées : GAPC_DISCIPLINE_00_RAG_PROFILE.md, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES.md`

Pour une question simple sur la hiérarchie d autorité, le mentor doit produire seulement :
- la hiérarchie,
- les sources utilisées.

Interdit :
- ajouter `Audit`, `Comparaison`, `Run plan` ou `Next step unique` si non demandés,
- annoter une source `PACKAGE` avec plusieurs arcs.

---

## 4) Qualité réponse/exécution (P0)
- sources obligatoires (IDs) ou `NON TROUVÉ`
- no-secrets/no-PII
- fallback API éventuel : explicite, justifié, minimisé, sans secret/PII (hérité CORE)
- > 3 actions → backlog CO (pas liste vague)
- décision structurante → ADR-lite

Pour une comparaison `CORE vs PACKAGE` :
- citer au minimum une source `CORE` et une source `PACKAGE`
- utiliser des arcs exacts si les sources sont annotées

Pour une matrice de rôles :
- nommer le rôle, pas le fichier
- `checklist documentaire` => `AnythingLLM local`
- `patch / exécution / tests` => `Codex`
- `API externe` => `API externe fallback`

Format attendu :
- 1 bloc par tâche
- `Tâche`
- `Rôle nominal`
- `Justification`
- `Sources utilisées`

Interdit :
- produire une liste condensée `tache -> role`
- ajouter `Conclusion`, `Audit`, `Run plan`, `Note` ou `Next step unique`

Exemple minimal valide :
- `Tâche : produire une checklist documentaire GAPC`
- `Rôle nominal : AnythingLLM local`
- `Justification : la checklist documentaire relève du mentor documentaire dans le périmètre GAPC.`
- `Sources utilisées : GAPC_DISCIPLINE_00_RAG_PROFILE.md, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES.md`

Pour un refus de package non actif :
- refuser explicitement
- demander isolation
- ne pas répondre `NON TROUVE` si la source existe mais que l actif est incorrect

---

## Changelog
- v1.8 (12-03-2026) : clarifie la difference de sortie entre `WS_01` (`PRODUCT actif`) et `WS_02` (`docs product actifs`) pour eviter la derive `T2`.
- v1.7 (11-03-2026) : ajoute le format de sortie exact pour une question simple sur les priorités de sources et interdit les blocs parasites de type `Matrice de rôles` ou `Audit`.
- v1.6 (11-03-2026) : ajoute le format bloc-par-bloc obligatoire pour la matrice des rôles et interdit les listes condensées et blocs parasites.
- v1.5 (11-03-2026) : ajoute les formats simples attendus pour hiérarchie et refus d isolation, et réduit le bruit des réponses package-scoped.
- v1.4 (10-03-2026) : ajoute le format attendu pour l ordre des sources GAPC et verrouille les règles `source -> arc` et `role -> tache`.
- v1.3 (10-03-2026) : réaligne les priorités de sources sur le CORE et rappelle la contrainte de fallback API héritée.
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création règles workspace GAPC (P1).

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
