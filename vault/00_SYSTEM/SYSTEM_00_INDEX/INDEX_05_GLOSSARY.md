---
id: INDEX_05_GLOSSARY
type: INDEX
title: SystemGlossary
version: v1.3
status: FROZEN
created: 27-02-2026
updated: 09-03-2026
tags: [system, glossary, index]
depends_on: []
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_00_INDEX
---

# INDEX_05 — Glossary (00_SYSTEM)

## Objet

Glossaire opérationnel (SYSTEM) pour harmoniser le vocabulaire du framework.

## Termes clés

- **Actifs** : package/product actifs uniques.
- **ADR-lite** : décision structurante, format court.
- **Amendements (FROZEN)** : règle de modification contrôlée.
- **CHECKLIST** : vérification binaire (CORE générique, PACKAGE add-on).
- **CACHE** : arc temporaire non source de vérité, canon `99_CACHE` (legacy

  `04_CACHE`).

- **CO** : composant atomique (1 intention = 1 CO = 1 commit).
- **CORE** : règles transversales (SOT).
- **depends_on** : références d’IDs (valides, dédupliquées).
- **diff-first** : patch minimal avant commit.
- **Evidence pack** : preuve minimale pour outils externes.
- **EVIDENCE FRAMEWORK** : artefacts canons `EVIDENCE_*_FRAMEWORK*` pour

  release/review/adr système.

- **EXTENSION** : protocoles d’outils externes.
- **FROZEN** : gelé (patch + validation + version bump + changelog).
- **Frontmatter** : YAML contractuel.
- **FRAMEWORK canon** : état de référence système (naming, IDs, dépendances)

  validé globalement.

- **Gate/QG** : PASS/FAIL (DocQG/CodeQG/RagQG/GelRules).
- **Hiérarchie** : CORE > PACKAGE > PRODUCT > SYSTEM > CACHE.
- **ID** : `id == filename`.
- **KNOWLEDGE** : référentiels (CORE) / sélection (PACKAGE).
- **NON TROUVÉ** : réponse si absence de source.
- **No-secrets** : aucun secret/PII en clair.
- **PACKAGE** : CORE transposé métier.
- **PIPELINE** : phases d’exécution (CORE) + overlays (PACKAGE).
- **PRODUCT** : workspace (preuves, OPS, validations).
- **RAG** : réponses basées sur sources.
- **READY_TO_FREEZE** : prêt à geler.
- **SYSTEM** : procédures opérateur.
- **TPL** : templates de production.

## Changelog

- v1.3 (09-03-2026) : ajout des termes `CACHE` canon (`99_CACHE`) et `EVIDENCE

  FRAMEWORK`.

- v1.2 (02-03-2026) : rédaction glossaire + nettoyage depends_on.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
