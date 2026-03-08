---
id: OPS_03_TESTPLAN_SMOKE_DOD
type: TESTPLAN
title: GapcBetaTestplanSmokeDod
version: v1.2
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, testplan, smoke, dod, p0]
depends_on: [OPS_02_SPEC_DOD, TPL_04_TEST_PLAN_SMOKE, RUN_06_VAULT_HEALTH_CHECK]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# OPS_03_TESTPLAN_SMOKE_DOD

## Perimetre
- Artefact: `BETA_GAPC_03_EVIDENCE` + backlog composants.
- Environnement: repo local dans VS Code terminal.
- Pre-requis: scripts validator/smoke executables.

## Scenarios P0
### S1 - Validator strict vault global
- Steps:
  1. Lancer `./scripts/ValidateFrontmatter.py --strict --enforce-unique-ids --vault vault`.
- Expected: sortie `PASS validated`.
- PASS/FAIL: PASS.

### S2 - Smoke runner repository
- Steps:
  1. Lancer `./scripts/SmokeRunner.py`.
- Expected: sortie `PASS smoke runner`.
- PASS/FAIL: PASS.

### S3 - Vault health check rapide
- Steps:
  1. Lancer `git status --short --branch`.
  2. Lancer `git push --dry-run`.
  3. Lancer `./scripts/ValidateFrontmatter.py --strict --enforce-unique-ids --vault vault`.
  4. Lancer `./scripts/SmokeRunner.py`.
- Expected: pas de fichier en attente, dry-run OK, validator PASS, smoke PASS.
- PASS/FAIL: PASS.

## Donnees de Test
- Dataset: fichiers markdown du product beta.
- Contraintes: no-secrets / no-PII.

## Observabilite
- Signaux PASS: code retour 0 + sorties PASS.
- Signaux FAIL: erreurs frontmatter, missing files, exit code != 0.

## Backout Plan
- Revert du commit thin-slice remediation si regression.

## Next Step Unique
- Produire la revue finale dans `EVIDENCE_01_REVIEW_DOD`.

## Changelog
- v1.1 (06-03-2026) : ajoute le scenario S3 de health check vault et sa reference.
- v1.2 (06-03-2026) : aligne S1/S3 sur validator strict global `vault/`.
