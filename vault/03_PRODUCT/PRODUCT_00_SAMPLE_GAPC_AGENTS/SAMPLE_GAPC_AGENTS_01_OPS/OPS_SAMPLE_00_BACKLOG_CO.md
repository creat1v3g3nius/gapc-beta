---
id: OPS_SAMPLE_00_BACKLOG_CO
type: DOD
title: GapcMentorBacklogCo
version: v1.3
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, backlog, co, dod]
depends_on: [OPS_SAMPLE_00_BACKLOG_PRODUCT, TPL_03_BACKLOG_CO, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale
- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_00 - Backlog CO

## Objet
Lister les CO atomiques du product mentor selon le format `Backlog CO`.

### CO_001 - Verifier la separation des roles
- Arc principal : PRODUCT
- Goal (1 phrase) : prouver que `Codex`, `AnythingLLM` et `API externe` gardent des roles distincts
- Inputs / dependances : `DOD_SAMPLE_00_PRODUCT_VALIDATION`, `LLM_00_RAG_PRINCIPES`, `SCRIPT_03_INSTRUCTIONS_CODEX`
- Output attendu : verdict PASS/FAIL sur la separation des roles
- Critere PASS/FAIL : aucune ambiguite d execution ou de fallback
- Scope : NOW
- Priorite : P0
- Risque : R1
- Next step unique : relier le verdict a `OPS_SAMPLE_05_CO_DOD`

### CO_002 - Prouver les workspaces RAG
- Arc principal : PRODUCT
- Goal (1 phrase) : demontrer que `RulesOnly` et `GAPC+Product` couvrent les besoins nominaux
- Inputs / dependances : `DOD_SAMPLE_02_RAG_WORKSPACE_TESTS`, `LLM_01_INGESTION_PROTOCOL`, `GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES`
- Output attendu : batterie de tests PASS/FAIL exploitable sans oral
- Critere PASS/FAIL : sources, `NON TROUVE`, no-secrets et non-substitution a `Codex` prouves
- Scope : NOW
- Priorite : P0
- Risque : R1
- Next step unique : consolider l evidence dans `OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD`

### CO_003 - Declarer le gel produit
- Arc principal : PRODUCT
- Goal (1 phrase) : declarer le gel `FROZEN` sur une base de preuves complete
- Inputs / dependances : `DOD_SAMPLE_03_RELEASE_FREEZE`, `CHECKLIST_03_READY_TO_FREEZE`, `GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON`
- Output attendu : checklist produit et verdict final
- Critere PASS/FAIL : aucun P0 ouvert, chaine de preuve complete
- Scope : NOW
- Priorite : P0
- Risque : R2
- Next step unique : figer la decision finale dans `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`

## Evidence documentee
```txt
CO_001:
- Verdict: PASS
- Evidence: separation `Codex / AnythingLLM / API externe fallback` prouvee par `WORKFLOW_07_TESTS_LLM`, `WORKFLOW_08_TESTS_CODEX`, `EVIDENCE_SAMPLE_00_INDEX`

CO_002:
- Verdict: PASS
- Evidence: `WS_00` PASS 6/6, `WS_01` PASS 5/5, `WS_02` PASS 8/8 traces dans `EVIDENCE_SAMPLE_01_WS00_RULESONLY`, `EVIDENCE_SAMPLE_02_WS01_PACKAGESCOPED`, `EVIDENCE_SAMPLE_03_WS02_PRODUCTSCOPED`

CO_003:
- Verdict: PASS
- Evidence: checklist de gel backfill, plus aucun P0 ouvert dans `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`
- Next step unique: reporter ce verdict dans la decision de gel finale
```

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (13-03-2026) : aligne `CO_003` sur la declaration finale `FROZEN`.
- v1.2 (13-03-2026) : passe le backlog CO en `READY_TO_FREEZE` apres cloture des trois CO.
- v1.1 (13-03-2026) : backfill les verdicts des CO a partir des preuves `WS_00`, `WS_01`, `WS_02` et des tests Codex.
- v1.0 (10-03-2026) : creation du backlog CO pour `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
