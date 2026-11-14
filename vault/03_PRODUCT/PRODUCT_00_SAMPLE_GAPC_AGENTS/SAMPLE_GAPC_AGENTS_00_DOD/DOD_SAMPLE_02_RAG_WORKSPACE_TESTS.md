---
id: DOD_SAMPLE_02_RAG_WORKSPACE_TESTS
type: DOD
title: GapcMentorRagWorkspaceTests
version: v1.9
status: FROZEN
created: 10-03-2026
updated: 14-11-2026
tags: [product, gapc-mentor, dod, rag, workspace, tests]
depends_on:
  - DOD_SAMPLE_00_PRODUCT_VALIDATION
  - LLM_04_AGENT_CLAUDE
  - DISCIPLINE_02_RAG_QG
  - GAPC_DISCIPLINE_02_RAG_QG
  - GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES
  - WORKFLOW_07_TESTS_LLM
  - WORKFLOW_08_TESTS_EXECUTION
  - EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_00_DOD
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# DOD_SAMPLE_02 - RAG Workspace Tests

## Objet

Definir la DoD de qualification de l agent Claude pour ce product. Les prompts
de reference ne sont pas recopies ici (`CONSTRAINT_02_NON_DUPLICATION_POLICY`) :
ils vivent dans `WORKFLOW_07_TESTS_LLM` et `WORKFLOW_08_TESTS_EXECUTION`.

## 1) Sessions cibles

| Serie | Mode | Perimetre | Tests |
| --- | --- | --- | --- |
| 1 | MENTOR (Plan mode) | RulesOnly | `WORKFLOW_07` T0-T6 |
| 2 | MENTOR (Plan mode) | PackageScoped `PACKAGE_00_GAPC` | `WORKFLOW_07` T0-T6 |
| 3 | MENTOR (Plan mode) | ProductScoped `PRODUCT_00_SAMPLE_GAPC_AGENTS` | `WORKFLOW_07` T0-T6 |
| 4 | EXECUTION | PackageScoped `PACKAGE_00_GAPC` | `WORKFLOW_08` E1-E6 |

## 2) Regle PASS / FAIL

PASS si :

- les 4 series sont PASS, chacune dans une nouvelle session,
- la trace de chaque serie est consignee dans `EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`.

FAIL si un seul test est FAIL : corriger `CLAUDE.md` et
`SCRIPT_07_INSTRUCTIONS_CLAUDE`, puis rejouer la serie complete.

## 3) Regle de sortie

- DoD PASS -> le product peut repasser `READY_TO_FREEZE`.
- Toute modification de `CLAUDE.md`, `SCRIPT_07_INSTRUCTIONS_CLAUDE` ou d un

  `META_*` du CORE impose de rejouer les 4 series.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.9 (14-11-2026) : passage en FROZEN apres qualification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`).

- v1.8 (14-11-2026) : requalification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`) ; DoD reecrite (renvoi a `WORKFLOW_07` / `WORKFLOW_08`), role API

  externe retire ; passage `READY_TO_FREEZE`.

- v1.7 (14-11-2026) : rollback (gel suspendu) ; references realignees sur l agent

  Claude, preuves AnythingLLM / Codex archivees (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- v1.6 (13-03-2026) : passe la batterie `WS_02` en `READY_TO_FREEZE` apres PASS

  complet des reruns.

- v1.5 (11-03-2026) : renforce `T2` avec interdiction des arcs a la place des

  categories de sources et ajoute un exemple minimal valide package+product.

- v1.4 (11-03-2026) : specialise la batterie `WS_02` pour le niveau produit avec

  `T2` priorites de sources produit, `T4` isolation d un autre product, `T6`
  bloc par tache obligatoire et `T7` compare `PACKAGE` vs `PRODUCT`.

- v1.3 (10-03-2026) : impose la coherence `source -> arc` sur `T5` et ajoute un

  exemple valide CORE/SYSTEM.

- v1.2 (10-03-2026) : aligne `DOD_02` sur la batterie `SYSTEM` complete avec

  formats attendus pour `T4/T5`.

- v1.1 (10-03-2026) : aligne les tests workspace sur la matrice des roles `Codex

  / AnythingLLM local / API externe`.

- v1.0 (10-03-2026) : creation de la batterie minimale de tests RAG pour

  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
