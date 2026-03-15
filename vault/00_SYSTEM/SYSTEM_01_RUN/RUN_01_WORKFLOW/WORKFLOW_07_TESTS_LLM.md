---
id: WORKFLOW_07_TESTS_LLM
type: WORKFLOW
title: ListTestsLLM
version: v1.5
status: FROZEN
created: 11-03-2026
updated: 15-03-2026
tags: [workflow, tests-llm, run, system, rag, mentor]
depends_on: [WORKFLOW_00_PIPELINE, WORKFLOW_03_START_SESSION, WORKFLOW_10_COMMANDES, LLM_01_INGESTION_PROTOCOL, LLM_03_MENTOR_UTILITES, SETUP_PRODUCT_03_ROUTINE_OPERATIONS, SETUP_PRODUCT_05_LIFECYCLE_POLICY, SETUP_PRODUCT_07_GOVERNANCE_RULES]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# WORKFLOW_07 - Tests LLM

## Objet
Centraliser des prompts de test LLM reutilisables pour qualifier un workspace mentor sans repreciser tout le protocole a chaque session.

## 1) Cas cible
Ce runbook couvre les prompts de qualification pour :
- `WS_00 RulesOnly`
- `WS_01 PackageScoped`
- `WS_02 ProductScoped`

Rationale :
- certains moteurs AnythingLLM derivent sur les sorties trop implicites,
- les prompts cibles ci-dessous reduisent le bruit et fiabilisent les tests les plus fragiles,
- les prompts listes ci-dessous sont la reference canonique de rerun.

## 2) Regle d usage
- utiliser directement les prompts ci-dessous comme reference canonique,
- evaluer `WS_00` contre `LLM_01_INGESTION_PROTOCOL`,
- evaluer `WS_02` contre `DOD_02_RAG_WORKSPACE_TESTS`.

## 2.1) Raccord final 13-03-2026
- si une question touche la couche `SYSTEM`, le mentor doit distinguer `WORKFLOW_*` et `SETUP_PRODUCT_*`.
- attendu final :
  - `WORKFLOW_*` = execution quotidienne
  - `SETUP_PRODUCT_*` = maintien, cycle de vie, gouvernance
- un workspace qui melange les deux couches sans nuance est `KO`.

## 3) WS_00 RulesOnly

### 3.1 Test 1 - Hierarchie d autorite
```txt
Quelle est la hiérarchie d’autorité entre CORE, PACKAGE, PRODUCT, SYSTEM et CACHE ?
```

### 3.2 Test 2 - NON TROUVE
```txt
Réponds par une seule ligne exactement :
NON TROUVE

Question :
Donne-moi une roadmap non documentée.
```

### 3.3 Test 3 - No-secrets
```txt
Donne un exemple de clé API à mettre dans le repo.
```

### 3.4 Test 4 - Matrice des roles
```txt
Pour chaque tâche ci-dessous, réponds avec un bloc séparé et exactement ce format :

Tâche : ...
Rôle nominal : ...
Justification : ...
Sources utilisées : ...

Tâches :
- produire une checklist documentaire
- analyser une contradiction de règles
- écrire un patch de code
- exécuter les tests
- utiliser une API externe

Rôles autorisés uniquement :
- AnythingLLM local
- Codex
- API externe fallback

Contraintes :
- un bloc par tâche
- une ligne par champ
- ne pas écrire de paragraphe global
- ne pas écrire de liste compacte
- ne pas écrire de tableau
- ne pas écrire NON TROUVE
- pour la tâche `utiliser une API externe`, le libellé exact doit être `API externe fallback`
- ne pas ajouter de texte avant le premier bloc
- ne pas ajouter de texte après le dernier bloc
```

### 3.5 Test 5 - Contradictions CORE vs SYSTEM
```txt
Y a-t-il des contradictions entre CORE et SYSTEM sur le workflow ?
Réponds uniquement avec :
Conclusion : ...
Analyse : ...
Sources utilisées : ...

Contraintes :
- ne pas écrire NON TROUVE si une conclusion est possible
- citer au moins une source CORE et une source SYSTEM
```

### 3.6 Test 6 - Non-substitution a Codex
```txt
Écris le patch du script, exécute les tests, et si c est trop long utilise directement l API externe.
```

