---
id: CONSTRAINT_02_NON_DUPLICATION_POLICY
type: CONSTRAINT
title: Nonduplicationpolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [limites, non-duplication-policy, llm, discipline, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_02 - Non-Duplication Policy (contraintes transversales)

## Objet

Empêcher les contradictions et le bruit (RAG/Git) en imposant une politique CORE
:

- **une règle = une source**,
- la duplication est une exception tracée,
- la référence est la norme.

CORE strict : aucune procédure opérateur.

---

## 1) Règles P0 (bloquantes)

### 1.1 Single Source of Truth

Toute règle normative doit avoir une **source unique** dans l’arc approprié :

- règles transversales → CORE,
- règles métier → PACKAGE,
- règles d’exécution locale → PRODUCT,
- procédures opérateur → SYSTEM.

### 1.2 Référence > copie

Quand un contenu existe déjà comme source :

- on **référence** (lien/ID) au lieu de copier-coller.

### 1.3 Contradiction = KO

Deux formulations incompatibles sur le même sujet = contradiction.
Une contradiction non résolue est un P0 et doit être :

- corrigée à la source,
- ou marquée `NON TROUVÉ` si la source est absente.

### 1.4 Exceptions contrôlées

La duplication n’est tolérée que si :

- elle est explicitement justifiée (objectif),
- elle est bornée (périmètre),
- elle renvoie vers la source,
- elle ne crée pas de divergence silencieuse.

---

## 3) Contrat d’extension

PACKAGE/PRODUCT peuvent renforcer (ex : règles anti-duplication plus strictes),
mais ne peuvent pas :

- autoriser des duplications non tracées,
- redéfinir la hiérarchie de vérité.

---

### Changelog

- v1.0 (01-03-2026) : création de la politique CORE anti-duplication.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
