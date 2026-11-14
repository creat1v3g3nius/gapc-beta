---
id: DOD_SAMPLE_00_PRODUCT_VALIDATION
type: DOD
title: GapcMentorProductValidation
version: v1.6
status: FROZEN
created: 10-03-2026
updated: 14-11-2026
tags: [product, gapc-mentor, dod, validation, rag, mentor]
depends_on:
  - PIPELINE_00_PRODUCT
  - CONSTRAINT_03_SECRETS_POLICY
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_02_RAG_QG
  - GAPC_DISCIPLINE_01_GEL_RULES
  - GAPC_DISCIPLINE_02_RAG_QG
  - GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
  - LLM_04_AGENT_CLAUDE
  - SCRIPT_07_INSTRUCTIONS_CLAUDE
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_00_DOD
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# DOD_SAMPLE_00 - Product Validation



## Objet

Valider que `PRODUCT_00_SAMPLE_GAPC_AGENTS` prouve un setup product exploitable
pour :

- `Agent EXECUTION` en execution, patch et diagnostic technique
- `Agent MENTOR` en mentor documentaire read-only
- `Humain (decision)` pour tout arbitrage ou nouvelle regle

Le product porte les preuves, les checks et les verdicts.
Les regles transverses restent dans `CORE`, les overlays restent dans
`PACKAGE_00_GAPC`.

## 1) Pre-conditions (P0)

- package actif = `PACKAGE_00_GAPC`
- product actif = `PRODUCT_00_SAMPLE_GAPC_AGENTS`
- no-secrets / no-PII
- actifs uniques et workspace scope
- 1 intention = 1 CO = 1 commit

## 2) Checks P0 (PASS/FAIL)

### 2.1 Separation des roles

PASS si :

- `Agent EXECUTION` porte code, patch, execution, smoke et diagnostics
- `Agent MENTOR` reste read-only, cite ses sources et n execute rien
- aucune ecriture en mode MENTOR, aucun commit ni push sans accord

KO si :

- le mentor produit un patch d implementation
- un test pousse a utiliser l API par defaut
- la frontiere `Agent EXECUTION / mentor / API` n est pas lisible

### 2.2 Scope et sources

PASS si :

- ordre d autorite = `CORE -> PACKAGE -> PRODUCT -> SYSTEM -> CACHE`
- product scoped = `PACKAGE_00_GAPC + PRODUCT_00_SAMPLE_GAPC_AGENTS`
- `NON TROUVE` est respecte

KO si :

- une reponse priorise le PACKAGE avant le CORE sur une regle transverse
- un autre package ou product est melange
- le cache sert de verite

### 2.3 Workspaces mentor

PASS si :

- `RulesOnly` et `GAPC+Product` sont definis
- les tests de `DOD_SAMPLE_02_RAG_WORKSPACE_TESTS` sont executables
- les droits read-only du mentor sont pris en compte

KO si :

- le workspace "all vault" devient nominal
- les actifs ne sont pas isoles
- les tests ne prouvent pas la non-substitution a Agent EXECUTION

### 2.4 Evidence minimale

PASS si :

- un thin slice documente existe (`DOD_SAMPLE_01_PRODUCT_THIN_SLICE`)
- un lot de tests RAG existe (`DOD_SAMPLE_02_RAG_WORKSPACE_TESTS`)
- une checklist de gel existe (`DOD_SAMPLE_03_RELEASE_FREEZE`)

KO si :

- la chaine de preuve est incomplete
- aucun verdict PASS/FAIL n est formulable sans oral

## 3) Sortie attendue

```txt
Verdict: OK | KO
P0 fails:
Evidence IDs:
Risques ouverts:
Next step unique:
```

## 3.1 Verdict documente

```txt
Verdict: OK
P0 fails:

- aucun

Evidence IDs:

- EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
- EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
- EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
- EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
- EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION

Risques ouverts:

- aucun P0 ouvert sur le setup mentor + Agent EXECUTION

Next step unique:

- consolider ce verdict dans `DOD_SAMPLE_03_RELEASE_FREEZE`

```

## 4) Notes de cadrage

- Le lot `OPS_*` complete la chaine de preuve operatoire du product.
- Le product sert d espace de preuve et de validation, pas de source de verite

  transverse.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.6 (14-11-2026) : passage en FROZEN apres qualification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`).

- v1.5 (14-11-2026) : requalification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`) ; role API

  externe retire ; passage `READY_TO_FREEZE`.

- v1.4 (14-11-2026) : rollback (gel suspendu) ; references realignees sur l agent

  Claude, preuves AnythingLLM / Codex archivees (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- v1.3 (13-03-2026) : normalise le libelle `API externe fallback` et passe le

  document en `READY_TO_FREEZE`.

- v1.2 (13-03-2026) : aligne le verdict final sur le lot `OPS` backfill et

  ajoute la preuve `EVIDENCE_SAMPLE_04_CODEX_IDE`.

- v1.1 (12-03-2026) : ajoute le verdict documente et les `Evidence IDs` du pack

  `SAMPLE_GAPC_GAPC_02_EVIDENCE`.

- v1.1 (10-03-2026) : aligne la note de cadrage sur la creation du lot `OPS_*`.
- v1.0 (10-03-2026) : creation du document de validation produit pour

  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
