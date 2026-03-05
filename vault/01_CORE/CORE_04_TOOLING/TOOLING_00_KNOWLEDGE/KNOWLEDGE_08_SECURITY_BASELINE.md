---
id: KNOWLEDGE_08_SECURITY_BASELINE
type: TOOLING
title: SecurityBaseline
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, security-baseline, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_08 — Security Baseline (référentiel) (CORE)

## Objet
Baseline sécurité (liste) pour éviter les erreurs classiques.  
Pas de procédure : seulement des points de contrôle.

---

## 1) Secrets
- Secrets hors repo/vault.
- Rotation possible.
- Aucun secret dans logs/exemples.

## 2) Permissions
- Moindre privilège (comptes dédiés).
- Read-only quand possible (mentor RAG).

## 3) Logs
- Pas de PII.
- Rétention limitée.
- Messages d’erreur actionnables (sans fuite).

## 4) Dépendances
- Limiter les dépendances.
- Traçabilité des décisions (ADR si structurant).

## 5) Backup / Restauration
- Backup régulier.
- Test restauration périodique.

## 6) Red flags
- `.env` tracké.
- Tokens dans tickets/docs.
- Copie de données perso en test.

### Extensions PACKAGE/PRODUCT
- Ajouter exigences légales locales (asso).
- Ajouter checklists opérateur (en SYSTEM).

---

## Changelog
- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
