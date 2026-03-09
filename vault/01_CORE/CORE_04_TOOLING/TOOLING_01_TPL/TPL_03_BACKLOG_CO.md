---
id: TPL_03_BACKLOG_CO
type: TOOLING
title: BacklogCoTemplate
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 09-03-2026
tags: [tooling, backlog, composant, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY, CONSTRAINT_03_SECRETS_POLICY]
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_01_TPL
---

# TPL_03 - Backlog Composants (CO) (Composants atomiques) (CORE)

## But
Lister les **CO** (unités de livraison) selon :
- 1 intention = 1 CO
- 1 intention = 1 commit (ou squash)
- priorisation NOW/NEXT/LATER/REJECT

---

## Format (à dupliquer par item)

### CO_XXX — <Titre>
- Arc principal : SYSTEM | CORE | PACKAGE | PRODUCT
- Goal (1 phrase) :
- Inputs / dépendances :
- Output attendu :
- Critère PASS/FAIL :
- Scope : NOW | NEXT | LATER | REJECT
- Priorité : P0 | P1 | P2
- Risque : R1 | R2 | R3
- Next step unique :

---

## Tableau (option)
| CO | Goal | Output | Scope | Prio | Risque | Owner |
|---|---|---|---|---|---|---|
| CO_001 |  |  |  |  |  |  |

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (09-03-2026) : debruitage title pour eviter collision semantique avec `PIPELINE_03_BACKLOG_COMPOSANTS`.
- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation depends_on.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
