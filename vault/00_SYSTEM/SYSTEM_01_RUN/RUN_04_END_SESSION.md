---
id: RUN_04_END_SESSION
type: RUN
title: EndSessionProtocol
version: v1.1
status: FROZEN
created: 27-02-2026
updated: 02-03-2026
tags: [workflow, end-session, run, system]
depends_on: [RUN_00_PIPELINE, RUN_01_COMPOSANT]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# RUN_04 - End Session Protocol

Clore chaque session avec un état **propre**, **traçable**, et **reproductible** :
- ce qui a été fait est committé (ou expliqué),
- la doc reflète la réalité,
- les validations minimales sont passées,
- le **next step** est unique.

Compatibilité : multi-package / multi-product, architecture v4.3 (CORE → PACKAGE → PRODUCT).

---

## 1) Règles non négociables
- **Pas de commit sans validator OK** (frontmatter/naming).
- **1 intention = 1 commit** (sinon, séparer).
- **Aucun secret / PII** dans le repo (diff, logs, docs).
- Si tu as touché **2 arcs** → noter l’écart + créer 2 CO (correction prochaine session).

---

## 2) Vérifications (P0)

### 2.1) Diff & propreté
- [ ] Diff relu (pas de fichiers parasites : exports, caches, temporaires).
- [ ] Aucun fichier hors scope “intention” n’est staged.

### 2.2) Validator (obligatoire)
- [ ] Validator frontmatter/naming **OK** (sinon : pas de commit).
- [ ] `id` = nom de fichier (sans extension).
- [ ] Champs YAML requis présents (`type`, `title`, `version`, `status`, `creation`, `maj`, `scope`, `tags`, `dependances`, `arc`).

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

**Stop condition**
Si tu ne peux pas commit :
- [ ] écrire “Pourquoi pas de commit”
- [ ] lister “Ce qui reste à faire pour committer”
- [ ] next step unique = action de reprise

---

## 4) Documentation

- [ ] La doc (Vault) reflète la réalité (pas de promesses non tenues).
- [ ] Si une **décision structurante** est apparue → ADR-lite créée (même courte).
- [ ] Les commandes/chemins ajoutés sont testés (copier-coller).
- [ ] Les liens Obsidian critiques ne sont pas cassés (ou fixés).

---

## 5) Pilotage CO / composant

### 5.1) Statut
- [ ] CO mis à jour : `Draft | Ready | In progress | Done | Blocked`

### 5.2) Si Blocked
- [ ] raison en 1 ligne
- [ ] 1 action de déblocage claire (qui, quoi, comment)
- [ ] dépendances mises à jour (frontmatter `dependances` si pertinent)

---

## 6) Mentor (AnythingLLM) — check rapide (option)

À faire si tu as :
- modifié CORE/PACKAGE,
- ajouté beaucoup de docs,
- ou observé des réponses “vagues”.

Test minimal :
> Donne-moi la checklist applicable au CO terminé et cite les fichiers. Si absent : “NON TROUVÉ”.

- [ ] Réponse actionnable
- [ ] Fichiers cités
- [ ] Pas d’invention
- [ ] Pas de mélange multi-packages

Si KO :
- [ ] réduire corpus
- [ ] relancer ingestion selon `RUN_01`

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
- v1.0 (27-02-2026) : version générique, alignée naming/frontmatter, multi-package/multi-product.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
