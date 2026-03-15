---
id: GAPC_TOOLING_TPL_00_BACKLOG_CO_ADDON
type: TOOLING
title: GapcBacklogCoAddon
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, tpl, addon, backlog, p0]
depends_on:
  - TPL_03_BACKLOG_CO
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_04_RISK_REGISTER
  - GAPC_DISCIPLINE_01_GEL_RULES
  - CONSTRAINT_00_GUARD_RAILS
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_01_TPL
---

# GAPC_TOOLING_TPL_00 - Backlog Composant (Co) (ADDON)

## Objet

Ajouter des champs **spécifiques GAPC** au template CORE `TPL_03_BACKLOG_CO`
(sans duplication).
But : rendre les CO immédiatement **product-ready** dans GAPC :

- priorisation NOW/NEXT/LATER/REJECT (scope classifier GAPC)
- signaux/risques GAPC
- cible de gel GAPC

---

## À ajouter dans chaque CO (champs GAPC)

```txt
GAPC_Scope: NOW|NEXT|LATER|REJECT
GAPC_Value: V1|V2|V3
GAPC_Signal: S1|S2|S3|S4|S5|S6
GAPC_RiskID: R-XXXX | NONE
GAPC_GateTarget: GAPC_READY_TO_FREEZE | GAPC_FROZEN | NA
GAPC_Evidence: (IDs attendus + lien evidence pack si applicable)
```

### Règles P0

- `GAPC_Scope` obligatoire (si doute → NEXT)
- si `GAPC_RiskID` critique (score 6–9) → mitigation + owner obligatoires (dans

  Risk Register)

- si `GAPC_GateTarget` ≠ NA → evidence pack GAPC requis

---

## Exemple (extrait)

```txt
CO_012 — Stabiliser frontmatter SYSTEM (updated/id/scope)
GAPC_Scope: NOW
GAPC_Value: V2
GAPC_Signal: S1
GAPC_RiskID: R-0001
GAPC_GateTarget: GAPC_READY_TO_FREEZE
GAPC_Evidence: GAPC_TPL_00_BETA_EVIDENCEPACK (rempli)
```

## Changelog

- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation

  frontmatter/id/depends_on.

- v1.0 (01-03-2026) : création addon Backlog CO (P0) pour GAPC.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
