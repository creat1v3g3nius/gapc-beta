---
id: SCRIPT_07_INSTRUCTIONS_CLAUDE
type: SCRIPT
title: InstructionsAgentClaude
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [system, script, agent, claude, instructions]
depends_on:
  - EVIDENCE_05_ADR_CLAUDE_AGENT
  - META_00_HANDBOOK
  - META_01_OUTPUT_PROTOCOL
  - META_02_SOP_STANDARD_LOOP
  - CONSTRAINT_00_GUARD_RAILS
  - CONSTRAINT_03_SECRETS_POLICY
  - GIT_02_BRANCH_POLICY
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_03_SCRIPT
---

# SCRIPT_07 - Instructions Agent Claude

## Objet

Definir les instructions canoniques de **Claude dans VS Code (Claude Code)**,
agent LLM unique du framework GAPC (`EVIDENCE_05_ADR_CLAUDE_AGENT`).

- Ce document est la **source de verite procedurale** de l agent.
- `CLAUDE.md` (racine du repo) en est la **projection executable**, lue

  automatiquement a chaque session. En cas d ecart, ce document prevaut et
  `CLAUDE.md` est realigne.

Remplace `SCRIPT_03_INSTRUCTIONS_CODEX`.

---

## 1) Modes de session

Le mode est fixe au debut de chaque session. Sans declaration, l agent le
demande avant toute action.

### MENTOR (lecture seule)

- usage : localiser une regle, extraire une checklist, auditer, comparer,

  cadrer un CO,

- Claude Code en **Plan mode** (aucune modification de fichier),
- reponse selon `META_01_OUTPUT_PROTOCOL` : run plan, sources utilisees,

  hypotheses, risques, next step unique,

- `NON TROUVE` + 1 action si l information n existe pas dans les sources

  autorisees.

### EXECUTION

- usage : creer ou modifier des documents et des scripts, lancer les

  controles, preparer les commits,

- diff-first : annoncer fichiers et changements avant de les appliquer,
- aucun commit ni push sans accord explicite de l utilisateur,
- branche `work/<topic>` (`GIT_02_BRANCH_POLICY`), un commit par arc,
- controles avant commit : validator, doc integrity, semantic noise, smoke si

  scripts touches.

---

## 2) Declaration de session (Context Pack)

```txt
Mode: MENTOR | EXECUTION
Package actif: PACKAGE_00_GAPC | PACKAGE_02_STUDIO | ...
Product actif: NA | PRODUCT_NN_<CODE>
CO: NA | CO_NNN
Objectif (1 phrase):
```

---

## 3) Perimetre de lecture (isolation des actifs)

Sources autorisees, dans cet ordre d autorite :

1. `vault/01_CORE/`
2. `vault/02_PACKAGE/<package actif>/`
3. `vault/03_PRODUCT/<product actif>/` (si product actif)
4. `vault/00_SYSTEM/`
5. `vault/99_CACHE/` : consultable pour l historique, jamais une verite

Interdit :

- lire ou citer un autre package ou un autre product que les actifs,
- melanger deux packages ou deux products dans une reponse,
- lire des fichiers client bruts (ils ne doivent pas etre dans le repo).

Une demande portant sur un autre package recoit un refus simple + demande
d isolation (pas `NON TROUVE`).

---

## 4) Invariants (non negociables)

- No-secrets / no-PII : jamais de cle, token, mot de passe ni donnee

  personnelle dans une reponse, un fichier, un commit.

- Confidentialite cloud : l agent est un service externe ; il ne lit que des

  documents texte pseudonymises.

- Pas de regle inventee : toute regle citee vient d un fichier reel, avec

  son ID.

- Pas de decision fantome : decision structurante -> `Decision requise` +

  ADR-lite proposee.

- 1 intention = 1 CO = 1 commit ; plus de 5 fichiers ou 2 arcs -> decouper.
- Un document `FROZEN` ne change que par patch cible + version bump +

  changelog.

---

## 5) Stop conditions

Arreter et demander un arbitrage si :

- la tache touche plusieurs arcs sans decoupage,
- une decision structurante n a pas d ADR-lite,
- un secret ou une donnee personnelle apparait,
- l etat Git est dangereux (rebase ou merge en cours, HEAD detache),
- deux sources se contredisent sans hierarchie applicable.

---

## 6) Mise a jour

Toute modification de ce document impose de realigner `CLAUDE.md` dans le
meme lot, puis de relancer `WORKFLOW_07_TESTS_LLM`.

## Changelog

- v1.0 (14-11-2026) : creation des instructions Claude Code (2 modes).
