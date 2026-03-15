---
id: CHECKLIST_01_START_SESSION
type: TOOLING
title: StartSession
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, checklist, session, start, core]
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
  - META_02_SOP_STANDARD_LOOP
  - CONSTRAINT_01_RAG_SCOPE_POLICY
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_03_CHECKLIST
---

# CHECKLIST_01 - Start Session Checklist (CORE)

## Objet

Démarrer une session de production **sans dérive**.

- [ ] Actifs fixés : 1 package (ou NA), 1 product (si applicable)
- [ ] Intention fixée : 1 CO / 1 livrable principal
- [ ] Sources fixées : corpus/scopes cohérents (pas “all vault”)
- [ ] Contraintes rappelées : no-secrets, actifs uniques, NON TROUVÉ,
      non-duplication
- [ ] Gate cible connue : DRAFT → READY_TO_FREEZE (ou autre)
- [ ] Next step unique défini (action immédiate)

## Output attendu

- CO actif + livrable attendu (ID)

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
