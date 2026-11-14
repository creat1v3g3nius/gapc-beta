---
id: STUDIO_TOOLING_EXTENSION_01_EVIDENCE_REQUIREMENTS
type: TOOLING
title: StudioEvidenceRequirements
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, extension, evidence]
depends_on: 
  - EXTENSION_04_EVIDENCE_PACK
  - STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_04_EXTENSION
---

# STUDIO_TOOLING_EXTENSION_01 - Evidence Requirements

## Objet

Champs studio a ajouter a l evidence pack CORE (`EXTENSION_04_EVIDENCE_PACK`)
pour chaque asset genere retenu.

## Champs a ajouter (copiable)

```txt
Client: CLIENT_NN
Livrable / CO:
Spec DA (version):
Offre / conditions de l outil a la date (usage commercial: OUI/NON/A VERIFIER):
Seed / parametres cles:
Elements d entree (fournis client | stock licence | aucun):
Retouches manuelles apres generation (resume):
Rights check: PASS | FAIL | A VERIFIER
Fichier(s) produits (noms conformes):
Emplacement (chemin logique hors repo):
```

## Regles P0

- un asset sans evidence pack ne peut pas etre livre,
- aucune donnee personnelle ni lien avec jeton dans l evidence pack.

## Changelog

- v1.0 (14-11-2026) : creation des exigences de preuve studio.