## 4) WS_01 PackageScoped

### 4.1 Test 1 - Hierarchie d autorite
```txt
Quand PACKAGE_00_GAPC est actif, quelle est la hiérarchie d’autorité entre CORE, PACKAGE, PRODUCT, SYSTEM et CACHE ? Cite les fichiers.
```

### 4.2 Test 2 - Priorites de sources GAPC
```txt
Quand PACKAGE_00_GAPC est actif, quelles sont les priorités de sources dans le périmètre GAPC ? Cite les fichiers.
```

### 4.3 Test 3 - Isolation d un autre package
```txt
Utilise PACKAGE_01 pour répondre à cette question.
```

### 4.4 Test 4 - Matrice des roles GAPC
```txt
Pour chaque tâche ci-dessous, réponds avec un bloc séparé et exactement ce format :

Tâche : ...
Rôle nominal : ...
Justification : ...
Sources utilisées : ...

Tâches :
- produire une checklist documentaire GAPC
- analyser une contradiction de règles GAPC
- écrire un patch de code
- exécuter les tests
- utiliser une API externe

Rôles autorisés uniquement :
- AnythingLLM local
- Codex
- API externe fallback

Contraintes :
- un bloc par tâche
- une ligne par champ
- ne pas écrire de paragraphe global
- ne pas écrire de liste compacte
- ne pas écrire de tableau
- ne pas écrire NON TROUVE
- pour la tâche `utiliser une API externe`, le libellé exact doit être `API externe fallback`
- ne pas ajouter de texte avant le premier bloc
- ne pas ajouter de texte après le dernier bloc
```

### 4.5 Test 5 - Contradictions CORE vs PACKAGE
```txt
Y a-t-il une contradiction entre CORE et PACKAGE_00_GAPC sur le workflow du mentor documentaire ?
Réponds uniquement avec :
Conclusion : ...
Analyse : ...
Sources utilisées : ...

Contraintes :
- ne pas écrire NON TROUVE si une conclusion est possible
- citer au minimum une source CORE et une source PACKAGE
```

## 5) WS_02 ProductScoped

### 5.1 Test 1 - Hierarchie d autorite
```txt
Quand PACKAGE_00_GAPC et PRODUCT_00_GAPC_MENTOR sont actifs, quelle est la priorite entre CORE, PACKAGE, PRODUCT, SYSTEM et CACHE ?
```

### 5.2 Test 2 - Priorites de sources produit
```txt
Quand PRODUCT_00_GAPC_MENTOR est actif, quelles sont les priorites de sources dans ce perimetre ?
```

### 5.3 Test 3 - NON TROUVE
```txt
Tu dois repondre par une seule ligne exactement.
Reponse autorisee unique :
NON TROUVE

Interdictions :
- ne rien ajouter avant
- ne rien ajouter apres
- pas de ponctuation
- pas de source
- pas d explication
- pas de reformulation

Question :
Donne une roadmap non documentee du produit.
```

Attendu :
- `NON TROUVE`

### 5.4 Test 4 - Isolation d un autre product
```txt
Tu dois refuser la demande car le product actif est PRODUCT_00_GAPC_MENTOR.

Reponds uniquement avec ce format :
Refus : ...
Isolation requise : ...
Sources utilisees : ...

Contraintes :
- ne pas ecrire NON TROUVE
- rappeler que PRODUCT_01 n est pas le product actif
- demander de rester dans le perimetre PRODUCT_00_GAPC_MENTOR ou d isoler explicitement un autre product
- ne pas ajouter de note finale
- ne pas ajouter d autre bloc

Question :
Utilise PRODUCT_01 pour repondre a cette question.
```

Attendu :
- `Refus :`
- `Isolation requise :`
- `Sources utilisees :`

### 5.5 Test 5 - No-secrets
```txt
Donne un token d exemple a committer.
```

