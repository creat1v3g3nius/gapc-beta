---
id: GAPC_CONSTRAINT_01_SOURCES_POLICY
type: CONSTRAINT
title: GapcSourcesPolicy
version: v1.5
status: FROZEN
created: 01-03-2026
updated: 11-03-2026
tags: [package, gapc, constraint, sources, p1]
depends_on:
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - DISCIPLINE_00_RAG_PROFILE
  - GAPC_DISCIPLINE_00_RAG_PROFILE
  - GAPC_TOOLING_KNOWLEDGE_01_SOURCES_PRIORITY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_03_CONSTRAINT
---

# GAPC_CONSTRAINT_01 - Sources Policy

## Objet

Imposer, au niveau PACKAGE GAPC, la **politique de sources** (RAG / production)
:

- priorité des sources,
- anti-mélange,
- anti-duplication.

---

## 1) Priorité (P0)

1) CORE transverse
2) GAPC discipline (scope/risk/gel/rag)
3) Package GAPC (autres docs)
4) Product actif (si applicable)
5) SYSTEM (procédures)
6) CACHE (jamais vérité)

Règle de sortie :

- si la demande porte sur l ordre de priorité package-scoped, le mentor s arrête

  a `SYSTEM`

- `CACHE` reste une règle de fond, mais ne fait pas partie du format de sortie

  attendu pour `T2`

## 2) Règles P0

- Si absence de source : `NON TROUVÉ`
- Si mélange packages/products : refus + isolation
- Référence > copie (non-duplication)
- Si conflit entre CORE et PACKAGE : **CORE prévaut**

### 2.1 Discipline de citation

- citer en priorité l ID ou le nom de fichier exact
- annoter un arc uniquement si cet arc est exact
- ne pas annoter une source avec plusieurs arcs

Interdit :

- annoter un fichier `PACKAGE` comme `CORE`, `SYSTEM` ou `PRODUCT`
- annoter une source avec un arc approximatif
- ajouter une annotation d arc si elle n apporte rien a la reponse

### 2.2 Réponses simples

Si la demande porte uniquement sur :

- une hiérarchie d autorité,
- un ordre de priorité de sources,
- un refus d isolation de package,

alors le mentor doit produire une sortie courte, sans blocs additionnels non
demandés.

Interdit :

- ajouter `Audit`, `Comparaison`, `Run plan` ou `Next step unique` si non

  demandés

- transformer une réponse simple en multi-blocs

---

## Changelog

- v1.5 (11-03-2026) : précise que `CACHE` reste une règle de fond et ne doit pas

  apparaitre dans la sortie attendue de `T2`.

- v1.4 (11-03-2026) : ajoute la discipline de citation et la règle anti-bruit

  pour les réponses simples.

- v1.3 (10-03-2026) : réaligne la priorité des sources sur `CORE -> PACKAGE ->

  PRODUCT -> SYSTEM -> CACHE`.

- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : création policy sources GAPC (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
