---
id: RUN_10_COMMANDES
type: RUN
title: ListCommandesLLM
version: v1.1
status: FROZEN
created: 27-02-2026
updated: 02-03-2026
tags: [workflow, commandes-llm, run, system]
depends_on: [RUN_00_PIPELINE, RUN_01_COMPOSANTS, RUN_02_CHECKLISTS, RUN_03_START_SESSION, RUN_04_END_SESSION, RUN_05_INCIDENT]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_01_RUN
---

# RUN_10 - List Commandes LLM

Bibliothèque de **prompts/commandes standard** pour piloter le workflow de production avec un LLM (ChatGPT / AnythingLLM / Codex in-IDE), de façon :
- **scalable** (multi-package, multi-product),
- **anti-dérive** (scope verrouillé, 1 intention),
- **compatible** avec les runbooks `RUN_00`/`RUN_05`/`RUN_06`,
- **no-secrets** (aucun token/PII en clair).

> Règle : colle toujours un **Context Pack** en tête. Sans fichiers/chemins, le LLM doit répondre par des hypothèses explicites.

---

## 1) Context Pack (obligatoire)

Copie/colle en tête de toute demande :

```text
Goal:
Constraints: no secrets, diff-first, no auto-commit, 1 intention = 1 commit
Active package: <PACKAGE_ID + path>
Active product: <PRODUCT_ID + path>
Active component (CO): <CO_ID + path>
Current state: (2–6 lignes)
Files: (paths exacts à lire/modifier)
Expected output: (fichier/patch/checklist)
Timebox:
```

### 1.1) Garde-fou “actifs” (anti-mélange)
Ajoute toujours :
- **Package actif unique** : OUI/NON
- **Product actif unique** : OUI/NON

Si NON → le LLM doit proposer un plan pour isoler.

---

## 2) Démarrer une session (RUN_05)

### 2.1) CMD_START_00 — Démarrage session “anti-dérive”
```text
Applique RUN_05_START.
1) Valide package/product actifs (1 seul chacun).
2) Propose 1 CO atomique (DoD 3 bullets, ≤ 5 fichiers).
3) Donne le plan 30–45min + stop conditions.
Output: checklist exécutable.
```

### 2.2) CMD_START_01 — Choisir l’arc (SYSTEM/CORE/PACKAGE/PRODUCT)
```text
À partir du contexte, dis quel arc je dois modifier (SYSTEM/CORE/PACKAGE/PRODUCT) et pourquoi.
Si plus d’un arc est requis, découpe en 2 sessions.
```

---

## 3) Produire des livrables (tooling-first / template-first)

### 3.1) CMD_DOC_00 — Écrire/compléter un document (sans drift)
```text
Rédige le document demandé en respectant :
- frontmatter YAML (id=nom fichier, type, title, version, status, creation/maj, scope, tags, dependances, arc)
- structure: H1 unique, sections courtes, checklists
- no duplication: liens/refs plutôt que copier-coller
Output: fichier complet .md
```

### 3.2) CMD_DOC_01 — Patch ciblé (START/END REPLACE)
```text
Donne un patch START/END REPLACE pour corriger uniquement la section ci-dessous.
Interdit: réécrire tout le doc.
```

### 3.3) CMD_DOC_02 — Normalisation naming + frontmatter
```text
Applique les règles Naming + Frontmatter au fichier ci-joint.
Corrige: id aligné, type valide, title UpperCamelCase, dates, scope/arc, dependances.
Output: fichier complet corrigé.
```

---

## 4) Production par composant (CO) (RUN_02)

### 4.1) CMD_CO_00 — Créer un CO atomique
```text
Crée un CO atomique (1 idée) pour atteindre l’objectif.
Inclure: Titre, DoD (3 bullets), fichiers impactés, risques (2), statut initial, next step.
Output: contenu du fichier CO.
```

