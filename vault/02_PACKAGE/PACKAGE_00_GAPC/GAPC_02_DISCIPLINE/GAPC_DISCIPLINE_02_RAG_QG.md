---
id: GAPC_DISCIPLINE_02_RAG_QG
type: DISCIPLINE
title: GapcRagQualityGates
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, discipline, rag, quality-gates, product-ready, no-secrets]
depends_on:
  - DISCIPLINE_02_RAG_QG
  - DISCIPLINE_01_GEL_RULES
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_00_GUARD_RAILS
  - GAPC_DISCIPLINE_00_RAG_PROFILE
  - GAPC_DISCIPLINE_04_RISK_REGISTER
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_02_DISCIPLINE
---

# GAPC_DISCIPLINE_02 - RAG Quality Gates

## Objet

Définir des **gates RAG** spécifiques à GAPC (extension PACKAGE) :

- **GAPC_RAG_READY_TO_FREEZE**
- **GAPC_RAG_FROZEN**

Ces gates **renforcent** les gates CORE (`DISCIPLINE_02_RAG_QG`) et ne les
remplacent pas.

CORE strict : aucune procédure opérateur ici (tests concrets en SYSTEM/LLM).

---

## 1) Pré-requis

Les critères CORE de `RAG_READY_TO_FREEZE` doivent être PASS (NON TROUVÉ,
sources, actifs uniques, no-secrets).

---

## 2) Gate GAPC_RAG_READY_TO_FREEZE — PASS/FAIL (P0)

PASS si :

### 2.1 GAPC-only sources (P0)

- Les réponses ne citent **que** CORE + PACKAGE_00_GAPC + PRODUCT actif (si
  applicable) + SYSTEM,
- aucun contenu d’un autre package n’est utilisé comme source “active”.

### 2.2 Alignement discipline GAPC (P0)

Quand une question touche :

- **priorisation** → le mentor renvoie à `GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER`,
- **risques** → renvoie à `GAPC_DISCIPLINE_04_RISK_REGISTER`,
- **gel** → renvoie à `GAPC_DISCIPLINE_01_GEL_RULES`.

### 2.3 Anti-derives (P0)

- Si > 3 items proposés : le mentor propose un Backlog CO (CO atomiques) plutôt
  qu’une liste vague.
- Si incertitude : classer NEXT plutôt que NOW.

### 2.4 Traçabilité (P0)

- Toute recommandation structurante propose une ADR-lite (pas de décision
  implicite).

FAIL si l’un des critères P0 échoue.

---

## 3) Gate GAPC_RAG_FROZEN — PASS/FAIL (P0)

GAPC_RAG_FROZEN = GAPC_RAG_READY_TO_FREEZE PASS + :

### 3.1 Stabilité du profil (P0)

- Le profil GAPC utilisé (GAPC_R0/R1/R2) est explicite et stable.

### 3.2 Zéro risque critique RAG ouvert (P0)

- Aucun risque critique “RAG” GAPC (score 6–9) n’est Open sans mitigation +
  owner (`GAPC_DISCIPLINE_04_RISK_REGISTER`).

### 3.3 Amendements contrôlés (P0)

- Toute modification des règles GAPC RAG passe par patch + validation + bump
  version (mécanisme défini par gel GAPC).

---

## 4) Sortie d’audit (format)

```txt
Target: GAPC_RAG_READY_TO_FREEZE | GAPC_RAG_FROZEN
Verdict: OK | KO
P0 fails:
Evidence: (IDs cités + exemples de réponses)
Next step unique:
```

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : corrections chemins + `scope` du frontmatter.
- v1.1 (01-03-2026) : passage en FROZEN (status+version bump) + amendements
  contrôlés + correction références.
- v1.0 (01-03-2026) : création gates RAG GAPC (renforcement CORE) : GAPC-only
  sources + alignement discipline + anti-derives + traçabilité.
