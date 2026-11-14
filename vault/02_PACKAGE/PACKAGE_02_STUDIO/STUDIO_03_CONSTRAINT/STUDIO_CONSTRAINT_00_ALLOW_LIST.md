---
id: STUDIO_CONSTRAINT_00_ALLOW_LIST
type: CONSTRAINT
title: StudioAllowList
version: v1.1
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, constraint, allowlist]
depends_on: 
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - STUDIO_TOOLING_EXTENSION_00_ALLOW_LIST
  - STUDIO_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS
  - STUDIO_CONSTRAINT_04_EXCEPTION_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_03_CONSTRAINT
---

# STUDIO_CONSTRAINT_00 - Allow List

## Objet

Fixer ce qui est autorise et interdit pour produire un projet studio. Ces
regles renforcent `CONSTRAINT_00_GUARD_RAILS` et n y creent aucune exception.

---

## 1) Autorise (par defaut)

- outils de repo et de session prevus par CORE / SYSTEM (diff-first),
- agent Claude en perimetre `STUDIO_R0` ou `STUDIO_R1` (MENTOR read-only,
  EXECUTION diff-first),
- generateurs et outils externes listes dans

  `STUDIO_TOOLING_EXTENSION_00_ALLOW_LIST`, utilises via leur protocole CORE,

- familles d outils de `STUDIO_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS`.

## 2) Interdit (P0)

- fichiers binaires de production (masters, exports, rushs) et fichiers

  fournis par le client dans le repo,

- nom, contact ou donnee personnelle d un client ou d un tiers dans le vault,
- visage ou voix d une personne reelle sans consentement ecrit trace,
- imitation explicite d un artiste vivant nomme, d une marque ou d un logo

  tiers sans autorisation,

- envoi de fichiers client confidentiels a un outil dont les conditions

  permettent leur reutilisation, sans accord du client,

- asset genere sans evidence pack,
- auto-commit, auto-push, lecture de plusieurs packages ou projets.

## 3) Regle P0

Toute derogation est **KO** sans `STUDIO_CONSTRAINT_04_EXCEPTION_POLICY`.

## Changelog

- v1.1 (14-11-2026) : roles realignes sur l agent Claude (`Agent MENTOR / Agent

  EXECUTION / Humain`), references AnythingLLM / Codex / API fallback retirees.

- v1.0 (14-11-2026) : creation de l allowlist studio.
