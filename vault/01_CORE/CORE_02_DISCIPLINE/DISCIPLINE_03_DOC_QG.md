---
id: DISCIPLINE_03_DOC_QG
type: DISCIPLINE
title: DocQualityGates
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [governance, quality-gates, doc, llm, discipline, core]
depends_on: [DISCIPLINE_05_DOC_COMPLIANCE, META_03_NAMING_CONVENTIONS, META_04_WRITING_RULES, META_05_FRONTMATTER]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_03 - Quality Gates Documentation (règles transversales)

Gates binaires (PASS/FAIL) pour qualifier un **document** :
- READY_TO_FREEZE
- FROZEN

CORE strict : aucune procédure opérateur, aucune cible spécifique.

---

## 1) Gate READY_TO_FREEZE — PASS/FAIL (P0)
PASS si :
- frontmatter conforme (`id==filename`, enums, arc/scope cohérents),
- objectif clair,
- structure lisible (H1 unique, sections cohérentes),
- non‑duplication de source de vérité,
- utilisable “sans oral”,
- no-secrets.

FAIL sinon.

---

## 2) Gate FROZEN — PASS/FAIL (P0)
FROZEN = READY_TO_FREEZE + :
- cohérence hiérarchique (pas de contradiction CORE),
- amendabilité contrôlée (modalités en SYSTEM),
- traçabilité suffisante (décisions structurantes tracées).

---

## 3) Extensions PACKAGE/PRODUCT
Peuvent renforcer, ne peuvent pas affaiblir.

---

### Changelog
- v1.1 (01-03-2026) : normalisation frontmatter + statut READY_TO_FREEZE + CORE strict.
- v1.0 (01-03-2026) : version initiale.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.3 (04-03-2026) : corrections frontmatter + heading.
