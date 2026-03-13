---
id: GIT_00_CONFIG
type: GIT
title: ConfigGitVsCode
version: v1.3
status: DEPRECATED
created: 28-02-2026
updated: 13-03-2026
tags: [boostrap, config, git, cache, deprecated]
depends_on: [INDEX_01_ARCHITECTURE, WORKFLOW_00_PIPELINE, EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION, EVIDENCE_04_CODEX_IDE]
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_02_GIT
---

# GIT_00 - Mode d'emploi Configuration Git dans Vs Code

## Statut
- `DEPRECATED`
- bootstrap historique uniquement
- obsolete en routine si la configuration effective est deja tracee dans `EVIDENCE`

## Regle operationnelle
Si la configuration Git/VS Code/hooks est deja couverte par :
- `EVIDENCE_01_RELEASE_NOTE_FRAMEWORK_VALIDATION`
- `EVIDENCE_04_CODEX_IDE`

alors `GIT_00_CONFIG` ne doit plus etre utilise comme source operationnelle.

En regime finalise :
- `GIT_01_ESSENTIEL` porte les commandes minimales,
- `GIT_03_PATCH_COMMIT` porte la doctrine patch/commit/merge,
- `EVIDENCE` porte la trace de configuration et de validation.

Mode d’emploi **unique** (simple, sûr, répétable) pour :
- configurer VS Code pour travailler dans le framework GAPC (Vault → Repo),
- configurer Git et exécuter un workflow quotidien (**diff → stage → commit atomique → validate/smoke → push**),
- éviter les erreurs débutant (mauvaise racine, commits “fourre‑tout”, secrets accidentels, conflits).

Ce guide est **adapté à l’architecture du framework** (arcs `00_SYSTEM/01_CORE/02_PACKAGE/03_PRODUCT/04_CACHE`) telle que décrite dans `INDEX_01`

Contraintes :
- **No secrets** (aucun token/clé/PII en clair).
- **1 intention = 1 commit**.
- **Validator frontmatter/naming bloquant** avant commit (quand disponible).
- **Diff-first / no auto-commit** avec assistants.

---

## 1) Pré-requis

### 1.1) Installer Git et vérifier
```bash
git --version
```

### 1.2) Configurer l’identité Git (une fois)
```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton@email"
git config --global --list
```

> astuce:  utiliser une adresse “no-reply” si tu veux éviter une adresse perso dans l’historique.

---

## 2) Ouvrir le bon dossier dans VS Code (racine Git)

Piège #1 : ouvrir **le mauvais dossier**, ce qui “casse” Git et crée de la confusion.

### 2.1) Règle simple
Dans VS Code, ouvre **toujours** le dossier qui contient `.git/`.

Commande de survie (terminal VS Code) :
```bash
git status
```

### 2.2) Architecture GAPC recommandée (Vault dans le repo)
Structure :
```txt
repo/
  .git/
  docs/
  scripts/
  vault/
    00_SYSTEM/
    01_CORE/
    02_PACKAGE/
    03_PRODUCT/
    04_CACHE/
```

- VS Code : ouvrir `repo/`
- Obsidian : ouvrir `repo/vault/`

 Avantages : Git détecté, chemins stables, moins d’erreurs.

### 2.3) Fichier sentinelle (anti-erreur)
Créer à la racine `repo/` :
- `REPO_ROOT.md` : “Ceci est la racine du repo Git.”

---

## 3) Extensions VS Code (minimum vital)

### 3.1) Recommandées
- **YAML (Red Hat)** : indentation/validation YAML (frontmatter)
- **ChatgptCodex** (si tu utilises un assistant in-IDE)

### 3.2) Optionnels
- **GitLens** : historique/blame visuels (peut être bruyant)
- **EditorConfig** : règles d’indentation partagées

Règle MVP :
- si une extension perturbe → désinstalle (stabilité > richesse).

---

## 4) Réglages VS Code (workspace) — minimal

Stocker dans :
- `repo/.vscode/settings.json`

Exemple minimal :
```json
{
  "files.eol": "\n",
  "files.trimTrailingWhitespace": true,
  "editor.formatOnSave": false,
  "editor.wordWrap": "on",
  "editor.rulers": [100],
  "yaml.validate": true
}
```

---

