---
id: STUDIO_META_01_DOMAIN_DEFINITIONS
type: META
title: StudioDomainDefinitions
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, meta, glossary, domain]
depends_on: 
  - STUDIO_META_00_PACKAGE_PROFILE
  - CONSTRAINT_06_TERMINOLOGY_POLICY
  - PIPELINE_00_PRODUCT
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_01_META
---

# STUDIO_META_01 - Domain Definitions

## Objet

Fixer le vocabulaire metier du studio et sa correspondance avec le cycle
GAPC, pour que le mentor et les documents utilisent un seul terme par notion.

---

## 1) Lexique metier

- **Client** : commanditaire d un projet, designe par `CLIENT_NN`.
- **Projet** : mission pour un client ou projet interne ; instancie en

  `PRODUCT`.

- **Brief creatif** : besoin du client cadre en une page (objectif, cible,

  livrables, contraintes, rounds, droits).

- **Moodboard** : planche de references visuelles servant a l exploration ;

  jamais un livrable.

- **Territoire creatif** : piste de direction proposee au client (en general

  2 a 3 en phase d exploration).

- **Direction artistique (DA)** : regles visuelles retenues pour le projet

  (palette, typographie, composition, lumiere, textures, do / don t).

- **Key visual (KV)** : visuel principal qui porte la DA.
- **Declinaison** : adaptation d un KV a un format, un support ou un canal.
- **Round de retours** : cycle presentation -> retours client -> corrections.

  Le nombre de rounds inclus est fixe dans le brief.

- **BAT** : validation finale explicite du client avant livraison.
- **Livrable** : fichier remis au client selon le brief.
- **Master** : fichier source editable conserve par le studio.
- **Export** : fichier final genere depuis un master pour un usage donne.
- **Asset genere** : image, video ou prototype produit avec un outil IA.
- **Cession** : droits d usage transferes au client (perimetre, duree,

  supports), definis dans le brief.

---

## 2) Correspondance avec le cycle GAPC

| Studio | Cycle GAPC (CORE) |
| --- | --- |
| Brief creatif | PRD (`TPL_00_PROD_ONE_PAGER` + add-on studio) |
| Spec DA | Spec (`TPL_01_SPEC_TECH` + add-on studio) |
| Livrable / declinaison / correction | CO (`TPL_03_BACKLOG_CO`) |
| Round de retours | serie de CO de revision + journal de revue |
| Pret pour BAT | `READY_TO_FREEZE` |
| Livre (BAT obtenu) | `FROZEN` |
| Demande hors brief | `NEXT` + decision tracee (ADR-lite) |

---

## 3) Regles de terminologie

- Utiliser les termes ci-dessus tels quels dans le package et les products.
- Un terme absent de ce lexique n est pas une regle : ajouter la definition

  ici avant de l utiliser comme critere.

## Changelog

- v1.0 (14-11-2026) : creation du lexique studio et du mapping vers le cycle GAPC.
