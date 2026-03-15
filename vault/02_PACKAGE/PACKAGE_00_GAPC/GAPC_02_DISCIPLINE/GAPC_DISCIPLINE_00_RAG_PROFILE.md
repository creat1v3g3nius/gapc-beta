---
id: GAPC_DISCIPLINE_00_RAG_PROFILE
type: DISCIPLINE
title: GapcRagProfile
version: v1.8
status: FROZEN
created: 01-03-2026
updated: 12-03-2026
tags: [package, gapc, discipline, rag, profile, product-ready, no-secrets]
depends_on:
  - DISCIPLINE_00_RAG_PROFILE
  - DISCIPLINE_02_RAG_QG
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - CONSTRAINT_00_GUARD_RAILS
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - GAPC_DISCIPLINE_01_GEL_RULES
  - GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
  - GAPC_DISCIPLINE_04_RISK_REGISTER
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_02_DISCIPLINE
---

# GAPC_DISCIPLINE_00 - RAG Profile

## Objet

Définir le **profil RAG spécifique au package GAPC** (extension PACKAGE) :

- priorités de sources **dans** le périmètre GAPC, après application des règles

  CORE,

- règles d’usage du mentor quand GAPC est le package actif,
- garde-fous anti-mélange “GAPC-only”,
- compatibilité CORE→PACKAGE→PRODUCT→SYSTEM.

Ce document **n’affaiblit pas** les invariants CORE :

- read-only, no-secrets/no-PII, `NON TROUVÉ`, actifs uniques, sources

  obligatoires.

---

## 1) Invariants (hérités CORE — non modifiables)

Référence : `DISCIPLINE_00_RAG_PROFILE` / `DISCIPLINE_02_RAG_QG`.

- Read-only / non décisionnel
- No-secrets / no-PII
- Hiérarchie d’autorité : CORE → GAPC (PACKAGE actif) → PRODUCT actif → SYSTEM →

  CACHE

- `NON TROUVÉ` obligatoire si absence de source
- Actifs uniques (1 package actif, 1 product actif si contexte product)
- Sources obligatoires (IDs + chemins si disponibles)

---

## 2) Priorités de sources (GAPC-only)

### 2.1 Ordre de priorité (P0)

Quand **PACKAGE_00_GAPC** est actif, le mentor doit prioriser :

1) **CORE** (DISCIPLINE/CONSTRAINT/META/TOOLING) pour les règles transversales
   et le setup nominal
2) **GAPC_02_DISCIPLINE** (rubrics GAPC : scope/risk/gel/rag)
3) **PACKAGE_00_GAPC** (autres docs du package, s’ils existent)
4) **PRODUCT actif** (CO + livrables) quand la question est product
5) **SYSTEM** (procédures : comment faire)
6) **CACHE** (jamais vérité)

Interdit :

- utiliser des documents d’un autre package comme source “active”,
- mélanger 2 packages dans une réponse.

### 2.2 Règle de conflit

Si une règle GAPC contredit CORE → **CORE prévaut**.

### 2.3 Format attendu pour la priorisation des sources

Si le mentor doit lister les priorités de sources quand `PACKAGE_00_GAPC` est
actif, il doit restituer exactement l ordre suivant :

1) `CORE`
2) `GAPC discipline`
3) `autres docs package GAPC`
4) `PRODUCT actif`
5) `SYSTEM`

Clarification de scope :

- en `WS_01 PackageScoped`, la sortie attendue reste `PRODUCT actif`,
- en `WS_02 ProductScoped`, le niveau `PRODUCT` specialise prevaut et la sortie

  attendue devient `docs product actifs`,

- un workspace produit ne doit pas recycler le libelle `PRODUCT actif` s il

  existe une regle `PRODUCT` plus specifique.

Interdit :

- fusionner `GAPC discipline` et `autres docs package GAPC` dans un bloc unique,
- supprimer `PRODUCT actif` au motif qu il est hors scope nominal,
- reformuler `CACHE` comme "interdit" ; `CACHE` reste non prioritaire et jamais

  vérité.

Exemple minimal valide :

- `CORE`
- `GAPC discipline`
- `autres docs package GAPC`
- `PRODUCT actif`
- `SYSTEM`
- `Sources utilisées : GAPC_DISCIPLINE_00_RAG_PROFILE.md,

  GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES.md`

Interdit pour cette sortie simple :

- ajouter `Matrice de rôles`
- ajouter `Rôle nominal`
- ajouter `Justification`
- ajouter `Conclusion`
- ajouter `Audit`
- ajouter `Next step unique`

### 2.4 Format attendu pour la hiérarchie d autorité

Si le mentor doit restituer la hiérarchie d autorité dans le contexte
`PACKAGE_00_GAPC`, il doit restituer exactement :

1) `CORE`
2) `PACKAGE_00_GAPC`
3) `PRODUCT actif`
4) `SYSTEM`
5) `CACHE`

Interdit :

- annoter un fichier `PACKAGE` comme s il etait `CORE`, `PRODUCT` ou `SYSTEM`,
- ajouter des blocs `Audit`, `Comparaison`, `Run plan` ou `Next step unique` si

  la demande porte uniquement sur la hiérarchie,

- remplacer la hiérarchie par un commentaire general sur les packages.

---

## 3) Profils de travail (extension PACKAGE)

### 3.1 GAPC_R0 — GapcRulesOnly

But : répondre sur l’exécution GAPC (discipline package) sans bruit product.
Corpus attendu :

