---
id: CONSTRAINT_05_CACHE_POLICY
type: CONSTRAINT
title: CachePolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [limites, cache-policy, llm, discipline, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_05 - Cache Policy (contraintes transversales)

## Objet

Définir une contrainte CORE minimale sur l’usage de l’arc **CACHE** :

- éviter que du contenu temporaire devienne “source de vérité”,
- réduire le bruit RAG,
- limiter les fuites (logs, exports).

CORE strict : pas de procédure opérateur.

---

## 1) Règles P0

1) **CACHE n’est jamais Source of Truth**.
2) Aucun document normatif ne doit référencer CACHE comme base (au mieux :
   référence de travail temporaire).
3) Interdit de stocker dans CACHE :
   - secrets/PII,
   - données sensibles,
   - artefacts non nécessaires à la reproduction.

## 2) Règles P1

4) Tout contenu utile doit être **promu** vers l’arc correct
   (SYSTEM/CORE/PACKAGE/PRODUCT) ou supprimé.
5) Les exports volumineux doivent avoir un compagnon `.md` si promus.

---

### Changelog

- v1.0 (01-03-2026) : version minimale de la contrainte CACHE.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
