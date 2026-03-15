---
id: GAPC_TOOLING_PIPELINE_00_PACKAGE
type: TOOLING
title: GapcPipelinePackage
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, pipeline, product-ready]
depends_on:
  - PIPELINE_00_PRODUCT
  - PIPELINE_01_RUNBOOK_PRODUCT
  - PIPELINE_02_BACKLOG_PRODUCT
  - PIPELINE_03_BACKLOG_COMPOSANTS
  - PIPELINE_04_OPTIMIZATION_PROTOCOL
  - PIPELINE_05_RELEASE_FREEZE
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_03_DOC_QG
  - DISCIPLINE_04_CODE_QG
  - DISCIPLINE_02_RAG_QG
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - DISCIPLINE_07_RISK_REGISTER
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_04_RISK_REGISTER
  - GAPC_DISCIPLINE_01_GEL_RULES
  - GAPC_INDEX_04_TOOLING
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_02_PIPELINE
---

# GAPC_TOOLING_PIPELINE_00 - Pipeline Package

## Objet

Définir **comment le package GAPC s’applique** aux pipelines CORE, sans créer de
procédures “beta” dans le PACKAGE.

- CORE fournit : phases, gates, gel générique.
- GAPC ajoute : priorisation (ScopeClassifier GAPC), risques/signaux GAPC,
  critères de gel GAPC.
- PRODUCT (workspace) contient : preuves, DoD, cycles réels.

---

## 1) Entrées / sorties

### Entrées

- Package actif : `PACKAGE_00_GAPC`
- Un besoin (PRD) ou une demande d’amélioration
- Product actif (optionnel) : `PRODUCT_XX`

### Sorties

- Backlog CO atomiques (NOW/NEXT/LATER/REJECT)
- Risques GAPC (mitigation + owner)
- États de gel GAPC : `GAPC_READY_TO_FREEZE` puis `GAPC_FROZEN`

---

## 2) Mapping “Pipeline CORE” → “Extension GAPC”

### Phase A — Cadrage

Ajouts GAPC :

- classer les items via **GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER**
- si conformité SYSTEM+CORE P0 (frontmatter/scope/no-secrets) → NOW, P0

### Phase B — Découpage (Backlog)

Ajouts GAPC :

- CO atomiques (1 intention)
- > 3 items → backlog CO obligatoire

### Phase C — Spec / Décisions

Ajouts GAPC :

- ADR-lite si décision structurante
- mise à jour risques si nouveaux signaux

### Phase D — Exécution

Ajouts GAPC :

- guardrails : no-secrets, non-duplication, actifs uniques
- review minimale avant gel

### Phase E — Gel / Release

Ajouts GAPC :

- appliquer `GAPC_DISCIPLINE_02_GELRULES` (package)
- release note et preuves dans PRODUCT (workspace)

---

## 3) Critères “product-ready” GAPC (P0)

- gates applicables (Doc/Code/RAG) = PASS
- risques critiques mitigés (score 6–9)
- no-secrets confirmé
- traçabilité (ADR-lite)
- découpage : 1 intention = 1 CO

---

## 4) Anti-dérive (P0)

- pas de DoD beta dans PACKAGE (=> PRODUCT)
- pas de listes vagues >3 items
- contradiction : CORE prévaut, sinon `NON TROUVÉ` + action

---

## Changelog

- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation
  frontmatter/id/depends_on.
- v1.0 (01-03-2026) : création pipeline PACKAGE GAPC (pont CORE→GAPC, P0).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
