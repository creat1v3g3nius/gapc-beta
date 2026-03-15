---
id: DISCIPLINE_06_SCOPE_CLASSIFIER
type: DISCIPLINE
title: ScopeClassifier
version: v1.3
status: FROZEN
created: 28-02-2026
updated: 04-03-2026
tags: [governance, scope-classifier, llm, discipline, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_00_RAG_PROFILE, DISCIPLINE_02_RAG_QG]
arc: CORE
scope: vault/01_CORE/CORE_02_DISCIPLINE
---

# DISCIPLINE_06 - Scope Classifier (générique)

Classifier toute demande / feature / idée / composant (CO) pour :
- empêcher la dérive (scope creep),
- garder une beta **product-ready**,
- décider vite et de façon reproductible,
- conserver une traçabilité (ADR-lite si décision structurante).

---

## 1) Labels (P0)
NOW / NEXT / LATER / REJECT  
Règle : si doute → NEXT.

---

## 2) Règles (P0)
NOW si :
- indispensable au happy path **ou** réduit un risque critique,
- effort maîtrisé,
- ne dépend pas d’une décision non prise (sinon NEXT + ADR).

LATER si valeur faible/non mesurable/effort non maîtrisé.  
REJECT si hors-scope/disproportion.

---

## 3) Extensions PACKAGE/PRODUCT
Peuvent ajouter des critères (métier, deadlines), pas modifier les labels ni assouplir les règles P0.

---

### Changelog
- v1.1 (01-03-2026) : normalisation frontmatter + statut READY_TO_FREEZE + CORE strict.
- v1.0 (28-02-2026) : version initiale.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (04-03-2026) : corrections frontmatter + heading.
- v1.2 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
