---
id: GAPC_TOOLING_EXTENSION_00_ALLOW_LIST
type: TOOLING
title: GapcExtensionAllowlist
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, extension, allowlist, p1]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, DISCIPLINE_06_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_01_GEL_RULES, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, EXTENSION_01_BOLT_NEW_PROTOCOL, EXTENSION_02_MIDJOURNEY_PROTOCOL, EXTENSION_03_KLING_AI_PROTOCOL]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_04_EXTENSION
---

# GAPC_TOOLING_EXTENSION_00 - Allowlist

## Objet
Définir quelles extensions CORE sont **autorisées** dans GAPC, et sous quelles contraintes.

## Autorisées (par défaut)
- BoltNew protocol (codegen) — si diff-first, no auto-commit
- Midjourney protocol (image) — si pas de PII + evidence pack
- KlingAI protocol (video) — si pas de PII + evidence pack

## Interdites (par défaut)
- toute extension non documentée dans CORE/EXTENSION
- tout usage d’assets basés sur personnes réelles sans consentement

## Règles
- Evidence Pack obligatoire (voir `GAPC_EXTENSION_02_EVIDENCE_REQUIREMENTS`)
- Si coût/temps dérive : reclassifier via ScopeClassifier (NOW→NEXT/LATER)

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
