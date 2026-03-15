---
id: CHECKLIST_08_RAG_SESSION
type: TOOLING
title: RagSession
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [tooling, checklist, rag, mentor, core]
depends_on:
  - CONSTRAINT_01_RAG_SCOPE_POLICY
  - DISCIPLINE_00_RAG_PROFILE
  - DISCIPLINE_02_RAG_QG
  - CONSTRAINT_00_GUARD_RAILS
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_03_CHECKLIST
---

# CHECKLIST_08 - RAG Session (CORE)

- [ ] Profil explicite : RulesOnly / PackageScoped / ProductScoped
- [ ] Actifs uniques (1 package, 1 product si applicable)
- [ ] Sources citées dans les réponses (ou `NON TROUVÉ`)
- [ ] `NON TROUVÉ` appliqué si absence de source
- [ ] Pas de mélange multi-package/product
- [ ] No-secrets / no-PII
- [ ] Si dérive : réduire le corpus (retirer une couche)

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (04-03-2026) : correction heading.
- v1.1 (01-03-2026) : passage en FROZEN.
- v1.0 (01-03-2026) : version initiale READY_TO_FREEZE.
