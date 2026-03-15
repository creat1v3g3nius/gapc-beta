---
id: GAPC_META_00_PACKAGE_PROFILE
type: META
title: GapcPackageProfile
version: v1.5
status: FROZEN
created: 01-03-2026
updated: 10-03-2026
tags: [package, gapc, meta, profile, product-ready]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, GAPC_TOOLING_PIPELINE_00_PACKAGE, GAPC_DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_01_META
---

# GAPC_META_00 - PACKAGE_PROFILE (P1)

## Objet
Définir le **profil du package** `PACKAGE_00_GAPC` (vérité de base), sans dupliquer la gouvernance CORE :
- rôle du package,
- périmètre (IN/OUT),
- règles d’extension (CORE → PACKAGE → PRODUCT → SYSTEM),
- invariants P0 product-ready.

---

## 1) Rôle du package GAPC
GAPC fournit :
- une architecture de production (Vault + repo + mentor read-only),
- une discipline (scope/risk/gel/rag) appliquée à la production,
- un outillage (TPL/PIPELINE/CHECKLIST/EXTENSION/KNOWLEDGE) **défini en CORE** et **spécialisé par add-ons** en PACKAGE.

Le package ne contient pas :
- preuves de validation (workspace) → PRODUCT,
- procédures opérateur détaillées → SYSTEM.

---

## 2) Périmètre (IN/OUT)

### IN (P0)
- extensions GAPC des rubrics (Scope/Risk/Gel/RAG)
- add-ons TPL GAPC (evidence/log/release/backlog) si nécessaires
- allowlists (outils/extensions) si besoin de verrouiller

### OUT (P0)
- duplication des règles CORE (frontmatter, no-secrets, non-dup, gates)
- pipelines de validation product (DoD/preuves/workspace) → PRODUCT actif

---

## 3) Invariants P0 (hérités CORE)
- no-secrets / no-PII
- actifs uniques (package/product)
- `NON TROUVÉ` (anti-invention)
- API externe en fallback ciblé, explicite, minimisé, sans secret
- 1 intention = 1 CO = 1 commit

---

## 4) Interfaces du package
- **CORE** : règles transversales (SOT)
- **PRODUCT** : workspace, preuves, DoD
- **SYSTEM** : procédures (comment faire)

Règle explicite :
- `PACKAGE_00_GAPC` étend `CORE` mais ne remplace ni la hiérarchie d autorité, ni la séparation des rôles `AnythingLLM local / Codex / API externe fallback`.
- toute comparaison `CORE vs PACKAGE_00_GAPC` doit donc conclure sur l extension ou l écart, jamais sur une substitution de rôle.

---

## 5) Liens de navigation (IDs)
- Discipline GAPC : `GAPC_DISCIPLINE_01_GEL_RULES`, `GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER`, `GAPC_DISCIPLINE_04_RISK_REGISTER`, 
- Pipelines GAPC : `GAPC_TOOLING_PIPELINE_00_PACKAGE`
- DoD workspace : `PRODUCT actif` (référence workspace, si applicable)

---

## Amendements (FROZEN)

Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.5 (10-03-2026) : explicite que GAPC étend CORE sans remplacer ni la hiérarchie d autorité ni la séparation des rôles.
- v1.4 (10-03-2026) : supprime les references produit legacy et aligne les invariants setup sur `mentor read-only` + `API fallback`.
- v1.3 (05-03-2026) : ajout amendements.
- v1.2 (04-03-2026) : corrections chemins + `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création package profile GAPC (P1, sans duplication CORE).
