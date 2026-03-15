---
id: GAPC_TOOLING_TPL_01_RELEASE_NOTE_ADDON
type: TOOLING
title: GapcReleaseNoteAddon
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, tpl, addon, release, p0]
depends_on:
  - TPL_10_RELEASE_NOTE
  - GAPC_DISCIPLINE_01_GEL_RULES
  - GAPC_DISCIPLINE_04_RISK_REGISTER
  - GAPC_TOOLING_TPL_02_BETA_EVIDENCE_PACK
  - CONSTRAINT_03_SECRETS_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_01_TPL
---

# GAPC_TOOLING_TPL_01 - Release Note (ADDON)

## Objet

Ajouter des sections **spécifiques GAPC** au template CORE `TPL_10_RELEASE_NOTE`
(sans duplication).
But : rendre un gel/release GAPC **auditable** et **product-ready**.

---

## Sections GAPC à ajouter

### A) Gate Target

- Target: `GAPC_READY_TO_FREEZE | GAPC_FROZEN`
- Scope : `PACKAGE_00_GAPC` (et product workspace si applicable)

### B) Evidence (IDs)

- Evidence Pack : `GAPC_TOOLING_TPL_02_BETA_EVIDENCE_PACK` (ID + lien)
- Artefacts : PRD / CO / Spec / ADR / TestPlan / Review (IDs)

### C) Gates (PASS/FAIL)

- DocQG :
- CodeQG : NA|PASS|FAIL
- RagQG : NA|PASS|FAIL
- GelRules CORE :
- GelRules GAPC :

### D) Risques

- Risques critiques ouverts : NONE | list
- Mitigations + owner :

### E) Backout (obligatoire si FAIL possible)

- Revert plan :
- Notes :

### Règles P0

- Si Target = GAPC_FROZEN → amendements contrôlés + version bump requis.
- KO si secrets/PII apparaissent dans la note.
- KO si gates non renseignés.

## Changelog

- v1.2 (04-03-2026) : correction `scope` + `depends_on` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : création addon Release Note (P0) pour GAPC.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
