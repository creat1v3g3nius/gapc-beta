---
id: FAQ_00_FORM
type: FAQ
title: FaqForm
version: v1.0
status: FROZEN
created: 02-03-2026
updated: 02-03-2026
tags: [system, faq, form, support]
depends_on: [INDEX_05_GLOSSARY, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_05_CACHE_POLICY]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_99_FAQ
---

# FAQ_00 — Form (sommaire + formulaire)

## Objet
Fichier unique pour :
1) **consulter les réponses courantes** (FAQ),
2) **déclarer une question/problème** via un formulaire standardisé, exploitable par un agent/mentor.

Règles P0 :
- no-secrets / no-PII
- si manque de source : `NON TROUVÉ` + action proposée
- toujours préciser les **actifs** (package/product) quand pertinent

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

### A2 — Comment éviter la dérive ?
- 1 intention = 1 livrable principal
- si > 3 items → créer un backlog (CO atomiques)

---

## B. Architecture

### B1 — Où mettre un document ?
- Procédure (comment faire) → **SYSTEM**
- Règle transverse → **CORE**
- Overlay métier → **PACKAGE**
- Preuves / DoD / logs / exemples → **PRODUCT**

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
- FROZEN : gelé, amendements contrôlés (patch + validation + version bump + changelog)

### D2 — Pourquoi mon gel est KO ?
Causes fréquentes :
- `status` pas à jour
- version non bumpée
- amendements/changelog manquants
- `depends_on` vers des IDs fantômes

---

## E. RAG / Mentor

### E1 — Que faire si le mentor n’a pas la réponse ?
Réponse attendue : `NON TROUVÉ` + proposition d’action (créer/compléter le document source).

### E2 — Comment éviter “mélange de packages” ?
Toujours préciser l’actif package/product. Refuser une réponse globale si contexte flou.

---

## F. Git / patches / commits

### F1 — Règle 1 intention = 1 commit
Un commit = une intention = un changement cohérent.
Pas de refactor massif non demandé.

### F2 — Diff-first
Toujours produire un patch ciblé (ou START/END REPLACE) avant commit.

---

## G. Cache

### G1 — À quoi sert CACHE ?
Zone temporaire. Jamais source de vérité. À promouvoir ou supprimer (rétention courte).

---

## H. Incidents

### H1 — Comment déclarer un incident ?
Utiliser le formulaire ci-dessous. Joindre uniquement des extraits non sensibles.

---

# I. Formulaire

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

## Changelog
- v1.0 (02-03-2026) : création FAQ+formulaire SYSTEM (minimal, P0).
