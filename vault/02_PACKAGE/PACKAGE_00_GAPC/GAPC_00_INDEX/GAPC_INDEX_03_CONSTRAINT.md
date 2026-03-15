---
id: GAPC_INDEX_03_CONSTRAINT
type: INDEX
title: GAPCPackageConstraintIndex
version: v1.2
status: FROZEN
created: 05-03-2026
updated: 05-03-2026
tags: [gapc, package, constraint, index]
depends_on: []
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_00_INDEX
---

# GAPC_INDEX_03 — CONSTRAINT

## Objet

Index des **contraintes** spécifiques au PACKAGE_00_GAPC.

Ces contraintes ajoutent (ou précisent) :

- allowlist métier
- politiques de sources
- politiques d’exception

Sans dupliquer les contraintes globales du CORE.

---

## Documents

### Allow List

[[GAPC_CONSTRAINT_00_ALLOW_LIST]] :  allowlist métier (ce qui est autorisé :
sources, outils, formats, périmètres).

### Sources Policy

[[GAPC_CONSTRAINT_01_SOURCES_POLICY]] : politique de sources (priorités,
interdits, conditions d’usage) spécifique au PACKAGE.

### Exception Policy

[[GAPC_CONSTRAINT_02_EXCEPTION_POLICY]] : politique d’exception (quand/comment
déroger, traçabilité, validations requises).

---

## Amendements (FROZEN)

Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (05-03-2026) : passage en FROZEN.
- v1.1 (05-03-2026) : ajout descriptions + chemins complets des fichiers.
- v1.0 (05-03-2026) : création index CONSTRAINT du PACKAGE_00_GAPC.
