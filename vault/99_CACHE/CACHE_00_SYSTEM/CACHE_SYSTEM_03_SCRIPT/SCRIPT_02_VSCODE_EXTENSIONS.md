---
id: SCRIPT_02_VSCODE_EXTENSIONS
type: SCRIPT
title: VsCodeExtensionsDecisionMatrix
version: v1.2
status: DEPRECATED
created: 06-03-2026
updated: 13-03-2026
tags: [vscode, extensions, script, cache, deprecated]
depends_on: [GIT_01_ESSENTIEL, WORKFLOW_00_PIPELINE]
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_03_SCRIPT
---

# SCRIPT_02 - VS Code Extensions

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

## Statut d archivage
- Ce document n est plus une source SYSTEM active du framework.
- La baseline extensions VS Code reste une aide locale et non un gate canonique.
- Le fichier est conserve en cache pour historique de poste de travail.

## Changelog
- v1.2 (13-03-2026) : archive en `CACHE_SYSTEM_03_SCRIPT` avec `status: DEPRECATED`.
- v1.1 (13-03-2026) : retire la dependance au bootstrap `GIT_00_CONFIG` devenu deprecated.
- v1.0 (08-03-2026) : creation.
