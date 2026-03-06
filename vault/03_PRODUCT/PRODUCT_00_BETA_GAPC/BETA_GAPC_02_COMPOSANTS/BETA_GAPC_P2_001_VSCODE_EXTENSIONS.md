---
id: BETA_GAPC_P2_001_VSCODE_EXTENSIONS
type: TOOLING
title: VsCodeExtensionsDecisionMatrix
version: v1.0
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [beta, p2, vscode, extensions, tooling]
depends_on: [GIT_00_CONFIG, BETA_GAPC_COMPOSANTS_00_BACKLOG]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_02_COMPOSANTS
---

# BETA_GAPC_P2_001_VSCODE_EXTENSIONS

Objet : décision P2.1 sur les extensions VS Code (recommandées vs optionnelles) avec règle de retrait si bruit/instabilité.

Hypothèse d'exécution :
- `code --list-extensions` indisponible dans cet environnement (`code-cli: absent`).
- Baseline définie selon les besoins réels du pipeline GAPC (validator, smoke, YAML/frontmatter, Git propre).

## Recommandées (MVP)
- `redhat.vscode-yaml`
Raison : validation YAML/frontmatter utile et directement alignée avec la qualité documentaire du vault.

## Optionnelles
- `eamodio.gitlens`
Raison : utile pour historique/blame, mais peut ajouter du bruit visuel.
- `editorconfig.editorconfig`
Raison : utile si un `.editorconfig` est maintenu; sinon valeur limitée.

## Règle d'exploitation
- Installer une extension à la fois.
- Vérifier impact sur : édition docs, flux Git, tâches Validate/Smoke.
- Si bruit, instabilité, latence ou comportement destructeur : retirer immédiatement.

## Décision P2.1
- Liste recommandées vs optionnelles : établie.
- Politique de retrait “si bruit/instable -> remove” : appliquée.
