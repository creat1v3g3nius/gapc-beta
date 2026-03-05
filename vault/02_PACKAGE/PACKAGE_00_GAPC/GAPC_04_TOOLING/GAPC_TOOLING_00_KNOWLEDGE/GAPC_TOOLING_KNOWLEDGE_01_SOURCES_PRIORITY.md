---
id: GAPC_TOOLING_KNOWLEDGE_01_SOURCES_PRIORITY
type: TOOLING
title: GapcSourcesPriority
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, knowledge, sources, p1]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, DISCIPLINE_06_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_01_GEL_RULES, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, GAPC_DISCIPLINE_00_RAG_PROFILE, CONSTRAINT_01_RAG_SCOPE_POLICY]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_00_KNOWLEDGE
---

# GAPC_TOOLING_KNOWLEDGE_01 - Sources Priority

## Objet
Définir la priorité de sources quand GAPC est actif (anti-mélange, anti-hallucination).

## Priorité (P0)
1) GAPC discipline (scope/risk/gel/rag)
2) PACKAGE_00_GAPC (reste du package)
3) CORE (META/DISCIPLINE/CONSTRAINT/TOOLING)
4) PRODUCT actif (CO + livrables) si question product
5) SYSTEM (procédures : comment faire)
6) CACHE (jamais vérité)

## Règles
- Si absence de source : `NON TROUVÉ`
- Si mélange packages/products : refuser + demander isolation
- Commencer par RulesOnly puis étendre par couches (RagScopePolicy)

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction `scope` + `depends_on` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
