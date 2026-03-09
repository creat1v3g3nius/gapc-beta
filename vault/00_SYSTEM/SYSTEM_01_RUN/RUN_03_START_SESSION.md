---
id: RUN_03_START_SESSION
type: RUN
title: WorkflowStartSession
version: v1.2
status: FROZEN
created: 27-02-2026
updated: 09-03-2026
tags: [workflow, start-session, run, system]
depends_on: [RUN_00_PIPELINE, RUN_01_COMPOSANTS, INDEX_01_ARCHITECTURE, INDEX_04_OBSIDIAN]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# RUN_03 - Workflow Start Session

Ce document permet d'exécuter en **30–45 minutes** une session de production **répétable** et **sans dérive** sur **n’importe quel package** et **n’importe quel product** :

**start → 1 composant (CO) → patch → validator/smoke → commit → test mentor (RAG) → clôture**.

Règle non négociable : **1 intention = 1 session de production = 1 commit**.

Références :
- Architecture (arcs CORE → PACKAGE → PRODUCT) : `INDEX_01_ARCHITECTURE`
- Usage Obsidian (Vault = Source of Truth) : `INDEX_04_OBSIDIAN`  

---

## 1) Variables de session (à remplir)
- **Package actif** : `<PACKAGE_ID>` (ex: `PACKAGE_02_GAPC`)
- **Product actif** : `<PRODUCT_ID>` (ex: `PRODUCT_02_GAPCMVP`)
- **Composant (CO) ciblé** : `<CO_ID>` (ex: `CO_003`)
- **Type de changement** : `docs | chore | feat | fix | refactor | test`
- **Scope** : `<scope>` (ex: `vault`, `scripts`, `llm`, `product`)

---

## 2) Pré-requis
- VS Code ouvert sur la racine du repo (`.git/` présent)
- Obsidian ouvert sur `repo/vault/`
- Validator frontmatter/naming disponible (bloquant avant commit)
- (Optionnel) Mentor AnythingLLM prêt (workspace RulesOnly ou package-scoped)

---

## 3) Fixer le scope (anti-dérive)

### 3.1) Choisir le triplet : CORE / PACKAGE / PRODUCT
- **CORE** : uniquement si tu changes une règle transverse (rare).
- **PACKAGE** : si tu adaptes/extends une discipline métier.
- **PRODUCT** : si tu produis un composant (CO) d’un produit.

Stop condition :
- Si tu touches à **2 arcs** dans la même session → **STOP** et scinde en 2 sessions.

### 3.2) Règle “package actif unique”
- Un seul package actif doit être considéré pendant la session.
- Le mentor (si utilisé) ne doit ingérer que : **CORE + package actif + product actif**.

---

## 4) Start session

Crée une note de session et colle ce **Context Pack** :

```txt
Goal:
Constraints: diff-first, no auto-commit, no secrets, 1 intention = 1 commit
Package active:
Product active:
Component (CO):
Current state:
Files (exact paths):
Expected output:
Timebox (max 45min):
```

Checklist :
- [ ] **1 CO unique**
- [ ] chemins exacts listés
- [ ] output attendu clair (doc OU code)

---

## 5) Définir 1 composant (CO) atomique

Dans le dossier du product actif, crée/complète le CO ciblé avec :

- **Titre** : verbe + objet (court)
- **Definition of Done** : 3 bullets max
- **Risques** : 1–2
- **Fichiers impactés** : liste

Stop condition :
- Si tu identifies **> 5 fichiers** à toucher → CO trop large → scinder.

---

## 6) Patch (diff-first)

## 3.1) Avec un assistant (Codex/Copilot) — prompt standard
> Propose un **diff Git minimal** pour réaliser le CO.  
> Ne modifie que les fichiers nécessaires.  
> Donne : commandes validator/smoke + message de commit `type(scope): action`.  
> Si une décision structurante apparaît : propose une ADR-lite.

## 3.2) Règles de patch (anti-bruit)
- [ ] Aucun fichier parasite (temp, caches, exports)
- [ ] Pas de secret/token/PII en clair
- [ ] Respect naming + frontmatter
- [ ] Si doc : 1 H1, sections courtes, checklists scannables

---

## 7) Validator (bloquant)

Lancer le validator (frontmatter + naming si disponible).

Attendu :
- **KO → pas de commit**
- Corriger → relancer → OK

Checklist KO fréquents :
- `id` ≠ nom de fichier
- `type` invalide
- champs manquants (`version`, `status`, `scope`, `arc`, `dependances`)
- format date incohérent

---

## 8) Smoke (si applicable)

Lancer le smoke runner si :
- tu as touché scripts/outillage/config
- tu as touché une règle qui impacte l’exécution

Attendu :
- smoke détecte : dossiers manquants, fichiers invariants absents, validator indisponible

---

## 9) Commit + push 

Dans l’ordre :
- [ ] stage **sélectif**
- [ ] commit : `type(scope): action`
- [ ] push/sync
- [ ] `git status` clean

Exemples :
- `docs(product): add CO_003 checklist`
- `chore(scripts): tighten frontmatter validator`
- `docs(llm): add package-scoped ingestion rules`

Stop condition :
- Si tu hésites sur le message → c’est souvent que la session contient **2 intentions**.

---

## 10) Mise à jour Obsidian (logistique)

- [ ] Mettre à jour le statut du CO (Draft/Ready/In progress/Done)
- [ ] Ajouter 1 lien vers le commit (hash ou message)
- [ ] Ajouter 1 risque max si nouveau
- [ ] Mettre à jour l’index du product si nécessaire (pas obligatoire à chaque session)

---

## 11) Test Mentor (AnythingLLM)

### 11.1) Mode recommandé
- **RulesOnly** pour vérifier les règles (CORE/SYSTEM)
- **Package-scoped** pour vérifier l’extension métier (package actif)
- **Product-scoped** pour vérifier le composant du jour

### 11.2) Prompt test (copier/coller)
> Donne-moi la checklist applicable pour exécuter ce CO, et cite les fichiers utilisés.  
> Si une info manque, répond **NON TROUVÉ**.

OK si :
- réponse actionnable
- fichiers cités
- “NON TROUVÉ” si absence (pas d’invention)

KO si :
- réponse vague/générique
- mélange plusieurs packages/products
- invente des règles

Actions KO :
- réduire le corpus
- corriger doublons
- renforcer `RUN_01` (ingestion + tests)

---

## 12) Output attendu (fin de session)

Tu dois pouvoir montrer :
- 1 CO (atomique)
- 1 diff appliqué
- validator OK
- smoke OK (si applicable)
- 1 commit pushé
- 1 test mentor OK (ou KO + action corrective définie)

---

## 13) Red flags (STOP)
- 2 intentions dans le même commit
- patch énorme sans tests
- “je ne sais pas où est la vérité” (doublons / contradictions)
- le mentor mélange des packages
- un secret apparaît dans un diff/log

---

## 14) Changelog
- v1.0 (27-02-2026) : version générique (multi-package/multi-product), anti-dérive, compatible Obsidian/VS Code/AnythingLLM.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
