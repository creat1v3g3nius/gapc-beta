---
id: DISCIPLINE_05_DOC_COMPLIANCE
type: DISCIPLINE
title: DocComplianceRules
version: v1.3
status: FROZEN
created: 28-02-2026
updated: 04-03-2026
tags: [governance, doc-compliance, llm, discipline, core]
depends_on: [META_03_NAMING_CONVENTIONS, META_04_WRITING_RULES, META_05_FRONTMATTER, DISCIPLINE_03_DOC_QG]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_05 - Compliance Doc (règles transversales)
Invariants transversaux de conformité documentaire : métadonnées, structure minimale, non‑duplication, “sans oral”, no‑secrets.  
CORE strict : aucune procédure opérateur.

---

## 1) Invariants CORE (P0)
- frontmatter conforme + `id==filename`
- H1 unique + sections cohérentes
- objectif explicite + hypothèses marquées si besoin
- pas de duplication de source de vérité (référencer)
- no-secrets/no-PII
- placement cohérent (CORE→PACKAGE→PRODUCT→SYSTEM)
- décision structurante traçable (ADR-lite)

---

## 2) Extensions PACKAGE/PRODUCT
Peuvent renforcer, ne peuvent pas affaiblir.

---

### Changelog
- v1.1 (01-03-2026) : normalisation frontmatter + statut READY_TO_FREEZE.
- v1.0 (01-03-2026) : version initiale.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.3 (04-03-2026) : corrections frontmatter + heading.
