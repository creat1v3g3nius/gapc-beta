---
id: DISCIPLINE_07_RISK_REGISTER
type: DISCIPLINE
title: RiskRegister
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [governance, risk-register, llm, discipline, core]
depends_on: [DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG, DISCIPLINE_06_SCOPE_CLASSIFIER, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_07 - Risk Register (règles transversales)

Invariants transversaux de gestion des risques : structure, scoring, no-secrets,
traçabilité, extension.
CORE strict : aucune routine opérateur.

---

## 1) Invariants CORE (P0)

- no-secrets/no-PII
- traçabilité (lien vers artefact)
- structure minimale : id, titre, description, catégorie, P, I, score,
  mitigation, signal, owner, statut
- score = P×I, critique si 6–9
- un risque critique ne reste pas ouvert sans mitigation + owner

---

## 2) Extensions PACKAGE/PRODUCT

Peuvent ajouter catégories/signaux/seuils plus stricts.
Interdit : modifier l’échelle P/I ou supprimer mitigation+signal.

---

## 3) Format canon

```txt
RISK_ID: R-0001
Titre:
Catégorie:
Description:
P: P1|P2|P3
I: I1|I2|I3
Score: PxI
Mitigation:
Signal:
Owner:
Statut: Open|Mitigating|Closed
Liens:
```

---

### Changelog

- v1.1 (01-03-2026) : normalisation frontmatter + statut READY_TO_FREEZE + CORE
  strict.
- v1.0 (01-03-2026) : version initiale.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : corrections frontmatter + heading.
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
