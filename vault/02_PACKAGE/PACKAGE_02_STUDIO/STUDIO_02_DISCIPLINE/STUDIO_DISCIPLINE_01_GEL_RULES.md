---
id: STUDIO_DISCIPLINE_01_GEL_RULES
type: DISCIPLINE
title: StudioGelRules
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, discipline, freeze, delivery]
depends_on: 
  - DISCIPLINE_01_GEL_RULES
  - DISCIPLINE_03_DOC_QG
  - PIPELINE_05_RELEASE_FREEZE
  - STUDIO_META_01_DOMAIN_DEFINITIONS
  - STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY
  - STUDIO_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON
  - STUDIO_TOOLING_TPL_04_DELIVERY_NOTE_ADDON
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_02_DISCIPLINE
---

# STUDIO_DISCIPLINE_01 - Gel Rules

## Objet

Traduire les gates CORE de `DISCIPLINE_01_GEL_RULES` dans le cycle d un
projet studio :

- **STUDIO_READY_TO_FREEZE** = projet **pret pour BAT**,
- **STUDIO_FROZEN** = projet **livre** (BAT obtenu, livraison tracee).

Extension PACKAGE : en cas de contradiction, CORE prevaut.

---

## 1) Gate STUDIO_READY_TO_FREEZE - pret pour BAT (P0)

PASS si **tous** les criteres sont vrais :

- gate CORE `READY_TO_FREEZE` PASS sur les documents du projet,
- chaque livrable du brief a un CO `Done` (ou est explicitement retire avec

  decision tracee),

- spec DA a jour et coherente avec les livrables (revue de coherence faite),
- formats et specifications conformes au brief

  (`STUDIO_TOOLING_KNOWLEDGE_01_DELIVERABLE_FORMATS`),

- evidence pack studio present pour chaque asset genere,
- controle droits PASS (`STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY`),
- journal de revue client a jour, aucun retour ouvert non classe.

Checklist : `STUDIO_TOOLING_CHECKLIST_01_READY_TO_FREEZE_ADDON`.

---

## 2) Gate STUDIO_FROZEN - livre (P0)

STUDIO_FROZEN = STUDIO_READY_TO_FREEZE PASS + :

- BAT client trace (date, canal, version validee) sans donnee personnelle,
- note de livraison redigee (`STUDIO_TOOLING_TPL_04_DELIVERY_NOTE_ADDON`),
- masters et exports archives hors repo, emplacement reference,
- versions `CORE`, `SYSTEM` et `PACKAGE` utilisees notees

  (`SETUP_PRODUCT_07_GOVERNANCE_RULES`),

- zero P0 ouvert sur le projet.

---

## 3) Apres livraison

- Une correction demandee apres BAT ouvre un **nouveau CO** et produit une

  nouvelle version d asset (`_v<N+1>`) ; le livrable gele n est pas ecrase.

- Une demande nouvelle hors brief est classee via

  `STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER` (par defaut `NEXT`).

- La sortie du projet suit `SETUP_PRODUCT_06_MERGE_OUT_POLICY` : le savoir

  reutilisable remonte dans le package, le reste est archive.

---

## 4) Gel du package lui-meme

`PACKAGE_02_STUDIO` passe `READY_TO_FREEZE` quand :

- son contenu metier est valide par le owner du studio,
- un projet pilote a parcouru le cycle complet jusqu a `STUDIO_FROZEN`.

## Changelog

- v1.0 (14-11-2026) : creation des gates pret pour BAT / livre.
