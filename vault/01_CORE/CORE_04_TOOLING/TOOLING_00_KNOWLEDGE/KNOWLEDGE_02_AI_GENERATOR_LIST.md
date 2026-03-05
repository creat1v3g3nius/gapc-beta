---
id: KNOWLEDGE_02_AI_GENERATOR_LIST
type: TOOLING
title: AiGeneratorList
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, ai-generator, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_02 — AI Generator List (CORE)

## Objet
Référentiel de familles de générateurs IA (pour choisir vite selon besoin), sans recommander de secrets ni de workflows non traçables.

---

## 1) Image
- **Texte → image** — visuels, moodboards, concepts.
- **Image → image** — variations, style transfer, retouche guidée.
- **Inpainting/Outpainting** — correction locale / extension de cadre.
- **Upscale** — montée en résolution.

## 2) Vidéo
- **Texte → vidéo** — clips courts, prototypes.
- **Image → vidéo** — animation de keyframes.
- **Vidéo → vidéo** — stylisation / restauration (à encadrer).

## 3) Audio
- **Texte → voix** — narration (attention droits/consentement).
- **Musique générative** — boucles, pistes (droits/usage).
- **Nettoyage** — denoise, enhancement.

## 4) 3D
- **Texte/Image → 3D** — meshes bruts (retopo souvent nécessaire).
- **Texture générative** — matériaux PBR.

## 5) Docs / Contenu structuré
- **Synthèse** — résumés, extraction.
- **Structuration** — TPL, checklists, tables.
- **Traduction** — attention à la terminologie “réservée”.

## 6) Red flags (STOP)
- Génération à partir de données sensibles (PII, secrets).
- Usage de voix/visages sans consentement explicite.
- Export non traçable (pas de source, pas de version).
- Promesses “commercial safe” non vérifiées.

### Extensions PACKAGE/PRODUCT
- Ajouter la liste des outils réellement autorisés (licences, budget).
- Ajouter les contraintes de droits (asso, diffusion, partenaires).

---

## Changelog
- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
