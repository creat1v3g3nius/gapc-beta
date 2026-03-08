---
id: HOSTING_03_OPERATION_MONITORING
type: PATCH
title: HostingOperationsMonitoring
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [hosting, operation-monitoring, patch, system]
depends_on: [HOSTING_01_TARGET_ARCHITECTURE]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_20_PATCH/PATCH_00_HOSTING
---

# HOSTING_03 — Operations & Monitoring (P1)

Routine simple pour éviter :
- disque plein,
- backup silencieusement cassé,
- corruption non détectée,
- mauvaise surprise le jour d’une restauration.

---

## 1) Routine quotidienne (2 minutes)
- [ ] Timer/cron OK (backup a tourné)
- [ ] Log rsync du jour présent
- [ ] Espace disque OK

Commandes :
```bash
systemctl --no-pager status gapc-backup.timer || true
ls -lh /srv/gapc/logs | tail
df -h
```

---

## 2) Routine hebdomadaire (10 minutes)
- [ ] dry-run rsync ≈ 0 changements (hors logs)
- [ ] tailles D1 vs D2 cohérentes
```bash
rsync -aHAX --delete --dry-run /srv/gapc/ /mnt/d2/gapc_backup/srv_gapc_mirror/
du -sh /srv/gapc /mnt/d2/gapc_backup/srv_gapc_mirror
```

---

## 3) Routine mensuelle (30 minutes)
### 3.1 SMART (santé disque)
Installer :
```bash
sudo apt-get update && sudo apt-get install -y smartmontools
```
Vérifier (adapter `/dev/sdX`) :
```bash
sudo smartctl -a /dev/sdX
```

### 3.2 Test restauration (mini)
- restaurer un fichier “canari” depuis D2
- vérifier contenu/hachage

---

## 4) Rotation logs (recommandé)
Mettre `logrotate` sur `/srv/gapc/logs/*.log` :
- quotidien
- garder 14 jours

---

## 5) Next step
Mettre `logrotate` en place et planifier un test restauration mensuel.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
