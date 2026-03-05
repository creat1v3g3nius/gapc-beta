---
id: TPL_08_AI_IMAGE_PROMPT_MODEL
type: TOOLING
title: ImageGeneratorGenericModel
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, image-generator, prompt, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_08 - Image Generator Generic Model (agent) (CORE)

## But
Cadrer une demande de génération/édition d’image :
- objectif clair
- contraintes droits/PII
- format livrable

---

## Input
```txt
Goal (1 phrase):
Usage (où l’image sera utilisée):
Style references (si existantes):
Format + dimensions:
Must include:
Must avoid:
PII/consent constraints:
Number of variants:
```

## Output attendu
- prompt final (copiable)
- variantes (si demandé)
- checklist “vérifs” (droits/PII/cohérence)
- next step unique

## Stop conditions
- PII/visages réels sans consentement
- demande trompeuse non signalée

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
