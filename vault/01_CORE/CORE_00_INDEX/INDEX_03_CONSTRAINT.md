---
id: INDEX_03_CONSTRAINT
type: INDEX
title: CoreConstraintIndex
version: v1.3
status: FROZEN
created: 05-03-2026
updated: 15-03-2026
tags: [core, constraint, index]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_00_INDEX
---

# INDEX_03 - CONSTRAINT

## Objet

Index des **contraintes structurelles du framework GAPC**.

Les contraintes définissent les **règles non négociables** :

- sécurité
- architecture
- gouvernance
- traçabilité.

---

## Documents

### Guard Rails

[[CONSTRAINT_00_GUARD_RAILS]]

Contraintes globales : no secrets, no PII et règles d'usage LLM.

---

### RAG Scope Policy

[[CONSTRAINT_01_RAG_SCOPE_POLICY]]

Règles d’ingestion et périmètre RAG.

---

### Non Duplication Policy

[[CONSTRAINT_02_NON_DUPLICATION_POLICY]]

Principe : référence > copie

---

### Decision Traceability Policy

[[CONSTRAINT_04_DECISION_TRACEABILITY_POLICY]]

Traçabilité : ADR, changelog dépendances.

---

### Cache Policy

[[CONSTRAINT_05_CACHE_POLICY]]

Règles de gestion du cache : temporaire, jamais source de vérité.

---

## Amendements (FROZEN)

Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (15-03-2026) : renomme le fichier et l id en prefixe canonique `INDEX_`.
- v1.2 (15-03-2026) : aligne le H1 sur l identifiant canonique de l index CORE.
- v1.1 (05-03-2026) : passage en FROZEN.
- v1.0 (05-03-2026) : création index CONSTRAINT du CORE.
