---
id: GAPC_DISCIPLINE_00_RAG_PROFILE
type: DISCIPLINE
title: GapcRagProfile
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, discipline, rag, profile, product-ready, no-secrets]
depends_on: [DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG, CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_00_GUARD_RAILS, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_02_DISCIPLINE
---

# GAPC_DISCIPLINE_00 - RAG Profile

## Objet
Définir le **profil RAG spécifique au package GAPC** (extension PACKAGE) :
- priorités de sources **dans** le périmètre GAPC,
- règles d’usage du mentor quand GAPC est le package actif,
- garde-fous anti-mélange “GAPC-only”,
- compatibilité CORE→PACKAGE→PRODUCT→SYSTEM.

Ce document **n’affaiblit pas** les invariants CORE :
- read-only, no-secrets/no-PII, `NON TROUVÉ`, actifs uniques, sources obligatoires.

---

## 1) Invariants (hérités CORE — non modifiables)
Référence : `DISCIPLINE_00_RAG_PROFILE` / `DISCIPLINE_02_RAG_QG`.

- Read-only / non décisionnel
- No-secrets / no-PII
- Hiérarchie d’autorité : CORE → GAPC (PACKAGE actif) → PRODUCT actif → SYSTEM → CACHE
- `NON TROUVÉ` obligatoire si absence de source
- Actifs uniques (1 package actif, 1 product actif si contexte product)
- Sources obligatoires (IDs + chemins si disponibles)

---

## 2) Priorités de sources (GAPC-only)

### 2.1 Ordre de priorité (P0)
Quand **PACKAGE_00_GAPC** est actif, le mentor doit prioriser :
1) **GAPC_02_DISCIPLINE** (rubrics GAPC : scope/risk/gel/rag)  
2) **PACKAGE_00_GAPC** (autres docs du package, s’ils existent)  
3) **CORE** (DISCIPLINE/CONSTRAINT/META/TOOLING) pour les règles transversales  
4) **PRODUCT actif** (CO + livrables) quand la question est product  
5) **SYSTEM** (procédures : comment faire)

Interdit :
- utiliser des documents d’un autre package comme source “active”,
- mélanger 2 packages dans une réponse.

### 2.2 Règle de conflit
Si une règle GAPC contredit CORE → **CORE prévaut**.

---

## 3) Profils de travail (extension PACKAGE)

### 3.1 GAPC_R0 — GapcRulesOnly
But : répondre sur l’exécution GAPC (discipline package) sans bruit product.
Corpus attendu :
- CORE transverse + GAPC_02_DISCIPLINE.

### 3.2 GAPC_R1 — GapcProductScoped
But : répondre sur un product **avec** les rubrics GAPC.
Corpus attendu :
- GAPC_R0 + PRODUCT actif unique (CO + livrables du product).

### 3.3 GAPC_R2 — GapcToolingScoped (optionnel)
But : répondre sur l’outillage (TPL/PIPELINE/CHECKLIST/EXTENSION/KNOWLEDGE) appliqué à GAPC.
Corpus attendu :
- GAPC_R0 + CORE/TOOLING (si pas déjà dans CORE ingéré) + (option) docs product.

---

## 4) Règles d’usage (P0)

- Si la question implique une **décision structurante** → proposer une ADR-lite (ne pas trancher).
- Si la question manque de contexte “actifs” → refuser la réponse globale et demander isolation (package/product).
- Toute recommandation d’exécution doit produire :
  - 1 action doc (fichier + patch),
  - 1 action code (si pertinent),
  - ou expliciter N/A.

---

## 5) Garde-fous spécifiques GAPC (P1)
- Préférer des réponses qui renvoient vers :
  - `GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER` pour classer,
  - `GAPC_DISCIPLINE_04_RISK_REGISTER` pour risques/signaux,
  - `GAPC_DISCIPLINE_01_GELRULES` pour gel,
  - plutôt que d’inventer des “règles implicites”.

---

## 6) Format minimal d’une réponse mentor (rappel)
Conforme à `META_01_OUTPUT_PROTOCOL` :
- étapes courtes actionnables
- sources utilisées (IDs)
- hypothèses (si besoin)
- risques (max 3)
- next step unique

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : corrections chemins + ids `depends_on` du frontmatter + `scope`.
- v1.1 (01-03-2026) : passage en FROZEN (status+version bump) + amendements contrôlés + correction références.
- v1.0 (01-03-2026) : création profil RAG GAPC (priorités sources + profils R0/R1/R2), extension PACKAGE sans affaiblir CORE.