---
id: KNOWLEDGE_04_DATA_SOURCE_LIST
type: TOOLING
title: DataSourceList
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, data-source, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_04 — Data Source List (Ingestion RAG) (CORE)

## Objet

Référentiel de **types de sources** pour ingestion RAG + règles de sélection
(sans procédure).

---

## 1) Sources internes (prioritaires)

- **Docs Vault (.md)** — règles, index, runbooks (SOT).
- **Templates (TPL)** — PRD/Spec/ADR/TestPlan.
- **Backlogs/CO** — décisions & exécution product (scopées).
- **Code repo (scripts)** — uniquement si utile au mentor (sinon bruit).

## 2) Sources externes (à encadrer)

- **PDFs** — rapports, docs partenaires (attention droits).
- **Sites web** — pages stables (risque de drift).
- **Emails / chats** — souvent bruités (PII possible) → éviter.
- **Spreadsheets** — tabulaire (bien si structuré, attention PII).

## 3) Critères de sélection (P0)

- **Autorité** : CORE > PACKAGE > PRODUCT > SYSTEM.
- **Stabilité** : éviter les brouillons non gelés.
- **Scope** : 1 package actif, 1 product actif.
- **Sensibilité** : pas de secrets/PII.
- **Bruit** : limiter la taille, préférer index.

## 4) Red flags (STOP)

- ingestion “all vault” par défaut
- ingestion de logs bruts
- ingestion de contenus contenant secrets/PII
- sources externes non contrôlées devenant “vérité”

### Extensions PACKAGE/PRODUCT

- Ajouter la liste des sources “autorisées” (domaines, dossiers).
- Ajouter règles de tri spécifiques (ex : compliance).

---

## Changelog

- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
