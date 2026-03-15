---
id: CONSTRAINT_00_GUARD_RAILS
type: CONSTRAINT
title: Guardrails
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [limites, guard-rails, llm, constraint, core]
depends_on: [META_00_HANDBOOK, META_01_OUTPUT_PROTOCOL, DISCIPLINE_06_SCOPE_CLASSIFIER, DISCIPLINE_07_RISK_REGISTER]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
---

# CONSTRAINT_00 - Guardrails (contraintes transversales)

## Objet

Fixer les **garde-fous non négociables** qui empêchent la dérive du système :

- dérive de scope,
- mélange multi-package/product,
- invention (hallucination),
- fuite de secrets/PII,
- confusion de hiérarchie CORE→PACKAGE→PRODUCT→SYSTEM.

CORE strict : aucune procédure opérateur (pas de commandes, pas d’evidence
pack).

---

## 1) Garde-fous P0 (bloquants)

### 1.1 No-secrets / no-PII

Interdit d’introduire ou de conserver en clair :

- tokens, clés API, mots de passe, secrets,
- données personnelles (PII),

dans docs, code, configs, logs, exemples, commits.

### 1.2 Hiérarchie d’autorité (Source of Truth)

En cas de contradiction :

1) CORE
2) PACKAGE actif
3) PRODUCT actif
4) SYSTEM
5) CACHE (jamais vérité)

### 1.3 Actifs uniques

Une session/production doit opérer avec :

- **1 package actif unique** (ou NA),
- **1 product actif unique** quand contexte product.

Tout mélange doit être isolé (réduction de scope/corpus) avant production.

### 1.4 NON TROUVÉ (anti-invention)

Si une information n’existe pas dans les sources applicables :

- réponse/état = `NON TROUVÉ`,
- + 1 action pour rendre l’information trouvable (créer/compléter un doc, tracer
  une ADR).

### 1.5 Une intention = une unité de changement

Interdit de mélanger plusieurs intentions dans un même changement :

- 1 intention = 1 CO = 1 commit (ou squash unique équivalent).

### 1.6 Anti-cross-arc

Un changement ne doit pas toucher plusieurs arcs (CORE+PRODUCT, etc.) sans
découpage explicite.

---

## 2) Garde-fous P1 (renforcement)

- Réduire le bruit : éviter la duplication de règles (cf. NonDuplicationPolicy).
- Traçabilité des décisions structurantes : ADR-lite.
- Limiter les exceptions : toute exception doit être tracée et bornée.

---

## 3) Contrat d’extension

PACKAGE/PRODUCT peuvent renforcer ces garde-fous (plus strict), mais ne peuvent
pas :

- créer des exceptions no-secrets,
- autoriser multi-actifs,
- assouplir `NON TROUVÉ`,
- inverser la hiérarchie d’autorité.

---

## Changelog

- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
- v1.0 (01-03-2026) : création des garde-fous transversaux CORE.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
