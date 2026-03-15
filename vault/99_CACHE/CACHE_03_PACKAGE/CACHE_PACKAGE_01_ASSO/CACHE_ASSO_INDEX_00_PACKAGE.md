---
id: CACHE_ASSO_INDEX_00_PACKAGE
type: INDEX
title: AssoPackageIndex
version: v1.3
status: DEPRECATED
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, index, p0, product-ready]
depends_on: []
arc: CACHE
scope: vault/99_CACHE/CACHE_03_PACKAGE/CACHE_PACKAGE_01_GAPC/
---

# CACHE_ASSO_INDEX_00 - PACKAGE

## Objet

Point d’entrée du package **ASSO** (CORE transposé métier “association 1901 /
gouvernance / communication / conformité”).
Pas de procédures opérateur (SYSTEM) ni de preuves/DoD (PRODUCT).

## Navigation

- INDEX : [[CACHE_ASSO_INDEX_01_META]] · [[CACHE_ASSO_INDEX_02_DISCIPLINE]] ·
  [[CACHE_ASSO_INDEX_03_CONSTRAINT]] · [[CACHE_ASSO_INDEX_04_TOOLING]]
- META : [[ASSO_META_00_PACKAGE_PROFILE]] · [[ASSO_META_01_DOMAIN_DEFINITIONS]]
- DISCIPLINE :  [[ASSO_DISCIPLINE_00_RAG_PROFILE]] ·
  [[ASSO_DISCIPLINE_01_GEL_RULES]] ·  [[ASSO_DISCIPLINE_02_RAG_QG]] ·
  [[ASSO_DISCIPLINE_03_LEXICAL_QG]] ·  [[ASSO_DISCIPLINE_04_SCOPE_CLASSIFIER]] ·
  [[ASSO_DISCIPLINE_05_RISK_REGISTER]]
- CONSTRAINT : [[ASSO_CONSTRAINT_00_ALLOW_LIST]] ·
  [[ASSO_CONSTRAINT_01_LEGAL_BASELINE_1901]] ·
  [[ASSO_CONSTRAINT_02_PUBLIC_MESSAGING_POLICY]] ·
  [[ASSO_CONSTRAINT_03_CONFLICT_OF_INTEREST_POLICY]] ·
  [[ASSO_CONSTRAINT_04_DATA_PRIVACY_POLICY]] ·
  [[ASSO_CONSTRAINT_05_SOURCES_POLICY]] ·
  [[ASSO_CONSTRAINT_99_EXCPETION_POLICY]]
- TOOLING :
  - KNOWLEDGE : [[ASSO_KNOWLEDGE_00_INDEX]] · [[ASSO_KNOWLEDGE_01_GLOSSARY]]
  - TPL : [[ASSO_TPL_00_STRUCTURED_DOC_CANON]]
  - PIPELINE
  - CHECKLIST : [[ASSO_CHECKLIST_00_INDEX]] ·
    [[ASSO_CHECKLIST_01_READY_TO_FREEZE_ADDON]]
  - EXTENSION

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : correction `scope` + `depend_on` du frontmatter +
  déplacement dans CACHE.
- v1.2 (01-03-2026) : passage en FROZEN (index P2) + harmonisation
  version/status.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : création index P0 package ASSO.
