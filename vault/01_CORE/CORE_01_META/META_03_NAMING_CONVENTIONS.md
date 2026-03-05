---
id: META_03_NAMING_CONVENTIONS
type: META
title: NamingConventionsFiles
version: v1.2
status: FROZEN
created: 28-02-2026
updated: 04-03-2026
tags: [governance, naming-conventions, llm, meta, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_01_META
---

# META_03 - Formats et Règles standard de nomination des fichiers 

Chaque fichier fait partie d'une famille (**INDEX / EXECUTION / GIT / SCRIPTS / LLM / BACKLOG / PATCH / FAQ / META / FIELD / RESTRAINT / TOOLING...**) existant dans une arc du système (**SYSTEM / CORE / PACKAGE / PRODUCT / CACHE**).
Chaque arc est composé des familles nécessaires à son fonctionnement, leur présence n'est pas systématique et dépend de la fonction de l'arc.


## 1) Naming

1) **Format arcs** : <NUM_TITRE/> 
2) **Format familles** : <ARC_NUM_TITRE/>
3) **Format sous-familles** : <FAMILLE_NUM_TITRE/>
**Format fichiers** :  `<FAMILLE_NUM_TITRE>`
2) **Format IDs** : `<FAMILLE_NUM_TITRE>`
3) **Titre** : `UpperCamelCase`, sans accent, caractères spéciaux ou espaces.
4) **Set de familles figé** : 
    (**INDEX / EXECUTION / GIT / SCRIPTS / LLM / BACKLOG / PATCH / FAQ / META / FIELD / RESTRAINT / TOOLING**)
    - Toute **nouvelle famille** nécessite une ADR.
5) Alignement obligatoire : ìd`= <FAMILLE_NUM/> du fichier`

## Changelog
- v1.2 (04-03-2026) : corrections ids `depends_on` du frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.0 (28-02-2026) : création des règles minimales de naming.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.
