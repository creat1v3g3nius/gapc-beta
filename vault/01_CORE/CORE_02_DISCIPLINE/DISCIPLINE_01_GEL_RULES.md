---
id: DISCIPLINE_01_GEL_RULES
type: DISCIPLINE
title: GelRules
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [governance, gel-rules, llm, discipline, core]
depends_on: [DISCIPLINE_02_RAG_QG, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_05_DOC_COMPLIANCE, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_01 - Gel Rules (règles transversales)

Définir **uniquement** les règles transversales CORE des statuts :
- **READY_TO_FREEZE** : stable et utilisable *sans oral*
- **FROZEN** : gelé (modifications contrôlées)

CORE strict : aucune procédure opérateur, aucune cible spécifique.  
Procédures/preuves : SYSTEM. Exigences spécifiques : PACKAGE/PRODUCT.

---

## 1) Invariants CORE (P0)
- **No-secrets** (repo/vault/patches/logs/exemples).
- **Traçabilité** : tout statut doit être justifiable par preuves consultables (définies en SYSTEM).
- **Amendements contrôlés** (FROZEN) : modification contrôlée, tracée, versionnée (modalités en SYSTEM).
- **Extensions non régressives** : PACKAGE/PRODUCT ne font qu’ajouter.

---

## 2) Gate READY_TO_FREEZE — PASS/FAIL (P0)
PASS si :
- conformité (naming/frontmatter/architecture) respectée,
- utilisable “sans oral” (contenu explicite ou renvois),
- risques critiques connus mitigés,
- no-secrets respecté.

FAIL sinon.

---

## 3) Gate FROZEN — PASS/FAIL (P0)
FROZEN = READY_TO_FREEZE + :
- amendements contrôlés appliqués,
- reproductibilité démontrable via procédure SYSTEM associée,
- zéro P0 ouvert sur le périmètre gelé.

---

### Changelog
- v1.1 (01-03-2026) : normalisation frontmatter + statut READY_TO_FREEZE + formulation CORE strict (sans procédure/cible).
- v1.0 (01-03-2026) : version initiale.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.3 (04-03-2026) : corrections frontmatter + heading.
