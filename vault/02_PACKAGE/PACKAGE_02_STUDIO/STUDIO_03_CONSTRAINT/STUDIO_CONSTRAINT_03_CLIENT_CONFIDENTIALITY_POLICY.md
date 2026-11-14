---
id: STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
type: CONSTRAINT
title: StudioClientConfidentialityPolicy
version: v1.1
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, constraint, confidentiality, no-pii]
depends_on: 
  - CONSTRAINT_03_SECRETS_POLICY
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - KNOWLEDGE_08_SECURITY_BASELINE
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_03_CONSTRAINT
---

# STUDIO_CONSTRAINT_03 - Client Confidentiality Policy

## Objet

Proteger l identite et les fichiers des clients du studio dans le repo, le
vault et le corpus du mentor. Renforce `CONSTRAINT_03_SECRETS_POLICY`.

---

## 1) Pseudonymisation (P0)

- chaque client recoit un code `CLIENT_NN` (NN sequentiel),
- la table de correspondance code -> identite vit **hors repo**,
- aucun nom, contact, adresse ou signature client dans les documents,

  noms de fichiers ou messages de commit.

## 2) Fichiers (P0)

- briefs originaux, contrats, fichiers sources et livrables restent dans le

  stockage externe du studio,

- le vault reference ces fichiers par **chemin logique** (ex :

  `CLIENT_03/PRODUCT_04/exports/`), jamais par lien de partage contenant un
  jeton.

## 3) Mentor et outils externes

- corpus mentor : documents texte du projet uniquement, pseudonymises,
- l agent est heberge : rien de ce qu il lit ne doit identifier un client,
- generateurs : pas d envoi de fichier client confidentiel sans accord du

  client (`STUDIO_CONSTRAINT_00_ALLOW_LIST`).

## 4) Incident

Une donnee client detectee dans le repo est traitee comme un incident
(`WORKFLOW_05_INCIDENT`) : retrait, purge de l historique si necessaire,
trace sans reproduire la donnee.

## Changelog

- v1.1 (14-11-2026) : roles realignes sur l agent Claude (`Agent MENTOR / Agent

  EXECUTION / Humain`), references AnythingLLM / Codex / API fallback retirees.

- v1.0 (14-11-2026) : creation de la politique de confidentialite client.
