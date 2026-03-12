---
id: OPS_00_BACKLOG_PRODUCT
type: DOD
title: GapcMentorBacklogProduct
version: v1.4
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, backlog, product, dod]
depends_on: [PIPELINE_02_BACKLOG_PRODUCT, TPL_03_BACKLOG_CO, DOD_00_PRODUCT_VALIDATION, DOD_01_PRODUCT_THIN_SLICE]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_GAPC_MENTOR/GAPC_MENTOR_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

# OPS_00 - Backlog Product

## Objet
Structurer le backlog produit minimal de `PRODUCT_00_GAPC_MENTOR` pour rendre la chaine de preuve lisible et actionnable.

## 1) Vision
- Product cible : `PRODUCT_00_GAPC_MENTOR`
- Package actif : `PACKAGE_00_GAPC`
- But : prouver un setup nominal ou `Codex` execute, `AnythingLLM` lit et l `API externe` reste un fallback cible
- Statut global : `FROZEN`

## 2) CO actifs
- `CO_001` : verifier la separation `Codex / AnythingLLM / API`
- `CO_002` : prouver les workspaces RAG et les tests P0
- `CO_003` : formaliser le passage `READY_TO_FREEZE`

## 3) Mapping recommande
- PRD / cadrage : `OPS_01_PRD_DOD`
- Spec : `OPS_02_SPEC_DOD`
- Smoke : `OPS_03_TESTPLAN_SMOKE_DOD`
- Action doc : `OPS_04_ACTION_DOC_DOD`
- CO : `OPS_05_CO_DOD`
- Gel : `OPS_06_READY_TO_FREEZE_CHECKLIST`

## 4) Regles P0
- 1 intention = 1 CO
- pas de multi-package ni multi-product
- pas de secret ou PII
- pas de fallback API implicite
- pour `WS_02`, 1 product actif = `PRODUCT_00_GAPC_MENTOR`
- un autre product doit etre refuse explicitement avec demande d isolation
- les priorites de sources produit suivent `CORE -> GAPC discipline -> autres docs package GAPC -> docs product actifs -> SYSTEM`
- la matrice des roles produit reste `1 bloc par tache`

## 5) Sortie attendue
```txt
Backlog status: DRAFT | READY_TO_FREEZE | FROZEN
CO actifs:
Risques:
Next step unique:
```

## 6) Formats de controle workspace

### 6.1 Refus d un autre product
Format attendu :
- `Refus :`
- `Isolation requise :`
- `Sources utilisees :`

### 6.2 Matrice des roles produit
Format attendu :
- `Tache :`
- `Role nominal :`
- `Justification :`
- `Sources utilisees :`

### 6.3 Priorites de sources produit
Format attendu :
- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `docs product actifs`
- `SYSTEM`
- `Sources utilisees :`

Interdit :
- repondre avec la hierarchie d autorite `CORE -> PACKAGE_00_GAPC -> PRODUCT_00_GAPC_MENTOR -> SYSTEM -> CACHE`,
- utiliser les arcs `PACKAGE_00_GAPC` ou `PRODUCT_00_GAPC_MENTOR` a la place des categories de sources,
- ajouter `CACHE`.

Exemple minimal valide :
- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `docs product actifs`
- `SYSTEM`
- `Sources utilisees : GAPC_DISCIPLINE_00_RAG_PROFILE.md, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES.md, OPS_02_SPEC_DOD.md`

## 7) Evidence documentee
```txt
Workspace status:
- WS_00 RulesOnly: PASS
- WS_01 PackageScoped: PASS
- WS_02 ProductScoped: PASS

Codex status:
- Batterie RUN_08_TESTS_CODEX: PASS

Evidence IDs:
- EVIDENCE_00_INDEX
- EVIDENCE_01_WS00_RULESONLY
- EVIDENCE_02_WS01_PACKAGESCOPED
- EVIDENCE_03_WS02_PRODUCTSCOPED

Backlog status: FROZEN
CO actifs: CO_001, CO_002, CO_003
Risques: aucun P0 ouvert sur la configuration mentor + Codex
Next step unique: conserver ce backlog comme reference gelée du produit
```

## Changelog
- v1.4 (13-03-2026) : bascule le backlog produit en `FROZEN`.
- v1.4 (13-03-2026) : passe le backlog produit en `READY_TO_FREEZE`.
- v1.3 (13-03-2026) : passe le backlog produit en `READY_TO_FREEZE candidate` apres PASS des batteries mentor et Codex.
- v1.2 (11-03-2026) : renforce le format `T2` pour `WS_02` avec interdictions explicites et exemple minimal valide.
- v1.1 (11-03-2026) : ajoute les regles `WS_02` sur product actif unique, priorites de sources produit et formats de controle workspace.
- v1.0 (10-03-2026) : creation du backlog product pour `PRODUCT_00_GAPC_MENTOR`.
