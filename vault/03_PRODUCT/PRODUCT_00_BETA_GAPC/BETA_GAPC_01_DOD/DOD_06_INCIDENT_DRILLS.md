---
id: DOD_06_INCIDENT_DRILLS
type: DOD
title: GapcBetaIncidentDrills
version: v1.0
status: DEPRECATED
created: 01-03-2026
updated: 01-03-2026
tags: [product, gapcbeta, dod, incident, p2]
depends_on: [PIPELINE_00_PRODUCT, PIPELINE_05_RELEASE_FREEZE, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG, DISCIPLINE_02_RAG_QG, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_01_RAG_SCOPE_POLICY, TPL_00_PROD_ONE_PAGER, TPL_01_SPEC_TECH, TPL_02_ADR_LITE, TPL_03_BACKLOG_CO, TPL_04_TEST_PLAN_SMOKE, TPL_05_ACTION_DOC, TPL_06_ACTION_CODE, TPL_09_REVIEW_CHECK, TPL_10_RELEASE_NOTE, CHECKLIST_05_INCIDENT]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_01_DOD
---

# GAPCBETA DoD — 06 Incident Drills (P2 minimal) — v1.0

- Drill 1 : frontmatter KO → stop + correction + re-validate.
- Drill 2 : smoke KO → backout + risk update + re-run.
- Drill 3 : RAG mélange → isolation actifs + retest.

## Changelog
- v1.0 (01-03-2026) : DoD drills minimal.
