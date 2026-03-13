---
id: OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST
type: DOD
title: GapcMentorReadyToFreezeChecklist
version: v1.5
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, ready-to-freeze, checklist, dod]
depends_on: [DOD_SAMPLE_03_RELEASE_FREEZE, OPS_SAMPLE_00_BACKLOG_PRODUCT, OPS_SAMPLE_00_BACKLOG_CO, OPS_SAMPLE_01_PRD_DOD, OPS_SAMPLE_02_SPEC_DOD, OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD, OPS_SAMPLE_04_ACTION_DOC_DOD, OPS_SAMPLE_05_CO_DOD, CHECKLIST_03_READY_TO_FREEZE, GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale
- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_06 - Ready To Freeze Checklist

## Objet
Fournir la checklist produit de reference pour `PRODUCT_00_SAMPLE_GAPC_AGENTS`.

## Checklist P0
- [x] backlog product present
- [x] backlog CO present
- [x] PRD controle via `OPS_SAMPLE_01_PRD_DOD`
- [x] spec controlee via `OPS_SAMPLE_02_SPEC_DOD`
- [x] smoke plan controle via `OPS_SAMPLE_03_TESTPLAN_SMOKE_DOD`
- [x] action doc controlee via `OPS_SAMPLE_04_ACTION_DOC_DOD`
- [x] CO atomique controle via `OPS_SAMPLE_05_CO_DOD`
- [x] tests workspace RAG PASS
- [x] separation `Codex / AnythingLLM / API` lisible
- [x] no-secrets / no-PII confirme
- [x] actifs package/product explicites
- [x] verdict final formulable sans oral

## Sortie attendue
```txt
Target: FROZEN
Verdict: OK | KO
P0 fails:
Evidence IDs:
Next step unique:
```

## 2) Evidence documentee
```txt
Target: FROZEN
Verdict: OK
P0 fails:
- aucun
Evidence IDs:
- EVIDENCE_SAMPLE_00_INDEX
- EVIDENCE_SAMPLE_01_WS00_RULESONLY
- EVIDENCE_SAMPLE_02_WS01_PACKAGESCOPED
- EVIDENCE_SAMPLE_03_WS02_PRODUCTSCOPED
- EVIDENCE_SAMPLE_04_CODEX_IDE
Next step unique:
- conserver cette checklist comme preuve du gel produit
```

## Regle
Si un item P0 est KO :
- ne pas declarer `FROZEN`
- corriger la source ou la preuve manquante

## Changelog
- v1.5 (13-03-2026) : bascule la checklist produit de `READY_TO_FREEZE` a `FROZEN`.
- v1.5 (13-03-2026) : remplace `WORKFLOW_08_TESTS_CODEX` par `EVIDENCE_SAMPLE_04_CODEX_IDE` dans les preuves de gel.
- v1.4 (13-03-2026) : passe la checklist de gel en `READY_TO_FREEZE`.
- v1.3 (13-03-2026) : coche les controles `OPS_01` a `OPS_05`, passe la checklist a `Verdict: OK` et ajoute `WORKFLOW_08_TESTS_CODEX` dans la preuve.
- v1.2 (12-03-2026) : coche les items P0 deja prouves par le pack `EVIDENCE` et ajoute l evidence documentee READY_TO_FREEZE.
- v1.1 (10-03-2026) : ajoute backlog product et backlog CO dans la checklist de gel.
- v1.0 (10-03-2026) : creation de la checklist produit `READY_TO_FREEZE` pour `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
