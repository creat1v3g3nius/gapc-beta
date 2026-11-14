---
id: STUDIO_TOOLING_TPL_03_CLIENT_REVIEW_LOG
type: TOOLING
title: StudioClientReviewLog
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, tpl, review, client]
depends_on: 
  - STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
  - TPL_09_REVIEW_CHECK
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_01_TPL
---

# STUDIO_TOOLING_TPL_03 - Client Review Log

## Objet

Tracer chaque round de retours client : ce qui est demande, ce qui est
decide, quels CO en decoulent. Seule source des decisions client du projet.

## Entree par round (copiable)

```txt
Round: R<n> / inclus: N
Date:
Version presentee (assets + spec DA):
Canal: reunion | email | outil de revue
Retours (resumes, sans donnee personnelle):
  - <retour> -> accepte | refuse | hors brief (NEXT) | a clarifier
Decisions client:
CO crees:
Statut du round: ouvert | clos
```

## Regles P0

- un retour hors brief est classe via `STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER`,
- un round au-dela du nombre inclus exige une decision tracee,
- le BAT est consigne comme dernier round (`Decision: BAT`).

## Changelog

- v1.0 (14-11-2026) : creation du journal de revue client.
