---
id: LLM_02_PERMISSION_SECURITY
type: LLM
title: PermissionsSecurity
version: v1.1
status: FROZEN
created: 28-02-2026
updated: 02-03-2026
tags: [agent, permission-security, llm, system]
depends_on: [LLM_00_RAG_PRINCIPES, LLM_01_INGESTION_PROTOCOL]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_04_LLM
---

# LLM_02 - Permissions & Sécurité minimale (read-only + hardening)

Garantir que le mentor AnythingLLM (RAG) est **utile** mais **incapable de nuire** au framework GAPC :

- **Lecture seule** sur le Vault (Source of Truth) et, par défaut, sur le repo Git.
- **Principe du moindre privilège** (compte service sans sudo).
- **No-secrets** : aucun secret en clair dans repo/Vault/logs.
- Paramétrage compatible avec le nouveau modèle (arcs `00_SYSTEM/01_CORE/02_PACKAGE/03_PRODUCT/04_CACHE`).

Ce document complète :
- `LLM_00_RAG_PRINCIPES` (contrat mentor) fileciteturn20file2
- `LLM_01_INGESTION_PROTOCOL` (workspaces + couches + tests) fileciteturn20file1
- ancien runbook permissions (référence) fileciteturn20file0

---

## 1) Modèle de menace (simple)

### Menaces à couvrir (P0)
- AnythingLLM peut **écrire** dans le Vault → corruption Source of Truth.
- AnythingLLM peut **modifier** le repo → backdoor / scripts falsifiés.
- Logs contiennent **PII/secrets** → fuite.
- Mauvaise config RAG → mélange packages/products (dérive).

### Non-objectifs (P2)
- Hardening “enterprise” complet (SIEM, IAM avancé).
- Isolation réseau avancée (à traiter plus tard si nécessaire).

---

## 2) Principes non négociables (P0)

1. **Read-only** pour AnythingLLM sur le Vault (toujours).
2. **Compte service dédié** (sans sudo).
3. **No-secrets** : secrets hors repo/Vault, via variables d’environnement + `.env` ignoré.
4. **Droits minimaux** : AnythingLLM lit uniquement les dossiers nécessaires au workspace actif (RulesOnly/PackageScoped/ProductScoped).
5. **Preuves** : test d’écriture KO documenté (commande + résultat).

---

## 3) Comptes & rôles (P0)

### 3.1) Comptes recommandés
- `gapc-admin` : admin (sudo), propriétaire du repo/vault
- `anythingllm` : service (sans sudo)

Création (Linux) :
```bash
sudo adduser --disabled-password --gecos "" anythingllm
```

Règle : le service n’a **jamais** besoin d’écrire dans le Vault.

---

## 4) Read-only Vault (P0) — 2 options

### Option A — Docker bind mount `:ro` (recommandé)
Si AnythingLLM tourne en conteneur, monter le Vault en lecture seule :

```txt
-v /srv/gapc/repo/vault:/data/vault:ro
```

Avantage : même si permissions UNIX sont mal réglées, le conteneur ne peut pas écrire.

### Option B — Permissions UNIX (complément)
Objectif : `gapc-admin` écrit, `anythingllm` lit.

Exemple (à adapter à ton chemin) :
```bash
sudo chown -R gapc-admin:gapc-admin /srv/gapc/repo/vault
sudo chmod -R u=rwX,go=rX /srv/gapc/repo/vault
```

Version plus stricte (recommandée) :
- créer un groupe `gapc-readers`,
- ajouter `anythingllm` au groupe,
- retirer lecture “others” si besoin.

---

## 5) Read-only repo Git (P1 recommandé)

Le repo contient scripts/outillage. Par défaut :
- AnythingLLM **n’a pas besoin** d’y écrire.
- Il peut lire certains fichiers (runbooks, prompt system) si tu les ingères.

Approche :
- soit tu montes le repo en lecture seule (`:ro`) côté conteneur,
- soit tu limites les permissions UNIX (lecture groupe).

---

## 6) Tests de vérification (P0)

### 6.1) Test d’écriture Vault (doit échouer)
```bash
sudo -u anythingllm touch /srv/gapc/repo/vault/_WRITE_TEST || echo "OK: no write"
```

Attendu :
- création impossible → **OK**

Supprimer le fichier test si jamais il a été créé.

### 6.2) Test d’accès lecture (doit réussir)
```bash
sudo -u anythingllm ls /srv/gapc/repo/vault/00_SYSTEM >/dev/null && echo "OK: can read"
```

---

## 7) Gestion des secrets (P0)

### Interdits
- tokens, clés API, mots de passe dans :
  - `vault/`
  - `repo/`
  - `scripts/`
  - logs
  - commits

### Pattern attendu
- `.env` local + `.gitignore`
- `.env.example` commitable (sans secret)
- variables d’environnement injectées au runtime (Docker/OS)

Checklist rapide :
- [ ] `.env` ignoré
- [ ] aucun secret dans `git diff`
- [ ] logs nettoyés (pas de PII)

---

## 8) Logs & données sensibles (P0/P1)

### P0 — Règles
- logs “utiles” mais **sans PII**
- ne pas logger des contenus entiers de documents si non nécessaire
- tronquer les erreurs (ex: 10 lignes max) dans les notes d’incident

### P1 — Rétention
- rotation des logs (si service long-running)
- suppression périodique des fichiers temporaires

---

## 9) RAG scope & isolation (P0)

Même avec read-only, le risque principal reste la **dérive** (mélange sources).

Règles :
- **Workspaces** : RulesOnly / PackageScoped / ProductScoped (`LLM_01_INGESTION`) fileciteturn20file1
- 1 seul **package actif** par workspace
- 1 seul **product actif** par workspace

Contrôle :
- tests “NON TROUVÉ” sur packages/products non actifs (batterie RUN_01/LLM_01)

---

## 10) Hardening serveur minimal (P1)

Si AnythingLLM tourne sur une VM/serveur :

### 10.1) SSH hardening (P1)
- Auth par clé (recommandé)
- Désactiver login root
- Désactiver password auth (si clé fonctionnelle)

`/etc/ssh/sshd_config` (extraits) :
```txt
PermitRootLogin no
PasswordAuthentication no
```

Puis :
```bash
sudo systemctl restart ssh
```

### 10.2 Firewall minimal (P1)
Exemple UFW :
```bash
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
```

---

## 11) Checklist READY_TO_FREEZE (sécurité)

- [ ] Vault monté en read-only côté service (ou permissions prouvées)
- [ ] Compte `anythingllm` sans sudo
- [ ] Test écriture KO documenté
- [ ] No-secrets appliqué (.env ignoré)
- [ ] Workspaces définis + tests RAG pass
- [ ] Procédure incident (si RAG dérive) connue

---

## Next step
1) Choisir Option A (Docker `:ro`) si possible, sinon Option B (permissions UNIX).  
2) Exécuter les **tests 6.1/6.2** et consigner le résultat dans une note de config.

---

### 12) Changelog
- v1.0 (28-02-2026) : contrat mentor (LLM_00), read-only Vault + no-secrets + hardening minimal.

---

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 : READY_TO_FREEZE.
