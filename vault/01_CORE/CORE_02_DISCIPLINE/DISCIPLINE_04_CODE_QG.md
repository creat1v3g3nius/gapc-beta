---
id: DISCIPLINE_04_CODE_QG
type: DISCIPLINE
title: CodeQualityGates
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [governance, quality-gates, code, llm, discipline, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_04 - Quality Gates Code (règles transversales)

Gates binaires (PASS/FAIL) pour qualifier un **changement exécutable** au moment
:

- MERGE (intégration),
- RELEASE (gel reproductible).

CORE strict : aucune procédure opérateur, aucun outil nommé, aucune cible
spécifique.
Contrôles concrets : SYSTEM.

---

## 1) Invariants CORE (P0)

- No-secrets
- Traçabilité (ADR-lite si décision structurante)
- Non‑régression (conventions + hiérarchie d’autorité)
- Reproductibilité minimale (via procédure SYSTEM)

---

## 2) Gate MERGE — PASS/FAIL (P0)

PASS si :

- intention atomique (ou lot cohérent justifié),
- contrôles d’exécution requis (SYSTEM) passent,
- no-secrets respecté,
- traçabilité suffisante,
- compatibilité Vault si le Vault est touché (contrat documentaire).

FAIL sinon.

---

## 3) Gate RELEASE — PASS/FAIL (P0)

RELEASE = MERGE PASS + :

- reproductibilité documentée (SYSTEM),
- observabilité minimale,
- rollback/backout défini,
- risques critiques mitigés.

---

## 4) Extensions PACKAGE/PRODUCT

Peuvent renforcer, ne peuvent pas affaiblir.

---

### Changelog

- v1.1 (01-03-2026) : normalisation frontmatter + statut READY_TO_FREEZE + CORE
  strict.
- v1.0 (01-03-2026) : version initiale.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : corrections frontmatter + heading.
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
