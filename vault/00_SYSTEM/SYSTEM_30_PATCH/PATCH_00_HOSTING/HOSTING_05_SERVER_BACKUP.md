---
id: HOSTING_05_SERVER_BACKUP
type: PATCH
title: HostingServerBackupHealth
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [hosting, server-backup, patch, system]
depends_on:
  - HOSTING_02_BACKUP_RSYNC
  - HOSTING_03_OPERATION_MONITORING
  - HOSTING_04_DISASTER_RECOVERY
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_20_PATCH/PATCH_00_HOSTING
---

# HOSTING_05 - Checklist santé backup (P1)

En 5–10 minutes, vérifier :

- backup tourne,
- D2 est à jour,
- AnythingLLM ne peut pas écrire dans le Vault,
- espace disque OK.

---

## 1) Backup quotidien

- [ ] Timer/cron OK (dernier run)
- [ ] Log rsync présent (date du jour)
- [ ] Code retour OK

Commandes :

```bash
systemctl --no-pager status gapc-backup.timer || true
ls -lh /srv/gapc/logs | tail
df -h
```

---

## 2) Vérification hebdo (dry-run)

- [ ] dry-run ≈ 0 changements (hors logs)

```bash
rsync -aHAX --delete --dry-run /srv/gapc/ /mnt/d2/gapc_backup/srv_gapc_mirror/
```

---

## 3) Permissions AnythingLLM (read-only)

- [ ] Test écriture KO :

```bash
sudo -u anythingllm touch /srv/gapc/repo/vault/_WRITE_TEST || echo "OK: no write"
```

Si le fichier est créé : supprimer et corriger permissions/mount `:ro`.

---

## 4) Santé disque (mensuel)

- [ ] SMART check OK (`smartctl`)
- [ ] marge espace disque ≥ 15%

---

## 5) Verdict

- OK : backup + logs + read-only + espace OK
- KO : corriger immédiatement (sinon dette OPS)

---

## 6) Next step

Planifier un rappel hebdo (dry-run)
et mensuel (SMART + test restauration canari).

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
