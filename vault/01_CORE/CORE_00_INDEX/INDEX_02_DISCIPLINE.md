---
id: INDEX_02_DISCIPLINE
type: INDEX
title: CoreDisciplineIndex
version: v1.3
status: FROZEN
created: 05-03-2026
updated: 15-03-2026
tags: [core, discipline, index]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_00_INDEX
---

# INDEX_02 - DISCIPLINE

## Objet

Index des **disciplines génériques du framework GAPC**.

Les disciplines définissent :

- standards de qualité
- règles d’exécution
- gouvernance documentaire
- mécanismes de validation.

---

## Documents

### RAG Profile

[[DISCIPLINE_00_RAG_PROFILE]]

Définit le profil RAG du framework,
la logique d’ingestion, l’isolation package/product.

---

### Gel Rules

[[DISCIPLINE_01_GEL_RULES]]

Règles de gel documentaire READY_TO_FREEZE, FROZEN et amendements contrôlés.

---

### RAG Quality Gate

[[DISCIPLINE_02_RAG_QG]]

Contrôle qualité pour sessions RAG.

---

### Doc Quality Gate

[[DISCIPLINE_03_DOC_QG]]

Standards qualité documentation.

---

### Code Quality Gate

[[DISCIPLINE_04_CODE_QG]]

Standards qualité code et scripts.

---

### Scope Classifier

[[DISCIPLINE_06_SCOPE_CLASSIFIER]]

Classification des modifications :

SYSTEM / CORE / PACKAGE / PRODUCT / CACHE.

---

### Risk Register

[[DISCIPLINE_07_RISK_REGISTER]]

Registre des risques du framework.

---

## Amendements (FROZEN)

Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (15-03-2026) : renomme le fichier et l id en prefixe canonique `INDEX_`.
- v1.2 (15-03-2026) : corrige le H1
  et réaligne la version courante avec l historique du changelog.
- v1.1 (05-03-2026) : passage en FROZEN.
- v1.0 (05-03-2026) : création index DISCIPLINE du CORE.
