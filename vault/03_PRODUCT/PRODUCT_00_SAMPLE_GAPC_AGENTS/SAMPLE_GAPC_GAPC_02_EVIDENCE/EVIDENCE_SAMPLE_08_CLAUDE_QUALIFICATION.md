---
id: EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
type: EVIDENCE
title: SampleClaudeQualificationEvidence
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [product, sample, evidence, agent, claude, qualification]
depends_on:
  - EVIDENCE_05_ADR_CLAUDE_AGENT
  - WORKFLOW_07_TESTS_LLM
  - WORKFLOW_08_TESTS_EXECUTION
  - SETUP_PRODUCT_05_LIFECYCLE_POLICY
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_GAPC_02_EVIDENCE
---

# EVIDENCE_SAMPLE_08 - Claude Qualification Evidence

## Objet

Porter les preuves de qualification de l agent Claude pour
`PRODUCT_00_SAMPLE_GAPC_AGENTS`. Remplace les preuves AnythingLLM / Codex
`EVIDENCE_SAMPLE_00..07` (archivees en `99_CACHE`).

## Etat du product

- **Rollback** (`SETUP_PRODUCT_05_LIFECYCLE_POLICY`) : les gates agent sont

  KO depuis le changement d agent (`EVIDENCE_05_ADR_CLAUDE_AGENT`) ; le gel est
  suspendu jusqu a requalification.

- Statut des preuves : **A PRODUIRE**.

## Preuves attendues

| Serie | Perimetre | Runbook | Resultat |
| --- | --- | --- | --- |
| MENTOR commune T0-T6 | RulesOnly | `WORKFLOW_07_TESTS_LLM` | A PRODUIRE |
| MENTOR commune T0-T6 + serie GAPC | PackageScoped `PACKAGE_00_GAPC` | `WORKFLOW_07_TESTS_LLM` | A PRODUIRE |
| MENTOR commune T0-T6 | ProductScoped (ce product) | `WORKFLOW_07_TESTS_LLM` | A PRODUIRE |
| EXECUTION E1-E6 | PackageScoped `PACKAGE_00_GAPC` | `WORKFLOW_08_TESTS_EXECUTION` | A PRODUIRE |

## Trace (a completer par serie)

```txt
Date:
Modele:
Perimetre:
Resultats: T0..T6 / E1..E6 PASS|FAIL (+ extrait si FAIL)
Verdict: QUALIFIE | KO
```

## Sortie

Quand les 4 series sont `QUALIFIE` : DoD et OPS du product sont realignes sur
ces preuves, puis le product repasse `READY_TO_FREEZE`.

## Changelog

- v1.0 (14-11-2026) : creation du support de preuve Claude (rollback du sample).
