---
id: WORKFLOW_04_END_SESSION
type: WORKFLOW
title: EndSessionProtocol
version: v1.5
status: FROZEN
created: 27-02-2026
updated: 14-11-2026
tags: [workflow, end-session, run, system]
depends_on:
  - WORKFLOW_00_PIPELINE
  - WORKFLOW_03_START_SESSION
  - CHECKLIST_02_END_SESSION
  - WORKFLOW_07_TESTS_LLM
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN/RUN_00_WORKFLOW
---

# WORKFLOW_04 - End Session Protocol

Clore chaque session avec un état **propre**, **traçable**, et **reproductible**
:

- ce qui a été fait est committé (ou expliqué),
- la doc reflète la réalité,
- les validations minimales sont passées,
- le **next step** est unique.

Compatibilité : multi-package / multi-product, architecture v4.3 (CORE → PACKAGE
→ PRODUCT).

Références :

- demarrage de session : `WORKFLOW_03_START_SESSION`
- checklist courte de cloture : `CHECKLIST_02_END_SESSION`
- requalification mentor si besoin : `WORKFLOW_07_TESTS_LLM`

---

## 1) Règles non négociables

- **Pas de commit sans validator OK** (frontmatter/naming).
- **1 intention = 1 commit** (sinon, séparer).
- **Aucun secret / PII** dans le repo (diff, logs, docs).
- Si tu as touché **2 arcs** → noter l’écart + créer 2 CO (correction prochaine

  session).

---

## 2) Vérifications (P0)

### 2.1) Diff & propreté

- [ ] Diff relu (pas de fichiers parasites : exports, caches, temporaires).
- [ ] Aucun fichier hors scope “intention” n’est staged.

### 2.2) Validator (obligatoire)

- [ ] Validator frontmatter/naming **OK** (sinon : pas de commit).
- [ ] `id` = nom de fichier (sans extension).
- [ ] Champs YAML requis présents (`id`, `type`, `title`, `version`,

  `status`, `created`, `updated`, `arc`, `scope`, `tags`, `depends_on`).

### 2.3) Smoke (si applicable)

À exécuter si :

- script/outillage/config modifié,
- règles CORE/PACKAGE impactées,
- pipeline/validator modifié.

- [ ] Smoke runner OK
- [ ] (Si KO) note d’erreur + lien vers logs

---

## 3) Git

- [ ] Stage **sélectif** (uniquement ce qui correspond à l’intention).
- [ ] Commit message conforme : `type(scope): action`
- [ ] Push/sync effectué (ou justification si offline).
- [ ] `git status` = clean

Stop condition :
Si tu ne peux pas commit :

- [ ] écrire “Pourquoi pas de commit”
- [ ] lister “Ce qui reste à faire pour committer”
- [ ] next step unique = action de reprise

---

## 4) Documentation

- [ ] La doc (Vault) reflète la réalité (pas de promesses non tenues).
- [ ] Si une **décision structurante** est apparue → ADR-lite créée (même

      courte).

- [ ] Les commandes/chemins ajoutés sont testés (copier-coller).
- [ ] Les liens Obsidian critiques ne sont pas cassés (ou fixés).

---

## 5) Pilotage CO / composant

### 5.1) Statut

- [ ] CO mis à jour : `Draft | Ready | In progress | Done | Blocked`

### 5.2) Si Blocked

- [ ] raison en 1 ligne
- [ ] 1 action de déblocage claire (qui, quoi, comment)
- [ ] dépendances mises à jour (frontmatter `depends_on` si pertinent)

---

## 6) Agent en mode MENTOR — check rapide (option)

À faire si tu as :

- modifié CORE/PACKAGE,
- ajouté beaucoup de docs,
- ou observé des réponses “vagues”.

Test minimal :
> Donne-moi la checklist applicable au CO terminé et cite les fichiers. Si
  absent : “NON TROUVÉ”.

- [ ] Réponse actionnable
- [ ] Fichiers cités
- [ ] Pas d’invention
- [ ] Pas de mélange multi-packages

Si KO :

- [ ] réduire le périmètre de lecture
- [ ] requalifier via `WORKFLOW_07_TESTS_LLM`

---

## 7) Next step unique (obligatoire)

Écrire **une seule** prochaine action :

```txt
NEXT STEP:
```

Règle :

- l’action doit être exécutable en < 1 session si possible.

---

## 8) Archive de session (recommandé, 1 minute)

- [ ] Lien vers le commit (hash ou message)
- [ ] Liste des fichiers touchés (3–10 max)
- [ ] 1 apprentissage / note (option)

---

## 9) Checklist express (copiable)

- [ ] Diff propre
- [ ] Validator OK
- [ ] Smoke OK (si applicable)
- [ ] Commit + push OK
- [ ] Doc à jour
- [ ] CO statut à jour
- [ ] Next step unique

---

## 10) Changelog

- v1.0 (27-02-2026) : version générique, alignée naming/frontmatter,

  multi-package/multi-product.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.5 (14-11-2026) : realigne sur l agent Claude (modes MENTOR / EXECUTION) ;

  references AnythingLLM / Codex retirees (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- v1.4 (14-11-2026) : aligne la liste des champs YAML requis sur le validator

  (`created`, `updated`, `depends_on`).

- v1.3 (14-11-2026) : aligne `scope` sur le dossier reel (`vault/00_SYSTEM/SYSTEM_01_RUN/RUN_00_WORKFLOW`).
- v1.2 (13-03-2026) : retire la dependance a `WORKFLOW_01` et recable la

  cloture vers `CHECKLIST_02` et `WORKFLOW_07`.

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
