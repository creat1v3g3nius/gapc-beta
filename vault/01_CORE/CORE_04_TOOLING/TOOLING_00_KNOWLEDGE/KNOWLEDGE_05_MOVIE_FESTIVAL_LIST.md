---
id: KNOWLEDGE_05_MOVIE_FESTIVAL_LIST
type: TOOLING
title: MovieFestivalList
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, movie-festival, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_05 — Movie Festival List (CORE)

## Objet

Référentiel de festivals (typologie + repères) sous forme de liste
**RAG-friendly**.
Pas de procédure (dates précises à vérifier selon l’année), pas de données
personnelles.

---

## 1) Catégories (classification)

- **A-list / généralistes** : forte visibilité internationale.
- **Spécialisés** : genre (animation, documentaire, court-métrage…).
- **Régionaux / nationaux** : focus territoire.
- **Industry / marché** : pitching, marchés, rencontres pro.

## 2) Festivals (liste indicative, non exhaustive)

### Généralistes / majeurs

- Cannes — A-list, industrie.
- Berlin (Berlinale) — A-list.
- Venice (Mostra) — A-list.
- Toronto (TIFF) — grande vitrine.
- Sundance — indie / US.

### Documentaire

- IDFA — doc international.
- Hot Docs — doc (Canada).

### Animation

- Annecy — animation (référence).

### Courts-métrages

- Clermont-Ferrand — courts.

### Genre / fantastique

- Sitges — fantastique.
- Fantasia — genre.

## 3) Champs de fiche (si tu instancies en PACKAGE/PRODUCT)

- Nom
- Catégorie
- Format (court/long/doc/anim)
- Période (mois)
- Pays/ville
- Notes (1 ligne)
- Contraintes (format/éligibilité)

## 4) Red flags

- Confondre repères génériques et dates/conditions annuelles.
- Mettre des emails/contacts nominatif (PII).
- Importer des listes “scrapées” non vérifiées.

### Extensions PACKAGE/PRODUCT

- Ajouter un dataset daté (année N) avec sources vérifiées.
- Ajouter un “pipeline soumission” (mais en SYSTEM, pas ici).

---

## Changelog

- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
