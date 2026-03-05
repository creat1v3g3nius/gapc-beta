---
id: GAPC_INDEX_02_DISCIPLINE
type: INDEX
title: GAPCPackageDisciplineIndex
version: v1.2
status: FROZEN
created: 05-03-2026
updated: 05-03-2026
tags: [gapc, package, discipline, index]
depends_on: []
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_00_INDEX
---

# GAPC_INDEX_02 — DISCIPLINE

## Objet

Index des **disciplines** appliquées dans le PACKAGE_00_GAPC.

Note :
- ces documents sont des **spécialisations** ou **sélections** adaptées au métier
- éviter la duplication : référencer le CORE lorsque possible

---

## Documents

### RAG Profile
[[GAPC_DISCIPLINE_00_RAG_PROFILE]] : profil d’usage RAG spécifique au PACKAGE (périmètre, règles d’exécution, garde-fous).

### Gel Rules
[[GAPC_DISCIPLINE_01_GEL_RULES]] : règles de gel (READY_TO_FREEZE → FROZEN), versioning et amendements pour le PACKAGE.

### RAG Quality Gate
[[GAPC_DISCIPLINE_02_RAG_QG]] : grille de qualité RAG (contrôles P0/P1/P2) appliquée aux livrables du PACKAGE.

### Scope Classifier
[[GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER]] : classification du scope (P0/P1/P2 + NOW/NEXT/LATER) et règles anti-scope creep.

### Risk Register
[[GAPC_DISCIPLINE_04_RISK_REGISTER]] : registre de risques (identification, mitigations, contrôles) pour les usages du PACKAGE.

---

## Amendements (FROZEN)
Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (05-03-2026) : passage en FROZEN.
- v1.1 (05-03-2026) : ajout descriptions + chemins complets des fichiers.
- v1.0 (05-03-2026) : création index DISCIPLINE du PACKAGE_00_GAPC.
