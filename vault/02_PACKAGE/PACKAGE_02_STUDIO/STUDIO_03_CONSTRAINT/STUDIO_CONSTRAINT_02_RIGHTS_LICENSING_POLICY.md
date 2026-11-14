---
id: STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY
type: CONSTRAINT
title: StudioRightsLicensingPolicy
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, constraint, rights, licensing]
depends_on: 
  - EXTENSION_07_RIGHTS_AND_ATTRIBUTION
  - EXTENSION_04_EVIDENCE_PACK
  - CONSTRAINT_04_DECISION_TRACEABILITY_POLICY
  - STUDIO_TOOLING_EXTENSION_01_EVIDENCE_REQUIREMENTS
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_03_CONSTRAINT
---

# STUDIO_CONSTRAINT_02 - Rights Licensing Policy

## Objet

Rendre verifiable, avant chaque livraison, que le studio a le droit d utiliser
et de ceder ce qu il livre. Extension de `EXTENSION_07_RIGHTS_AND_ATTRIBUTION`.

Ce document trace des verifications ; il ne constitue pas un avis juridique.
En cas de doute : `Decision requise` + ADR-lite, et avis qualifie si besoin.

---

## 1) Controles par asset (P0)

- **Outil de generation** : conditions d usage et offre utilisee a la date de

  generation notees dans l evidence pack (usage commercial couvert : OUI /
  NON / A VERIFIER).

- **Ressources tierces** (polices, banques d images, sons, modeles 3D) :

  licence identifiee et notee ; usage prevu couvert.

- **Elements fournis par le client** : le client en garantit les droits ; le

  noter dans le brief.

- **Personnes reelles** : consentement trace (reference, sans donnee

  personnelle dans le vault).

- **Marques, logos, oeuvres** : pas de reproduction sans autorisation.

Resultat : `Rights check: PASS | FAIL | A VERIFIER`. Seul `PASS` permet le BAT.

## 2) Cession au client

- perimetre de cession (supports, territoire, duree) fixe dans le brief,
- toute extension apres livraison = decision tracee.

## 3) Credits

- credits a afficher (studio, ressources tierces) listes dans la note de

  livraison,

- l usage d outils IA est mentionne au client quand le brief ou le contrat

  le prevoit.

## Changelog

- v1.0 (14-11-2026) : creation de la politique droits et licences.
