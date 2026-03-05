---
id: ASSO_DISCIPLINE_02_RAG_QG
type: DISCIPLINE
title: AssoRagQualityGates
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, discipline, rag, qg, p1]
depends_on: [DISCIPLINE_02_RAG_QG, ASSO_DISCIPLINE_00_RAG_PROFILE, ASSO_CONSTRAINT_05_SOURCES_POLICY, ASSO_DISCIPLINE_03_LEXICAL_QG, CONSTRAINT_03_SECRETS_POLICY, ASSO_DISCIPLINE_05_RISK_REGISTER]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_02_DISCIPLINE
---

# ASSO_DISCIPLINE_02 - Rag Quality Gates

## Objet
Renforcer les gates RAG CORE pour le métier ASSO.

## ASSO_RAG_READY_TO_FREEZE (PASS/FAIL)
PASS si :
- sources citées (ou `NON TROUVÉ`)
- pas de mélange de package (ASSO-only)
- messaging policy respectée
- glossaire respecté
- no-secrets/no-PII

## ASSO_RAG_FROZEN
READY_TO_FREEZE PASS + stabilité du profil + zéro risque critique RAG ouvert sans mitigation+owner.

## Changelog
- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (02-03-2026) : passage en FROZEN v1.2 + correction depends_on.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création gates RAG ASSO (P1).

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
