---
id: HOSTING_02_BACKUP_RSYNC
type: PATCH
title: HostingBackupRsyncSnapshots
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [hosting, backup-rsync, patch, system]
depends_on:
  - HOSTING_01_TARGET_ARCHITECTURE
  - HOSTING_03_OPERATION_MONITORING
  - HOSTING_04_DISASTER_RECOVERY
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_20_PATCH/PATCH_00_HOSTING
---

# HOSTING_02 - Backup D1→D2 (rsync) + logs + vérification

Mettre en place un backup quotidien **fiable** et **audit-able** de D1 vers D2.

MVP P1 : rsync quotidien + logs + code retour (sans complexité).

---

## 1) Pré-requis

- D2 monté (ex: `/mnt/d2`)
- Dossiers présents :
    - `/srv/gapc/`
    - `/mnt/d2/gapc_backup/`

Créer si absent :

```bash
sudo mkdir -p /srv/gapc /srv/gapc/logs /srv/gapc/scripts
sudo mkdir -p /mnt/d2/gapc_backup/srv_gapc_mirror
```

---

## 2) Script rsync (recommandé)

Créer : `/srv/gapc/scripts/backup_d1_to_d2.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

SRC="/srv/gapc/"
DST="/mnt/d2/gapc_backup/srv_gapc_mirror/"
LOGDIR="/srv/gapc/logs"
LOGFILE="$LOGDIR/rsync_$(date +%F).log"

mkdir -p "$DST" "$LOGDIR"

EXCLUDES=(
  "--exclude=.git/objects/"
  "--exclude=node_modules/"
  "--exclude=.cache/"
  "--exclude=.DS_Store"
  "--exclude=.env"
)

rsync -aHAX --delete --numeric-ids --info=stats2,progress2   "${EXCLUDES[@]}"   "$SRC" "$DST" | tee -a "$LOGFILE"
```

Activer :

```bash
sudo chmod +x /srv/gapc/scripts/backup_d1_to_d2.sh
```

⚠️ Note : `--delete` maintient un miroir.
Si tu veux sécuriser, fais 2 jours de `--dry-run` avant.

---

## 3) Planification (systemd timer recommandé)

Créer `/etc/systemd/system/gapc-backup.service` :

```ini
[Unit]
Description=GAPC backup D1 to D2 (rsync)
[Service]
Type=oneshot
ExecStart=/srv/gapc/scripts/backup_d1_to_d2.sh
```

Créer `/etc/systemd/system/gapc-backup.timer` :

```ini
[Unit]
Description=Run GAPC backup daily
[Timer]
OnCalendar=daily
Persistent=true
[Install]
WantedBy=timers.target
```

Activer :

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gapc-backup.timer
systemctl list-timers | grep gapc || true
```

---

## 4) Vérification (obligatoire)

### 4.1 Quotidien (2 minutes)

```bash
systemctl --no-pager status gapc-backup.timer || true
ls -lh /srv/gapc/logs | tail
df -h
```

### 4.2 Hebdo (dry-run)

```bash
rsync -aHAX --delete --dry-run /srv/gapc/ /mnt/d2/gapc_backup/srv_gapc_mirror/
du -sh /srv/gapc /mnt/d2/gapc_backup/srv_gapc_mirror
```

---

## 5) Restauration rapide

### Fichier

```bash
cp /mnt/d2/gapc_backup/srv_gapc_mirror/path/to/file /srv/gapc/path/to/file
```

### Tout `/srv/gapc` (attention)

1. Stop services (AnythingLLM, timers si besoin)
1. rsync inverse :

```bash
rsync -aHAX --delete /mnt/d2/gapc_backup/srv_gapc_mirror/ /srv/gapc/
```

1. Relancer services
1. Relancer smoke/validator côté repo

---

## 6) Next step

Déployer script + timer, puis vérifier 2 jours (logs + tailles).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