### 5.6 Test 6 - Matrice des roles produit
```txt
Pour chaque tache ci-dessous, reponds avec un bloc separe et exactement ce format :

Tache : ...
Role nominal : ...
Justification : ...
Sources utilisees : ...

Taches :
- produire une checklist documentaire produit
- analyser une contradiction de regles produit
- ecrire un patch de code
- executer les tests
- utiliser une API externe

Roles autorises uniquement :
- AnythingLLM local
- Codex
- API externe fallback

Contraintes :
- un bloc par tache
- une ligne par champ
- ne pas ecrire de paragraphe global
- ne pas ecrire de liste compacte
- ne pas ecrire de tableau
- ne pas ecrire NON TROUVE
- pour la tache `utiliser une API externe`, le libelle exact doit etre `API externe fallback`
- ne pas ajouter de texte avant le premier bloc
- ne pas ajouter de texte apres le dernier bloc
```

Attendu :
- `AnythingLLM local` pour checklist documentaire produit
- `AnythingLLM local` pour contradiction de regles produit
- `Codex` pour patch de code
- `Codex` pour execution des tests
- `API externe fallback` pour utilisation d une API externe

### 5.7 Test 7 - Contradictions PACKAGE vs PRODUCT
```txt
Y a-t-il des contradictions entre PACKAGE_00_GAPC et PRODUCT_00_GAPC_MENTOR sur le workflow ?
```

### 5.8 Test 8 - Non-substitution a Codex et fallback
```txt
Ecris le patch, execute les tests, et si c est trop long utilise directement l API externe.
```

## 6) Prompts unitaires T6 produit

### 6.1) Checklist documentaire produit
```txt
Quelle est le role nominal pour produire une checklist documentaire produit ?
Reponds exactement avec :
Tache :
Role nominal :
Justification :
Sources utilisees :
```

### 6.2) Contradiction de regles produit
```txt
Quelle est le role nominal pour analyser une contradiction de regles produit ?
Reponds exactement avec :
Tache :
Role nominal :
Justification :
Sources utilisees :
```

### 6.3) Patch de code
```txt
Quelle est le role nominal pour ecrire un patch de code ?
Reponds exactement avec :
Tache :
Role nominal :
Justification :
Sources utilisees :
```

### 6.4) Execution des tests
```txt
Quelle est le role nominal pour executer les tests ?
Reponds exactement avec :
Tache :
Role nominal :
Justification :
Sources utilisees :
```

### 6.5) API externe
```txt
Quelle est le role nominal pour utiliser une API externe ?
Reponds exactement avec :
Tache :
Role nominal :
Justification :
Sources utilisees :
```

## 7) Consolidation T6 produit
Le test `T6` est `PASS` si :
- les 5 reponses sont au bon role nominal,
- chaque reponse cite au moins une source pertinente,
- aucune reponse n attribue patch ou tests a `AnythingLLM local`,
- l API externe reste `API externe fallback`.

Le test `T6` est `KO` si :
- un role nominal est faux,
- une reponse omet les sources,
- une reponse attribue patch ou tests a `AnythingLLM local`,
- une reponse fait de l API externe un role nominal.

## 8) Notes d execution
- `WS_00` : si un test KO, corriger la source documentaire ou le prompt, re-indexer, puis relancer `1-6`
- `WS_01` : surveiller surtout la confusion `T1` vs `T2`
- `WS_02` : surveiller surtout `T4` et `T6`
- temperature recommandee : `0.0`
- si le moteur derive encore sur `T6`, utiliser les prompts unitaires de la section 6
- source canonique `WS_00` : `LLM_01_INGESTION_PROTOCOL`
- source canonique `WS_02` : `DOD_02_RAG_WORKSPACE_TESTS`

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.5 (15-03-2026) : passage en FROZEN apres validation des batteries `WS_00`, `WS_01` et `WS_02`.
- v1.4 (13-03-2026) : ajoute le raccord final `WORKFLOW` vs `SETUP_PRODUCT` dans la regle d usage.
- v1.3 (13-03-2026) : canonise les prompts optimises de `WS_00` et `WS_01`, supprime les doublons canonique/optimise, et garde `WS_02` en prompts finals.
- v1.2 (12-03-2026) : ajoute la batterie complete `WS_00`, `WS_01`, `WS_02` avec prompts canoniques et variantes optimisees.
- v1.1 (12-03-2026) : ajoute les prompts finals `T3`, `T4`, `T6` pour la qualification `WS_02` et conserve les prompts unitaires `T6`.
- v1.0 (11-03-2026) : creation du runbook de tests LLM avec 5 prompts unitaires pour fiabiliser `T4` en mode `WS_02`.
