---
id: GAPC_VAULT_HEALTH_CHECK
type: TOOLING
title: GapcVaultHealthCheck
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [vault, audit, health-check, gapc, checklist, tooling]
depends_on: [META_03_NAMING_CONVENTIONS, META_04_WRITING_RULES, META_05_FRONTMATTER, DISCIPLINE_03_DOC_QG, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_04_DECISION_TRACEABILITY_POLICY, PIPELINE_00_PRODUCT, PIPELINE_03_BACKLOG_COMPOSANT]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# GAPC_VAULT_HEALTH_CHECK

## Objectif

Fournir un **health check rapide du vault GAPC** pour détecter en quelques minutes les écarts P0/P1 les plus critiques :

- structure d’arcs incohérente
- frontmatter non conforme
- duplication de règles
- traçabilité incomplète
- repo Git instable
- outillage cassé

Le document sert de **contrôle rapide post-changement** ou **pré-gel**.

---

## Portée

Ce contrôle couvre le vault documentaire et son outillage minimal :

- `vault/00_SYSTEM`
- `vault/01_CORE`
- `vault/02_PACKAGE`
- `vault/03_PRODUCT`
- `scripts/`
- `.githooks/`
- `.vscode/`

Il ne remplace pas un audit complet.  
Il fournit un **signal rapide PASS / FIX_REQUIRED**.

---

## Préconditions

- racine Git ouverte dans VS Code
- validator disponible
- smoke runner disponible
- hook Git configuré
- package actif et product actif explicités si audit ciblé

---

## Commandes de contrôle rapide

### 1 — État Git
```bash
git status --short --branch
```

### 2 — Remote + hook
```bash
git remote -v
git push --dry-run
```

### 3 — Validator
```bash
./scripts/ValidateFrontmatter.py
```

### 4 — Smoke runner
```bash
./scripts/SmokeRunner.py
```

### 5 — Hook path
```bash
git config --get core.hooksPath
ls -la .githooks
```

### 6 — Traçabilité des artefacts
```bash
git ls-files | grep -i "backlog\|dod\|release\|adr\|gate"
```

### 7 — Tags / gel
```bash
git tag --list
```

### 8 — Historique récent
```bash
git log --oneline -10
```

---

## Lecture des résultats

## P0 — Santé minimale

### H0.1 — Repo stable
PASS si :
- `git status --short --branch` ne liste aucun fichier
- la branche est alignée avec `origin`

KO si :
- fichiers modifiés/non trackés
- branche en avance/en retard sans justification

### H0.2 — Remote et push opérationnels
PASS si :
- `git remote -v` retourne `origin`
- `git push --dry-run` passe sans erreur

KO si :
- remote absent
- auth KO
- hook absent ou cassé

### H0.3 — Frontmatter conforme
PASS si :
- `./scripts/ValidateFrontmatter.py` retourne PASS

KO si :
- ID orphelin
- `id != filename`
- champs obligatoires manquants
- `depends_on` fantôme

### H0.4 — Outillage vivant
PASS si :
- `./scripts/SmokeRunner.py` retourne PASS
- `.githooks/pre-push` existe et est exécutable
- `core.hooksPath = .githooks`

KO si :
- smoke KO
- hook non actif
- hook présent mais non exécuté

---

## P1 — Santé structurelle

### H1.1 — Hiérarchie d’autorité lisible
PASS si :
- CORE porte les règles transversales
- PACKAGE porte les overlays métier
- PRODUCT porte preuves / DoD / validations
- SYSTEM porte procédures opérateur

KO si :
- une règle CORE est redéfinie silencieusement dans PACKAGE/PRODUCT/SYSTEM
- une procédure opérateur sert de source de vérité

### H1.2 — Non-duplication
PASS si :
- une règle = une source
- les autres documents référencent la source

KO si :
- même règle répétée dans plusieurs arcs
- contradictions entre formulations

### H1.3 — Chaîne de preuve complète
Chaîne attendue :

```text
Backlog CO
→ Gate PASS
→ DoD
→ ADR
→ Release Note
```

PASS si la chaîne est retrouvable dans le repo.  
KO si une étape structurante manque.

---

## P2 — Santé de maturité

### H2.1 — Jalons de gel présents
PASS si :
- tags de jalons présents
- release notes ou preuves de gel disponibles

### H2.2 — Historique lisible
PASS si :
- commits atomiques
- messages `type(scope): action`
- squash / merge cohérents

### H2.3 — Confort opérateur
PASS si :
- `.vscode/settings.json` présent
- `.vscode/tasks.json` aligné avec validator / smoke
- extensions recommandées documentées si nécessaires

---

## Grille de verdict

### Verdict P0
```text
VAULT_HEALTH_P0 = PASS | FIX_REQUIRED
```

### Verdict P1
```text
VAULT_HEALTH_P1 = PASS | FIX_REQUIRED
```

### Verdict P2
```text
VAULT_HEALTH_P2 = PASS | FIX_REQUIRED
```

### Verdict global
```text
GAPC_VAULT_HEALTH = PASS | FIX_REQUIRED
```

Règle :
- si un seul H0 est KO → verdict global = `FIX_REQUIRED`
- si tous les H0 sont PASS mais un H1 est KO → verdict global = `FIX_REQUIRED`
- P2 n’est jamais bloquant pour le happy path, mais doit être tracé

---

## Format de sortie recommandé

```md
## GAPC_VAULT_HEALTH

- H0.1 Repo stable : PASS
- H0.2 Remote et push : PASS
- H0.3 Frontmatter : PASS
- H0.4 Outillage : PASS

- H1.1 Hiérarchie d’autorité : PASS
- H1.2 Non-duplication : PASS
- H1.3 Chaîne de preuve : PASS

- H2.1 Jalons de gel : PASS
- H2.2 Historique lisible : PASS
- H2.3 Confort opérateur : PASS

Verdict global : PASS
Next step : READY_TO_FREEZE
```

---

## Critères PASS

Le health check est validé si :

- aucun P0 ouvert
- aucun P1 de contradiction documentaire
- validator PASS
- smoke PASS
- repo stable
- chaîne de preuve lisible

---

## Retour arrière

Si un fix documentaire ou outillage casse le vault :

```bash
git revert <commit_health_fix>
```

---

## Résultat attendu

Après exécution du health check :

- le statut du vault est explicite
- les défauts critiques sont visibles immédiatement
- le passage à READY_TO_FREEZE ou FROZEN est plus sûr
