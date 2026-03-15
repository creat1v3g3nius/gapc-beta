---
id: GAPC_TOOLING_TPL_03_RAG_SESSION_LOG
type: TOOLING
title: GapcRagSessionLog
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, tpl, addon, rag, log, p1]
depends_on:
  - DISCIPLINE_02_RAG_QG
  - GAPC_DISCIPLINE_02_RAG_QG
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - META_01_OUTPUT_PROTOCOL
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_01_TPL
---

# GAPC_TOOLING_TPL_03 - RAG Session Log

## Objet

Standardiser un log de session mentor RAG (GAPC actif) pour :

- prouver citations/sources,
- prouver `NON TROUVÉ`,
- prouver actifs uniques (pas de mélange).

Ce template sert de **preuve** (pas de procédure). No-secrets/no-PII.

---

## Format (copiable)

```txt
Date:
Workspace:
Active package: PACKAGE_00_GAPC
Active product: <NA|PRODUCT_XX>
Profile: RulesOnly | GAPC+Product

Test / Question ID: T-001
Question:
Expected (si test):
Sources citées (IDs + chemins si dispo):
Answer (résumé):
Verdict:
- OK | KO
Observations:
- (ex: NON TROUVÉ respecté / actif mélangé / sources manquantes)
Next step unique:

---
(repeat)
```

### Règles de verdict (P0)

- KO si : pas de sources, pas de `NON TROUVÉ` quand nécessaire, mélange
  d’actifs, mention de secrets.

## Changelog

- v1.2 (04-03-2026) : correction `scope` + `depends_on` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation
  frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création template log session RAG GAPC (P1).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
