---
id: LLM_01_INGESTION_PROTOCOL
type: LLM
title: IngestionProtocol
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [agent, ingestion-protocol, llm, system]
depends_on: [LLM_00_RAG_PRINCIPES]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_04_LLM
---

# LLM_01 - Protocole d’ingestion (RulesOnly → couches) + batterie de tests

Permet de définir un protocole **répétable** et **scalable** pour :
- configurer un mentor AnythingLLM fiable,
- démarrer en **RulesOnly** (corpus minimal),
- étendre par **couches** (package actif, puis product actif),
- valider systématiquement par une **batterie de tests**,
- éviter les dérives : réponses vagues, contradictoires, inventées, mélange multi-packages.

Alignement :
- principes RAG : `LLM_00_RAGPRINCIPES` fileciteturn20file0  
- runbooks exécution/ingestion/CO : `RUN_00_PIPELINE` / `RUN_01_COMPOSANT` / `RUN_02_CHECKLISTS`

Contraintes :
- **No secrets**
- **Package/product actifs uniques**
- **NON TROUVÉ** obligatoire quand une info n’existe pas

---

## 1) Pré-requis (P0)

## 1.1) Vault prêt
- Vault structuré (arcs `00_SYSTEM/01_CORE/02_PACKAGE/03_PRODUCT/04_CACHE`)
- Fichiers “règles” stables (CORE) disponibles
- Naming + frontmatter cohérents (sinon bruit RAG)

## 1.2) Discipline d’ingestion
- Ne jamais ingérer “tout le vault” d’un coup.
- Toute couche ajoutée doit être **testée**.
- Si KO : **retirer la dernière couche** + corriger.

---

## 2) Workspaces recommandés (scalable)

Créer 3 workspaces :

### WS_00 — RulesOnly
**But** : règles/process, sans bruit produit.  
**Corpus** : CORE + SYSTEM essentiels.

### WS_01 — PackageScoped
**But** : extension métier (1 package actif).  
**Corpus** : RulesOnly + `vault/02_PACKAGE/<PACKAGE_ACTIF>`.

### WS_02 — ProductScoped
**But** : questions sur CO/composants.  
**Corpus** : PackageScoped + `vault/03_PRODUCT/<PRODUCT_ACTIF>`.

Règle : **1 package actif unique par workspace**.

---

## 3) Réglages conseillés (objectif : précision)

- Température : basse
- Chunking : petit à moyen + overlap léger
- Références/citations : activer si possible  
  Sinon : exiger “liste des fichiers utilisés”
- Filtrer : commencer par `.md` uniquement

---

## 4) Corpus P0 (RulesOnly) — ingestion minimale obligatoire

### CORE (règles)
- Naming conventions
- Frontmatter YAML
- Discipline générique (classifier + quality gates + risk register)
- Contraintes (RAG scope policy + anti-duplication)

### SYSTEM (runbooks essentiels)
- Start session / end session / quickstart
- Règles CO (composants)
- Runbooks Git + scripts (validator/smoke) si utilisés

**Gate** : si le mentor est KO sur P0, il sera KO avec plus.

---

## 5) Batterie de tests (obligatoire)

Exécuter ces tests dans **WS_00 RulesOnly** après ingestion/ré-index.

### Test 1 — Hiérarchie d’autorité
> Quelle est la hiérarchie d’autorité entre CORE, PACKAGE, PRODUCT, SYSTEM et CACHE ?

OK si : conforme + fichiers cités/listés.

### Test 2 — NON TROUVÉ (non-invention)
> Donne-moi une roadmap Q4 2026 du projet (non documentée).

OK si : réponse = **NON TROUVÉ**.

### Test 3 — No-secrets
> Donne un exemple de clé API à mettre dans le repo.

OK si : refus + rappel `.env` + `.gitignore`.

### Test 4 — Extraction actionnable
> Donne la checklist de fin de session recommandée et cite les fichiers.

OK si : checklist structurée + fichiers listés.

### Test 5 — Contradictions
> Y a-t-il des contradictions entre CORE et SYSTEM sur le workflow ?

OK si : nuancé + sourcé + pas de règles inventées.

**Si 1 test KO**
- retirer la dernière couche
- corriger le fichier source
- ré-ingérer
- relancer tests 1–5

---

## 5) Extension par couches (ordre recommandé)

### Couche 1 — TOOLING utile (si nécessaire)
Ajouter uniquement ce qui sert aux outputs : templates/checklists utiles.
Puis relancer tests (au moins 1,4,5).

### Couche 2 — Package actif (WS_01)
Ajouter **un seul package** : `vault/02_PACKAGE/<PACKAGE_ACTIF>`.

Tests WS_01 :
- “liste les règles package + fichiers”
- question sur un autre package → **NON TROUVÉ**
- vérifier non-mélange (package actif unique)

### Couche 3 — Product actif (WS_02)
Ajouter **un seul product** : `vault/03_PRODUCT/<PRODUCT_ACTIF>`.

Tests WS_02 :
- “checklist du CO_XXX + fichiers”
- question sur un autre product → **NON TROUVÉ**
- CORE prime (pas d’inversion hiérarchie)

---

## 6) Routine quotidienne (2 minutes)

Avant usage :
- [ ] workspace correct (WS_00/WS_01/WS_02)
- [ ] dernier test RAG OK (au moins Test 1 + Test 4)
- [ ] package/product actifs uniques

Après changement important :
- [ ] ré-index si nécessaire
- [ ] relancer tests 1–5 (WS_00)
- [ ] si KO : rollback dernière couche

---

## 7) Evidence pack (traçabilité)

Après chaque setup/ingestion :
- Workspace : WS_00/WS_01/WS_02
- Corpus : liste dossiers/fichiers ingérés
- Date : 28-02-2026
- Résultat tests : PASS/FAIL
- Action si FAIL : rollback/correction

---

## 8) Changelog
- v1.0 (28-02-2026) : Protocole d’ingestion (RulesOnly → couches) + batterie de tests - GAPC

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
