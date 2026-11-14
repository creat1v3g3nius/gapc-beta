---
id: STUDIO_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS
type: TOOLING
title: StudioAllowedTools
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, knowledge, tools]
depends_on: 
  - KNOWLEDGE_02_AI_GENERATOR_LIST
  - EXTENSION_01_BOLT_NEW_PROTOCOL
  - EXTENSION_02_MIDJOURNEY_PROTOCOL
  - EXTENSION_03_KLING_AI_PROTOCOL
  - STUDIO_TOOLING_EXTENSION_00_ALLOW_LIST
  - STUDIO_CONSTRAINT_00_ALLOW_LIST
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_00_KNOWLEDGE
---

# STUDIO_TOOLING_KNOWLEDGE_00 - Allowed Tools

## Objet

Associer chaque famille d outils du studio a son statut et au protocole qui
l encadre. Les familles viennent de `KNOWLEDGE_02_AI_GENERATOR_LIST`.

---

## 1) Familles et statut

| Famille | Usage studio | Statut | Protocole |
| --- | --- | --- | --- |
| Texte -> image | KV, declinaisons, explorations | Autorise | `EXTENSION_02_MIDJOURNEY_PROTOCOL` |
| Image -> image, inpainting, upscale | retouche, variantes | Autorise | `EXTENSION_02_MIDJOURNEY_PROTOCOL` |
| Texte / image -> video | motion court, animation de KV | Autorise | `EXTENSION_03_KLING_AI_PROTOCOL` |
| Prototype web | maquette interactive, landing | Autorise | `EXTENSION_01_BOLT_NEW_PROTOCOL` |
| Design, mise en page, retouche manuelle | masters, exports | Autorise | hors protocole IA, nommage studio |
| Audio (voix, musique) | habillage sonore | NEXT | protocole a creer |
| 3D generative | volumes, textures | NEXT | protocole a creer |

## 2) Regles

- un outil d une famille `NEXT` n est utilise qu apres creation de son

  protocole (ADR-lite + extension),

- un nouvel outil dans une famille autorisee est ajoute a

  `STUDIO_TOOLING_EXTENSION_00_ALLOW_LIST` avant usage,

- les conditions d usage de chaque outil sont verifiees selon

  `STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY`.

## Changelog

- v1.0 (14-11-2026) : creation du referentiel d outils studio.