## 5) Git — notions minimales (rappel)
- **Commit** : photo d’un changement (1 intention)
- **Branch** : ligne de travail (`main`, `work/*`)
- **Diff** : ce qui change (à lire avant tout commit)
- **Stage** : sélection des changements à committer
- **Remote** : repo distant (GitHub)
- **Push/Pull** : envoyer / recevoir

---

## 6) Initialiser / connecter le repo (bootstrap)

### 6.1) Initialiser (si pas déjà fait)
```bash
cd repo
git init
git branch -M main
```

## 6.2 Ajouter un remote (si GitHub)
```bash
git remote add origin <URL_DU_REMOTE>
git remote -v
```

## 6.3 Premier commit propre
```bash
git add -A
git commit -m "chore(repo): bootstrap framework"
git push -u origin main
```

---

## 7) Branch policy (recommandation GAPC)

### 7.1) Règles simples
- `main` : stable (pas de commit direct sauf exception)
- `work/<topic>` : branche de travail

Créer une branche de travail :
```bash
git switch -c work/bootstrap
git push -u origin work/bootstrap
```

### 7.2) Routine quotidienne
- tu travailles sur `work/*`
- tu pushes souvent
- tu merges vers `main` uniquement après validate/smoke (si en place)

---

## 8) Workflow quotidien (safe) — diff → stage → commit → validate/smoke → push

### 8.1) Checklist courte
1) Lire le **diff**
2) Stage uniquement ce qui correspond à **1 intention**
3) (Si présent) lancer **validator** (frontmatter/naming)
4) (Si applicable) lancer **smoke**
5) Commit `type(scope): action`
6) Push

Exemples commit :
- `docs(system): update quickstart runbook`
- `docs(core): tighten frontmatter rules`
- `chore(scripts): improve validator output`

### 8.2) Commandes terminal “survie”
```bash
git status
git diff
git add -p
git commit -m "type(scope): action"
git push
git log --oneline -10
```

---

## 9) Conflits (débutant) — procédure safe

### 9.1) Résoudre un conflit
1) `git status` (voir fichiers en conflit)
2) Ouvrir le fichier en conflit dans VS Code  
   → utiliser **Accept Current / Incoming / Both / Compare**
3) Sauvegarder
4) `git add <fichier>`
5) Terminer :
- merge : `git commit`
- rebase : `git rebase --continue`
6) Relancer validator/smoke si nécessaire

### 9.2) Abort (si panique)
```bash
git merge --abort
git rebase --abort
```

---

## 10) No secrets : `.env`, `.gitignore`, réflexes

Interdit dans Git / docs :
- clés API, tokens, mots de passe, clés privées, cookies de session.

Pattern recommandé :
- `.env` (local) ignoré
- `.env.example` (commit) sans secrets

Extrait `.gitignore` :
```gitignore
.env
.env.*
!.env.example
*.key
*.pem
```

Si `.env` apparaît dans les changements :
```bash
git restore --staged .env
# si déjà tracké :
git rm --cached .env
```

---

## 11) VS Code Tasks (optionnel, recommandé)

Objectif : 1 clic pour lancer **Validate** / **Smoke**.

Fichier recommandé :
- `repo/.vscode/tasks.json`

Exemple minimal (à adapter aux scripts existants) :
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "GAPC: Validate Vault",
      "type": "shell",
      "command": "python scripts/ValidateFrontmatter.py",
      "problemMatcher": []
    },
    {
      "label": "GAPC: Smoke",
      "type": "shell",
      "command": "python scripts/SmokeRunner.py",
      "problemMatcher": []
    }
  ]
}
```

---

## 12) Check final (5 minutes)

- [ ] VS Code a ouvert la racine contenant `.git/`
- [ ] `git status` OK
- [ ] diff visible, stage sélectif OK
- [ ] commit atomique OK
- [ ] push OK
- [ ] `.env` non tracké
- [ ] validator OK (si présent)
- [ ] smoke OK (si applicable)

---

## 13) Changelog
- v1.0 (28-02-2026) : configuration git dans Vscode, workflow commit atomique.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.3 (13-03-2026) : archive en `CACHE_SYSTEM_02_GIT` car la configuration effective est deja tracee dans `EVIDENCE`.
- v1.2 (13-03-2026) : passe en `DEPRECATED` ; obsolete si la configuration est deja tracee dans `EVIDENCE`.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
