---
id: STUDIO_INDEX_00_PACKAGE
type: INDEX
title: StudioPackageNavigationIndex
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [studio, package, index, navigation]
depends_on: []
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_00_INDEX
---

# STUDIO_INDEX_00 - Navigation Package

## Objet

Point d entree du **PACKAGE_02_STUDIO** : overlay metier d un studio
independant de creation et de direction artistique digitale.

Le PACKAGE contient :

- des **overlays** de discipline (scope, risques, gel, RAG) adaptes au metier
- des **contraintes** metier (droits, confidentialite client, allowlist)
- des **add-ons** de tooling (brief creatif, spec DA, revue client, livraison)

Le PACKAGE ne contient pas :

- les regles transverses (CORE)
- les procedures operateur (SYSTEM)
- les preuves et livrables d un projet client (PRODUCT)

---

## Navigation

### INDEX

[[STUDIO_INDEX_01_META]] · [[STUDIO_INDEX_02_DISCIPLINE]] ·
[[STUDIO_INDEX_03_CONSTRAINT]] · [[STUDIO_INDEX_04_TOOLING]]

### META

- [[STUDIO_META_00_PACKAGE_PROFILE]] : role, perimetre, invariants.
- [[STUDIO_META_01_DOMAIN_DEFINITIONS]] : lexique metier et correspondance

  avec le cycle GAPC.

### DISCIPLINE

- [[STUDIO_DISCIPLINE_00_RAG_PROFILE]] : profil RAG du package.
- [[STUDIO_DISCIPLINE_01_GEL_RULES]] : gel = BAT client puis livraison.
- [[STUDIO_DISCIPLINE_02_RAG_QG]] : quality gates RAG studio.
- [[STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER]] : tri des demandes client.
- [[STUDIO_DISCIPLINE_04_RISK_REGISTER]] : risques metier (droits, rounds,

  couts, coherence DA).

### CONSTRAINT

- [[STUDIO_CONSTRAINT_00_ALLOW_LIST]] : autorise / interdit.
- [[STUDIO_CONSTRAINT_01_SOURCES_POLICY]] : sources et references visuelles.
- [[STUDIO_CONSTRAINT_02_RIGHTS_LICENSING_POLICY]] : droits, licences,

  credits.

- [[STUDIO_CONSTRAINT_03_CLIENT_CONFIDENTIALITY_POLICY]] : confidentialite

  client.

- [[STUDIO_CONSTRAINT_04_EXCEPTION_POLICY]] : derogations tracees.

### TOOLING

Voir [[STUDIO_INDEX_04_TOOLING]].

## Changelog

- v1.0 (14-11-2026) : creation index PACKAGE du PACKAGE_02_STUDIO.
