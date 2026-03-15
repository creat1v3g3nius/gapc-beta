---
id: GAPC_DISCIPLINE_01_GEL_RULES
type: DISCIPLINE
title: GapcGelRules
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, discipline, freeze, ready-to-freeze, frozen, product-ready, no-secrets]
depends_on:
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_03_DOC_QG
  - DISCIPLINE_04_CODE_QG
  - DISCIPLINE_02_RAG_QG
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - DISCIPLINE_07_RISK_REGISTER
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - PIPELINE_00_PRODUCT
  - PIPELINE_05_RELEASE_FREEZE
  - TPL_10_RELEASE_NOTE
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_02_DISCIPLINE
---

# GAPC_DISCIPLINE_01 - Gel Rules (P0)

## Objet

Définir des règles de gel **spécifiques au package GAPC** :

- **GAPC_READY_TO_FREEZE** : package GAPC prêt à être utilisé pour produire un

  premier product (beta “product-ready”)

- **GAPC_FROZEN** : package GAPC gelé (amendements contrôlés)

Ce document est une **extension PACKAGE** :

- il **ne contredit pas** CORE (GelRules/QG/Guardrails/RiskRegister),
- il précise **ce qui est “suffisant”** pour considérer GAPC prêt et stable.

---

## 1) Définitions (extension PACKAGE)

- **CORE gel** : définitions READY_TO_FREEZE / FROZEN (référence

  `DISCIPLINE_01_GEL_RULES`).

- **GAPC_READY_TO_FREEZE** : READY_TO_FREEZE + conditions minimales GAPC (§2).
- **GAPC_FROZEN** : FROZEN + conditions minimales GAPC (§3).
- **Artefacts GAPC** : docs + tooling

  (TPL/PIPELINE/CHECKLIST/EXTENSION/KNOWLEDGE) nécessaires au cycle product.

Règle : en cas de contradiction, **CORE prévaut**.

---

## 2) Gate GAPC_READY_TO_FREEZE (P0) — PASS/FAIL

PASS si **tous** les critères P0 ci-dessous sont vrais.

## 2.1 Conformité SYSTEM+CORE (P0)

- Tous les documents SYSTEM+CORE nécessaires au cycle sont conformes

  (frontmatter, scope, no-secrets).

- Les règles “sans oral” sont respectées (SYSTEM = procédures, CORE = règles).

> Référence de contrôle : DocQG/DocCompliance (CORE).

## 2.2 Set TOOLING minimal disponible (P0)

Le package peut exécuter un cycle product car les familles TOOLING suivantes
sont présentes et utilisables :

- **TPL** : PRD / Spec / ADR-lite / Backlog CO / TestPlan Smoke +

  ActionDoc/ActionCode

- **PIPELINE** : product pipeline + freeze/release
- **CHECKLIST** : start/end session + ready_to_freeze + incident
- **EXTENSION** : protocoles + evidence pack (si usage média/codegen)
- **KNOWLEDGE** : index + listes P0

## 2.3 Cycle réel minimal (P0)

Il existe **au moins 1 exemple réel** (dans un PRODUCT sandbox ou fictif)
démontrant :

- PRD → CO → Spec/ADR → Action Doc/Code → TestPlan → (review) → note de release

  (si gel)

Règle : l’exemple doit être traçable (IDs + liens) et sans secrets.

## 2.4 Mentor RAG (conditionnel, P0)

Si le mentor RAG est utilisé :

- règles `NON TROUVÉ`, sources obligatoires, actifs uniques, no-secrets

  respectées (RagQG).

Si mentor non utilisé : NA.

## 2.5 Risques critiques (P0)

- Aucun risque critique (score 6–9) lié à GAPC n’est **Open** sans mitigation +

  owner.

---

## 3) Gate GAPC_FROZEN (P0) — PASS/FAIL

GAPC_FROZEN = GAPC_READY_TO_FREEZE PASS + critères ci-dessous.

## 3.1 Amendements contrôlés (P0)

- Toute modification du package GAPC passe par patch ciblé + validation + bump

  version si substantiel.

- Changelog tenu sur les fichiers “structurants” (si applicable).

## 3.2 Reproductibilité (P0)

- Le cycle minimal (§2.3) est **repassable** (mêmes étapes, mêmes gates

  applicables).

- Les procédures SYSTEM associées existent et sont stables.

## 3.3 Zéro P0 ouvert (P0)

- Aucun P0 KO (DocQG/CodeQG/RagQG/GelRules/Guardrails) sur le périmètre GAPC

  gelé.

---

## 4) Format de rapport (audit de gel GAPC)

```txt
Target: GAPC_READY_TO_FREEZE | GAPC_FROZEN
Verdict: OK | KO
P0 fails:
Evidence:

- artefacts (IDs):
- gates (Doc/Code/RAG):
- risques critiques:

Next step unique:
```

---

## 5) Notes d’usage (anti-dérive)

- Les critères “métier” (asso, financeurs, légal) ne vivent pas ici : ils vivent

  dans un PACKAGE dédié.

- Si un critère implique une décision structurante → ADR-lite.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (01-03-2026) : passage en FROZEN (status+version bump) + amendements

  contrôlés + correction références.

- v1.0 (01-03-2026) : version initiale.
