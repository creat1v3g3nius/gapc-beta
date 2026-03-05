---
id: ASSO_INDEX_00_PACKAGE
type: INDEX
title: AssoPackageNavigationIndex
version: v1.1
status: FROZEN
created: 05-03-2026
updated: 05-03-2026
tags: ['asso', 'package', 'index', 'navigation']
depends_on: []
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_01_ASSO/ASSO_00_INDEX
---

# ASSO_INDEX_00 — Navigation Package

## Objet

Point d’entrée du **PACKAGE_01_ASSO** (overlay métier “association”).

Le PACKAGE contient :
- des **overlays** (règles métier spécifiques, sans duplication du CORE)
- des **add-ons** (templates, checklists, extensions) propres au métier
- des **allowlists** et politiques spécifiques (sources, communication, données)

---

## ASSO_INDEX_00 - Package Navigation

### INDEX
[[ASSO_INDEX_01_META]] · [[ASSO_INDEX_02_DISCIPLINE]] · [[ASSO_INDEX_03_CONSTRAINT]] · [[ASSO_INDEX_04_TOOLING]]

---

### META
[[ASSO_META_00_PACKAGE_PROFILE]] : Profil du package - périmètre, overlays, add-ons, invariants P0.
[[ASSO_META_01_DOMAIN_DEFINITIONS]] : Définitions métier et lexique de base (association, CA, bureau, adhérents…).`

---

### DISCIPLINE
[[ASSO_DISCIPLINE_00_RAG_PROFILE]] : Profil RAG métier association (priorités, garde-fous, anti-invention).
[[ASSO_DISCIPLINE_01_GEL_RULES]] : Règles de gel (READY_TO_FREEZE / FROZEN), versioning, amendements pour ASSO.
[[ASSO_DISCIPLINE_02_RAG_QG]] : Quality gates RAG (P0/P1/P2) spécialisés pour les livrables ASSO.
[[ASSO_DISCIPLINE_03_LEXICAL_QG]] : Quality gates lexicaux : ton, vocabulaire, clarté, neutralité, conformité rédactionnelle.
[[ASSO_DISCIPLINE_04_SCOPE_CLASSIFIER]] : Classifieur de scope (CORE/SYSTEM/PACKAGE/PRODUCT/CACHE) + priorisation NOW/NEXT/LATER.
[[ASSO_DISCIPLINE_05_RISK_REGISTER]] : Registre de risques : identification, mitigations, contrôles, owners.

---

### CONSTRAINT
[[ASSO_CONSTRAINT_00_ALLOW_LIST]] : Allowlist métier : sources, outils, formats explicitement autorisés.
[[ASSO_CONSTRAINT_01_LEGAL_BASELINE_1901]] : Baseline juridique (cadre loi 1901) : points d’attention, invariants rédactionnels.
[[ASSO_CONSTRAINT_02_PUBLIC_MESSAGING_POLICY]] : Politique de communication publique : prudence, vérifiabilité, pas d’allégations non sourcées.
[[ASSO_CONSTRAINT_03_CONFLICT_OF_INTEREST_POLICY]] : Politique conflits d’intérêts : séparation asso / intérêts privés, transparence.
[[ASSO_CONSTRAINT_04_DATA_PRIVACY_POLICY]] : Politique données & confidentialité : minimisation, pas de PII, traitements cadrés.
[[ASSO_CONSTRAINT_05_SOURCES_POLICY]] : Politique de sources : ordre de priorité, exclusions, conditions d’usage.
[[ASSO_CONSTRAINT_99_EXCEPTION_POLICY]] : Politique d’exception : comment déroger, traçabilité, validations requises.

---

### TOOLING (navigation par famille)

> Objectif : naviguer **directement** vers chaque fichier de TOOLING, groupé par famille.

#### KNOWLEDGE
[[ASSO_KNOWLEDGE_01_GLOSSARY]] : Glossaire opérationnel ASSO (termes, définitions, usage).

#### TPL
[[ASSO_TPL_00_STRUCTURED_DOC_CANON]] : Canon de document structuré (trames/sections) pour livrables ASSO.

#### PIPELINE
- (vide)

#### CHECKLIST
[[ASSO_CHECKLIST_01_READY_TO_FREEZE_ADDON]] : Checklist add-on passage READY_TO_FREEZE (DocQG / risques).

#### EXTENSION
- (vide)

## Amendements (FROZEN)

Modifications uniquement via patch ciblé + validation + version bump.

## Changelog
- v1.1 (05-03-2026) : passage en FROZEN.
- v1.0 (05-03-2026) : création index PACKAGE du PACKAGE_01_ASSO.