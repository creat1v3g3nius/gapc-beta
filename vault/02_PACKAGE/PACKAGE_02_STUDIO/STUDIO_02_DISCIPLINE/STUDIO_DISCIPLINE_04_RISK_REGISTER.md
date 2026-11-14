---
id: STUDIO_DISCIPLINE_04_RISK_REGISTER
type: DISCIPLINE
title: StudioRiskRegister
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, discipline, risk, register]
depends_on: 
  - DISCIPLINE_07_RISK_REGISTER
  - CONSTRAINT_03_SECRETS_POLICY
  - EXTENSION_06_COST_LIMITS
  - EXTENSION_07_RIGHTS_AND_ATTRIBUTION
  - STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_02_DISCIPLINE
---

# STUDIO_DISCIPLINE_04 - Risk Register

## Objet

Ajouter les categories, signaux et risques types du metier studio au registre
CORE (`DISCIPLINE_07_RISK_REGISTER`). L echelle `P x I` et le seuil critique
(score 6-9) sont inchanges.

---

## 1) Regles P0

- Max 3 risques actifs par projet.
- Chaque risque : mitigation, signal, owner (role), statut, liens (CO / ADR).
- Aucun nom de client ni donnee personnelle dans le registre.
- Un risque critique ne reste pas `Open` sans mitigation ni owner.

---

## 2) Categories studio

- **A - Droits et licences** : conditions d usage d un outil, ressemblance

  avec une personne, une marque ou une oeuvre, ressource sans licence.

- **B - Confidentialite client** : fuite de brief, de fichier ou d identite

  client.

- **C - Derive de scope** : rounds non bornes, demandes hors brief absorbees.
- **D - Couts de generation** : credits ou temps depasses par CO.
- **E - Coherence DA** : declinaisons qui s ecartent de la spec DA.
- **F - Livraison** : format non conforme, master perdu, version ambigue.

---

## 3) Signaux

- **S1** : evidence pack manquant pour un asset genere.
- **S2** : fichier ou nom client present dans le repo ou le corpus.
- **S3** : round au-dela du nombre inclus sans decision tracee.
- **S4** : CO depassant son budget temps / credits.
- **S5** : asset livre sans reference a la spec DA.
- **S6** : export sans master archive ou nom hors convention.

---

## 4) Risques types (catalogue)

### R-S001 - Usage commercial non couvert par la licence de l outil

- Categorie : A | P : P2 | I : I3 | Score : 6 (critique)
- Signal : S1
- Mitigation : verifier et noter la licence a la generation

  (`STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY`).

### R-S002 - Donnee client dans le repo

- Categorie : B | P : P1 | I : I3 | Score : 3
- Signal : S2
- Mitigation : pseudonymisation `CLIENT_NN`, fichiers hors repo, purge.

### R-S003 - Rounds non bornes

- Categorie : C | P : P3 | I : I2 | Score : 6 (critique)
- Signal : S3
- Mitigation : rounds fixes au brief, classement `NEXT` + decision au-dela.

### R-S004 - Depassement de credits

- Categorie : D | P : P2 | I : I2 | Score : 4
- Signal : S4
- Mitigation : budget par CO, reclassement via scope classifier.

### R-S005 - Incoherence entre declinaisons

- Categorie : E | P : P2 | I : I2 | Score : 4
- Signal : S5
- Mitigation : spec DA comme reference unique, revue de coherence avant BAT.

### R-S006 - Master introuvable apres livraison

- Categorie : F | P : P1 | I : I3 | Score : 3
- Signal : S6
- Mitigation : archivage hors repo trace dans la note de livraison.

---

## 5) Format

Format d instance : celui de `DISCIPLINE_07_RISK_REGISTER`, avec
`RISK_ID: R-Snnn` et une categorie A-F.

## Changelog

- v1.0 (14-11-2026) : creation du registre de risques studio.
