---
id: STUDIO_TOOLING_EXTENSION_00_ALLOW_LIST
type: TOOLING
title: StudioExtensionAllowList
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, extension, allowlist]
depends_on: 
  - EXTENSION_01_BOLT_NEW_PROTOCOL
  - EXTENSION_02_MIDJOURNEY_PROTOCOL
  - EXTENSION_03_KLING_AI_PROTOCOL
  - EXTENSION_06_COST_LIMITS
  - STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_04_EXTENSION
---

# STUDIO_TOOLING_EXTENSION_00 - Allow List

## Objet

Lister les protocoles d outils externes autorises dans un projet studio.

## Protocoles autorises

| Protocole CORE | Usage studio |
| --- | --- |
| `EXTENSION_02_MIDJOURNEY_PROTOCOL` | generation et variation d images |
| `EXTENSION_03_KLING_AI_PROTOCOL` | generation video / motion |
| `EXTENSION_01_BOLT_NEW_PROTOCOL` | prototypes web |

## Conditions d usage (P0)

- conditions d usage de l outil verifiees pour un usage commercial,
- budget par CO (`EXTENSION_06_COST_LIMITS`),
- evidence pack studio a chaque generation retenue.

## Ajout d un outil

ADR-lite + protocole d extension (CORE ou add-on studio) + mise a jour de ce
document et de `STUDIO_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS`.

## Changelog

- v1.0 (14-11-2026) : creation de l allowlist des extensions studio.
