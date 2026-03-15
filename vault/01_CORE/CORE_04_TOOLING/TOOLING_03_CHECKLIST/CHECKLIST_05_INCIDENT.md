---
id: CHECKLIST_05_INCIDENT
type: TOOLING
title: Incident
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, checklist, incident, core]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_03_DOC_QG
  - DISCIPLINE_04_CODE_QG
  - DISCIPLINE_02_RAG_QG
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - DISCIPLINE_07_RISK_REGISTER
  - PIPELINE_00_PRODUCT
  - PIPELINE_01_RUNBOOK_PRODUCT
  - PIPELINE_05_RELEASE_FREEZE
  - TPL_05_ACTION_DOC
  - TPL_06_ACTION_CODE
  - TPL_09_REVIEW_CHECK
  - TPL_10_RELEASE_NOTE
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_03_CHECKLIST
---

# CHECKLIST_05 - Incident Checklist (CORE)

## Objet

Réagir à une dérive / incohérence / fuite / mélange d’actifs.

- [ ] STOP : ne pas continuer la production
- [ ] Identifier la cause (1 phrase)
- [ ] Isoler : 1 package / 1 product / réduire le corpus
- [ ] No-secrets : vérifier qu’aucune fuite n’a eu lieu
- [ ] Tracer un risque + mitigation + owner (Risk Register)
- [ ] Reprendre uniquement après correction
- [ ] Next step unique

## Output attendu

- Incident clôturé ou plan correctif clair

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
