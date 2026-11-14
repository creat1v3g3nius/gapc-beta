---
id: STUDIO_META_00_PACKAGE_PROFILE
type: META
title: StudioPackageProfile
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, meta, profile]
depends_on: 
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_02_NON_DUPLICATION_POLICY
  - DISCIPLINE_01_GEL_RULES
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_01_META
---

# STUDIO_META_00 - Package Profile

## Objet

Definir le profil de `PACKAGE_02_STUDIO` sans dupliquer la gouvernance CORE :
role, perimetre, invariants, interfaces.

---

## 1) Role du package

`PACKAGE_02_STUDIO` porte la verite metier d un **studio independant de
creation et de direction artistique digitale** :

- cadrage creatif (brief, territoires, direction artistique),
- production assistee par IA (image, video, prototypes web) et retouche,
- revue et validation client (rounds, BAT),
- livraison, archivage, droits et credits.

Chaque projet client (ou projet interne du studio) est instancie comme un
`PRODUCT` temporaire qui declare `PACKAGE_02_STUDIO` comme package actif.

---

## 2) Perimetre (IN / OUT)

### IN (P0)

- overlays metier des disciplines CORE (scope, risques, gel, RAG),
- contraintes metier : droits et licences, confidentialite client, allowlist,
- add-ons de tooling : brief creatif, spec DA, revue client, livraison,

  nommage et preuves des assets.

### OUT (P0)

- regles transverses (frontmatter, no-secrets, gates) -> `CORE`,
- procedures operateur (session, Git, incident) -> `SYSTEM`,
- briefs, assets, retours et preuves d un projet -> `PRODUCT` actif,
- conseil juridique : le package trace les verifications, il ne qualifie pas

  le droit applicable.

---

## 3) Invariants P0 (herites CORE, non modifiables)

- no-secrets / no-PII,
- actifs uniques : 1 package actif, 1 product (projet) actif,
- `NON TROUVE` si absence de source,
- mentor read-only, API externe en fallback explicite,
- 1 intention = 1 CO = 1 commit.

## 4) Invariants P0 propres au studio

- **Assets hors repo** : le repo porte les sources texte (brief, spec DA,

  prompts, journaux, preuves) ; les fichiers binaires (masters, exports,
  fichiers client) vivent dans un stockage externe reference par chemin
  logique (`STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY`).

- **Client pseudonymise** : un client est designe par un code `CLIENT_NN`

  dans tout le vault.

- **Tout asset genere est trace** : evidence pack studio obligatoire

  (`STUDIO_TOOLING_EXTENSION_01_EVIDENCE_REQUIREMENTS`).

- **Droits verifies avant livraison** : aucun livrable sans controle droits

  PASS (`STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY`).

---

## 5) Interfaces

- **CORE** : regles transverses (source de verite).
- **PACKAGE_00_GAPC** : gouverne le framework lui-meme. Il n est jamais actif

  en meme temps que `PACKAGE_02_STUDIO`.

- **PRODUCT** : un projet client = un product temporaire, ouvert via

  `SETUP_PRODUCT_01_BOOTSTRAP` et structure selon
  `STUDIO_TOOLING_PIPELINE_01_WORKSPACE_RULES`.

- **SYSTEM** : sessions, Git, incidents (`WORKFLOW_*`).

Regle : `PACKAGE_02_STUDIO` etend `CORE` ; il ne remplace ni la hierarchie
d autorite, ni la separation des roles `AnythingLLM local / Codex / API
externe fallback`.

---

## 6) Statut

Package en `DRAFT`. Passage `READY_TO_FREEZE` apres validation du contenu
metier par le owner du studio et un premier projet pilote
(`STUDIO_DISCIPLINE_01_GEL_RULES`).

## Changelog

- v1.0 (14-11-2026) : creation du profil PACKAGE_02_STUDIO derive du CORE.
