---
id: SETUP_PRODUCT_07_GOVERNANCE_RULES
type: SETUP_PRODUCT
title: SetupProductGovernanceRules
version: v1.4
status: FROZEN
created: 13-03-2026
updated: 15-03-2026
tags: [system, multi-product, governance, rules]
depends_on:
  - SETUP_PRODUCT_00_INDEX
  - SETUP_PRODUCT_01_BOOTSTRAP
  - SETUP_PRODUCT_05_LIFECYCLE_POLICY
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_03_SECRETS_POLICY
  - WORKFLOW_03_START_SESSION
  - WORKFLOW_04_END_SESSION
  - WORKFLOW_05_INCIDENT
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT
---

# SETUP_PRODUCT_07 - Governance Rules

## Objet

Definir la gouvernance de products multiples dans le repo.

## Frontiere avec `WORKFLOW`

- ce document definit **les obligations de gouvernance**.
- il ne donne pas les commandes ni le protocole de session.
- l application quotidienne des obligations de gouvernance passe par

  `WORKFLOW_03_START_SESSION`, `WORKFLOW_04_END_SESSION` et
  `WORKFLOW_05_INCIDENT`.

## Regles de base

- un package actif
- un product actif
- owner explicite
- isolation obligatoire d un autre product
- aucune chaine de preuve mixte entre products

## Compatibilite

- un product gele doit tracer les versions de `CORE`, `SYSTEM` et `PACKAGE` sur
  lesquelles il repose

## Regle de verite

- `PRODUCT` n est pas source de verite durable des regles
- `PRODUCT` est source de verite locale des preuves tant qu il est actif

## Regle d impact du changement

- toute modification de `CORE`, `SYSTEM` ou `PACKAGE` qui affecte un product

  actif impose une revalidation

- toute modification locale stable dans `PRODUCT` appelle une decision de
  merge-out

## Obligations operatoires derivees

- tout changement de perimetre actif doit etre explicite des l ouverture de
  session
- toute chaine de preuve mixte ou ambiguite de perimetre declenche un

  traitement via `WORKFLOW_05_INCIDENT`

- toute cloture de session doit laisser un next step unique et un etat de
  product explicite

## Next step unique

- valider cette couche de composition avant d ouvrir un nouveau product hors
  sample.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.4 (15-03-2026) : passage en FROZEN des regles de gouvernance
  `SETUP_PRODUCT`.
- v1.3 (13-03-2026) : rehoste le protocole sous
  `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`.
- v1.2 (13-03-2026) : clarifie la frontiere gouvernance vs runbooks

  `WORKFLOW` et derive les obligations operatoires minimales.

- v1.1 (13-03-2026) : renommage `MP_07_GOVERNANCE_RULES` ->
  `SETUP_PRODUCT_07_GOVERNANCE_RULES`.
