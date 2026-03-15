---
id: FAQ_00_FORM
type: FAQ
title: FaqForm
version: v1.1
status: FROZEN
created: 02-03-2026
updated: 13-03-2026
tags: [system, faq, form, support]
depends_on:
  - INDEX_05_GLOSSARY
  - WORKFLOW_00_PIPELINE
  - WORKFLOW_06_VAULT_HEALTH_CHECK
  - SCRIPT_03_INSTRUCTIONS_CODEX
  - LLM_00_RAG_PRINCIPES
  - EVIDENCE_00_FRAMEWORK_INDEX
  - EVIDENCE_00_INDEX
  - CONSTRAINT_03_SECRETS_POLICY
  - CONSTRAINT_05_CACHE_POLICY
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_99_FAQ
---

# FAQ_00 — Form (sommaire + formulaire)

## Objet

Fichier unique pour :

1) **consulter les réponses courantes** (FAQ),
2) **déclarer une question/problème** via un formulaire standardisé,
   exploitable par un agent/mentor.

Règles P0 :

- no-secrets / no-PII
- si manque de source : `NON TROUVÉ` + action proposée
- toujours préciser les **actifs** (package/product) quand pertinent

Références courantes :

- runbooks quotidiens : `WORKFLOW_00_PIPELINE`
- health check documentaire : `WORKFLOW_06_VAULT_HEALTH_CHECK`
- cadrage Codex IDE : `SCRIPT_03_INSTRUCTIONS_CODEX`
- mentor documentaire : `LLM_00_RAG_PRINCIPES`
- preuves framework : `EVIDENCE_00_FRAMEWORK_INDEX`
- preuves agents : `EVIDENCE_00_INDEX`

---

## 1) Sommaire

- [A. Démarrage session](#a-démarrage-session)
- [B. Architecture](#b-architecture)
- [C. Frontmatter & naming](#c-frontmatter--naming)
- [D. Gel READY_TO_FREEZE / FROZEN](#d-gel-ready_to_freeze--frozen)
- [E. RAG / Mentor](#e-rag--mentor)
- [F. Git / patches / commits](#f-git--patches--commits)
- [G. Cache](#g-cache)
- [H. Incidents](#h-incidents)
- [I. Formulaire](#i-formulaire)

---

## A. Démarrage session

### A1 — Comment fixer les actifs ?

Définir explicitement :

- `Active package` = `PACKAGE_XX`
- `Active product` = `PRODUCT_XX` ou `NA`

Si tu ne sais pas : mettre `Active product = NA`.
Source utile : `WORKFLOW_00_PIPELINE`.

### A2 — Comment éviter la dérive ?

- 1 intention = 1 livrable principal
- si > 3 items → créer un backlog (CO atomiques)
- rerun minimal de contrôle : `WORKFLOW_06_VAULT_HEALTH_CHECK`

---

## B. Architecture

### B1 — Où mettre un document ?

- Procédure (comment faire) → **SYSTEM**
- Règle transverse → **CORE**
- Overlay métier → **PACKAGE**
- Preuves / DoD / logs / exemples → **PRODUCT**

Repères actuels :

- exécution quotidienne → `RUN_00_WORKFLOW`
- setup produit → `RUN_01_SETUP_PRODUCT`
- preuves framework SYSTEM → `EVIDENCE_00_FRAMEWORK`
- preuves agents → `EVIDENCE_01_AGENTS`

---

## C. Frontmatter & naming

### C1 — Champ `id`

Règle : `id == filename` (sans extension).

### C2 — Champs dates

`created` et `updated` sont obligatoires (format `DD-MM-YYYY`).

### C3 — `depends_on`

Liste dédupliquée d’IDs ; référence > copie.

---

## D. Gel READY_TO_FREEZE / FROZEN

### D1 — Différence entre READY_TO_FREEZE et FROZEN

- READY_TO_FREEZE : conforme + validable
- FROZEN : gelé, amendements contrôlés
  (patch + validation + version bump + changelog)

### D2 — Pourquoi mon gel est KO ?

Causes fréquentes :

- `status` pas à jour
- version non bumpée
- amendements/changelog manquants
- `depends_on` vers des IDs fantômes

Contrôles utiles :

- `WORKFLOW_06_VAULT_HEALTH_CHECK`
- `SCRIPT_00_VALIDATOR`
- `SCRIPT_04_DOC_INTEGRITY_CHECKER`

---

## E. RAG / Mentor

### E1 — Que faire si le mentor n’a pas la réponse ?

Réponse attendue : `NON TROUVÉ` + proposition d’action
(créer/compléter le document source).
Source utile : `LLM_00_RAG_PRINCIPES`.

### E2 — Comment éviter “mélange de packages” ?

Toujours préciser l’actif package/product.
Refuser une réponse globale si contexte flou.

Sources utiles :

- `LLM_01_INGESTION_PROTOCOL`
- `LLM_03_MENTOR_UTILITES`

---

## F. Git / patches / commits

### F1 — Règle 1 intention = 1 commit

Un commit = une intention = un changement cohérent.
Pas de refactor massif non demandé.

### F2 — Diff-first

Toujours produire un patch ciblé (ou START/END REPLACE) avant commit.
Source utile : `SCRIPT_03_INSTRUCTIONS_CODEX`.

---

## G. Cache

### G1 — À quoi sert CACHE ?

Zone temporaire. Jamais source de vérité.
À promouvoir ou supprimer (rétention courte).
Source utile : `CONSTRAINT_05_CACHE_POLICY`.

---

## H. Incidents

### H1 — Comment déclarer un incident ?

Utiliser le formulaire ci-dessous.
Joindre uniquement des extraits non sensibles.
Si incident documentaire : penser à relancer `WORKFLOW_06_VAULT_HEALTH_CHECK`.

---

## I. Formulaire

> Copier/coller ce bloc, remplir, puis envoyer.

```txt
[FAQ/FORM] Titre:
Type: Question | Incident | Bug | Amélioration | Demande doc
Priorité: P0 | P1 | P2

Contexte:
- Active package: PACKAGE_XX
- Active product: PRODUCT_XX | NA
- Arc concerné: SYSTEM | CORE | PACKAGE | PRODUCT
- Dossier / scope (path):
- Statut visé: DRAFT | READY_TO_FREEZE | FROZEN

Problème / Question:
- Description (1-5 phrases):

Attendu:
- Résultat attendu (1-3 bullets):

Observé:
- Résultat observé (1-3 bullets):

Preuves (sans secrets / sans PII):
- Fichiers/IDs concernés:
- Extraits (max 30 lignes):
- Logs (optionnel, max 30 lignes):

Hypothèses:
- (optionnel, max 5)

Contraintes:
- no-secrets: OUI
- diff-first: OUI
- no auto-commit: OUI
- 1 intention = 1 commit: OUI

Next step souhaité:
- (une action)
```

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (13-03-2026) : aligne la FAQ sur la structure active
  `WORKFLOW / SETUP_PRODUCT / EVIDENCE / LLM`
  et ajoute les references courantes.
- v1.0 (02-03-2026) : création FAQ+formulaire SYSTEM (minimal, P0).
