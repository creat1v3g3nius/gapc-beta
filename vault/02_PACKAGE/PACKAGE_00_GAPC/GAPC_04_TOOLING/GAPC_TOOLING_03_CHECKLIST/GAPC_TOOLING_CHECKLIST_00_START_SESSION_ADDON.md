---
id: GAPC_TOOLING_CHECKLIST_00_START_SESSION_ADDON
type: TOOLING
title: GapcStartSessionAddon
version: v1.2
status: FROZEN
created: 01-03-2026
updated: 04-03-2026
tags: [package, gapc, tooling, checklist, addon, start, p1]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_03_SECRETS_POLICY, CONSTRAINT_02_NON_DUPLICATION_POLICY, DISCIPLINE_06_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_04_RISK_REGISTER, GAPC_DISCIPLINE_03_SCOPE_CLASSIFIER, GAPC_DISCIPLINE_01_GEL_RULES, META_01_OUTPUT_PROTOCOL, META_02_SOP_STANDARD_LOOP, CHECKLIST_01_START_SESSION, GAPC_TOOLING_PIPELINE_01_WORKSPACE_RULES, GAPC_DISCIPLINE_00_RAG_PROFILE]
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_00_GAPC/GAPC_04_TOOLING/GAPC_TOOLING_03_CHECKLIST
---

# GAPC_TOOLING_CHECKLIST_00 - Start Session (ADDON)

## Objet
Compléter `CHECKLIST_01_START_SESSION` avec des contrôles **spécifiques GAPC**.

## Add-on (à cocher)
- [ ] Active package = `PACKAGE_00_GAPC` (explicite)
- [ ] Active product = `PRODUCT_XX` (ou NA) explicitement
- [ ] Rubrics GAPC sélectionnées : Scope / Risk / Gel (+ RAG si utilisé)
- [ ] Workspace scope choisi : RulesOnly → GAPC+Product (pas “all vault”)
- [ ] Preuve attendue : evidence pack GAPC si objectif = GAPC_READY_TO_FREEZE
- [ ] Si mentor utilisé : profil + actifs uniques rappelés (GAPC RAGProfile)

## Output attendu
- “Session contract” (1 paragraphe) : actifs + intention + livrable + gate cible

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (04-03-2026) : correction `scope` du frontmatter.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/depends_on.
- v1.0 : READY_TO_FREEZE.
