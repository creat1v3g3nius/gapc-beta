---
id: ASSO_DISCIPLINE_00_RAG_PROFILE
type: DISCIPLINE
title: AssoRagProfile
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, discipline, rag, profile, p1, no-secrets]
depends_on:
  - DISCIPLINE_00_RAG_PROFILE
  - DISCIPLINE_02_RAG_QG
  - ASSO_CONSTRAINT_05_SOURCES_POLICY
  - ASSO_CONSTRAINT_02_PUBLIC_MESSAGING_POLICY
  - ASSO_DISCIPLINE_03_LEXICAL_QG
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - META_01_OUTPUT_PROTOCOL
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_02_DISCIPLINE
---

# ASSO_DISCIPLINE_00 - Rag Profile

## Objet

Profil RAG **métier association** (overlay PACKAGE) : priorités de sources,
posture “sobre”, anti-invention.

## Invariants (hérités CORE)

- no-secrets/no-PII
- sources obligatoires (IDs) ou `NON TROUVÉ`
- actifs uniques (package/product)

## Priorité de sources (ASSO actif)

1) PACKAGE_01_ASSO (discipline/constraints/knowledge)
2) CORE (règles transversales)
3) PRODUCT actif (si contexte projet)
4) SYSTEM (procédures)
5) CACHE (jamais vérité)

## Posture / style

- institutionnel sobre
- pas d’absolus non vérifiables
- limites/incertitudes explicites si nécessaire

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + correction depends_on.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation
  frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création profil RAG ASSO (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
