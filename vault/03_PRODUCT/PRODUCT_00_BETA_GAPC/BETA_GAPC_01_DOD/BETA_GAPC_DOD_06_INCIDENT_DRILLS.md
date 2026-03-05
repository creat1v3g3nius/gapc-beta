---
id: BETA_GAPC_DOD_06_INCIDENT_DRILLS
type: DOD
title: GapcBetaIncidentDrills
version: v1.0
status: READY_TO_FREEZE
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, incident, p2]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOCQG, DISCIPLINE_04_CODEQG, DISCIPLINE_02_RAGQG, DISCIPLINE_01_GELRULES, CONSTRAINT_00_GUARDRAILS, CONSTRAINT_03_SECRETSPOLICY, CONSTRAINT_01_RAGSCOPEPOLICY, TPL_00_PRDONEPAGER, TPL_01_SPECTECH, TPL_02_ADRLITE, TPL_03_BACKLOGCO, TPL_04_TESTPLANSMOKE, TPL_05_ACTIONDOC, TPL_06_ACTIONCODE, TPL_09_REVIEWCHECK, TPL_10_RELEASENOTE, CHECKLIST_05_INCIDENT]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_01_DOD
---

# GAPCBETA DoD — 06 Incident Drills (P2 minimal) — v1.0

- Drill 1 : frontmatter KO → stop + correction + re-validate.
- Drill 2 : smoke KO → backout + risk update + re-run.
- Drill 3 : RAG mélange → isolation actifs + retest.

## Changelog
- v1.0 (01-03-2026) : DoD drills minimal.
