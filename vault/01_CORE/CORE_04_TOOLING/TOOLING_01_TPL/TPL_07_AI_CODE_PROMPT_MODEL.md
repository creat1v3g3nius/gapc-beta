---
id: TPL_07_AI_CODE_PROMPT_MODEL
type: TOOLING
title: CodeGeneratorGenericModel
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, code-generator, prompt, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_04_CODE_QG]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_07 - Code Generator Generic Model (agent) (CORE)

## But
Cadrer une demande de génération de code (agent/LLM) en mode **diff-first**.

---

## Input
```txt
Goal:
Repo context:
Constraints: diff-first, no auto-commit, no secrets, 1 intention = 1 commit
Active package:
Active product:
Files to touch (max 5):
Non-goals:
Expected output:
Validation required (smoke/validator):
```

## Output attendu
1) Plan d’exécution (3–10 étapes)
2) Patch minimal (diff)
3) Tests/validations
4) Commit message proposé
5) Risques + backout
6) Next step unique

## Stop conditions
- > 5 fichiers sans découpage
- secrets/PII
- refactor massif non demandé
- multi-intentions

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
