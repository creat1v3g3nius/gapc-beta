---
id: EXTENSION_04_EVIDENCE_PACK
type: TOOLING
title: EvidencePack
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, extension, evidence, traceability, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_04_EXTENSION
---

# EXTENSION_04 - Evidence Pack (CORE)

## Objet

Standardiser la **preuve minimale** d’une production via une extension (outil
externe), pour traçabilité et reproductibilité.

CORE strict : pas de secrets, pas de données perso.

---

## Format (copiable)

```txt
Tool:
Protocol ID:
Date:
Active package:
Active product:
Goal:
Inputs summary:
Prompt(s) final(s):
Key params:
Outputs produced (filenames):
Storage location (path):
Checks (PII/rights/no-secrets):
Notes:
Next step:
```

Règle : sans evidence pack, un asset ne peut pas être déclaré “livrable final”.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : FROZEN + depends_on minimisé et dédupliqué + corection

  heading.

- v1.1 (01-03-2026) : correction erreurs.
- v1.0 (01-03-2026) : version initiale.
