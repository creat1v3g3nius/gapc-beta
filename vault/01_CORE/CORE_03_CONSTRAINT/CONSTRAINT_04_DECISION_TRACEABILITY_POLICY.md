---
id: CONSTRAINT_04_DECISION_TRACEABILITY_POLICY
type: CONSTRAINT
title: DecisionTraceabilityPolicy
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [limites, decision-traceability, llm, discipline, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG, DISCIPLINE_01_GEL_RULES, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_04 - Decision Traceability Policy (contraintes transversales)

## Objet

Imposer une contrainte CORE : toute **décision structurante** doit être
**traçable**, pour éviter :

- décisions fantômes,
- incohérences entre arcs,
- dérive d’architecture,
- perte de contexte lors des itérations.

CORE strict : ce document définit **quand** tracer, pas **comment** remplir une
ADR (procédure en SYSTEM/TPL).

---

## 1) Définition “décision structurante”

Une décision est structurante si elle modifie durablement :

- architecture (arcs, familles, hiérarchie),
- conventions (naming/frontmatter, statuts),
- sécurité (permissions, secrets),
- workflow d’exécution (git policy, gates),
- choix de stack/outillage,
- règles RAG (scope, profils, hiérarchie),
- critères de gel (READY_TO_FREEZE/FROZEN).

---

## 2) Obligation (P0)

Si une décision est structurante :

- elle doit être tracée dans un artefact décisionnel (ex : ADR-lite),
- et référencée depuis les documents impactés (depends_on / liens).

Interdit :

- introduire une décision structurante “implicitement” dans un document de
  règle.

---

## 3) Signal de décision (P0)

Un changement doit être considéré “décision structurante” si :

- il touche CORE/META, CORE/DISCIPLINE ou CORE/CONSTRAINT,
- il introduit une nouvelle famille / nouvel arc / nouveau statut,
- il change une règle “contractuelle” (ex : `id==filename`, NON TROUVÉ),
- il introduit une nouvelle surface d’attaque (secrets, permissions, hosting).

---

## 4) Contrat d’extension (PACKAGE/PRODUCT)

PACKAGE/PRODUCT peuvent ajouter :

- leur propre registre de décisions métier,
- des décisions locales (DoD, critères spécifiques).

Ils ne peuvent pas :

- contourner la traçabilité CORE,
- modifier une règle CORE sans décision explicite et traçable.

---

### Changelog

- v1.0 (01-03-2026) : création de la contrainte CORE de traçabilité des
  décisions structurantes.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
