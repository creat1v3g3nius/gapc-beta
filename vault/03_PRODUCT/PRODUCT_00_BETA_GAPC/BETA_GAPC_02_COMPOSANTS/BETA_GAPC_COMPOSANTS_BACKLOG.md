---
id: BETA_GAPC_COMPOSANTS_00_BACKLOG
type: BACKLOG_CO
title: Backlog CO — Bootstrap Git + Qualité
version: v1.1
status: READY_TO_FREEZE
created: 05-03-2026
updated: 06-03-2026
tags: [beta, backlog, git, vscode, validator, smoke, hooks, dod, gapc]
depends_on: [GIT_00_CONFIG, GIT_01_ESSENTIEL, GIT_02_BRANCH_POLICY, GIT_03_PATCH_COMMIT]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC
---

# BETA_GAPC_COMPOSANTS_00_BACKLOG

Contexte :
- Vault `vault/` : **FROZEN**, Gate PASS = OK (structure/doc prête).
- Environnement Git : **créé**, remote connecté, hooks/gates P0 opérationnels.
- Objectif : rendre l’exécution **product-ready** pour Beta v1.0 : repo Git + bootstrap VS Code + **Validator + Hook + Smoke Runner** (P0), puis dépannage + DoD merge (P1), puis options hors pipeline (P2).

Références SYSTEM (procédures opérateur) :
- `GIT_00_CONFIG` (bootstrap VS Code + workflow + tasks)
- `GIT_01_ESSENTIEL` (commandes + dépannage)
- `GIT_02_BRANCH_POLICY` (main/work + squash + tags + DoD merge)
- `GIT_03_PATCH_COMMIT` (checklist patch→commit + gates validator/smoke)

Règles d’exécution :
- 1 CO = 1 intention = 1 résultat vérifiable.
- P0 d’abord. Pas de scope creep.

État d’exécution (06-03-2026) :
- P0.1 → P0.8 : **DONE**
- P1.1 → P1.3 : **TODO**
- P2.1 → P2.3 : **TODO**

---

## P0 — Pipeline (obligatoire) : Repo Git + Bootstrap + Gates (Validator/Hook/Smoke)

### CO_P0_001 — Créer le repo Git local (init) et figer la racine repo/vault
**But** : obtenir un repo opérationnel (`.git/`) et éviter l’erreur “mauvaise racine VS Code”.
**Entrées** : arborescence `repo/` existante (ou à créer).
**Sorties** :
- `.git/` présent à la racine `repo/`
- `REPO_ROOT.md` présent à la racine
- `vault/` présent dans `repo/` (Vault inside repo)

**Étapes**
- `git init` ; `git branch -M main`
- Ajouter `REPO_ROOT.md`
- Vérifier `git status` depuis `repo/`

**AC (Acceptance Criteria)**
- [x] `git status` fonctionne dans VS Code Terminal ouvert sur `repo/`
- [x] `git branch --show-current` retourne `main`
- [x] `REPO_ROOT.md` visible et versionnable

**Estimation** : 0.5–1.0 h

---

### CO_P0_002 — Config Git identité + `.gitignore` no-secrets (baseline)
**But** : éviter les secrets et stabiliser les commits multi-machines.
**Sorties** :
- config `user.name/user.email` validée (global ou local)
- `.gitignore` incluant `.env`, `*.key`, `*.pem`, etc.

**AC**
- [x] `git config --list` affiche `user.name` et `user.email`
- [x] `.env` n’apparaît pas dans `git status` même s’il existe localement
- [x] Procédure “remove cached secret” documentée (si besoin)

**Estimation** : 0.5–1.0 h

---

### CO_P0_003 — Connecter le remote (GitHub/GitLab) + premier push `main`
**But** : assurer le cycle push/pull (remote prêt).
**Sorties** :
- remote `origin` configuré
- `main` poussé sur le remote

**AC**
- [x] `git remote -v` OK
- [x] `git push -u origin main` OK
- [x] historique contient 1 commit bootstrap propre (ex: `chore(repo): bootstrap framework`)

**Estimation** : 0.5–1.5 h (inclut aléas auth)

---

### CO_P0_004 — Bootstrap VS Code workspace (settings + conventions)
**But** : rendre l’édition stable et répétable.
**Sorties** :
- `repo/.vscode/settings.json` minimal (EOL, trim, yaml validate…)
- doc “ouvrir repo/ dans VS Code ; vault/ dans Obsidian” rappelée

**AC**
- [x] VS Code ouvre `repo/` et détecte Git
- [x] YAML validate actif (frontmatter)
- [x] pas de format-on-save destructeur par défaut

**Estimation** : 0.5–1.0 h

---

### CO_P0_005 — Installer/valider **Validator** (frontmatter/naming) + commande unique
**But** : gate qualité “Vault” exécutable (pas seulement papier).
**Sorties** :
- script `scripts/ValidateFrontmatter.py` présent **ou** alternative explicitée
- commande unique de validation (ex: `python scripts/ValidateFrontmatter.py`)

**AC**
- [x] lancer le validator retourne succès sur l’état actuel (Vault FROZEN)
- [x] en cas d’erreur volontaire introduite, le validator la détecte
- [x] output lisible (fichier + ligne / message utile)

**Estimation** : 1.0–2.5 h (selon existence du script)

---

