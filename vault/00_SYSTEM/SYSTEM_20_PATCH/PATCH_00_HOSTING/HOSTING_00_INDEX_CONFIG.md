---
id: HOSTING_00_INDEX_CONFIG
type: PATCH
title: HostingConfigIndex
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [hosting, index, patch, system]
depends_on: [LLM_02_PERMISSION_SECURITY, SCRIPT_01_SMOKE_RUNNER, SCRIPT_00_VALIDATOR]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_20_PATCH/PATCH_00_HOSTING
---

# HOSTING_00 - Index configuration (D1/D2)

Ce patch (P1) documente la mise en place d’un **serveur d’hébergement externe** pour le framework GAPC :
- D1 = disque principal (repo + vault + services)
- D2 = disque de backup (miroir rsync quotidien + vérifications)
- AnythingLLM = **read-only** sur le Vault

**No secrets** : aucune clé/token/PII dans le Vault/repo/logs.

---

## 1) Documents (ordre recommandé)
1) `HOSTING_01_TARGET_ARCHITECTURE` — architecture cible (chemins + rôles)  
2) `HOSTING_02_BACKUP_RSYNC` — rsync quotidien + logs + vérifs  
3) `HOSTING_03_OPERATION_MONITORING` — routine monitoring/maintenance  
4) `HOSTING_04_DISASTER_RECOVERY` — scénarios + restauration  
5) `HOSTING_05_SERVER_BACKUP` — checklist santé backup

---

## 2) Definition of Done (P1 Hosting)
- [ ] Chemins standardisés (`/srv/gapc`)
- [ ] Repo + Vault présents (Vault recommandé dans `repo/vault/`)
- [ ] rsync D1→D2 quotidien (timer/cron) + logs + exit codes
- [ ] Vérif hebdo (dry-run) ≈ 0 changements (hors logs)
- [ ] AnythingLLM **read-only** prouvé (test écriture KO)
- [ ] Runbook restauration testé au moins 1 fois (fichier “canari”)

---

## 3) Next step
Appliquer `HOSTING_01_TARGET`, puis `HOSTING_02_BACKUPRSYNC`.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
