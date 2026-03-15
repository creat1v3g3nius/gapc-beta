---
id: EXTENSION_01_BOLT_NEW_PROTOCOL
type: TOOLING
title: BoltNewProtocol
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, protocol, boltnew, codegen, core]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - EXTENSION_04_EVIDENCE_PACK
  - TPL_07_AI_CODE_PROMPT_MODEL
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_04_EXTENSION
---

# EXTENSION_01 - Bolt.new Protocol (CORE)

## Objet

Cadrer l’usage d’un **app builder / code generator** (type Bolt.new) pour
produire du code sans dérive.

CORE strict : pas de procédure opérateur, pas d’identifiants/secrets.

---

## 1) Inputs attendus (P0)

- Goal (1 phrase)
- Contexte repo (langage, structure)
- Contraintes : diff-first, no auto-commit, 1 intention = 1 commit
- Fichiers touchés (max 5) ou modules ciblés
- Non-goals (explicites)
- Validation attendue (smoke/validator)

## 2) Outputs attendus (P0)

- Patch minimal (diff)
- Explication : quoi/pourquoi/risques (max 5 lignes)
- Backout plan (revert)
- Next step unique

## 3) Stop conditions (P0)

- propose de committer automatiquement
- touche > 5 fichiers sans découpage
- refactor massif non demandé
- introduit secrets/PII ou demande des secrets
- mélange 2 intentions

## 4) Evidence Pack (P0)

Référencer `EXTENSION_04_EVIDENCE_PACK`.

## 5) Extension PACKAGE/PRODUCT

PACKAGE/PRODUCT peuvent ajouter :

- stack autorisée
- tests additionnels
- conventions locales

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : FROZEN + depends_on minimisé et dédupliqué + corection
  heading.
- v1.1 (01-03-2026) : correction erreurs.
- v1.0 (01-03-2026) : version initiale.
