---
id: EXTENSION_02_MIDJOURNEY_PROTOCOL
type: TOOLING
title: MidjourneyProtocol
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, protocol, midjourney, image, core]
depends_on:
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - EXTENSION_04_EVIDENCE_PACK
  - EXTENSION_05_ASSET_NAMING_POLICY
  - TPL_08_AI_IMAGE_PROMPT_MODEL
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_04_EXTENSION
---

# EXTENSION_02 - Midjourney Protocol (CORE)

## Objet

Cadrer la génération d’images via un outil type Midjourney :

- prompts propres,
- contraintes droits/PII,
- livrables versionnés.

---

## 1) Inputs attendus (P0)

- Goal (1 phrase)
- Usage (où l’image sera utilisée)
- Style references (si existantes)
- Format + dimensions
- Must include / Must avoid
- Variants (nb)
- Contraintes PII/consentement

## 2) Output attendu (P0)

- Prompt final (copiable)
- Variantes (si demandé)
- Livrables : fichiers + naming (voir Asset Naming Policy)
- Next step unique

## 3) Stop conditions (P0)

- visage/personne réelle sans consentement
- demande trompeuse non signalée
- contenu sensible non autorisé (selon package/product)

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
