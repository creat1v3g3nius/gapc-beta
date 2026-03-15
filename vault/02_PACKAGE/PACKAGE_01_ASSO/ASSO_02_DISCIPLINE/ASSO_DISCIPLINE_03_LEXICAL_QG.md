---
id: ASSO_DISCIPLINE_03_LEXICAL_QG
type: DISCIPLINE
title: AssoLexicalQG
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, discipline, qg, lexical, p0]
depends_on:
  - ASSO_KNOWLEDGE_01_GLOSSARY
  - ASSO_CONSTRAINT_02_PUBLIC_MESSAGING_POLICY
  - DISCIPLINE_03_DOC_QG
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_02_DISCIPLINE
---

# ASSO_DISCIPLINE_03 - Lexical Quality Gates

PASS si :

- glossaire respecté
- pas de surpromesse
- assertions bornées ou sourcées

FAIL sinon.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + correction depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : gate lexicale ASSO.
