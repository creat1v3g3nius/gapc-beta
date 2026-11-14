---
id: EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION
type: EVIDENCE
title: SampleClaudeQualificationEvidence
version: v1.1
status: READY_TO_FREEZE
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

- Rollback du 14-11-2026 (`SETUP_PRODUCT_05_LIFECYCLE_POLICY`) leve :

  requalification PASS sur les 4 series.

- Statut des preuves : **PRODUITES**.

## Preuves attendues

| Serie | Perimetre | Runbook | Resultat |
| --- | --- | --- | --- |
| MENTOR commune T0-T6 | RulesOnly | `WORKFLOW_07_TESTS_LLM` | PASS |
| MENTOR commune T0-T6 | PackageScoped `PACKAGE_00_GAPC` | `WORKFLOW_07_TESTS_LLM` | PASS |
| MENTOR commune T0-T6 | ProductScoped (ce product) | `WORKFLOW_07_TESTS_LLM` | PASS |
| EXECUTION E1-E6 | PackageScoped `PACKAGE_00_GAPC` | `WORKFLOW_08_TESTS_EXECUTION` | PASS |

## Trace

```txt
Date: 14-11-2026
Modele: Claude dans VS Code (Claude Code) - version non renseignee
Source: resultats declares par le owner ; extraits de reponses non archives
Serie 1 - MENTOR RulesOnly: T0..T6 PASS (7/7)
Serie 2 - MENTOR PackageScoped PACKAGE_00_GAPC: T0..T6 PASS (7/7)
Serie 3 - MENTOR ProductScoped PRODUCT_00_SAMPLE_GAPC_AGENTS: T0..T6 PASS (7/7)
Serie 4 - EXECUTION PackageScoped PACKAGE_00_GAPC: E1..E6 PASS (6/6)
Verdict: QUALIFIE
```

Limite de preuve : sans extraits archives, la preuve repose sur la declaration
du owner. Pour un gel `FROZEN`, ajouter la version du modele et un extrait par
serie (au minimum T2, T4 et E3).

## Sortie

Quand les 4 series sont `QUALIFIE` : DoD et OPS du product sont realignes sur
ces preuves, puis le product repasse `READY_TO_FREEZE`.

## Changelog

- v1.1 (14-11-2026) : 4 series PASS (declaration owner), product requalifie,

  passage `READY_TO_FREEZE`.

- v1.0 (14-11-2026) : creation du support de preuve Claude (rollback du sample).
