---
id: DISCIPLINE_02_RAG_QG
type: DISCIPLINE
title: RagQualityGates
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [governance, quality-gates, rag, llm, discipline, core]
depends_on: [DISCIPLINE_00_RAG_PROFILE, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_02 - Quality Gates RAG (règles transversales)

Gates binaires (PASS/FAIL) pour qualifier un mentor RAG :

- **RAG_READY_TO_FREEZE**
- **RAG_FROZEN**

CORE strict : aucune procédure opérateur, aucune commande, aucune cible
spécifique.
Procédures de test : SYSTEM/LLM. Exigences spécifiques : PACKAGE/PRODUCT.

---

## 1) Gate RAG_READY_TO_FREEZE — PASS/FAIL (P0)

PASS si :

- read-only + non décisionnel,
- hiérarchie d’autorité respectée,
- `NON TROUVÉ` respecté,
- actifs uniques (anti-mélange),
- sources obligatoires,
- no-secrets,
- risques RAG critiques mitigés.

FAIL sinon.

---

## 2) Gate RAG_FROZEN — PASS/FAIL (P0)

RAG_FROZEN = RAG_READY_TO_FREEZE + :

- profil explicite et stable,
- amendements contrôlés (modalités en SYSTEM),
- reproductibilité via procédure SYSTEM associée.

---

## 3) Extensions PACKAGE/PRODUCT

Peuvent renforcer, ne peuvent pas affaiblir les P0 CORE.

---

### Historique initial

- v1.0 (01-03-2026) : version initiale.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
