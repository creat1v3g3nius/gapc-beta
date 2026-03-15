---
id: GAPC_DISCIPLINE_04_RISK_REGISTER
type: DISCIPLINE
title: GapcRiskRegister
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, risk, register, rubric, product-ready, no-secrets]
depends_on:
  - DISCIPLINE_07_RISK_REGISTER
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_04_CODE_QG
  - DISCIPLINE_03_DOC_QG
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - TPL_03_BACKLOG_CO
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_02_DISCIPLINE
---

# GAPC_DISCIPLINE_04 - Risk Register

## Objet

Définir la **discipline de risques** spécifique au package **GAPC** :

- même structure/scoring CORE (non modifiable),
- catégories + signaux + risques types “GAPC product-ready”,
- intégration directe avec le cycle CO/gates/gel.

Ce document est une **extension PACKAGE** :

- il **renforce** CORE (catégories + signaux + exigences),
- il ne change pas l’échelle P/I, ni la règle “risque critique”.

CORE → PACKAGE → PRODUCT → SYSTEM.

---

## 1) Règles P0 (non négociables)

Ces règles complètent CORE :

1) **Max 3 risques actifs** (Open/Mitigating) à un instant donné.
2) **Chaque risque a** : mitigation (action), signal (indicateur), owner,
   statut, lien(s).
3) **No-secrets / no-PII** : aucun secret/PII dans le registre. (Guardrails +
   SecretsPolicy).
4) **Couplage CO** : tout risque P0 doit pointer vers **un CO** (Backlog CO) ou
   une ADR si décision structurante.
5) **Risque critique** (score 6–9) : ne peut pas rester Open sans mitigation +
   owner.

---

## 2) Échelles (héritées CORE)

- Probabilité : `P1|P2|P3`
- Impact : `I1|I2|I3`
- Score = `P × I`
- Critique si 6–9 fileciteturn56file8

---

## 3) Catégories GAPC (extension PACKAGE)

Catégories recommandées (tu peux en ajouter, pas en retirer côté CORE) :

### A) Governance / Discipline

- Frontmatter & naming incohérents
- Dérive “procédure vs règle” (SYSTEM vs CORE)
- Contradictions SOT (duplication)

### B) Tooling / Repo / Scripts

- Validator absent/non fiable
- Smoke runner absent/non fiable
- Git policy non appliquée (multi-intentions, commits sales)

### C) Mentor RAG / Corpus

- Invention (pas de `NON TROUVÉ`)
- Mélange multi-package/product
- Corpus trop large (bruit), citations absentes

### D) Delivery

- Dérive scope (trop de P1/P2 en P0)
- Dépendances non tranchées (ADR manquante)

### E) Security

- Secrets/PII dans docs, logs, exemples
- Permissions AnythingLLM non read-only

---

## 4) Signaux (indicateurs) GAPC (P0)

Signaux minimaux à utiliser dans les risques :

- **S1 Frontmatter KO** : validator détecte `updated` manquant / `id!=filename`

  / `scope` incohérent.

- **S2 Duplications** : contradictions entre docs CORE/SYSTEM sur une même

  règle.

- **S3 RAG KO** : le mentor ne cite pas les sources ou n’utilise pas `NON

  TROUVÉ`.

- **S4 Smoke KO** : smoke tests échouent (ou non reproductibles).
- **S5 Secrets risk** : présence de tokens/keys dans diff, docs, logs.
- **S6 Dérive CO** : un CO touche > 1 intention ou > 1 arc sans découpage.

---

## 5) Format canon (à instancier)

Format CORE (à dupliquer):

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
Date revue:
Liens: (CO/ADR/doc/issue/commit)
```

---

## 6) Risques types (catalogue P0/P1)

> Ce catalogue sert à accélérer l’identification. À instancier dans PRODUCT si
  besoin.

### R-0001 — Frontmatter incohérent (SYSTEM/CORE)

- Catégorie : Governance / Discipline
- P : P2 | I : I3 | Score : 6
- Signal : S1
- Mitigation : corriger frontmatter + re-run validator
- Liens : CO + audit

### R-0002 — Mélange multi-package/product (mentor RAG)

- Catégorie : Mentor RAG / Corpus
- P : P2 | I : I3 | Score : 6
- Signal : S3
- Mitigation : réduire corpus (RulesOnly → couche) + actifs uniques

### R-0003 — Secrets/PII dans repo/vault

- Catégorie : Security
- P : P1 | I : I3 | Score : 3
- Signal : S5
- Mitigation : purge + règles no-secrets + hooks/validator

### R-0004 — Validator / smoke runner non fiable

- Catégorie : Tooling / Repo / Scripts
- P : P2 | I : I2 | Score : 4
- Signal : S4
- Mitigation : stabiliser scripts + tests de scripts

### R-0005 — Dérive scope (P0 gonflé)

- Catégorie : Delivery
- P : P2 | I : I2 | Score : 4
- Signal : S6
- Mitigation : reclassifier via ScopeClassifier (NOW/NEXT/LATER/REJECT)

---

## 7) Utilisation (règle)

- Le registre est **mis à jour** :
    - en fin de session (si nouveau signal),
    - avant READY_TO_FREEZE,
    - avant FROZEN.
- Si un risque critique apparaît : créer un **CO P0** dédié.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction du `scope` du frontmatter.
- v1.1 (01-03-2026) : passage en FROZEN (status+version bump) + amendements

  contrôlés + correction références.

- v1.0 (01-03-2026) : version initiale.
