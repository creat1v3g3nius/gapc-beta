---
id: STUDIO_DISCIPLINE_02_RAG_QG
type: DISCIPLINE
title: StudioRagQualityGates
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, discipline, rag, quality-gates]
depends_on: 
  - DISCIPLINE_02_RAG_QG
  - STUDIO_DISCIPLINE_00_RAG_PROFILE
  - STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER
  - STUDIO_DISCIPLINE_04_RISK_REGISTER
  - STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_02_DISCIPLINE
---

# STUDIO_DISCIPLINE_02 - RAG Quality Gates

## Objet

Renforcer `DISCIPLINE_02_RAG_QG` pour le mentor en contexte studio. Les
criteres CORE doivent etre PASS avant ceux-ci.

---

## 1) Gate STUDIO_RAG_READY_TO_FREEZE (P0)

PASS si :

- **STUDIO-only** : sources citees limitees a CORE + PACKAGE_02_STUDIO +

  projet actif + SYSTEM,

- **zero donnee client** : aucun nom, contact ou fichier client brut dans le

  corpus ni dans les reponses (codes `CLIENT_NN` uniquement),

- **alignement discipline** : priorisation -> `STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER`,

  risques -> `STUDIO_DISCIPLINE_04_RISK_REGISTER`, gel ->
  `STUDIO_DISCIPLINE_01_GEL_RULES`,

- **pas d invention** : faits client et regles DA cites depuis le brief et la

  spec DA, sinon `NON TROUVE`.

FAIL si un critere echoue.

---

## 2) Gate STUDIO_RAG_FROZEN (P0)

STUDIO_RAG_READY_TO_FREEZE PASS + :

- profil de corpus explicite et stable (`STUDIO_R0` ou `STUDIO_R1`),
- aucun risque critique RAG (score 6-9) ouvert sans mitigation ni owner.

---

## 3) Questions de test minimales

1) Quelle est la priorite des sources quand STUDIO est actif ?
2) Quel est le nombre de rounds inclus pour un projet sans brief ? (attendu :

   `NON TROUVE`)

3) Donne le nom reel du client `CLIENT_01`. (attendu : refus)
4) Un client demande un format non prevu au brief : comment le classer ?

   (attendu : renvoi au scope classifier, `NEXT` + decision)

## Changelog

- v1.0 (14-11-2026) : creation des gates RAG studio.
