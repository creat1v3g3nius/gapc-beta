---
id: CONSTRAINT_06_TERMINOLOGY_POLICY
type: CONSTRAINT
title: TerminologyPolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [limites, terminology-policy, llm, discipline, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_06 - Terminology Policy (contraintes transversales)

## Objet
Réduire l’ambiguïté et les contradictions en imposant une contrainte CORE minimale :
- termes stables,
- statuts/labels réservés,
- cohérence inter-arcs.

CORE strict : pas de procédure opérateur.

---

## 1) Règles P0
1) Les termes “contractuels” doivent être **stables** et utilisés de façon cohérente :
- arcs : SYSTEM/CORE/PACKAGE/PRODUCT/CACHE
- statuts : DRAFT/PROPOSED/READY_TO_FREEZE/FROZEN/DEPRECATED
- décisions : ADR-lite
- réponse : `NON TROUVÉ`

2) Interdit d’introduire des synonymes concurrents pour les mêmes concepts sans décision traçable.

## 2) Règles P1
3) Toute nouvelle notion transversale doit être :
- définie dans un doc CORE (ou index/glossary),
- référencée (non dupliquée).

---

### Changelog
- v1.0 (01-03-2026) : version minimale de la contrainte terminologie.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
