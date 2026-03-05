---
id: GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER
type: DISCIPLINE
title: GAPCScopeClassifier
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, rubric, scope, prioritization, mvp, product-ready]
depends_on: [DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER, DISCIPLINE_01_GEL_RULES, CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_01_RAG_SCOPE_POLICY, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, TPL_03_BACKLOG_CO]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_02_DISCIPLINE
---

# GAPC_DISCIPLINE_03 - Scope Classifier

## Objet
Classifier toute demande / feature / idée / tâche dans une catégorie **actionnable** pour le package GAPC, en restant aligné avec l’architecture :
**CORE → PACKAGE → PRODUCT → SYSTEM**.

Ce classifier est une **extension PACKAGE** (GAPC) :
- il **ne contredit pas** les règles CORE (ScopeClassifier, RiskRegister, Guardrails),
- il ajoute une **priorisation product-ready** et des critères GAPC.


---

## 1) Ce que l’on classifie (items)
Un item peut être :
- un livrable doc (INDEX/RUN/GIT/LLM/…),
- un script/outillage (validator, smoke, etc.),
- une règle de gouvernance (CORE/PACKAGE),
- un composant product (CO).

**Règle anti-dérive** :
- si l’item touche 2 arcs (ex : CORE + PRODUCT) → **scinder** en 2 items.

---

## 2) Labels de décision (P0)
Un item reçoit **un seul label** :

- **NOW** : requis pour livrer le minimum product-ready
- **NEXT** : utile mais non indispensable maintenant
- **LATER** : reporté (faible ROI / dépendances)
- **REJECT** : hors-scope / non aligné / trop coûteux

**Règle** : si doute → **NEXT**.

---

## 3) Critères de valeur “GAPC product-ready”
Un item est candidat **NOW** si au moins un critère est vrai :

### V1 — Parcours minimal exécutable
- permet de réaliser un cycle complet : cadrage → exécution → validation → traçabilité → gel.

### V2 — Qualité / conformité bloquante
- corrige une non-conformité P0 (frontmatter/naming/no-secrets),
- réduit un risque critique (score 6–9).

### V3 — Fiabilité d’exécution
- supprime une friction récurrente de production (gates, pipeline, checklist).

---

## 4) Grille rapide (Oui/Non)
Répondre O/N :

1) **Happy path** : nécessaire au parcours minimal complet ?
2) **Gate P0** : nécessaire pour passer un gate P0 (DocQG/CodeQG/RagQG/GelRules) ?
3) **Risque critique** : réduit un risque score 6–9 ?
4) **Effort maîtrisé** : livrable sans casser le planning ?
5) **Dépendance non décidée** : dépend d’une décision (ADR) ?
6) **Mesurable** : impact mesurable rapidement (signal clair) ?

---

## 5) Règles de classification (algorithme P0)
- Si (1 **ou** 2 **ou** 3) = OUI **et** 4 = OUI **et** 5 = NON → **NOW**
- Si 5 = OUI → **NEXT** (jusqu’à ADR)
- Si (1,2,3) = NON **et** valeur plausible **et** 4 = OUI/peut-être → **NEXT**
- Si 4 = NON **ou** non mesurable **ou** coût disproportionné → **LATER**
- Si hors objectif GAPC / complexité non justifiée / cosmétique → **REJECT**

---

## 6) Priorisation interne (P0/P1/P2)
- **P0** : bloque un gate / le happy path / la conformité no-secrets
- **P1** : améliore fortement, contournable
- **P2** : confort / polish

---

## 7) Format de sortie (copiable)
À utiliser dans un backlog CO :

```txt
Item:
Arc: SYSTEM|CORE|PACKAGE|PRODUCT
Active package: PACKAGE_00_GAPC
Active product: <NA|PRODUCT_XX>
Valeur: V1|V2|V3
Questions (1..6): O/N + notes
Décision: NOW|NEXT|LATER|REJECT
Priorité: P0|P1|P2
Dépendances (IDs):
Justification (1 phrase):
Next step unique:
```

**Règle** : si > 3 items → convertir en **CO atomiques** (TPL Backlog CO).

---

## 8) Exemples rapides

### Exemple A — Correction frontmatter SYSTEM (typo `uptaded`)
- (2)=OUI, (4)=OUI → **NOW**, P0

### Exemple B — Ajout d’un nouveau protocole extension “nice-to-have”
- (1..3)=NON → **LATER**, P2

### Exemple C — Nouveau pipeline core-strict pour gel
- (1)=OUI, (4)=OUI, (5)=NON → **NOW**, P0

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (01-03-2026) : passage en FROZEN (status+version bump) + amendements contrôlés + correction références.
- v1.0 (01-03-2026) : version initiale.