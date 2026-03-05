---
id: TPL_09_REVIEW_CHECK
type: TOOLING
title: ReviewCheck
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, review-check, quality, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY, DISCIPLINE_03_DOC_QG, DISCIPLINE_04_CODE_QG]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_09 - Review Check (Doc/Code) (CORE)

## But
Cadre de review rapide (binaire) avant merge/gel.

---

## Doc (si doc touché)
- [ ] Frontmatter conforme
- [ ] H1 unique + sections cohérentes
- [ ] Non-duplication (SOT)
- [ ] Sans oral
- [ ] No-secrets/no-PII

## Code (si code touché)
- [ ] Intention atomique
- [ ] Contrôles requis PASS
- [ ] No-secrets/no-PII
- [ ] Traçabilité (ADR si décision)
- [ ] Backout plan possible

## Verdict
- Verdict : OK | KO
- P0 fails :
- Next step unique :

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
