---
id: OPS_SAMPLE_04_ACTION_DOC_DOD
type: DOD
title: GapcMentorActionDocDod
version: v1.3
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, action-doc, dod]
depends_on: [OPS_SAMPLE_02_SPEC_DOD, OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD, TPL_05_ACTION_DOC, DOD_SAMPLE_02_RAG_WORKSPACE_TESTS]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_GAPC_MENTOR/GAPC_MENTOR_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

## Copie locale
- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_04 - Action Doc DoD

## Objet
Verifier qu une action documentaire sur le setup mentor est diff-first, sourcee et sans duplication de verite.

## 1) PASS / FAIL
PASS si :
- le fichier cible est nomme
- la section cible est nommee
- le patch reste atomique
- la validation cite la coherence `CORE -> PACKAGE -> PRODUCT -> SYSTEM`

FAIL si :
- le patch recrit une regle CORE dans le product
- la modification introduit secret, PII ou scope mixte
- aucun controle documentaire n est note

## 2) Evidence
```txt
Fichier:
Section:
Intention:
Patch:
Validation:
Verdict:
Next step unique:
```

## 3) Evidence documentee
```txt
Fichier:
- RUN_07_TESTS_LLM
- RUN_08_TESTS_CODEX
- GAPC_DISCIPLINE_00_RAG_PROFILE
- GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
- OPS_SAMPLE_02_SPEC_DOD

Section:
- prompts de qualification canonises
- formats critiques `T1/T2/T4/T6`
- priorites de sources package et produit

Intention:
- stabiliser la qualification mentor AnythingLLM et agent Codex

Patch:
- canonisation des prompts optimises
- backfill des preuves produit
- suppression des collisions documentaires sur les formats critiques

Validation:
- `WS_00` PASS
- `WS_01` PASS
- `WS_02` PASS
- Codex PASS

Verdict: PASS
Next step unique: figer ces prompts comme reference operative dans le lot produit
```

## Changelog
- v1.3 (13-03-2026) : aligne le controle action doc sur l etat final `FROZEN`.
- v1.2 (13-03-2026) : passe le controle action doc en `READY_TO_FREEZE`.
- v1.1 (13-03-2026) : backfill l action doc avec les patchs ayant stabilise la qualification mentor + Codex.
- v1.0 (10-03-2026) : creation du controle action doc pour `PRODUCT_00_GAPC_MENTOR`.
