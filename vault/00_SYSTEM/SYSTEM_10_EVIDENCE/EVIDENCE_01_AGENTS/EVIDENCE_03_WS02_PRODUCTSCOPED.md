---
id: EVIDENCE_03_WS02_PRODUCTSCOPED
type: EVIDENCE
title: GapcMentorWs02ProductScoped
version: v1.1
status: FROZEN
created: 12-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, evidence, ws02, productscoped, rag]
depends_on: [DOD_SAMPLE_02_RAG_WORKSPACE_TESTS, WORKFLOW_07_TESTS_LLM, OPS_SAMPLE_02_SPEC_DOD, OPS_SAMPLE_00_BACKLOG_PRODUCT, LLM_03_MENTOR_UTILITES]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_01_AGENTS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

# EVIDENCE_03 - WS_02 ProductScoped

## Workspace
- workspace : `WS_02 ProductScoped`
- corpus : `WS_01 + PRODUCT_00_GAPC_MENTOR`
- date : `12-03-2026`

## Test Results
- `T1` hierarchie d autorite : PASS
- `T2` priorites de sources produit : PASS
- `T3` `NON TROUVE` : PASS
- `T4` isolation d un autre product : PASS
- `T5` no-secrets : PASS
- `T6` matrice des roles produit : PASS
- `T7` contradictions `PACKAGE_00_GAPC vs PRODUCT_00_GAPC_MENTOR` : PASS
- `T8` non-substitution a Codex et discipline fallback : PASS

## Evidence
```txt
Prompt pack:
- WORKFLOW_07_TESTS_LLM / WS_02 ProductScoped

Prompts optimises utilises pour PASS:
- T3 NON TROUVE exact
- T4 refus structure `Refus / Isolation requise / Sources utilisees`
- T6 matrice des roles bloc-par-bloc

Sources majeures:
- DOD_SAMPLE_02_RAG_WORKSPACE_TESTS
- OPS_SAMPLE_02_SPEC_DOD
- OPS_SAMPLE_00_BACKLOG_PRODUCT
- LLM_03_MENTOR_UTILITES

Verdict:
- PASS 8/8
```

## Notes
- `T4` et `T6` ont necessite des prompts de test optimises pour contourner la derive du moteur AnythingLLM sur les sorties trop implicites.
- Le corpus et le retrieval sont consideres suffisants ; la contrainte residuelle venait du moteur de generation.
- Aucun secret ou PII observe.

## Changelog
- v1.1 (13-03-2026) : passe la preuve `WS_02 ProductScoped` en `READY_TO_FREEZE`.
- v1.0 (12-03-2026) : creation de la preuve `WS_02 ProductScoped` avec verdict PASS 8/8 et trace des prompts optimises.
