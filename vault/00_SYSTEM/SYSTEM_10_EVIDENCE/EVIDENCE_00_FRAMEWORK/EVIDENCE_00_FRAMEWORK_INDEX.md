---
id: EVIDENCE_00_FRAMEWORK_INDEX
type: EVIDENCE
title: FrameworkEvidenceIndex
version: v1.0
status: FROZEN
created: 13-03-2026
updated: 13-03-2026
tags: [system, evidence, framework, index]
depends_on: [EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION, EVIDENCE_02_REVIEW_FRAMEWORK, EVIDENCE_03_RISK_REGISTER, EVIDENCE_04_ADR_FRAMEWORK_SCOPE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_00_FRAMEWORK
---

# EVIDENCE_00 - Framework Evidence Index

## Objet
- regrouper les preuves framework canoniques du lot `SYSTEM_10_EVIDENCE`
- fournir un point d entree stable pour la chaine de preuves framework
- separer explicitement les preuves framework des preuves agents

## Contenu
- `EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION`
- `EVIDENCE_02_REVIEW_FRAMEWORK`
- `EVIDENCE_03_RISK_REGISTER`
- `EVIDENCE_04_ADR_FRAMEWORK_SCOPE`

## Regle d usage
- utiliser ce sous-lot pour les preuves framework globales
- utiliser `EVIDENCE_01_AGENTS` pour les preuves de qualification agents
- conserver les references par ID, pas par chemin

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.0 (13-03-2026) : creation du sous-lot `EVIDENCE_00_FRAMEWORK` et indexation des preuves framework.
