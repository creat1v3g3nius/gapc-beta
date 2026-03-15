---
id: EVIDENCE_07_ADR_PRODUCT_SCOPE
type: EVIDENCE
title: AdrProductScope
version: v1.0
status: FROZEN
created: 13-03-2026
updated: 13-03-2026
tags: [product, gapc-mentor, evidence, adr, scope, decision]
depends_on: [TPL_02_ADR_LITE, DOD_SAMPLE_00_PRODUCT_VALIDATION, DOD_SAMPLE_03_RELEASE_FREEZE, OPS_SAMPLE_00_BACKLOG_PRODUCT, OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST, EVIDENCE_00_INDEX]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_10_EVIDENCE/EVIDENCE_01_AGENTS
active-package: PACKAGE_00_GAPC
active-product: PRODUCT_00_GAPC_MENTOR
---

# EVIDENCE_07 - ADR Product Scope

## 0) Statut
- Status : ACCEPTED
- Date : 13-03-2026
- Owner : repo-maintainer
- Liens : `DOD_SAMPLE_00_PRODUCT_VALIDATION`, `DOD_SAMPLE_03_RELEASE_FREEZE`, `OPS_SAMPLE_06_READY_TO_FREEZE_CHECKLIST`

## 1) Contexte
- Problème : décider si le setup `PRODUCT_00_GAPC_MENTOR` peut être considéré finalisé et `FROZEN`
- Contraintes :
  - alignement `CORE -> PACKAGE -> PRODUCT`
  - no-secrets / no-PII
  - séparation `Codex / AnythingLLM / API externe fallback`
  - workspaces mentor et agent Codex qualifiés
- Drivers :
  - besoin d une preuve stable et réutilisable sans oral
  - nécessité de fixer la chaîne de vérité `DOD -> OPS -> EVIDENCE`

## 2) Options considerees
### Option A
- Description : maintenir le lot en `DRAFT` malgré les PASS
- Pros :
  - prudence maximale
- Cons :
  - statut incohérent avec les preuves
  - gel documentaire retardé sans raison P0
- Risques :
  - dérive entre contenu et statut

### Option B
- Description : passer le lot en `FROZEN` après backfill complet des preuves
- Pros :
  - cohérence entre gates, statuts et evidence pack
  - lot exploitable sans oral
- Cons :
  - nécessite discipline de rerun à chaque changement significatif
- Risques :
  - relâchement si le rerun n est pas appliqué après modification

## 3) Decision
- Decision : retenir l option B et considérer `PRODUCT_00_GAPC_MENTOR` comme `FROZEN` après PASS de `DOD_00` à `DOD_03`, `WORKFLOW_07_TESTS_LLM` et `WORKFLOW_08_TESTS_CODEX`

## 4) Consequences
- Positives :
  - statut produit cohérent avec les preuves
  - chaîne `DOD -> OPS -> EVIDENCE` stabilisée
  - setup mentor + Codex finalisé
- Négatives :
  - obligation de rerun en cas d évolution documentaire ou prompt
- Dette créée :
  - aucune dette P0 ; dette opérationnelle limitée au rerun périodique
- Backout plan :
  - repasser les fichiers concernés en `DRAFT` si une gate `DOD` ou une batterie de tests redevient `KO`

## 5) Next step unique
- conserver cette ADR comme décision structurante de périmètre du lot `FROZEN`

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.0 (13-03-2026) : aligne l ADR sur la bascule finale `FROZEN`.
- v1.0 (13-03-2026) : création de l ADR de périmètre produit après PASS complet des gates DOD.