### 4.2) CMD_CO_01 — Détecter la dérive d’un CO
```text
Audit ce CO selon RUN_02:
- contient-il 2 intentions ?
- >5 fichiers ?
- DoD flou ?
Propose soit: réduction scope, soit découpage en 2–3 CO.
```

---

## 5) Git / VS Code / Codex (diff-first, no auto-commit)

### 5.1) CMD_CODE_00 — Patch Git minimal + commit + tests
```text
Propose un diff Git minimal pour réaliser X.
Inclure:
- fichiers touchés
- commandes pour vérifier (validator/smoke)
- message commit: type(scope): action
Interdit: auto-commit.
```

### 5.2) CMD_CODE_01 — Debug erreur Git (safe)
```text
Diagnostique cette erreur Git.
Propose la correction la plus safe, avec les commandes exactes.
Ajoute comment vérifier que c’est résolu.
```

### 5.3) CMD_CODE_02 — Smoke minimal
```text
Écris un smoke minimal (happy path) adapté à ce repo.
Donne: comment l’exécuter, quels signaux = OK/KO.
```

---

## 6) AnythingLLM / RAG (RUN_01)

### 6.1) CMD_RAG_00 — Setup “RulesOnly”
```text
Applique RUN_01.
Propose un plan d’ingestion RulesOnly (CORE+SYSTEM minimaux), puis une batterie de 10 tests.
Règle: si info absente -> répondre NON TROUVÉ.
```

### 6.2) CMD_RAG_01 — Passage package-scoped
```text
Je veux activer <PACKAGE_ID>. Donne:
- ordre d’ingestion (couche par couche)
- tests après chaque couche
- garde-fous anti-mélange multi-packages
```

### 6.3) CMD_RAG_02 — Réponse actionnable + sources
```text
Réponds uniquement avec:
1) checklist actionnable
2) fichiers cités (paths)
Si une info n’existe pas -> NON TROUVÉ.
```

---

## 7) Fin de session (RUN_06)

### 7.1) CMD_END_00 — End session obligatoire
```text
Applique RUN_06_END.
Vérifie: diff propre, validator OK, smoke (si applicable), commit+push, doc à jour, statut CO, next step unique.
Output: checklist cochable + next step.
```

---

## 8) Incident (RUN_06_INCIDENT si présent) / Troubleshooting

### 8.1) CMD_INC_00 — Triage incident
```text
Je colle un symptôme + logs (10 lignes max).
1) Classifie: A Git / B Vault / C Scripts / D RAG / E Infra
2) Impact: P0/P1/P2
3) Plan: fix vs rollback (safe)
4) Evidence pack (no secrets)
Output: procédure pas-à-pas.
```

---

## 9) Qualité / gel (READY_TO_FREEZE)

### 9.1) CMD_QA_00 — Ready-to-freeze check (doc)
```text
Audit ce document pour READY_TO_FREEZE:
- frontmatter complet
- structure H1/H2
- sections courtes
- pas de duplication
- utilisable sans oral
Output: verdict + patch START/END REPLACE.
```

### 9.2) CMD_QA_01 — Ready-to-freeze check (repo)
```text
À partir de l’arborescence et des fichiers listés:
- détecte collisions (index, naming)
- détecte typos (SpecTech etc.)
- vérifie package/product actifs uniques
Output: P0/P1/P2 + fixes.
```

---

## 10) Prompts “mini” (copiables)

- **NON TROUVÉ**
  - `Si l’info n’existe pas dans les fichiers fournis: réponds exactement "NON TROUVÉ".`

- **Hypothèses**
  - `Si une info manque: liste max 5 hypothèses, puis propose une version best-effort.`

- **Anti-scope creep**
  - `Si c’est trop large: découpe en CO atomiques et propose l’ordre d’exécution.`

- **No secrets**
  - `Ne demande ni n’affiche jamais de token/clé. Propose .env + .gitignore si nécessaire.`

---

## 11) Changelog
- v1.0 (28-02-2026) : version générique dérivée de RUN_10_COMMANDES_MVP, alignée RUN_00/01/02/05/06, multi-package/multi-product.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
