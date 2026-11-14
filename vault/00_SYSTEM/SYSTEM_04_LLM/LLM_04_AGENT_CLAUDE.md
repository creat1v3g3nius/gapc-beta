---
id: LLM_04_AGENT_CLAUDE
type: LLM
title: AgentClaudeSetup
version: v1.1
status: FROZEN
created: 14-11-2026
updated: 14-11-2026
tags: [system, llm, agent, claude, security]
depends_on:
  - EVIDENCE_05_ADR_CLAUDE_AGENT
  - SCRIPT_07_INSTRUCTIONS_CLAUDE
  - META_00_HANDBOOK
  - CONSTRAINT_03_SECRETS_POLICY
  - WORKFLOW_07_TESTS_LLM
  - WORKFLOW_08_TESTS_EXECUTION
arc: SYSTEM
scope: vault/00_SYSTEM/SYSTEM_04_LLM
---

# LLM_04 - Agent Claude Setup

## Objet

Decrire le dispositif LLM nominal de GAPC : **Claude dans VS Code (Claude
Code)**, agent unique en 2 modes (`EVIDENCE_05_ADR_CLAUDE_AGENT`).
Remplace `LLM_00_RAG_PRINCIPES`, `LLM_01_INGESTION_PROTOCOL`,
`LLM_02_PERMISSION_SECURITY` et `LLM_03_MENTOR_UTILITES` (archives).

---

## 1) Architecture

- **Obsidian (vault)** : source de verite documentaire.
- **VS Code + Git** : execution, ouvert sur le dossier `repo/`.
- **Claude Code** : agent LLM unique.

  - instructions : `CLAUDE.md` (racine du repo), projection de

    `SCRIPT_07_INSTRUCTIONS_CLAUDE`,

  - mode **MENTOR** = Plan mode (lecture seule),
  - mode **EXECUTION** = mode normal, chaque ecriture et commande soumise a

    approbation.

---

## 2) Chargement des regles (remplace l ingestion)

- `CLAUDE.md` est lu automatiquement au demarrage d une session ouverte sur

  `repo/`.

- L agent lit ensuite les sources a la demande, dans le perimetre declare

  (CORE -> package actif -> product actif -> SYSTEM).

- Les profils de perimetre restent ceux du CORE : `RulesOnly` (aucun package),

  `PackageScoped` (1 package), `ProductScoped` (1 package + 1 product).

- Un changement de package ou de product actif = nouvelle session.

---

## 3) Securite et permissions

- **Ecriture** : interdite en Plan mode ; en mode normal, chaque modification

  et chaque commande est approuvee par l utilisateur.

- **Ne jamais activer** l acceptation automatique des modifications ni un mode

  qui contourne les approbations pour une session GAPC.

- **Git** : l agent ne commit ni ne push sans accord explicite ; le hook

  `pre-push` reste le dernier controle.

- **Secrets** : `.env` ignore par Git ; l agent ne lit pas les fichiers de

  secrets.

---

## 4) Confidentialite (agent heberge)

- Tout ce que lit l agent est envoye au service Claude.
- Le repo ne contient que des documents texte pseudonymises

  (`CONSTRAINT_03_SECRETS_POLICY`, contraintes de confidentialite du package
  actif).

- Aucun fichier client brut, aucun export de messagerie, aucune donnee

  personnelle dans le perimetre de lecture.

---

## 5) Qualification

- mode MENTOR : `WORKFLOW_07_TESTS_LLM`,
- mode EXECUTION : `WORKFLOW_08_TESTS_EXECUTION`,
- a relancer apres toute modification de `CLAUDE.md`, de

  `SCRIPT_07_INSTRUCTIONS_CLAUDE` ou d un document `META_*` du CORE.

## Amendements (FROZEN)

- Modifications uniquement via patch ciblé + validation + version bump.

## Changelog

- v1.1 (14-11-2026) : passage en FROZEN apres qualification Claude PASS (`EVIDENCE_SAMPLE_08_CLAUDE_QUALIFICATION`).

- v1.0 (14-11-2026) : creation du dispositif Claude Code (remplace LLM_00..03).
