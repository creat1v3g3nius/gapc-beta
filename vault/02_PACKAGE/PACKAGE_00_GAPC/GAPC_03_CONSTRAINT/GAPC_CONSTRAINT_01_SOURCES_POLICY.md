---
id: GAPC_CONSTRAINT_01_SOURCES_POLICY
type: CONSTRAINT
title: GapcSourcesPolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, constraint, sources, p1]
depends_on: [CONSTRAINT_01_RAG_SCOPE_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, DISCIPLINE_00_RAG_PROFILE, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_TOOLING_KNOWLEDGE_02_SOURCES_PRIORITY]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_03_CONSTRAINT
---

# GAPC_CONSTRAINT_01 - Sources Policy

## Objet
Imposer, au niveau PACKAGE GAPC, la **politique de sources** (RAG / production) :
- priorité des sources,
- anti-mélange,
- anti-duplication.

---

## 1) Priorité (P0)
1) GAPC discipline (scope/risk/gel/rag)
2) Package GAPC (autres docs)
3) CORE transverse
4) Product actif (si applicable)
5) SYSTEM (procédures)
6) CACHE (jamais vérité)

## 2) Règles P0
- Si absence de source : `NON TROUVÉ`
- Si mélange packages/products : refus + isolation
- Référence > copie (non-duplication)

---

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création policy sources GAPC (P1).

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
