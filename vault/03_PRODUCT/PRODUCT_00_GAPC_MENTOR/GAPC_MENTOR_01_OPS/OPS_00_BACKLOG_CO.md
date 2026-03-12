---
id: OPS_00_BACKLOG_CO
type: DOD
title: GapcMentorBacklogCo
version: v1.2
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, backlog, co, dod]
depends_on: [OPS_00_BACKLOG_PRODUCT, TPL_03_BACKLOG_CO, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_GAPC_MENTOR/GAPC_MENTOR_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

# OPS_00 - Backlog CO

## Objet
Lister les CO atomiques du product mentor selon le format `Backlog CO`.

### CO_001 - Verifier la separation des roles
- Arc principal : PRODUCT
- Goal (1 phrase) : prouver que `Codex`, `AnythingLLM` et `API externe` gardent des roles distincts
- Inputs / dependances : `DOD_00_PRODUCT_VALIDATION`, `LLM_00_RAG_PRINCIPES`, `SCRIPT_03_INSTRUCTIONS_CODEX`
- Output attendu : verdict PASS/FAIL sur la separation des roles
- Critere PASS/FAIL : aucune ambiguite d execution ou de fallback
- Scope : NOW
- Priorite : P0
- Risque : R1
- Next step unique : relier le verdict a `OPS_05_CO_DOD`

### CO_002 - Prouver les workspaces RAG
- Arc principal : PRODUCT
- Goal (1 phrase) : demontrer que `RulesOnly` et `GAPC+Product` couvrent les besoins nominaux
- Inputs / dependances : `DOD_02_RAG_WORKSPACE_TESTS`, `LLM_01_INGESTION_PROTOCOL`, `GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES`
- Output attendu : batterie de tests PASS/FAIL exploitable sans oral
- Critere PASS/FAIL : sources, `NON TROUVE`, no-secrets et non-substitution a `Codex` prouves
- Scope : NOW
- Priorite : P0
- Risque : R1
- Next step unique : consolider l evidence dans `OPS_03_TESTPLAN_SMOKE_DOD`

### CO_003 - Formaliser le gel produit
- Arc principal : PRODUCT
- Goal (1 phrase) : preparer la decision `READY_TO_FREEZE` sur une base de preuves complete
- Inputs / dependances : `DOD_03_RELEASE_FREEZE`, `CHECKLIST_03_READY_TO_FREEZE`, `GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON`
- Output attendu : checklist produit et verdict final
- Critere PASS/FAIL : aucun P0 ouvert, chaine de preuve complete
- Scope : NOW
- Priorite : P0
- Risque : R2
- Next step unique : finaliser `OPS_06_READY_TO_FREEZE_CHECKLIST`

## Evidence documentee
```txt
CO_001:
- Verdict: PASS
- Evidence: separation `Codex / AnythingLLM / API externe fallback` prouvee par `RUN_07_TESTS_LLM`, `RUN_08_TESTS_CODEX`, `EVIDENCE_00_INDEX`

CO_002:
- Verdict: PASS
- Evidence: `WS_00` PASS 6/6, `WS_01` PASS 5/5, `WS_02` PASS 8/8 traces dans `EVIDENCE_01_WS00_RULESONLY`, `EVIDENCE_02_WS01_PACKAGESCOPED`, `EVIDENCE_03_WS02_PRODUCTSCOPED`

CO_003:
- Verdict: PASS
- Evidence: checklist de gel backfill, plus aucun P0 ouvert dans `OPS_06_READY_TO_FREEZE_CHECKLIST`
- Next step unique: reporter ce verdict dans la decision de gel finale
```

## Changelog
- v1.2 (13-03-2026) : passe le backlog CO en `READY_TO_FREEZE` apres cloture des trois CO.
- v1.1 (13-03-2026) : backfill les verdicts des CO a partir des preuves `WS_00`, `WS_01`, `WS_02` et des tests Codex.
- v1.0 (10-03-2026) : creation du backlog CO pour `PRODUCT_00_GAPC_MENTOR`.
