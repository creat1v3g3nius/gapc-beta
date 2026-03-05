---
id: HOSTING_01_TARGET_ARCHITECTURE
type: PATCH
title: HostingTargetArchitectureD1D2
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [hosting, target-architecture, patch, system]
depends_on: [HOSTING_00_INDEX_CONFIG]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_20_PATCH/PATCH_00_HOSTING
---

# HOSTING_01 - Architecture cible (P1) — D1/D2 + chemins + rôles

Définir une architecture serveur **simple** pour héberger :
- le repo Git (exécution, scripts),
- le Vault Obsidian (Source of Truth),
- AnythingLLM (mentor RAG, read-only),
avec **backup quotidien D1→D2**.

Hypothèse : Linux Debian/Ubuntu.

---

## 1) Chemins recommandés (standardiser = éviter erreurs)
### Racine GAPC
- `/srv/gapc/` : racine fonctionnelle

### D1 (principal)
- `/srv/gapc/repo/` : repo Git (contient `.git/`)
- `/srv/gapc/repo/vault/` : Vault Obsidian (recommandé : Vault dans repo)
- `/srv/gapc/logs/` : logs (rsync, services)
- `/srv/gapc/scripts/` : scripts ops (backup)

### D2 (backup)
- `/mnt/d2/gapc_backup/` : racine backup
- `/mnt/d2/gapc_backup/srv_gapc_mirror/` : miroir rsync de `/srv/gapc/`
- (option) `/mnt/d2/gapc_backup/_snapshots/` : snapshots si FS le permet

---

## 2) Variante stockage
### Variante A (recommandée) — Vault dans repo
- Vault = `/srv/gapc/repo/vault/`
Avantages :
- une seule racine à backuper (`/srv/gapc/`)
- cohérence doc+scripts+conventions

### Variante B — Vault séparé
- Vault = `/srv/gapc/vault/`, repo = `/srv/gapc/repo/`
Inconvénient : plus de confusion (chemins, backups)

---

## 3) Comptes & rôles (moindre privilège)
- `gapc-admin` : admin (ssh, maintenance)
- `anythingllm` : compte service **sans sudo**, lecture seule sur le Vault

Si Docker :
- bind-mount du Vault en `:ro` dans le conteneur AnythingLLM.

---

## 4) Sécurité minimale (P1)
- SSH : clé recommandée, root login désactivé si possible
- No secrets : `.env` ignoré, jamais commité
- AnythingLLM : read-only prouvé par un test d’écriture KO

---

## 5) Next step
Choisir Variante A ou B, puis appliquer `HOSTING_02_BACKUPRSYNC`.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
