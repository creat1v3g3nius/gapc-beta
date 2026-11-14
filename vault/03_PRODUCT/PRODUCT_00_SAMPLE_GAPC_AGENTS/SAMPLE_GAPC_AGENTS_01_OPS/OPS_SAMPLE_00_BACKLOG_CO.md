---
id: OPS_SAMPLE_00_BACKLOG_CO
type: DOD
title: GapcMentorBacklogCo
version: v1.4
status: DRAFT
created: 10-03-2026
updated: 14-11-2026
tags: [product, gapc-mentor, ops, backlog, co, dod]
depends_on:
  - OPS_SAMPLE_00_BACKLOG_PRODUCT
  - TPL_03_BACKLOG_CO
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_04_RISK_REGISTER
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_00 - Backlog CO

> **Rollback 14-11-2026** (`SETUP_PRODUCT_05_LIFECYCLE_POLICY`) : le dispositif
> AnythingLLM / Codex est remplace par l agent Claude
> (`EVIDENCE_05_ADR_CLAUDE_AGENT`). Gel suspendu, document repasse en `DRAFT`
> en attente des preuves `EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`. Les mentions `API externe` restantes
> designent un role retire, a supprimer a la requalification.


## Objet

Lister les CO atomiques du product mentor selon le format `Backlog CO`.

### CO_001 - Verifier la separation des roles

- Arc principal : PRODUCT
- Goal (1 phrase) : prouver que `Agent EXECUTION`, `Agent MENTOR` et `API externe` gardent

  des roles distincts

- Inputs / dependances : `DOD_SAMPLE_00_PRODUCT_VALIDATION`,

  `LLM_04_AGENT_CLAUDE`, `SCRIPT_07_INSTRUCTIONS_CLAUDE`

- Output attendu : verdict PASS/FAIL sur la separation des roles
- Critere PASS/FAIL : aucune ambiguite d execution ou de fallback
- Scope : NOW
- Priorite : P0
- Risque : R1
- Next step unique : relier le verdict a `OPS_SAMPLE_05_CO_DOD`

### CO_002 - Prouver les workspaces RAG

- Arc principal : PRODUCT
- Goal (1 phrase) : demontrer que `RulesOnly` et `GAPC+Product` couvrent les

  besoins nominaux

- Inputs / dependances : `DOD_SAMPLE_02_RAG_WORKSPACE_TESTS`,

  `LLM_04_AGENT_CLAUDE`, `GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES`

- Output attendu : batterie de tests A REQUALIFIER (PASS historique AnythingLLM / Codex)/FAIL exploitable sans oral
- Critere PASS/FAIL : sources, `NON TROUVE`, no-secrets et non-substitution a

  `Agent EXECUTION` prouves

- Scope : NOW
- Priorite : P0
- Risque : R1
- Next step unique : consolider l evidence dans

  `OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD`

### CO_003 - Declarer le gel produit

- Arc principal : PRODUCT
- Goal (1 phrase) : declarer le gel `FROZEN` sur une base de preuves complete
- Inputs / dependances : `DOD_SAMPLE_03_RELEASE_FREEZE`,

  `CHECKLIST_03_READY_TO_FREEZE`,
  `GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON`

- Output attendu : checklist produit et verdict final
- Critere PASS/FAIL : aucun P0 ouvert, chaine de preuve complete
- Scope : NOW
- Priorite : P0
- Risque : R2
- Next step unique : figer la decision finale dans

  `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`

## Evidence documentee

```txt
CO_001:

- Verdict: A REQUALIFIER (PASS historique AnythingLLM / Codex)
- Evidence: separation `Agent EXECUTION / Agent MENTOR / API externe fallback` a prouver par `WORKFLOW_07_TESTS_LLM`, `WORKFLOW_08_TESTS_EXECUTION`, `EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`

CO_002:

- Verdict: A REQUALIFIER (PASS historique AnythingLLM / Codex)
- Evidence: historique AnythingLLM `RulesOnly` 6/6, `PackageScoped` 5/5, `ProductScoped` 8/8 (preuves archivees) ; nouvelles traces attendues dans `EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`

CO_003:

- Verdict: A REQUALIFIER (PASS historique AnythingLLM / Codex)
- Evidence: checklist de gel backfill, plus aucun P0 ouvert dans `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`
- Next step unique: reporter ce verdict dans la decision de gel finale

```

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (14-11-2026) : rollback (gel suspendu) ; references realignees sur l agent

  Claude, preuves AnythingLLM / Codex archivees (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- v1.3 (13-03-2026) : aligne `CO_003` sur la declaration finale `FROZEN`.
- v1.2 (13-03-2026) : passe le backlog CO en `READY_TO_FREEZE` apres cloture des

  trois CO.

- v1.1 (13-03-2026) : backfill les verdicts des CO a partir des preuves `WS_00`,

  `WS_01`, `WS_02` et des tests Codex.

- v1.0 (10-03-2026) : creation du backlog CO pour

  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
