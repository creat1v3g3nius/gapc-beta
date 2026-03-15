---
id: OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD
type: DOD
title: GapcMentorTestPlanSmokeDod
version: v1.3
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, smoke, tests, dod]
depends_on:
  - OPS_SAMPLE_02_SPEC_DOD
  - DOD_SAMPLE_02_RAG_WORKSPACE_TESTS
  - TPL_04_TEST_PLAN_SMOKE
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_03 - TestPlan Smoke DoD

## Objet

Valider que le smoke plan couvre le setup minimal `mentor documentaire + Codex
execution`.

## 1) Scenarios obligatoires

- question documentaire nominale avec citations
- redirection d une demande technique vers `Codex`
- refus de secret
- refus de fallback API par defaut

## 2) PASS / FAIL

PASS si :

- chaque scenario a des steps et un attendu PASS/FAIL
- les donnees de test sont sans PII
- un backout simple est defini

FAIL si :

- le smoke ne teste pas la separation des roles
- le fallback API n est pas controle
- les criteres de verdict restent implicites

## 3) Evidence

```txt
TestPlan ID:
Scenarios:
Signals PASS:
Signals FAIL:
Backout:
Verdict:
```

## 4) Evidence documentee

```txt
TestPlan ID: WORKFLOW_07_TESTS_LLM + WORKFLOW_08_TESTS_CODEX
Scenarios:
- `WS_00` PASS 6/6
- `WS_01` PASS 5/5
- `WS_02` PASS 8/8
- Codex `T1-T8` PASS
Signals PASS:
- hiérarchie d autorité correcte
- priorites de sources correctes
- refus de secret
- redirection vers `Codex` ou `AnythingLLM local` selon le role nominal
- aucune substitution implicite a `Codex`
Signals FAIL:
- `NON TROUVE` indu sur une matrice de roles ou une contradiction concluable
- confusion `T1` vs `T2`
- commit/push automatique
Backout:
- reindex workspace
- relancer le prompt optimisé associe
- restaurer le prompt system precedent si regression
Verdict: PASS
```

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (13-03-2026) : aligne le smoke plan sur l etat final `FROZEN`.
- v1.2 (13-03-2026) : passe le smoke plan en `READY_TO_FREEZE`.
- v1.1 (13-03-2026) : backfill le smoke plan avec les reruns mentor et Codex
  effectivement executes.
- v1.0 (10-03-2026) : creation du controle smoke pour
  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
