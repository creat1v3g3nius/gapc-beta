---
id: ASSO_KNOWLEDGE_01_GLOSSARY
type: TOOLING
title: AssoGlossary
version: v1.4
status: FROZEN
created: 01-03-2026
updated: 06-03-2026
tags: [package, asso, tooling, knowledge, glossary, p0]
depends_on: [ASSO_META_01_DOMAIN_DEFINITIONS, CONSTRAINT_06_TERMINOLOGY_POLICY]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_04_TOOLING/ASSO_TOOLING_00_KNOWLEDGE
---

# ASSO_KNOWLEDGE_01 - Glossary
## Termes
- Objet social
- Gouvernance
- Convention
- Partenaire
- Livrable canon (FROZEN)

## Règles
- 1 concept = 1 terme
- si doute : ajouter au glossaire (référence > copie)

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.4 (06-03-2026) : alignement `id==filename` et heading.
- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + normalisation metadata.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : glossaire ASSO initial.
