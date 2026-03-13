---
id: SCRIPT_01_SMOKE_RUNNER
type: SCRIPT
title: SmokeRunnerNotice
version: v1.2
status: FROZEN
created: 28-02-2026
updated: 13-03-2026
tags: [quality, smoke-runner, script, system]
depends_on: [SCRIPT_00_VALIDATOR, WORKFLOW_00_PIPELINE, GIT_02_BRANCH_POLICY, GIT_03_PATCH_COMMIT]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_03_SCRIPT
---

# SCRIPT_01 - Smoke runner (notice & mise en place)

Permet de disposer d’un test “happy path” exécutable en **1 commande** pour vérifier que le repo GAPC est **sain** :

- Git OK (racine repo détectée)
- Vault OK (structure présente)
- Validator OK (frontmatter/naming)
- Aucun invariant manquant (dossiers clés)
- Code de retour standard :
  - `0` = OK
  - `!=0` = KO

Contraintes :
- **No secrets**
- **Rapide** (< 30 secondes idéal)
- **Cross-platform** (Python recommandé)

---

## 1) Emplacement recommandé

### Script (repo)
- `repo/scripts/SmokeRunner.py` *(Python, cross-platform)*

### Notice (vault)
- `vault/00_SYSTEM/SYSTEM_03_SCRIPT/SCRIPT_01_SMOKE_RUNNER.md` (ce document)

---

## 2) Ce que le smoke doit vérifier (V1)

### P0 (obligatoire)
1. **Racine repo** : présence `.git/` (ou `git status` OK)
2. **Vault présent** : `vault/` existe
3. **Arcs présents** :
   - `vault/00_SYSTEM/`
   - `vault/01_CORE/`
   - `vault/02_PACKAGE/`
   - `vault/03_PRODUCT/`
   - `vault/99_CACHE/` *(ou legacy `vault/04_CACHE/`)*
4. **Validator exécutable** : appelle `scripts/ValidateFrontmatter.py` et lit le code retour
5. **DocIntegrity optionnel** : peut appeler `scripts/DocIntegrityChecker.py` sur le scope cible

### P1 (recommandé)
6. **Package actif** : si explicitement demandé, vérifier existence dans `vault/02_PACKAGE/`
7. **Product actif** : si explicitement demandé, vérifier existence dans `vault/03_PRODUCT/`
8. **Typo traps** : détecter patterns connus (ex: `SpechTech`)

---

## 3) Commandes d’exécution

Depuis la racine `repo/` :

```bash
python scripts/SmokeRunner.py
```

Option utile avec integrite documentaire :
```bash
python scripts/SmokeRunner.py --run-doc-integrity --doc-integrity-scope vault
```

Option pre-freeze :
```bash
python scripts/SmokeRunner.py --run-doc-integrity --doc-integrity-scope vault --check-pre-freeze
```

---

## 4) Intégration VS Code Tasks (1 clic)

Ajouter/mettre à jour `repo/.vscode/tasks.json` :

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "GAPC: Smoke",
      "type": "shell",
      "command": "python scripts/SmokeRunner.py --run-doc-integrity --doc-integrity-scope vault",
      "problemMatcher": []
    }
  ]
}
```

---

## 5) Interpréter un KO (table rapide)

| KO | Cause probable | Fix minimal |
|---|---|---|
| Git KO | mauvais dossier ouvert | ouvrir `repo/` |
| Vault KO | mauvais chemin | vérifier `vault/` |
| Arcs KO | arbo incomplète | créer dossiers manquants |
| Validator KO | frontmatter/naming invalides | corriger fichiers listés |
| Python KO | python non installé / PATH | installer / utiliser `python3` |

---

## 6) Règles d’usage
- Smoke à exécuter :
  - avant merge vers `main`
  - après modification scripts/outillage/config
  - après gros ajout de docs structurants
- Interdit : ignorer un KO sans note (CO/incident)

---

## 8) Changelog
-v1.0 (28-02-2026) :  Notice et mis en place Smoke runner GAPC

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.2 (13-03-2026) : recale la notice sur `scripts/SmokeRunner.py`, `ValidateFrontmatter.py` et l option `DocIntegrityChecker`.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
