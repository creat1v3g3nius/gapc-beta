---
id: HOSTING_04_DISASTER_RECOVERY
type: PATCH
title: HostingDisasterRecoveryRunbook
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [hosting, disaster-recovery, patch, system]
depends_on: [HOSTING_02_BACKUP_RSYNC, HOSTING_03_OPERATION_MONITORING]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_20_PATCH/PATCH_00_HOSTING
---

# HOSTING_04 — Disaster Recovery (P1)

Procédure de restauration en cas de :

- suppression accidentelle,
- perte D1,
- perte D2,
- corruption répliquée.

Définitions :

- **RPO** cible : ≤ 24h (backup quotidien)
- **RTO** cible : 2–4h (selon volume et débit)

---

## 1) Scénario A — fichier supprimé sur D1

1) Identifier le chemin dans le miroir D2
2) Copier vers D1
3) Si repo Git : commit “restore”

```bash
cp /mnt/d2/gapc_backup/srv_gapc_mirror/srv/gapc/repo/vault/path/to/doc.md    /srv/gapc/repo/vault/path/to/doc.md
```

---

## 2) Scénario B — D1 perdu (disque HS)

1) Remplacer D1 + monter `/srv/gapc`
2) Restaurer depuis D2 :

```bash
rsync -aHAX /mnt/d2/gapc_backup/srv_gapc_mirror/ /srv/gapc/
```

3) Reconfigurer services (AnythingLLM, timers)
4) Vérifier :
- `git status` dans `/srv/gapc/repo`
- smoke/validator

---

## 3) Scénario C — D2 perdu (backup HS)

1) Remplacer D2 + remonter `/mnt/d2`
2) Recréer dossier :

```bash
mkdir -p /mnt/d2/gapc_backup/srv_gapc_mirror
```

3) Lancer rsync manuel :

```bash
/srv/gapc/scripts/backup_d1_to_d2.sh
```

---

## 4) Scénario D — corruption répliquée (effet `--delete`)

Mitigations :

- snapshots FS (si maîtrisé)
- tags Git “freeze”
- test restauration mensuel (canari)

---

## 5) Checklist post-incident

- [ ] Backup rétabli (timer OK)
- [ ] Espace disque OK
- [ ] Services OK (AnythingLLM)
- [ ] Repo “green” (smoke/validator)
- [ ] Note d’incident (cause → action corrective)

---

## 6) Next step

Faire un test restauration contrôlé (fichier canari),
puis consigner le résultat.

---

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
