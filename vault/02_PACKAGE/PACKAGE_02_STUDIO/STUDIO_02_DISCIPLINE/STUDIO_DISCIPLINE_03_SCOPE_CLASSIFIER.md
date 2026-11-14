---
id: STUDIO_DISCIPLINE_03_SCOPE_CLASSIFIER
type: DISCIPLINE
title: StudioScopeClassifier
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, discipline, scope, prioritization]
depends_on: 
  - DISCIPLINE_06_SCOPE_CLASSIFIER
  - EXTENSION_06_COST_LIMITS
  - TPL_02_ADR_LITE
  - STUDIO_META_01_DOMAIN_DEFINITIONS
  - STUDIO_TOOLING_TPL_00_CREATIVE_BRIEF
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_02_DISCIPLINE
---

# STUDIO_DISCIPLINE_03 - Scope Classifier

## Objet

Classer toute demande d un projet studio (livrable, declinaison, correction,
exploration) avec les labels CORE `NOW / NEXT / LATER / REJECT`. Extension de
`DISCIPLINE_06_SCOPE_CLASSIFIER` : les labels et la regle `si doute -> NEXT`
sont inchanges.

---

## 1) Criteres studio (grille O/N)

1) **Dans le brief** : la demande figure-t-elle dans les livrables du brief ?
2) **Round inclus** : reste-t-il un round inclus pour cette correction ?
3) **Conformite** : corrige-t-elle un defaut de format, de droits ou de

   coherence DA ?

4) **Budget** : tient-elle dans le budget temps / credits du CO

   (`EXTENSION_06_COST_LIMITS`) ?

5) **Decision client manquante** : depend-elle d un arbitrage non obtenu ?

---

## 2) Algorithme (P0)

- (1 ou 3) = OUI **et** 4 = OUI **et** 5 = NON -> **NOW**
- correction avec 2 = OUI **et** 4 = OUI -> **NOW**
- 1 = NON (hors brief) -> **NEXT** + decision tracee (ADR-lite : avenant,

  echange, refus)

- 2 = NON (rounds epuises) -> **NEXT** + decision tracee
- 5 = OUI -> **NEXT** jusqu a decision
- exploration non demandee -> **LATER** (timebox explicite si reprise)
- contraire aux contraintes (droits, confidentialite) -> **REJECT**

---

## 3) Priorite interne

- **P0** : bloque le BAT ou la conformite (droits, formats).
- **P1** : ameliore un livrable du brief.
- **P2** : finition hors exigence du brief.

---

## 4) Format de sortie

```txt
Item:
Type: livrable | declinaison | correction | exploration
Active package: PACKAGE_02_STUDIO
Active product: PRODUCT_NN_<CODE>
Questions (1..5): O/N
Decision: NOW | NEXT | LATER | REJECT
Priorite: P0 | P1 | P2
Decision client requise: OUI | NON
Next step unique:
```

## Changelog

- v1.0 (14-11-2026) : creation du classifier de demandes client.
