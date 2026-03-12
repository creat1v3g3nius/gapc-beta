---
id: DOD_03_RELEASE_FREEZE
type: DOD
title: GapcMentorReleaseFreeze
version: v1.4
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, dod, release, freeze, frozen]
depends_on: [DOD_00_PRODUCT_VALIDATION, DOD_01_PRODUCT_THIN_SLICE, DOD_02_RAG_WORKSPACE_TESTS, DISCIPLINE_01_GEL_RULES, GAPC_DISCIPLINE_01_GEL_RULES, CHECKLIST_03_READY_TO_FREEZE, GAPC_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON, TPL_10_RELEASE_NOTE]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_GAPC_MENTOR/GAPC_MENTOR_00_DOD
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

# DOD_03 - Release Freeze

## Objet
Poser les criteres minimaux pour declarer `PRODUCT_00_GAPC_MENTOR` :
- `READY_TO_FREEZE`
- puis `FROZEN` quand le lot est stable et reproductible

## 1) Gate READY_TO_FREEZE (P0)
PASS si :
- `DOD_00_PRODUCT_VALIDATION` est OK
- le thin slice est prouve
- les tests workspace RAG sont PASS
- les sources et actifs sont explicites
- aucun P0 open lie a secrets, scope ou confusion de roles

## 2) Gate FROZEN (P0)
PASS si :
- `READY_TO_FREEZE` est deja PASS
- le lot est reproductible sans oral
- les amendements sont controles
- le release note existe si un gel est declare

## 3) Evidence de gel
```txt
Target: READY_TO_FREEZE | FROZEN
Verdict: OK | KO
P0 fails:
Evidence IDs:
Release note:
Next step unique:
```

## 3.1 Evidence de gel documentee
```txt
Target: FROZEN
Verdict: OK
P0 fails:
- aucun
Evidence IDs:
- DOD_00_PRODUCT_VALIDATION
- DOD_01_PRODUCT_THIN_SLICE
- EVIDENCE_00_INDEX
- EVIDENCE_01_WS00_RULESONLY
- EVIDENCE_02_WS01_PACKAGESCOPED
- EVIDENCE_03_WS02_PRODUCTSCOPED
- EVIDENCE_04_CODEX_IDE
- OPS_06_READY_TO_FREEZE_CHECKLIST
Release note:
- EVIDENCE_05_RELEASE_NOTE_PRODUCT_VALIDATION
Next step unique:
- conserver le lot `FROZEN`
```

## 4) Anti-derive
- pas de redescription des regles CORE dans le product
- pas de fallback API implicite
- pas de secret ni PII
- pas de multi-package ou multi-product

## Changelog
- v1.4 (13-03-2026) : bascule le gate final produit en `FROZEN`.
- v1.4 (13-03-2026) : raccorde la release note produit au gate `READY_TO_FREEZE`.
- v1.3 (13-03-2026) : passe la gate de gel en `READY_TO_FREEZE`.
- v1.2 (13-03-2026) : aligne la gate de gel sur le backfill `OPS` complet et ajoute la preuve Codex.
- v1.1 (12-03-2026) : ajoute l evidence de gel documentee et les `Evidence IDs` du pack produit.
- v1.0 (10-03-2026) : creation de la checklist de gel pour `PRODUCT_00_GAPC_MENTOR`.
