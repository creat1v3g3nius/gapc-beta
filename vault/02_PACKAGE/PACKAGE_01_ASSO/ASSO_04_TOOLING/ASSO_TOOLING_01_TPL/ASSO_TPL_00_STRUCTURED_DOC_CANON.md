---
id: ASSO_TPL_00_STRUCTURED_DOC_CANON
type: TOOLING
title: AssoStructuredDocCanon
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, tooling, tpl, p0]
depends_on:
  - TPL_05_ACTION_DOC
  - DISCIPLINE_03_DOC_QG
  - ASSO_DISCIPLINE_01_GEL_RULES
  - ASSO_DISCIPLINE_03_LEXICAL_QG
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_04_TOOLING/ASSO_TOOLING_01_TPL
---

# ASSO_TPL_00 - Structured Doc Canon

## Structure (copiable)

```md
# <Titre>

## Objet
## Contexte (faits / hypothèses)
## Gouvernance & responsabilités
## Conformité (legal baseline / no-secrets)
## Contenu principal
## Risques (top 3)
## Décisions (ADR si structurant)
## Next step unique
```

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation metadata.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : template canon ASSO.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
