---
id: GAPC_TOOLING_EXTENSION_02_EVIDENCE_REQUIREMENTS
type: TOOLING
title: GapcEvidenceRequirements
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 06-03-2026
tags: [package, gapc, tooling, extension, evidence, p1]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, DISCIPLINE_06_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_01_GEL_RULES, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, EXTENSION_04_EVIDENCE_PACK, GAPC_TOOLING_TPL_02_BETA_EVIDENCE_PACK]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_04_EXTENSION
---

# GAPC_TOOLING_EXTENSION_02 - Evidence Requirements

## Objet
Renforcer les exigences de preuve quand une extension est utilisée dans une production GAPC.

## Exigences (P0)
- evidence pack (CORE) rempli : `EXTENSION_04_EVIDENCE_PACK`
- evidence pack GAPC (si objectif = GAPC_READY/FROZEN) : `GAPC_TOOLING_TPL_02_BETA_EVIDENCE_PACK`
- outputs listés : noms de fichiers + emplacement (path)
- check no-secrets/no-PII validé
- lien vers le CO responsable (Backlog CO)

## KO si
- asset livré sans evidence
- sources/prompt non tracés
- PII / secrets présents

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (06-03-2026) : alignement `id==filename` et heading.
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 : READY_TO_FREEZE.
