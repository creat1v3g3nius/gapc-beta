---
id: STUDIO_CONSTRAINT_04_EXCEPTION_POLICY
type: CONSTRAINT
title: StudioExceptionPolicy
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, constraint, exception]
depends_on: 
  - CONSTRAINT_04_DECISION_TRACEABILITY_POLICY
  - TPL_02_ADR_LITE
  - STUDIO_CONSTRAINT_00_ALLOW_LIST
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_03_CONSTRAINT
---

# STUDIO_CONSTRAINT_04 - Exception Policy

## Objet

Encadrer les derogations aux contraintes du package studio.

## Regle

Une exception est valable seulement si elle est :

- tracee en ADR-lite (`TPL_02_ADR_LITE`) dans le projet concerne,
- bornee : un projet, une duree ou un livrable,
- justifiee : objectif et alternative ecartee,
- portee par un owner (role).

Aucune exception possible sur les invariants CORE : no-secrets / no-PII,
actifs uniques, `NON TROUVE`, hierarchie d autorite.

## Changelog

- v1.0 (14-11-2026) : creation de la politique d exception studio.
