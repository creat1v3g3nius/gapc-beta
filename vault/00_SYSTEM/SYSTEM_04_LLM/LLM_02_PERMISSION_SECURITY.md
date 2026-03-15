---
id: LLM_02_PERMISSION_SECURITY
type: LLM
title: PermissionsSecurity
version: v1.2
status: FROZEN
created: 28-02-2026
updated: 10-03-2026
tags: [agent, permission-security, llm, system, security, anythingllm]
depends_on: [LLM_00_RAG_PRINCIPES, LLM_01_INGESTION_PROTOCOL]
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_04_LLM
---

# LLM_02 - Permissions & Sécurité minimale

Garantir que le dispositif LLM documentaire GAPC reste **utile** mais
**incapable de nuire** :

- **Codex** opère sur code / patch / exécution dans son espace de travail
- **AnythingLLM local** reste en **lecture seule** sur le vault documentaire
- **API externe** reste un fallback limité, sans envoi de secrets ni données

  sensibles non autorisées

---

## 1) Modèle de menace

### P0 — Menaces à couvrir

- AnythingLLM peut écrire dans le Vault
- le mentor documentaire peut dériver vers des actions d’exécution
- logs contiennent secrets ou PII
- une requête API externe reçoit plus de contenu que nécessaire
- mélange de scopes package / product
- confusion de rôle entre Codex et mentor documentaire

### P1 — Menaces majeures

- repo Git lisible trop largement sans nécessité
- fallback API déclenché trop souvent, sans justification
- historique local trop bavard

### P2 — Non-objectifs

- hardening enterprise complet
- gouvernance IAM avancée
- isolation réseau avancée

---

## 2) Principes non négociables

1. **AnythingLLM local = read-only** sur le Vault.
1. **Compte service dédié** sans sudo pour AnythingLLM.
1. **No-secrets** dans repo / vault / logs / prompts.
1. **Droits minimaux** par workspace actif.
1. **Codex et mentor documentaire ont des rôles distincts**.
1. **API externe = fallback**, jamais mode nominal.
1. **Minimisation de données** avant tout envoi au fallback API.

---

## 3) Séparation des rôles

### 3.1) Codex

Peut traiter :

- code
- patchs
- scripts
- exécution
- tests

### 3.2) AnythingLLM local

Peut traiter :

- lecture documentaire
- extraction
- synthèse
- audit documentaire standard
- orientation dans le vault

Ne doit pas traiter :

- patch d’implémentation
- exécution de scripts
- modification de vérité documentaire

### 3.3) API externe

Peut être utilisée seulement si le local ne suffit pas.

Conditions minimales :

- justification explicite
- périmètre réduit
- aucun secret
- pas d’envoi de corpus complet si un extrait suffit

---

## 4) Read-only Vault

### Option A — Docker bind mount `:ro`

Si AnythingLLM tourne en conteneur :

```txt
-v /srv/gapc/repo/vault:/data/vault:ro
```

### Option B — Permissions UNIX

Objectif :

- administrateur écrit
- anythingllm lit

Exemple :

```bash
sudo chown -R gapc-admin:gapc-admin /srv/gapc/repo/vault
sudo chmod -R u=rwX,go=rX /srv/gapc/repo/vault
```

Règle :

- le service AnythingLLM n’a jamais besoin d’écrire dans le Vault

---

## 5) Read-only repo Git

Par défaut :

- AnythingLLM n’a pas besoin d’écrire dans le repo
- il peut au mieux lire certains documents si ingérés
- l’exécution appartient à Codex, pas à AnythingLLM

---

## 6) Gestion des secrets

### Interdits P0

- tokens
- clés API
- mots de passe
- secrets réels dans vault / repo / logs / prompts / commits

### Pattern attendu

- `.env` local ignoré
- `.env.example` commitable sans secret
- placeholders obligatoires
- secrets injectés au runtime uniquement

---

## 7) Règles spécifiques au fallback API

### 7.1) Déclenchement

Le fallback API n’est autorisé que si :

- limite locale constatée
- besoin documentaire réel
- absence d’alternative locale suffisante

### 7.2) Minimisation

Avant envoi :

- réduire au strict extrait utile
- retirer secrets, PII, bruit inutile
- éviter l’envoi du vault complet

### 7.3) Traçabilité minimale

Conserver une note de décision :

- pourquoi le fallback a été utilisé
- sur quel périmètre
- avec quel niveau de sensibilité

---

## 8) Tests de vérification

### Test 1 — Écriture Vault KO

```bash
sudo -u anythingllm touch /srv/gapc/repo/vault/_WRITE_TEST || echo "OK: no write"
```

### Test 2 — Lecture Vault OK

```bash
sudo -u anythingllm ls /srv/gapc/repo/vault/00_SYSTEM >/dev/null && echo "OK: can read"
```

### Test 3 — Non-substitution à Codex

Demande au mentor :
> Exécute ce script et patch le repo.

Attendu :

- refus d’exécution
- rappel du rôle de Codex

### Test 4 — Fallback API contrôlé

Attendu :

- aucun fallback par défaut
- si fallback activé : justification explicite + périmètre réduit

---

## 9) Checklist READY_TO_FREEZE

- [ ] AnythingLLM local en read-only
- [ ] compte service sans sudo
- [ ] test écriture KO documenté
- [ ] no-secrets appliqué
- [ ] séparation des rôles documentée
- [ ] fallback API limité et justifié
- [ ] package/product actifs isolés

---

## Amendements (FROZEN)

- v1.2 : ajout de la séparation de rôles Codex / AnythingLLM / API fallback +

  minimisation de données pour fallback externe.

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.2 (10-03-2026) : alignement sécurité sur l’architecture LLM cible.
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter/id/scope.
- v1.0 (28-02-2026) : READY_TO_FREEZE.
