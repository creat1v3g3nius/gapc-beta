---
id: OPS_SAMPLE_02_SPEC_DOD
type: DOD
title: GapcMentorSpecDod
version: v1.5
status: FROZEN
created: 10-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, ops, spec, dod]
depends_on:
  - OPS_SAMPLE_00_BACKLOG_PRODUCT
  - OPS_SAMPLE_00_BACKLOG_CO
  - OPS_SAMPLE_01_PRD_DOD
  - DOD_SAMPLE_01_PRODUCT_THIN_SLICE
  - TPL_01_SPEC_TECH
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_SAMPLE_GAPC_AGENTS/SAMPLE_GAPC_AGENTS_01_OPS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_SAMPLE_GAPC_AGENTS
---

## Copie locale

- Copie locale non canonique pour raccordement du lot PRODUCT.
- Utiliser les ids `*_SAMPLE` dans le lot PRODUCT.

# OPS_SAMPLE_02 - Spec DoD

## Objet

Verifier que la spec technique traduit le PRD en contrat executable sans deriver
du setup nominal.

La spec doit deriver d un backlog produit et d un CO explicites.

## 1) Verifications P0

PASS si :

- la spec distingue clairement question documentaire et action technique
- `Codex` porte l implementation et les tests
- le mentor reste read-only
- les permissions et no-secrets sont mentionnes
- la priorisation produit distingue `GAPC discipline`, `autres docs package
  GAPC` et `docs product actifs`
- la spec impose `1 product actif` et un refus explicite d un autre product
- la matrice des roles produit reste au format `1 bloc par tache`

FAIL si :

- la spec laisse le mentor executer ou patcher
- la hierarchie `CORE -> PACKAGE -> PRODUCT -> SYSTEM` disparait
- les interfaces sont floues ou non testables
- la spec confond hierarchie d autorite et priorites de sources produit
- la spec autorise `NON TROUVE` a la place d un refus d isolation produit
- la spec autorise une liste compacte `tache -> role` pour la matrice des roles

## 2) Formats critiques produit

### 2.1 Priorites de sources produit

Format attendu :

- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `docs product actifs`
- `SYSTEM`
- `Sources utilisees :`

Interdit :

- remplacer ce format par `CORE -> PACKAGE -> PRODUCT -> SYSTEM -> CACHE`,
- ajouter `CACHE`,
- supprimer `docs product actifs`,
- ecrire `PACKAGE_00_GAPC` ou `PRODUCT_00_SAMPLE_GAPC_AGENTS` a la place des
  categories de sources,
- annoter une source `PRODUCT` comme `CORE`,
- annoter une source `PACKAGE` comme `PRODUCT`.

Exemple minimal valide :

- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `docs product actifs`
- `SYSTEM`
- `Sources utilisees : GAPC_DISCIPLINE_00_RAG_PROFILE.md,
  GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES.md, OPS_SAMPLE_02_SPEC_DOD.md`

### 2.2 Isolation d un autre product

Format attendu :

- `Refus :`
- `Isolation requise :`
- `Sources utilisees :`

Interdit :

- repondre seulement `NON TROUVE`.

### 2.3 Matrice des roles produit

Format attendu :

- `Tache :`
- `Role nominal :`
- `Justification :`
- `Sources utilisees :`

Interdit :

- justification globale unique,
- tableau ou liste compacte `tache -> role`,
- blocs `Audit`, `Run plan` ou `Next step unique` si non demandes.

## 3) Evidence

```txt
Spec ID:
PRD reference:
Contrats:
Contraintes:
Verdict:
Next step unique:
```

## 4) Evidence documentee

```txt
Spec ID: OPS_SAMPLE_02_SPEC_DOD
PRD reference: OPS_SAMPLE_00_BACKLOG_PRODUCT
Contrats:
- `Codex` = implementation, patch, execution, tests
- `AnythingLLM local` = mentor documentaire read-only
- `API externe fallback` = fallback cible, jamais nominal
- priorites de sources produit = `CORE -> GAPC discipline -> autres docs package GAPC -> docs product actifs -> SYSTEM`
Contraintes:
- `1 package actif` = `PACKAGE_00_GAPC`
- `1 product actif` = `PRODUCT_00_SAMPLE_GAPC_AGENTS`
- refus explicite d un autre product
- `no-secrets / no-PII`
Verdict: PASS
Next step unique: conserver cette spec comme reference produit pour les reruns
```

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.5 (13-03-2026) : passe la spec produit en `READY_TO_FREEZE`.
- v1.4 (13-03-2026) : backfill l evidence de spec avec les contrats finaux et le
  verdict PASS du setup.
- v1.3 (11-03-2026) : renforce le format `T2` avec interdiction des arcs a la
  place des categories et ajoute un exemple valide package+product.
- v1.2 (11-03-2026) : ajoute les formats critiques produit pour priorites de
  sources, isolation d un autre product et matrice des roles.
- v1.1 (10-03-2026) : rattache la spec au backlog product et au backlog CO.
- v1.0 (10-03-2026) : creation du controle spec pour
  `PRODUCT_00_SAMPLE_GAPC_AGENTS`.
