---
id: WORKFLOW_05_INCIDENT
type: WORKFLOW
title: IncidentResolutionProtocol
version: v1.1
status: FROZEN
created: 27-02-2026
updated: 02-03-2026
tags: [workflow, incident-protocol, run, system]
depends_on: [WORKFLOW_00_PIPELINE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# WORKFLOW_05 - Incident Resolution Protocol

Protocole **anti-panique** pour diagnostiquer et résoudre un incident pendant l’exécution du workflow GAPC :
**Obsidian (Vault) → VS Code + Git → (scripts validator/smoke) → AnythingLLM (mentor)**.

Contraintes :
- **No secrets** (aucun token/PII dans les logs, tickets, commits).
- **1 action = 1 intention** (si correctif : 1 commit atomique).
- **Source of Truth** : Vault / règles CORE (INDEX_00/INDEX_01 + WORKFLOW_00/01/02).

---

## 1) Définitions rapides
- **P0** : bloque production / risque perte de données / incohérence majeure.
- **P1** : dégrade qualité / ralentit fortement, contournable.
- **P2** : cosmétique / confort.

---

## 2) STOP conditions
Si **P0**, fais immédiatement :
- [ ] **STOP** : ne pas committer “au hasard”.
- [ ] **Snapshot** : copier/coller 10 lignes max de logs, `git status`, message d’erreur.
- [ ] **Isoler le scope** : quel arc est touché ? `SYSTEM | CORE | PACKAGE | PRODUCT`.
- [ ] **Geler l’écriture** : pas d’édition simultanée Obsidian + VS Code sur les mêmes fichiers tant que l’origine n’est pas identifiée.

Interdits :
- Push forcé (`--force`) sans procédure explicite.
- Réparer en modifiant plusieurs arcs à la fois.
- Ajouter des clés/tokens dans un fichier “temp”.

---

## 3) TRIAGE (2–5 min)

### 3.1) Catégorie (cocher 1 principale)
- [ ] A — **Repo/Git**
- [ ] B — **Vault/Obsidian**
- [ ] C — **Scripts/Validator/Smoke**
- [ ] D — **Mentor/RAG (AnythingLLM)**
- [ ] E — **Données/Backup/Infra**

### 3.2) Impact
- [ ] P0 (bloquant)
- [ ] P1 (dégradant)
- [ ] P2 (mineur)

### 3.3) Symptôme (1 phrase)
- Symptôme :
- Contexte (CO/session) :
- Dernier changement (commit / fichiers) :

### 3.4) Décision rapide
- Si P0 : **rollback** prioritaire (revenir à un état sain) avant “fix”.
- Si P1/P2 : fix possible en session, sinon backlog.

---

## 4) CHECKS UNIVERSELS (P0)

### 4.1) Git : état minimal
Exécuter :
- [ ] `git status`
- [ ] `git diff`
- [ ] `git log -5 --oneline`

### 4.2) Hygiène fichiers
- [ ] Aucun fichier export/cache/temp dans le diff
- [ ] Pas de secret/PII dans le diff

### 4.3) Package/Product actif
- [ ] 1 package actif (unique)
- [ ] 1 product actif (unique)

---

## 5) DIAGNOSTIC PAR DOMAINE

### A — Repo/Git

#### A1) Conflit / pull/push rejected
Actions safe :
- [ ] `git fetch`
- [ ] `git pull --rebase` (si policy rebase) ou `git merge`
- [ ] Résoudre conflits fichier par fichier
- [ ] Rejouer validator/smoke si nécessaire

#### A2) Mauvaise branche / HEAD détachée
- [ ] `git branch --show-current`
- [ ] `git switch <branch>`
- [ ] Si HEAD détachée : `git switch -c work/incident-<date>`

#### A3) Repo “cassé”
- [ ] Créer branche : `work/incident-<date>`
- [ ] Sauvegarder un diff local : `git diff > /tmp/diff.patch`
- [ ] Revenir à un état sain :
  - `git revert <sha>` (préféré)
  - ou `git restore .` (annuler changements locaux)

**Commit type** : `fix(incident): revert to last known good state`

---

### B — Vault/Obsidian

#### B1) Liens cassés / renommage
- [ ] Renommer via Obsidian (mise à jour liens) ou corriger liens.
- [ ] Éviter noms proches (SpecTech vs SpechTech).

#### B2) Frontmatter invalide → commit bloqué
- [ ] Corriger YAML (champs requis)
- [ ] Vérifier : `id` = nom du fichier sans extension
- [ ] Repasser validator

#### B3) Mauvais arc / mauvais dossier
- [ ] Déplacer dans le bon arc
- [ ] Mettre à jour `scope` et `arc` dans le frontmatter
- [ ] Mettre à jour l’index si besoin

---

### C — Scripts/Validator/Smoke

#### C1) Validator KO
- [ ] Identifier la règle violée
- [ ] Corriger le fichier fautif
- [ ] Relancer validator

#### C2) Validator “bug”
- [ ] Reproduire sur un fichier simple
- [ ] Patch minimal + test
- [ ] Commit atomique

#### C3) Smoke runner KO
- [ ] Lire la première erreur (root cause)
- [ ] Vérifier prérequis (paths, droits, env)
- [ ] Corriger puis relancer

---

### D — Mentor/RAG (AnythingLLM)

#### D1) Contention (immédiat)
- [ ] Basculer sur workspace **RulesOnly**
- [ ] Retirer la dernière couche ingérée

#### D2) Tests (obligatoires) — cf WORKFLOW_01
- [ ] Hiérarchie des règles = OK
- [ ] Non-invention = OK (**NON TROUVÉ**)
- [ ] Contradictions = OK (nuancé)

#### D3) Actions correctives
- [ ] Corriger doc source si ambiguë
- [ ] Ré-ingérer couche par couche + tests après chaque couche
- [ ] Revalider package/product actif unique

---

### E — Données/Backup/Infra

#### E1) Permissions / accès
- [ ] Vérifier propriétaire/permissions (sans exposer de données sensibles)
- [ ] Vérifier chemins Vault/repo

#### E2) Backup KO
- [ ] Vérifier job (cron/timer)
- [ ] Lire logs (10 lignes max)
- [ ] Exécution manuelle si script prévu
- [ ] Si D2 HS : remplacer D2 puis resync

---

## 6) Fix vs Rollback (règle)

### 6.1) Fix quand
- incident P1/P2,
- root cause claire,
- validator/smoke repassent.

## 6.2) Rollback quand
- incident P0,
- perte de confiance,
- risque d’aggraver.

---

## 7) Sortie d’incident (10 minutes)

### 7.1) Evidence pack (minimal)
À consigner :
- Symptôme
- Catégorie + impact
- Root cause probable
- Fix ou rollback
- Fichiers touchés
- Commit(s)

### 7.2) Action corrective unique
- Une action qui empêche la récidive (validator, doc, test RAG).

---

## 8) Template “note incident”

```txt
INCIDENT_ID:
Date:
Impact: P0|P1|P2
Catégorie: A|B|C|D|E
Symptôme:
Contexte (CO/session):
Dernier commit:
Root cause probable:
Action (fix/rollback):
Commit(s):
Next step unique:
```

---

## 9) Changelog
- v1.0 (28-02-2026) : version améliorée (triage + domaines + fix/rollback + evidence pack), compatible no-secrets, naming/frontmatter.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
