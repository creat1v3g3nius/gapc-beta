---
id: STUDIO_DISCIPLINE_00_RAG_PROFILE
type: DISCIPLINE
title: StudioRagProfile
version: v1.1
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, discipline, rag, profile]
depends_on: 
  - DISCIPLINE_00_RAG_PROFILE
  - DISCIPLINE_02_RAG_QG
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - STUDIO_META_00_PACKAGE_PROFILE
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_02_DISCIPLINE
---

# STUDIO_DISCIPLINE_00 - RAG Profile

## Objet

Definir l usage du mentor documentaire quand `PACKAGE_02_STUDIO` est le
package actif. Extension de `DISCIPLINE_00_RAG_PROFILE` : elle n affaiblit
aucun invariant CORE (read-only, no-secrets/no-PII, `NON TROUVE`, actifs
uniques, sources obligatoires).

---

## 1) Priorite des sources (P0)

Quand `PACKAGE_02_STUDIO` est actif, le mentor priorise :

1) `CORE`
2) `STUDIO discipline` (`STUDIO_02_DISCIPLINE`)
3) `autres docs package STUDIO`
4) `PRODUCT actif` (projet client : brief, spec DA, journal de revue)
5) `SYSTEM`
6) `CACHE` (jamais verite)

Regle de conflit : si une regle STUDIO contredit CORE, **CORE prevaut**.

---

## 2) Profils de corpus

- **STUDIO_R0 - StudioRulesOnly** : CORE + `STUDIO_02_DISCIPLINE` +

  `STUDIO_03_CONSTRAINT`. Pour les questions de methode et de regles.

- **STUDIO_R1 - StudioProjectScoped** : STUDIO_R0 + 1 projet actif (documents

  texte du product). Pour cadrer un CO, une revue ou une livraison.

Interdit dans tout corpus :

- fichiers binaires et fichiers bruts fournis par le client,
- documents d un autre projet client,
- documents d un autre package comme source active.

---

## 3) Regles d usage (P0)

- **Pas de fait client invente** : delais, budgets, rounds, cession et

  validations viennent du brief du projet actif, sinon `NON TROUVE`.

- **Pas de DA inventee** : une recommandation visuelle cite la spec DA du

  projet (`STUDIO_TOOLING_TPL_01_ART_DIRECTION_SPEC`) ; a defaut, le mentor
  propose de completer la spec plutot que d improviser.

- **Prompts** : le mentor peut structurer un prompt a partir de la spec DA et

  de `TPL_08_AI_IMAGE_PROMPT_MODEL` ; il ne lance aucune generation.

- **Decision client** (hors brief, cession, nombre de rounds) : signaler

  `Decision requise` et proposer une ADR-lite, ne pas trancher.

- **Autre projet ou autre package** : refus simple + demande d isolation.

---

## 4) Roles (inchanges)

- `Agent MENTOR` : lecture, checklist, synthese, audit documentaire.
- `Agent EXECUTION` : fichiers, scripts, execution (diff-first).
- `Humain (decision)` : arbitrage client, validation, nouvelle regle.

## Changelog

- v1.1 (14-11-2026) : roles realignes sur l agent Claude (`Agent MENTOR / Agent

  EXECUTION / Humain`), references AnythingLLM / Codex / API fallback retirees.

- v1.0 (14-11-2026) : creation du profil RAG studio.