### CO_P0_006 — Installer/valider **Smoke Runner** + commande unique
**But** : gate qualité “outillage/scripts/.vscode” exécutable.
**Sorties** :
- script `scripts/SmokeRunner.py` présent **ou** alternative explicitée
- commande unique (ex: `python scripts/SmokeRunner.py`)

**AC**
- [x] smoke passe sur l’état actuel
- [x] smoke détecte au moins 1 failure contrôlée (test volontaire) **ou** justification “non applicable en Beta v1.0” écrite

**Estimation** : 1.0–2.5 h (selon existence du script)

---

### CO_P0_007 — Mettre en place les **Hooks Git** (P0) : gate validator/smoke avant push
**But** : rendre “bloquant” réel (enforcement), au minimum avant diffusion remote.
**Décision** : hook recommandé = **pre-push** (bloque moins le flow que pre-commit).
**Sorties** :
- `.githooks/` (ou `.git/hooks/` documenté) avec script `pre-push`
- `git config core.hooksPath .githooks`
- règles :
  - si `vault/**` modifié → validator
  - si `scripts/**` ou `.vscode/**` modifié → smoke
  - si scripts absents → message clair + policy (bloquant ou non) documentée

**AC**
- [x] un push est refusé si validator (ou smoke) échoue, selon règles ci-dessus
- [x] le hook n’exécute pas de secrets, ne log pas de secrets
- [x] le hook est reproductible sur une nouvelle machine (documenté)

**Estimation** : 1.0–2.0 h

---

### CO_P0_008 — “Happy path” complet : work/* → commit atomique → validate/smoke → push
**But** : prouver le pipeline end-to-end sur 1 patch test.
**Sorties** :
- une branche `work/bootstrap-test`
- un commit `docs(system): ...` (ou `chore(repo): ...`) atomique
- push OK

**AC**
- [x] `git diff` relu, `git add -p` utilisé au moins une fois
- [x] validator/smoke exécutés (via hook ou manuel) et PASS
- [x] push de `work/bootstrap-test` OK

**Estimation** : 0.5–1.0 h

---

## P1 — Stabilisation (recommandé) : Dépannage + DoD merge vers main

### CO_P1_001 — Dépannage “top 6” prêt (checklist opérateur) + scénarios
**But** : réduire les blocages débutants (repo non détecté, push rejected, detached HEAD, merge/rebase, undo, secret).
**Sorties** : une checklist P1 consolidée (référence `GIT_01` + `GIT_02`).

**AC**
- [ ] chaque scénario a : symptôme → cause probable → fix safe (commandes)
- [ ] inclut “STOP conditions” (ne pas improviser)

**Estimation** : 0.5–1.0 h

---

### CO_P1_002 — DoD merge vers `main` + procédure squash merge reproductible
**But** : définir “quand main est présentable/gelable” + intégrer proprement.
**Sorties** :
- DoD merge (validator OK, smoke OK si applicable, no-secrets, 1 intention)
- procédure squash merge (local ou via PR)

**AC**
- [ ] 1 merge test (squash) effectué depuis `work/*` vers `main`
- [ ] `main` reste clean et push OK
- [ ] DoD copiable et appliqué

**Estimation** : 0.5–1.5 h

---

### CO_P1_003 — VS Code Tasks (Validate/Smoke) alignées sur hooks
**But** : un “1 clic” identique aux commandes hooks (zéro divergence).
**Sorties** : `repo/.vscode/tasks.json` avec 2 tâches.

**AC**
- [ ] `GAPC: Validate Vault` == commande hook (même script/args)
- [ ] `GAPC: Smoke` == commande hook
- [ ] exécution depuis VS Code OK

**Estimation** : 0.5–1.0 h

---

## P2 — Nice to have (optionnel = hors pipeline Beta v1.0)

### CO_P2_001 — Extensions VS Code (optionnel)
**But** : confort (pas requis).
**Options** : GitLens, EditorConfig, etc.

**AC**
- [ ] liste “recommandées” vs “optionnelles” claire
- [ ] règle : si bruit/instable → remove

**Estimation** : 0.25–0.5 h

---

### CO_P2_002 — Tags jalons freeze (optionnel)
**But** : états reproductibles (release markers).
**AC**
- [ ] tag `v1.0` (ou `v1.0-beta`) annoté créé sur `main`
- [ ] push tag OK

**Estimation** : 0.25–0.5 h

---

### CO_P2_003 — PR GitHub (optionnel, hors pipeline)
**But** : revue/trace même solo (scalable).
**AC**
- [ ] règle PR (même solo) documentée
- [ ] template PR optionnel (si souhaité)

**Estimation** : 0.5–1.0 h

---

## Résumé effort (ordre de grandeur)

- **P0 (obligatoire)** : ~6 à 13 h (selon existence/adaptation validator + smoke + aléas auth)
- **P1 (recommandé)** : +1.5 à 3.5 h
- **P2 (optionnel / hors pipeline)** : +1 à 2 h

---

## Amendements
- Ce backlog est READY_TO_FREEZE : toute modification via patch ciblé + version bump.

## Changelog
- v1.1 (06-03-2026) : backlog d’exécution généré, P0.1→P0.8 marqués DONE, contexte et date mis à jour.
- v1.0 (05-03-2026) : création backlog CO bootstrap Git/VS Code + gates validator/smoke/hooks pour Beta v1.0.
