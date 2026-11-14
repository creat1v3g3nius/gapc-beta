---
id: OPS_SAMPLE_01_PRD_DOD
type: DOD
title: GapcMentorPrdDod
version: v1.5
status: FROZEN
created: 10-03-2026
updated: 14-11-2026
tags: [product, gapc-mentor, ops, prd, dod]
depends_on:
  - DOD_SAMPLE_00_PRODUCT_VALIDATION
  - DOD_SAMPLE_01_PRODUCT_THIN_SLICE
  - TPL_00_PROD_ONE_PAGER
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_01 - PRD DoD



## Objet

Verifier que le PRD du product mentor est suffisant pour lancer un thin slice
sans oral.

## 1) Inputs attendus

- objectif produit en 1 phrase
- perimetre IN/OUT
- hypothese testable
- contraintes setup : `Agent EXECUTION`, `Agent MENTOR`, `Humain (decision)`

## 2) DoD PRD (PASS/FAIL)

PASS si :

- le besoin est formule pour `PRODUCT_00_SAMPLE_GAPC_AGENTS`
- le role de chaque agent est explicite
- les risques principaux sont notes
- le next step unique est formulable

FAIL si :

- le PRD melange documentaire et implementation sans frontiere
- le mode MENTOR est decrit comme pouvant ecrire
- les actifs package/product sont absents

## 3) Evidence

```txt
PRD ID:
Goal:
In/Out:
Risques:
Verdict:
Next step unique:
```

## 4) Evidence documentee

```txt
PRD ID: OPS_SAMPLE_00_BACKLOG_PRODUCT
Goal: prouver un setup nominal ou `Agent EXECUTION` execute, `Agent MENTOR` lit et l `Humain` decide
In/Out:

- IN: configuration mentor documentaire, separation des roles, workspaces `RulesOnly`, `PackageScoped`, `ProductScoped`, discipline no-secrets
- OUT: implementation applicative hors setup mentor/Agent EXECUTION

Risques:

- derive moteur Agent MENTOR sur des sorties trop implicites
- confusion residuale entre consultation documentaire et action IDE

Verdict: PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`)
Next step unique: reporter ce PASS dans `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`
```

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.5 (14-11-2026) : passage en FROZEN apres qualification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`).

- v1.4 (14-11-2026) : requalification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`) ; role API

  externe retire ; passage `READY_TO_FREEZE`.

- v1.3 (14-11-2026) : rollback (gel suspendu) ; references realignees sur l agent

  Claude, preuves AnythingLLM / Codex archivees (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- v1.2 (13-03-2026) : passe le controle PRD en `READY_TO_FREEZE`.
- v1.1 (13-03-2026) : backfill l evidence PRD avec le but, le perimetre et le

  verdict PASS du setup finalise.

- v1.0 (10-03-2026) : creation du controle PRD pour

  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
