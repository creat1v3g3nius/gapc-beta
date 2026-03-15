---
id: DOD_SAMPLE_01_PRODUCT_THIN_SLICE
type: DOD
title: GapcMentorProductThinSlice
version: v1.4
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, dod, thin-slice, mentor, validation]
depends_on:
  - DOD_SAMPLE_00_PRODUCT_VALIDATION
  - PIPELINE_00_PRODUCT
  - PIPELINE_02_BACKLOG_PRODUCT
  - TPL_00_PROD_ONE_PAGER
  - TPL_01_SPEC_TECH
  - TPL_03_BACKLOG_CO
  - TPL_04_TEST_PLAN_SMOKE
  - TPL_05_ACTION_DOC
  - TPL_06_ACTION_CODE
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - OPS_SAMPLE_00_BACKLOG_PRODUCT
  - OPS_SAMPLE_00_BACKLOG_CO
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_00_DOD
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# DOD_SAMPLE_01 - Product Thin Slice

## Objet

Definir le cycle minimal que `PRODUCT_00_SAMPLE_GAPC_AGENTS` doit demontrer sans
oral.

## 1) Thin slice cible

Le thin slice valide un scenario simple :

1. une question documentaire ciblee est posee au mentor
2. le mentor repond avec sources, hypothese et next step unique
3. une demande d implementation est redirigee vers `Codex`
4. `Codex` produit le patch ou l action technique correspondante
5. les checks documentaires et de scope restent PASS

## 2) Artefacts minimaux

- backlog product
- backlog CO atomique
- PRD one-pager
- spec tech
- plan de smoke
- action doc et/ou action code
- verdict final documente

## 3) PASS / FAIL

PASS si :

- la question documentaire est resolue sans invention
- les sources sont citees
- le mentor reste read-only
- la demande technique passe bien chez `Codex`
- aucun secret n est expose

FAIL si :

- la reponse documentaire derive vers patch ou execution
- le fallback API devient obligatoire pour un cas nominal
- le scope package/product n est pas stable

## 4) Evidence attendue

```txt
Question:
Sources:
Reponse mentor:
Redirection Codex:
Action technique:
Verdict thin slice:
```

## 4.1 Evidence documentee

```txt
Question:
- question documentaire ciblee dans `WS_02 ProductScoped` sur le setup mentor / product

Sources:
- DOD_SAMPLE_02_RAG_WORKSPACE_TESTS
- OPS_SAMPLE_02_SPEC_DOD
- LLM_03_MENTOR_UTILITES

Reponse mentor:
- reponse sourcee, read-only, sans patch ni execution

Redirection Codex:
- demande technique redirigee vers Codex pour patch / execution / tests

Action technique:
- batterie `WORKFLOW_08_TESTS_CODEX` executee avec PASS

Verdict thin slice:
- PASS
```

## 5) Next step standard

- conserver ce thin slice comme preuve du lot gele si tous les P0 restent PASS

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (13-03-2026) : aligne le next step du thin slice sur l etat `FROZEN`.
- v1.3 (13-03-2026) : passe le thin slice en `READY_TO_FREEZE` apres backfill
  des preuves.
- v1.2 (13-03-2026) : backfill l evidence du thin slice a partir des reruns
  mentor + Codex et passe le verdict thin slice a PASS.
- v1.1 (10-03-2026) : rattache le thin slice au backlog product et au backlog CO
  du lot OPS.
- v1.0 (10-03-2026) : creation du thin slice minimal pour
  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
