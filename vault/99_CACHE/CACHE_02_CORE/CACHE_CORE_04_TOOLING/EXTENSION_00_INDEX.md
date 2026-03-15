---
id: EXTENSION_00_INDEX
type: TOOLING
title: ExtensionIndex
version: v1.2
status: DEPRECATED
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, index, core]
depends_on: []
arc: CACHE
scope: vault/99_CACHE/CACHE_02_CORE/CACHE_CORE_04_TOOLING/
---

# EXTENSION_00 - Index (CORE)

## Objet

Index des extensions “protocole” (outils externes) utilisables par un product.
CORE strict : règles d’usage + garde-fous, sans procédures détaillées ni
secrets.

## P0

- [[EXTENSION_01_BOLT_NEW_PROTOCOL]]
- [[EXTENSION_02_MIDJOURNEY_PROTOCOL]]
- [[EXTENSION_03_KLING_AI_PROTOCOL]]

## P1

- [[EXTENSION_04_EVIDENCE_PACK]]
- [[EXTENSION_05_ASSET_NAMING_POLICY]]

## P2 (minimal)

- [[EXTENSION_06_COST_LIMITS]]
- [[EXTENSION_07_RIGHTS_AND_ATTRIBUTION]]

## Règles CORE

- No-secrets / no-PII.
- 1 intention = 1 output principal (sinon découper).
- Actifs uniques (si contexte package/product).
- Evidence pack obligatoire pour toute production “livrable”.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : FROZEN + depends_on minimisé et dédupliqué + déplacement

  dans CACHE.

- v1.1 (01-03-2026) : correction erreurs.
- v1.0 (01-03-2026) : version initiale.
