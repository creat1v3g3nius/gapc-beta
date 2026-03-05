---
id: SCRIPT_00_VALIDATOR
type: SCRIPT
title: VaultValidatorAndHook
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [quality, validator, hook, script, system]
depends_on: [RUN_00_PIPELINE, GIT_00_CONFIG, GIT_03_PATCH_COMMIT]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_03_SCRIPT
---

# SCRIPT_00 - Validator Vault + Hook Pre-Commit (notice & mise en place)

Permet de mettre en place une qualité **bloquante mais simple** pour le framework GAPC :

- un **validator** qui vérifie les fichiers du Vault (`repo/vault/`) : frontmatter YAML + naming + invariants,
- un **hook Git pre-commit** (optionnel mais recommandé) qui empêche de committer si le validator est KO,
- une intégration **VS Code Tasks** (1 clic).

Contraintes :
- **No secrets** : aucun token/clé/PII dans repo/docs/logs.
- **Fail fast** : si KO → code de sortie non-zéro.
- **Scalable** : multi-package / multi-product (package actif unique par session).

---

## 1) Portée du validator (ce qu’il doit vérifier)

### P0 (obligatoire)
1. **Frontmatter YAML présent** sur tous les fichiers “structurants” (au minimum SYSTEM/CORE/PACKAGE/PRODUCT).
2. Champs requis :
   - `id`, `type`, `title`, `version`, `status`, `created`, `updated`, `scope`, `tags`, `depends_on`, `arc`
3. **Alignement** : `id` = **nom du fichier sans extension** *(règle contractuelle)*.
4. Enum :
   - `type` ∈ set familles
   - `status` ∈ `DRAFT|PROPOSED|READY_TO_FREEZE|FROZEN|DEPRECATED`
   - `arc` ∈ `SYSTEM|CORE|PACKAGE|PRODUCT|CACHE`
5. **Naming** : fichier conforme au pattern de famille (`<FAMILLE_NUM_...>.md`) et `UpperCamelCase` pour `title` (frontmatter).

### P1 (recommandé)
6. Unicité :
   - `id` **unique** sur le corpus analysé.
7. Cohérence :
   - `scope` correspond au chemin du fichier (préfixe cohérent).
8. Anti-duplication (simple) :
   - détecter collisions “quasi-doublons” (ex: `SpecTech` vs `SpechTech`).

### P2 (option)
9. Vérifier “package actif unique” via une variable de config (voir §4).

---

## 2) Emplacement & nommage des scripts

### Repo (exécution)
- `repo/scripts/validate_vault.py` *(ou extension de ton `ValidateFrontmatter.py`)*
- option : `repo/scripts/validate_naming.py` (si séparé)

### Vault (notice)
- `vault/00_SYSTEM/SYSTEM_03_SCRIPT/SCRIPT_00_VALIDATOR.md` (ce document)

---

## 3) Commandes d’exécution (dev)

### 3.1) Exécuter le validator (manuel)
Depuis la racine `repo/` :

```bash
python scripts/validate_vault.py --vault vault
```

Variantes utiles :
- cibler un arc :
```bash
python scripts/validate_vault.py --vault vault --arc SYSTEM
```

- cibler un package :
```bash
python scripts/validate_vault.py --vault vault --package PACKAGE_02_GAPC
```

Attendu :
- `0` = OK
- `!=0` = KO (avec liste des fichiers en erreur)

---

## 4) Configuration (scalable, multi-package/product)

Créer un fichier de config (optionnel mais utile) :
- `repo/scripts/validator.config.json`

Exemple (sans secrets) :
```json
{
  "vaultPath": "vault",
  "enforceIdEqualsFilename": true,
  "enforceUniqueIds": true,
  "activePackage": "PACKAGE_02_GAPC",
  "activeProduct": "PRODUCT_02_GAPCMVP",
  "requiredFrontmatterKeys": ["id","type","title","version","status","creation","maj","scope","tags","dependances","arc"]
}
```

Règle :
- le validator ne doit **pas** dépendre d’une config pour fonctionner (fallback sur défauts).

---

## 5) Hook Git pre-commit (optionnel mais recommandé)

### 5.1) Principe
À chaque `git commit`, exécuter le validator.
Si KO → **commit bloqué**.

### 5.2) Installation locale (simple)
Créer le fichier :
- `repo/.git/hooks/pre-commit`

Contenu (macOS/Linux) :
```bash
#!/usr/bin/env bash
python scripts/validate_vault.py --vault vault
```

Rendre exécutable :
```bash
chmod +x .git/hooks/pre-commit
```

Windows : utiliser un hook `.bat` ou appeler `python` de façon équivalente.

### 5.3) Bypass (exceptionnel)
```bash
git commit --no-verify -m "..."
```
Interdit en routine. Si bypass :
- documenter pourquoi dans le CO / note de session,
- relancer validator juste après.

---

## 6) VS Code Tasks (1 clic)

Créer/mettre à jour :
- `repo/.vscode/tasks.json`

Exemple minimal :
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "GAPC: Validate Vault",
      "type": "shell",
      "command": "python scripts/validate_vault.py --vault vault",
      "problemMatcher": []
    }
  ]
}
```

---

## 7) Dépannage (KO fréquents)

### “id != filename”
- Renommer le fichier **ou** corriger `id` (mais garder alignement).

### “missing keys”
- Copier un frontmatter valide, compléter les champs.

### “python not found”
- Essayer `python3` (macOS/Linux).
- Sur Windows : vérifier PATH Python.

---

## 8) Changelog
-v1.0 (28-02-2026) : Validator Vault + Hook pre-commit (notice & mise en place) — GAPC.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
