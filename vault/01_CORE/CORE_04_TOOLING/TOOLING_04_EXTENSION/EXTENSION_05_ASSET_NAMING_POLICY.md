---
id: EXTENSION_05_ASSET_NAMING_POLICY
type: TOOLING
title: AssetNamingPolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, assets, naming, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_04_EXTENSION
---

# EXTENSION_05 - Asset Naming Policy (CORE)

## Objet

Définir une convention minimale de nommage des assets générés (image/vidéo) pour
rester diffable et traçable.

---

## Règle de base

Format recommandé (sans espaces) :

`PRODUCT_CO_ASSETTYPE_SHORTDESC_vX.ext`

Exemples :

- `P01_CO003_IMG_banner_v1.png`
- `P01_CO003_VID_intro_v2.mp4`

## Invariants

- pas de PII dans les noms
- versions incrémentales
- l’asset doit être relié à un CO

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : FROZEN + depends_on minimisé et dédupliqué + corection

  heading.

- v1.1 (01-03-2026) : correction erreurs.
- v1.0 (01-03-2026) : version initiale.
