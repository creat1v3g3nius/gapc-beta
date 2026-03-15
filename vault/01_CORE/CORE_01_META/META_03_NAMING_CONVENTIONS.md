---
id: META_03_NAMING_CONVENTIONS
type: META
title: NamingConventionsFiles
version: v1.4
status: FROZEN
created: 28-02-2026
updated: 15-03-2026
tags: [governance, naming-conventions, llm, meta, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_01_META
---

# META_03 - Formats et Règles standard de nomination des fichiers

Chaque fichier fait partie d'une famille (**INDEX / EXECUTION / GIT / SCRIPTS /
LLM / BACKLOG / PATCH / FAQ / META / FIELD / RESTRAINT / TOOLING...**) existant
dans une arc du système (**SYSTEM / CORE / PACKAGE / PRODUCT / CACHE**).
Chaque arc est composé des familles nécessaires à son fonctionnement, leur
présence n'est pas systématique et dépend de la fonction de l'arc.

## 1) Naming

1) **Format arcs** : `<NUM_TITRE>/`
2) **Format familles** : `<ARC_NUM_TITRE>/`
3) **Format sous-familles** : `<FAMILLE_TYPE_SF_NUM_TITRE>/`
4) **Format fichiers** :
   - standard : `<FAMILLE_NUM_TITRE>`
   - sous-famille : `<FAMILLE_TYPE_SF_NUM_TITRE>`
5) **Format IDs** :
   - standard : `<FAMILLE_NUM_TITRE>`
   - sous-famille : `<FAMILLE_TYPE_SF_NUM_TITRE>`
6) **Titre** : `UpperCamelCase`, sans accent, caractères spéciaux ou espaces.
7) **Set de familles figé** :

    (**INDEX / EXECUTION / GIT / SCRIPTS / LLM / BACKLOG / PATCH / FAQ / META /
FIELD / RESTRAINT / TOOLING**)

    - Toute **nouvelle famille** nécessite une ADR.
8) **Alignement obligatoire** :
   - `id = nom du fichier sans extension`
   - le prefixe du H1 doit reprendre l identifiant logique du document
9) **Format H1** :
   - standard : `# <FAMILLE_NUM> - <Titre>`
   - sous-famille : `# <FAMILLE_TYPE_SF_NUM> - <Titre>`
10) **Exemples canoniques** :
   - standard :
     - fichier : `CONSTRAINT_00_GUARD_RAILS.md`
     - id : `CONSTRAINT_00_GUARD_RAILS`
     - H1 : `# CONSTRAINT_00 - GUARD_RAILS`
   - sous-famille :
     - fichier : `GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS.md`
     - id : `GAPC_TOOLING_KNOWLEDGE_00_ALLOWED_TOOLS`
     - H1 : `# GAPC_TOOLING_KNOWLEDGE_00 - ALLOWED_TOOLS`

## Changelog

- v1.4 (15-03-2026) : explicite le format de nommage des fichiers et IDs de
  sous-famille, et harmonise les exemples standard / sous-famille.
- v1.3 (15-03-2026) : formalise la convention H1 canonique pour familles et
  sous-familles, et clarifie l alignement `id` / nom de fichier.
- v1.2 (04-03-2026) : corrections ids `depends_on` du frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.0 (28-02-2026) : création des règles minimales de naming.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
