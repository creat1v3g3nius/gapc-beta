---
id: META_06_REFERENCE_EXISTING_FILES
type: META
title: ReferenceExistingFiles
version: v1.1
status: FROZEN
created: 06-03-2026
updated: 15-03-2026
tags: [governance, references, non-duplication, meta, core]
depends_on: [META_03_NAMING_CONVENTIONS, META_05_FRONTMATTER, CONSTRAINT_02_NON_DUPLICATION_POLICY]
arc: CORE
scope: vault/01_CORE/CORE_01_META
---

# META_06 - Reference Existing Files

## Objet
Standardiser la methode "reference-first" dans le vault:
- ne pas recopier une regle qui existe deja,
- pointer vers la source canonique par `id`,
- conserver un seul point de verite.

---

## Regles P0

### 1) Reference avant duplication
Si un contenu normatif existe deja, le document consommateur doit:
- citer l'`id` canonique,
- appliquer la regle sans la re-ecrire.

### 2) Format minimal de reference
Chaque reference normative doit contenir:
- `id` de la source (obligatoire),
- chemin de fichier (recommande),
- decision locale (pourquoi la regle est utilisee ici).

Exemple:

```md
Source canonique: `META_05_FRONTMATTER`
Fichier: `vault/01_CORE/CORE_01_META/META_05_FRONTMATTER.md`
Decision: ce document applique le schema frontmatter sans le dupliquer.
```

### 3) Exception controlee
Une copie partielle est autorisee uniquement si:
- l'extrait est necessaire a la comprehension locale,
- la source canonique est citee explicitement,
- le texte copie reste court et non divergent.

### 4) Contradiction interdite
Une regle locale qui contredit la source canonique est `KO`.
Correction requise:
- corriger le document local, ou
- amender la source canonique via le process de gouvernance.

---

## Procedure d'application

1. Identifier le contenu duplique (regex/recherche textuelle).
2. Trouver la source canonique (ID de reference).
3. Supprimer la duplication.
4. Remplacer par un bloc de reference.
5. Valider frontmatter + smoke runner.

Bloc recommande:

```md
Reference canonique:
- `ID_SOURCE`
- `vault/.../SOURCE.md`
Decision locale:
- Application de la regle sans duplication.
```

---

## Criteres PASS

- pas de duplication normative active,
- references d'ID presentes et resolvables,
- aucune contradiction detectee entre source et document local.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (15-03-2026) : passage en FROZEN du standard `reference-first` apres validation globale du vault.
- v1.0 (06-03-2026) : creation du standard "reference-first" pour supprimer les duplications.
