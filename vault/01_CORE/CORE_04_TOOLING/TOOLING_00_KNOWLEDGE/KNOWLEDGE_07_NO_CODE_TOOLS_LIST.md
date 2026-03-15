---
id: KNOWLEDGE_07_NO_CODE_TOOLS_LIST
type: TOOLING
title: NoCodeToolsList
version: v1.1
status: FROZEN
created: 01-03-2026
updated: 02-03-2026
tags: [tooling, knowledge, nocode-tools, core]
depends_on: []
arc: CORE
scope: vault/01_CORE/CORE_04_TOOLING/TOOLING_00_KNOWLEDGE
---

# KNOWLEDGE_07 — No-Code Tools List (CORE)

## Objet

Référentiel de familles d’outils no-code/low-code (choix rapide), avec
garde-fous anti-dérive.

---

## 1) Bases / tables

- Airtable-like — table+views.
- Spreadsheets — simple, attention PII.

## 2) Automatisation

- Make / Zapier-like — workflows.
- n8n — automation self-host.

## 3) CMS / sites

- Webflow-like — site.
- Headless CMS — contenu structuré.

## 4) Docs / Knowledge

- Notion-like — docs + DB (attention duplication vs Vault).
- Obsidian — Vault (SOT dans GAPC).

## 5) Formulaires

- Typeform-like — collecte (attention PII).

## 6)Red flags

- Stocker la SOT dans 2 outils en parallèle (duplication).
- Dépendance forte à un SaaS sans export.
- Collecte PII sans politique.

### Extensions PACKAGE/PRODUCT

- Liste des outils autorisés + règles de gouvernance.
- Templates de workflow (en SYSTEM).

---

## Changelog

- v1.0 (01-03-2026) : version minimale.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (02-03-2026) : passage en FROZEN + normalisation frontmatter.
