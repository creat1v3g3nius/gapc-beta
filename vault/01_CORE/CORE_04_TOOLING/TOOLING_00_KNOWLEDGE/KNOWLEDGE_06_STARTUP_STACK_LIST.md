---
id: KNOWLEDGE_06_STARTUP_STACK_LIST
type: TOOLING
title: StartupStackList
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, startup-stack, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_06 — Startup Stack List (référentiel) (CORE)

## Objet
Liste de composants “stack” (par catégorie) pour construire un produit rapidement, avec garde-fous no-secrets.

---

## 1) Frontend
- Web SPA (React/Vue/Svelte) — UI rapide.
- SSR/Fullstack (Next/Nuxt) — SEO + perf.
- Mobile (React Native/Flutter) — cross-platform.

## 2) Backend
- API (FastAPI/Node/Nest/Django) — services.
- Auth (OIDC, JWT) — attention no-secrets.
- Jobs/Queue (Redis/RabbitMQ) — asynchrone.

## 3) Data
- SQL (Postgres) — standard.
- Cache (Redis) — perf.
- Search (OpenSearch/Meilisearch) — recherche.

## 4) Hosting / Ops
- Container (Docker) — reproductible.
- PaaS (Render/Fly/Heroku-like) — rapide.
- Observabilité (logs/metrics/traces) — minimal.

## 5) Analytics / Monitoring
- Product analytics (self-host ou SaaS) — attention PII.
- Error tracking — alerting.

## 6) Paiement (si besoin)
- PSP (Stripe-like) — conformité.

## 7) Red flags
- Ajouter 10 services “par défaut” (scope creep).
- Logs contenant PII.
- Secrets dans repo (clés, tokens).

### Extensions PACKAGE/PRODUCT
- Définir une stack autorisée + rubrics de choix.
- Ajouter des exigences légales/compliance.

---

## Changelog
- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)
- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