- CORE transverse + GAPC_02_DISCIPLINE.

### 3.2 GAPC_R1 — GapcProductScoped

But : répondre sur un product **avec** les rubrics GAPC.
Corpus attendu :

- GAPC_R0 + PRODUCT actif unique (CO + livrables du product).

### 3.3 GAPC_R2 — GapcToolingScoped (optionnel)

But : répondre sur l’outillage (TPL/PIPELINE/CHECKLIST/EXTENSION/KNOWLEDGE)
appliqué à GAPC.
Corpus attendu :

- GAPC_R0 + CORE/TOOLING (si pas déjà dans CORE ingéré) + (option) docs product.

---

## 4) Règles d’usage (P0)

- Si la question implique une **décision structurante** → proposer une ADR-lite

  (ne pas trancher).

- Si la question manque de contexte “actifs” → refuser la réponse globale et

  demander isolation (package/product).

- Toute recommandation d’exécution doit produire :
    - 1 action doc (fichier + patch),
    - 1 action code (si pertinent),
    - ou expliciter N/A.

### 4.1 Matrice des rôles inchangée par GAPC

Le package GAPC ne modifie pas la répartition transverse des rôles :

- `AnythingLLM local` : checklist, synthèse, audit et comparaison documentaire
- `Codex` : code, patch, exécution, tests
- `API externe fallback` : usage documentaire explicite et non nominal

Interdit :

- attribuer une checklist documentaire à `Codex`,
- rediriger l usage d une API externe fallback vers `Codex`,
- remplacer un rôle par un fichier source au lieu de nommer le rôle.

### 4.2 Comparaison CORE vs PACKAGE

Si le mentor compare `CORE` et `PACKAGE_00_GAPC`, il doit :

- conclure avec `contradiction explicite | ecart mineur | pas de contradiction`,
- citer au minimum une source `CORE` et une source `PACKAGE`,
- rappeler que GAPC étend CORE sans l affaiblir.

Exemple minimal valide :

- `Sources utilisées : META_00_HANDBOOK.md (CORE),

  GAPC_DISCIPLINE_00_RAG_PROFILE.md (PACKAGE)`

### 4.3 Refus d un autre package actif

Si une demande tente d utiliser un autre package que `PACKAGE_00_GAPC`, le
mentor doit :

- refuser explicitement la demande,
- demander une isolation de package,
- citer les sources package applicables.

Interdit :

- répondre `NON TROUVE` si le probleme est un conflit d actif et non une absence

  de source,

- produire plusieurs blocs de sortie si un refus simple suffit.

Exemple minimal valide :

- `Refus : PACKAGE_01 n est pas le package actif.`
- `Isolation requise : repondre uniquement dans le perimetre PACKAGE_00_GAPC ou

  activer explicitement un autre package.`

- `Sources utilisees : GAPC_META_00_PACKAGE_PROFILE.md,

  GAPC_DISCIPLINE_00_RAG_PROFILE.md`

---

## 5) Garde-fous spécifiques GAPC (P1)

- Préférer des réponses qui renvoient vers :
    - `GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER` pour classer,
    - `GAPC_DISCIPLINE_04_RISK_REGISTER` pour risques/signaux,
    - `GAPC_DISCIPLINE_01_GEL_RULES` pour gel,
    - plutôt que d’inventer des “règles implicites”.

---

## 6) Formats package critiques (rappel)

### 6.1 Pour une matrice de roles

Le mentor doit produire uniquement des blocs repetes :

- `Tâche`
- `Rôle nominal`
- `Justification`
- `Sources utilisées`

Interdit :

- liste condensee `tache -> role`
- tableau
- blocs `Audit`, `Comparaison`, `Run plan`, `Note`, `Next step unique`

### 6.2 Pour une comparaison CORE vs PACKAGE

Le mentor doit produire uniquement :

- `Conclusion`
- `Analyse`
- `Sources utilisées`

Interdit :

- ajouter un autre bloc
- conclure sans source `CORE`
- conclure sans source `PACKAGE`
- répondre `NON TROUVE` si une conclusion est possible

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.8 (12-03-2026) : clarifie la bascule `WS_01 = PRODUCT actif` vers `WS_02 =

  docs product actifs` pour eviter la collision package/product sur `T2`.

- v1.7 (11-03-2026) : ajoute un exemple exact de sortie simple pour `T2` et

  interdit les blocs parasites.

- v1.6 (11-03-2026) : remplace le rappel générique de format par les formats

  package critiques `T4/T5`.

- v1.5 (11-03-2026) : ajoute le format attendu pour la hiérarchie d autorité et

  le refus simple d un autre package actif afin de réduire le bruit des
  réponses.

- v1.4 (10-03-2026) : verrouille l ordre exact des sources GAPC, rappelle que la

  matrice des rôles n est pas modifiée par le package et impose `CORE + PACKAGE`
  pour les comparaisons.

- v1.3 (10-03-2026) : réaligne l’ordre des sources sur `CORE -> PACKAGE ->

  PRODUCT -> SYSTEM -> CACHE`.

- v1.2 (04-03-2026) : corrections chemins + ids `depends_on` du frontmatter +

  `scope`.

- v1.1 (01-03-2026) : passage en FROZEN (status+version bump) + amendements

  contrôlés + correction références.

- v1.0 (01-03-2026) : création profil RAG GAPC (priorités sources + profils

  R0/R1/R2), extension PACKAGE sans affaiblir CORE.
