---
id: EVIDENCE_05_ADR_CLAUDE_AGENT
type: EVIDENCE
title: AdrClaudeAgent
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [system, evidence, adr, llm, agent, claude]
depends_on:
  - TPL_02_ADR_LITE
  - CONSTRAINT_04_DECISION_TRACEABILITY_POLICY
  - META_00_HANDBOOK
  - LLM_00_RAG_PRINCIPES
  - SCRIPT_03_INSTRUCTIONS_CODEX
  - SCRIPT_07_INSTRUCTIONS_CLAUDE
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_00_FRAMEWORK
---

# EVIDENCE_05 - ADR Claude Agent

## Statut

- Status: ACCEPTED
- Date: 14-11-2026
- Owner: framework-owner
- Liens: `LLM_00_RAG_PRINCIPES`, `SCRIPT_03_INSTRUCTIONS_CODEX`,
  `SCRIPT_07_INSTRUCTIONS_CLAUDE`

## Contexte

- Le dispositif nominal repose sur 3 outils : AnythingLLM local (mentor

  documentaire read-only), Codex (code / patch / execution), API externe
  (fallback).

- Le owner decide d utiliser **Claude dans VS Code (Claude Code)** comme agent

  LLM unique.

- Claude Code lit l ensemble du repo et peut modifier les fichiers : l isolation

  par ingestion de corpus ne s applique plus.

- Claude est un service cloud : tout contenu lu par l agent sort du poste.

## Options

### Option A - Claude remplace mentor et executant (2 modes)

- Description : un seul agent, mode `MENTOR` (read-only) ou `EXECUTION`

  (diff-first), fixe en debut de session.

- Pros : un seul outil, un seul jeu d instructions, contexte complet.
- Cons : la separation des roles devient une discipline de session et non une

  separation d outils.

- Risques : derive mentor -> execution ; envoi de donnees client au cloud.

### Option B - Claude remplace le mentor seulement

- Pros : separation d outils conservee.
- Cons : deux agents a maintenir.

### Option C - Claude remplace Codex seulement

- Pros : mentor local conserve (pas de sortie cloud pour la lecture).
- Cons : deux agents a maintenir, AnythingLLM toujours requis.

## Decision

- **Option A retenue.**
- Mode `MENTOR` : lecture seule (Plan mode de Claude Code), reponse sourcee,

  `NON TROUVE`, format `META_01_OUTPUT_PROTOCOL`.

- Mode `EXECUTION` : diff-first, aucun commit ni push sans accord explicite,

  branche `work/*`, controles avant commit.

- L isolation des actifs passe par la declaration de session (package /

  product actifs) et l interdiction de lire un autre package ou product.

- SOT procedurale : `SCRIPT_07_INSTRUCTIONS_CLAUDE`. Projection executable :

  `CLAUDE.md` a la racine du repo.

- Les documents AnythingLLM (`LLM_00..03`, preuves `WS_00/01/02`) et

  `SCRIPT_03_INSTRUCTIONS_CODEX` passent `DEPRECATED` et sont archives en
  `99_CACHE`.

## Consequences

- Positives : un agent unique, instructions chargees a chaque session.
- Negatives : chantier de realignement (CORE, SYSTEM, PACKAGE, PRODUCT sample).
- Dette creee : la notion `API externe fallback` disparait du mode nominal ;

  le CORE doit etre realigne (`META_00`, `META_01`, `META_02`).

- Confidentialite : seuls des documents texte pseudonymises entrent dans le

  repo ; aucun fichier client brut n est lu par l agent.

- Backout plan : revert du lot ; les documents archives restent restaurables

  depuis `99_CACHE`.

## Mise en oeuvre (lots)

1. ADR + `SCRIPT_07_INSTRUCTIONS_CLAUDE` + `CLAUDE.md`.
1. CORE : `META_00`, `META_01`, `META_02` (roles et format).
1. SYSTEM : nouveaux `LLM_*` Claude, `WORKFLOW_07/08`, workflows de session,

   archivage `LLM_00..03` et `SCRIPT_03`.

1. PACKAGE : `PACKAGE_00_GAPC`, `PACKAGE_02_STUDIO` (profils RAG, allowlists,

   confidentialite).

1. PRODUCT : realignement ou archivage des preuves AnythingLLM du sample.

## Changelog

- v1.0 (14-11-2026) : decision Claude Code agent unique en 2 modes.
