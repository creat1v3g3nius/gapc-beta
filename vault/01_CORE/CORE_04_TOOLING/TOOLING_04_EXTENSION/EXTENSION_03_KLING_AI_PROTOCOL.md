---
id: EXTENSION_03_KLING_AI_PROTOCOL
type: TOOLING
title: KlingAiProtocol
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, protocol, klingai, video, core]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - EXTENSION_04_EVIDENCE_PACK
  - EXTENSION_05_ASSET_NAMING_POLICY
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_04_EXTENSION
---

# EXTENSION_03 - Kling AI Protocol (CORE)

## Objet

Cadrer la génération vidéo via un outil type Kling AI :

- inputs clairs,
- contraintes (PII/droits),
- livrables stables.

---

## 1) Inputs attendus (P0)

- Goal (1 phrase)
- Usage
- Durée / ratio
- Style references
- Must include / Must avoid
- Contraintes PII/consentement
- Variants

## 2) Output attendu (P0)

- Prompt final (copiable)
- Paramètres clés (durée/ratio)
- Livrables (fichiers) + naming
- Next step unique

## 3) Stop conditions (P0)

- PII/visages réels sans consentement
- usage illégal/trompeur
- export non traçable

## 4) Evidence Pack (P0)

Référencer `EXTENSION_04_EVIDENCE_PACK`.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : FROZEN + depends_on minimisé et dédupliqué + corection
  heading.
- v1.1 (01-03-2026) : correction erreurs.
- v1.0 (01-03-2026) : version initiale.
