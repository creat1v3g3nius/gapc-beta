---
id: OPS_SAMPLE_05_CO_DOD
type: DOD
title: GapcMentorComponentOutputDod
version: v1.3
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, co, dod, backlog]
depends_on:
  - OPS_SAMPLE_00_BACKLOG_PRODUCT
  - OPS_SAMPLE_00_BACKLOG_CO
  - OPS_SAMPLE_01_PRD_DOD
  - OPS_SAMPLE_02_SPEC_DOD
  - OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD
  - OPS_SAMPLE_04_ACTION_DOC_DOD
  - TPL_03_BACKLOG_CO
  - DOD_SAMPLE_01_PRODUCT_THIN_SLICE
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_05 - CO DoD

## Objet

Verifier qu un CO du product mentor reste atomique et prouvable.

## 1) Regles P0

PASS si :

- 1 CO = 1 intention
- output attendu et critere PASS/FAIL sont explicites
- le risque principal est note
- le CO ne melange pas plusieurs arcs sans justification

FAIL si :

- le CO couvre plusieurs intentions
- la sortie attendue ne peut pas etre verifiee
- le CO force un fallback API non justifie

## 2) Evidence

```txt
CO:
Goal:
Output:
PASS/FAIL:
Risque:
Verdict:
Next step unique:
```

## 3) Notes

- Utiliser ce fichier comme point d entree des preuves liees a un lot de

  modifications.

- Le CO verifie ici doit exister en amont dans `OPS_SAMPLE_00_BACKLOG_CO`.

## 4) Evidence documentee

```txt
CO: CO_001 / CO_002 / CO_003
Goal:

- CO_001: verifier la separation des roles
- CO_002: prouver les workspaces RAG
- CO_003: formaliser le gel produit

Output:

- separation mentor / Codex / API prouvee
- batteries workspace `WS_00`, `WS_01`, `WS_02` PASS
- checklist `READY_TO_FREEZE` backfill et formulable sans oral

PASS/FAIL:

- CO_001: PASS
- CO_002: PASS
- CO_003: PASS

Risque:

- pas de P0 restant sur le setup mentor + Codex

Verdict: PASS
Next step unique: reporter ce verdict dans `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`
```

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (13-03-2026) : passe le controle CO en `READY_TO_FREEZE`.
- v1.2 (13-03-2026) : backfill les preuves des trois CO produits avec verdict

  PASS.

- v1.1 (10-03-2026) : rattache le controle CO au backlog product et au backlog

  CO.

- v1.0 (10-03-2026) : creation du controle CO pour

  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
