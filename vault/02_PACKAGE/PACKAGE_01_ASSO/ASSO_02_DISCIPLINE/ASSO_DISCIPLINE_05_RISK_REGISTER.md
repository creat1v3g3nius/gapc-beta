---
id: ASSO_DISCIPLINE_05_RISK_REGISTER
type: DISCIPLINE
title: AssoRiskRegister
version: v1.3
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, asso, discipline, risk, p0]
depends_on:
  - DISCIPLINE_07_RISK_REGISTER
  - ASSO_CONSTRAINT_01_LEGAL_BASELINE_1901
  - ASSO_CONSTRAINT_02_PUBLIC_MESSAGING_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_02_DISCIPLINE
---

# ASSO_DISCIPLINE_05 - Risk Register

## Règles P0

- mitigation + signal + owner + statut + liens
- risque critique (6–9) jamais Open sans mitigation+owner
- no-secrets/no-PII

## Catégories

Legal · Gouvernance · Réputation · Data/Privacy · Delivery

## Format

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
Statut:
Date revue:
Liens:
```

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.3 (04-03-2026) : correction `scope` du frontmatter.
- v1.2 (01-03-2026) : passage en FROZEN v1.2 + correction depends_on.
- v1.1 (01-03-2026) : passage en FROZEN + normalisation ids/depends_on.
- v1.0 (01-03-2026) : registre risques ASSO.
