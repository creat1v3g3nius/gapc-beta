---
id: BETA_GAPC_ACTION_DOC_00_DOD
type: ACTION
title: GapcBetaActionDocDodRemediation
version: v1.3
status: READY_TO_FREEZE
created: 06-03-2026
updated: 06-03-2026
tags: [product, gapcbeta, action, dod, remediation]
depends_on: [BETA_GAPC_CO_00_DOD, BETA_GAPC_ADR_00_DOD_SCOPE, GAPC_VAULT_HEALTH_CHECK]
arc: PRODUCT
scope: vault/03_PRODUCT/PRODUCT_00_BETA_GAPC/BETA_GAPC_03_EVIDENCE
---

# BETA_GAPC_ACTION_DOC_00_DOD

## Actions Executees
1. Conformite DocQG alignee sur tout `vault/` (`id==filename`, `title` UpperCamelCase, arc/scope coherents).
2. References `depends_on` mises a jour vers `BETA_GAPC_COMPOSANTS_BACKLOG`.
3. Pack evidence thin-slice cree sous `BETA_GAPC_03_EVIDENCE`.
4. Registre risques product instancie.
5. Health check vault execute et integre au lot evidence.
6. Rerun DoD_00 global execute et confirme (validator strict global PASS).

## Commandes Executees
```bash
./scripts/ValidateFrontmatter.py --strict --enforce-unique-ids --vault vault
./scripts/SmokeRunner.py
git status --short --branch
git push --dry-run
```

## Critere de Cloture
- PASS strict sur l'ensemble du vault.
- PASS smoke runner.
- GAPC_VAULT_HEALTH verifie et trace dans `GAPC_VAULT_HEALTH_CHECK`.
- Risques R-0001 / R-0005 / R-0009 clotures.

## Next Step Unique
- Executer le plan smoke dans `BETA_GAPC_TESTPLAN_00_SMOKE_DOD`.

## Changelog
- v1.1 (06-03-2026) : integre l'execution du vault health check dans les actions et criteres.
- v1.2 (06-03-2026) : bascule execution/critere DocQG vers scope global `vault/`.
- v1.3 (06-03-2026) : ajoute la preuve de rerun DOD_00 global et la cloture des risques.
