---
id: META_05_FRONTMATTER
type: META
title: FrontmatterStandard
version: v1.4
status: FROZEN
created: 28-02-2026
updated: 09-03-2026
tags: [governance, frontmatter, llm, meta, core]
depends_on: [META_03_NAMING_CONVENTIONS, META_04_WRITING_RULES]
arc: CORE
scope: vault/01_CORE/CORE_01_META
---

# META_05 - Règles et Champs standard du Frontmatter YAML

## Objet

Définir le **standard unique** du frontmatter YAML pour tous les fichiers
“source” du Vault (SYSTEM/CORE/PACKAGE/PRODUCT), afin de :

- faciliter recherche/indexation (Obsidian/RAG),
- rendre l’audit et la traçabilité simples,
- permettre la validation automatique (validator),
- réduire les ambiguïtés (naming + scope).

> Ce document remplace/normalise l’ancienne version contenant des champs non
  standard (`uptaded`, `dependances`) fileciteturn43file0.

---

## 1) Règles P0 (contractuelles)

### 1.1 Frontmatter obligatoire

Tout document “source” (SYSTEM/CORE/PACKAGE/PRODUCT) doit avoir un frontmatter
YAML conforme.

### 1.2 Règle d’ID

**`id` = nom du fichier sans extension** (contrat).
Exemple :

- fichier : `CONSTRAINT_06_TERMINOLOGY_POLICY.md`
- frontmatter : `id: CONSTRAINT_06_TERMINOLOGY_POLICY`

### 1.3 Champs obligatoires (P0)

Champs requis :

- `id`
- `type`
- `title`
- `version`
- `status`
- `created`
- `updated`
- `tags`
- `depends_on`
- `arc`
- `scope`

### 1.4 No-secrets

Aucun secret/PII dans le frontmatter.

---

## 2) Schéma standard (P0)

```yaml
id: <FAMILLE_NUM_TITRE>
type: <INDEX|WORKFLOW|GIT|SCRIPTS|LLM|BACKLOG|PATCH|FAQ|META|DISCIPLINE|CONSTRAINT|TOOLING>
title: <UpperCamelCaseTitle>
version: vX.Y
status: DRAFT|PROPOSED|READY_TO_FREEZE|FROZEN|DEPRECATED
created: JJ-MM-AAAA
updated: JJ-MM-AAAA
tags: [tag1, tag2]
depends_on: [ID1, ID2]
arc: SYSTEM|CORE|PACKAGE|PRODUCT|CACHE
scope: vault/<ARC_PATH>/<FAMILY_PATH>
```

### Notes

- `depends_on` contient **des IDs** (pas des chemins).
- `scope` est un **chemin logique de rattachement** (dossier), pas

  nécessairement le fichier complet.

- `title` : UpperCamelCase (sans accents/espaces).

---

## 3) Exemple (conforme)

```yaml
id: CONSTRAINT_06_TERMINOLOGY_POLICY
type: CONSTRAINT
title: TerminologyPolicyExample
version: v1.0
status: READY_TO_FREEZE
created: 01-03-2026
updated: 01-03-2026
tags: [constraint, core]
depends_on: [CONSTRAINT_00_GUARD_RAILS, CONSTRAINT_02_NON_DUPLICATION_POLICY]
arc: CORE
scope: vault/01_CORE/CORE_03_CONSTRAINT
```

---

## 4) Champs optionnels (P1)

### 4.1 Actifs (utile en PRODUCT)

```yaml
active-package: PACKAGE_XX_NAME
active-product: PRODUCT_XX_NAME
co: CO_XXX
```

### 4.2 Gouvernance / conformité

```yaml
source: Interne|Externe
proprietaire: role|equipe
confidentialite: publique|interne
references: [ID1, ID2]
```

Règle : n’ajouter ces champs que s’ils sont réellement exploités (sinon bruit).

---

## 5) Validations attendues (validator)

Le validator doit au minimum vérifier :

- frontmatter présent
- champs P0 présents
- enums valides (`type`, `status`, `arc`)
- **`id == filename`**
- unicité des `id` (sur le périmètre analysé)

---

## Changelog

- v1.4 (09-03-2026) : debruitage de l'exemple `title` pour eviter collision avec

  un frontmatter reel.

- v1.3 (09-03-2026) : aligne les exemples sur les IDs canoniques

  (`*_TERMINOLOGY_POLICY`, `*_NON_DUPLICATION_POLICY`).

- v1.2 (04-03-2026) : corrections frontmatter + heading.
- v1.1 (01-03-2026) : standardisation `created/updated/depends_on`, correction

  des typos, clarification `scope`, exemple CONSTRAINT.

- v1.0 (28-02-2026) : version initiale fileciteturn43file0.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.
