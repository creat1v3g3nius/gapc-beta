---
id: CONSTRAINT_03_SECRETS_POLICY
type: CONSTRAINT
title: Secretspolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [limites, secrets-policy, llm, discipline, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_03 - No-Secrets Policy (contraintes transversales)

## Objet
Centraliser la contrainte CORE **no-secrets / no-PII** pour éviter toute fuite via :
- documents,
- code/config,
- logs,
- exemples,
- historiques Git.

CORE strict : aucune procédure opérateur (pas de commandes, pas de checklists).

---

## 1) Interdits (P0, bloquants)

### 1.1 Secrets
Interdit de versionner ou publier :
- tokens API, clés privées, secrets OAuth,
- mots de passe, cookies de session, JWT,
- clés SSH privées, certificats privés.

### 1.2 Données personnelles (PII)
Interdit de versionner ou publier :
- noms/adresses/email/téléphone de personnes réelles,
- identifiants personnels,
- données sensibles de santé/finance, etc.

### 1.3 Données d’accès internes
Interdit :
- URLs privées avec credentials,
- dumps de configuration contenant secrets.

---

## 2) Règle CORE
Un artefact est **KO** si :
- il contient un secret/PII,
- ou il suggère une pratique qui conduit à stocker des secrets en clair.

Cette contrainte prime sur toute priorité produit (toujours P0).

---

## 3) Exceptions
Aucune exception “en clair”.
Les seules formes acceptables (conceptuellement) :
- secret injecté par environnement (hors repo/Vault),
- exemple **factice** explicitement marqué (ex : `TOKEN_EXAMPLE_DO_NOT_USE`).

---

## 4) Contrat d’extension (PACKAGE/PRODUCT)
PACKAGE/PRODUCT peuvent renforcer (ex : exigences légales, masking), mais ne peuvent pas :
- autoriser un secret en clair,
- autoriser de la PII réelle.

---

### Changelog
- v1.0 (01-03-2026) : création de la contrainte CORE no-secrets/no-PII.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.2 (04-03-2026) : corrections frontmatter + heading.
