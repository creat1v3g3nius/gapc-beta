---
id: EVIDENCE_SAMPLE_02_WS01_PACKAGESCOPED
type: EVIDENCE
title: GapcMentorWs01PackageScopedSample
version: v1.1
status: FROZEN
created: 12-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, evidence, ws01, packagescoped, rag]
depends_on: [RUN_07_TESTS_LLM, GAPC_DISCIPLINE_00_RAG_PROFILE, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES, GAPC_CONSTRAINT_01_SOURCES_POLICY]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_GAPC_MENTOR/GAPC_MENTOR_02_EVIDENCE
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

# EVIDENCE_SAMPLE_02 - WS_01 PackageScoped

## Workspace
- workspace : `WS_01 PackageScoped`
- corpus : `WS_00 + PACKAGE_00_GAPC`
- date : `12-03-2026`

## Test Results
- `T1` hierarchie d autorite : PASS
- `T2` priorites de sources GAPC : PASS
- `T3` isolation d un autre package : PASS
- `T4` matrice des roles GAPC : PASS
- `T5` contradictions `CORE vs PACKAGE_00_GAPC` : PASS

## Evidence
```txt
Prompt pack:
- RUN_07_TESTS_LLM / WS_01 PackageScoped

Sources majeures:
- GAPC_DISCIPLINE_00_RAG_PROFILE
- GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
- GAPC_CONSTRAINT_01_SOURCES_POLICY
- GAPC_META_00_PACKAGE_PROFILE

Verdict:
- PASS 5/5
```

## Notes
- La collision `PRODUCT actif` vs `docs product actifs` a ete levee pour ne pas contaminer `WS_01`.
- Le format inline d AnythingLLM a ete traite en mode tolerant tant que le fond restait exact.

## Changelog
- v1.1 (13-03-2026) : passe la preuve `WS_01 PackageScoped` en `READY_TO_FREEZE`.
- v1.0 (12-03-2026) : creation de la preuve `WS_01 PackageScoped` avec verdict PASS 5/5.
