---
id: BACKLOG_01_SYSTEM_RUN_SETUP_PRODUCT
type: BACKLOG
title: SystemRunSetupProductMigrationBacklog
version: v1.13
status: DEPRECATED
created: 13-03-2026
updated: 13-03-2026
tags: [system, backlog, workflow, setup-product, migration, multi-product, cache, deprecated]
depends_on:
  - INDEX_01_ARCHITECTURE
  - INDEX_02_REPOSITORY
  - WORKFLOW_00_PIPELINE
  - SETUP_PRODUCT_00_INDEX
arc: CACHE
scope: vault/99_CACHE/CACHE_00_SYSTEM/CACHE_SYSTEM_20_BACKLOG
---

# BACKLOG_01 - Migration `WORKFLOW` + `SETUP_PRODUCT`

## Objet

Cadrer l update operationnelle de la couche systeme pour converger vers une
structure unifiee :

- `WORKFLOW_*` pour l execution quotidienne,
- `SETUP_PRODUCT_*` pour bootstrap, routine, cycle de vie et gouvernance
  multi-products.

Le backlog ne migre rien automatiquement.
Il decoupe le chantier en CO atomiques.

## Statut d archivage

- backlog historique conserve pour tracabilite
- migration executee et closee
- document sorti du scope SYSTEM actif

## Cible d architecture

### Bloc 1 - Runbooks quotidiens

- `WORKFLOW_00_PIPELINE`
- `WORKFLOW_03_START_SESSION`
- `WORKFLOW_04_END_SESSION`
- `WORKFLOW_05_INCIDENT`
- `WORKFLOW_06_VAULT_HEALTH_CHECK`
- `WORKFLOW_07_TESTS_LLM`
- `WORKFLOW_08_TESTS_CODEX`
- `WORKFLOW_10_COMMANDES`

### Bloc 2 - Setup produit

- `SETUP_PRODUCT_00_INDEX`
- `SETUP_PRODUCT_01_BOOTSTRAP`
- `SETUP_PRODUCT_02_PROFILE_SELECTION`
- `SETUP_PRODUCT_03_ROUTINE_OPERATIONS`
- `SETUP_PRODUCT_04_DESTINATION_POLICY`
- `SETUP_PRODUCT_05_LIFECYCLE_POLICY`
- `SETUP_PRODUCT_06_MERGE_OUT_POLICY`
- `SETUP_PRODUCT_07_GOVERNANCE_RULES`

### Bloc 3 - Annexes a declasser ou fusionner

- `WORKFLOW_01_COMPOSANTS`
- `WORKFLOW_02_CHECKLISTS`
- plus aucun `MP_*` actif apres `CO_003`

## Principes non negociables

- `CORE` definit
- `PACKAGE` adapte
- `PRODUCT` execute et prouve
- `SYSTEM` orchestre
- un package actif
- un product actif
- pas de duplication durable entre `WORKFLOW` et `SETUP_PRODUCT`

## CO_001 - Cartographier l existant

- Statut : DONE
- Goal : etablir la table de correspondance entre `WORKFLOW_*`, `MP_*` et la
  cible `SETUP_PRODUCT_*`
- DoD :
  - inventaire des fichiers `WORKFLOW` et `MP`
  - identification des doublons
  - mapping `source -> cible`
- Fichiers cibles :
  - `SYSTEM_01_RUN/*`
  - `SYSTEM_20_MULTI_PRODUCT/*`
  - `INDEX_01_ARCHITECTURE`
  - `INDEX_02_REPOSITORY`

### Execution CO_001 - Cartographie validee

#### Table de correspondance cible

| Document actuel | Bloc observe | Cible nominale | Decision CO_001 | Impact
principal |
| --- | --- | --- | --- | --- |
| `WORKFLOW_00_PIPELINE` | runbook quotidien | `WORKFLOW_00_PIPELINE` | garder |
doctrine d execution globale |
| `WORKFLOW_01_COMPOSANTS` | annexe WORKFLOW | a declasser ou recadrer en
`CO_002` | declasser candidat | recouvrement avec backlog CO |
| `WORKFLOW_02_CHECKLISTS` | annexe WORKFLOW | a declasser ou recadrer en
`CO_002` | declasser candidat | recouvrement avec `CHECKLIST_*` |
| `WORKFLOW_03_START_SESSION` | runbook quotidien | `WORKFLOW_03_START_SESSION`
| garder | demarrage de session |
| `WORKFLOW_04_END_SESSION` | runbook quotidien | `WORKFLOW_04_END_SESSION` |
garder | cloture de session |
| `WORKFLOW_05_INCIDENT` | runbook quotidien | `WORKFLOW_05_INCIDENT` | garder |
triage incident |
| `WORKFLOW_06_VAULT_HEALTH_CHECK` | runbook quotidien |
`WORKFLOW_06_VAULT_HEALTH_CHECK` | garder | controle post-changement |
| `WORKFLOW_07_TESTS_LLM` | runbook quotidien | `WORKFLOW_07_TESTS_LLM` | garder
| qualification mentor |
| `WORKFLOW_08_TESTS_CODEX` | runbook quotidien | `WORKFLOW_08_TESTS_CODEX` |
garder | qualification agent IDE |
| `WORKFLOW_10_COMMANDES` | runbook quotidien | `WORKFLOW_10_COMMANDES` | garder
| bibliotheque de commandes |
| `MP_00_INDEX` | index de famille | `SETUP_PRODUCT_00_INDEX` | renomme en
`CO_003` | index de famille |
| `MP_01_PRODUCT_BOOTSTRAP` | setup produit | `SETUP_PRODUCT_01_BOOTSTRAP` |
renomme en `CO_003` | bootstrap |
| `MP_02_PROFILE_SELECTION` | setup produit |
`SETUP_PRODUCT_02_PROFILE_SELECTION` | renomme en `CO_003` | profil
package/product |
| `MP_03_ROUTINE_OPERATIONS` | setup produit |
`SETUP_PRODUCT_03_ROUTINE_OPERATIONS` | renomme en `CO_003` | routine produit
actif |
| `MP_04_PRODUCT_DESTINATION_POLICY` | setup produit |
`SETUP_PRODUCT_04_DESTINATION_POLICY` | renomme en `CO_003` | destination finale
|
| `MP_05_LIFECYCLE_POLICY` | setup produit | `SETUP_PRODUCT_05_LIFECYCLE_POLICY`
| renomme en `CO_003` | etats de cycle de vie |
| `MP_06_MERGE_OUT_POLICY` | setup produit | `SETUP_PRODUCT_06_MERGE_OUT_POLICY`
| renomme en `CO_003` | merge-out / extraction |
| `MP_07_GOVERNANCE_RULES` | setup produit | `SETUP_PRODUCT_07_GOVERNANCE_RULES`
| renomme en `CO_003` | gouvernance multi-products |

#### Doublons et recouvrements a traiter ensuite

- `WORKFLOW_01_COMPOSANTS` recouvre le pilotage backlog deja porte par les lots
  `BACKLOG_*` et par la discipline de production; il ne doit pas rester dans le
  noyau `WORKFLOW`.
- `WORKFLOW_02_CHECKLISTS` recouvre un role d index deja porte par
  `CHECKLIST_00_INDEX`; il releve d un recadrage ou d un declassement, pas d un
  maintien coeur.
- `WORKFLOW_03_START_SESSION` et `SETUP_PRODUCT_03_ROUTINE_OPERATIONS` se
  touchent sur la notion de routine, mais pas au meme niveau : `WORKFLOW_03`
  pilote la session quotidienne, `SETUP_PRODUCT_03` pilote la maintenance du
  product actif.
- `WORKFLOW_06_VAULT_HEALTH_CHECK`, `WORKFLOW_07_TESTS_LLM` et
  `WORKFLOW_08_TESTS_CODEX` restent des runbooks d execution; `SETUP_PRODUCT_03`
  ne doit garder qu une obligation de rerun et non dupliquer leurs protocoles.
- l arbitrage `00_INDEX + 01..07` supprime la collision historique entre index
  et bootstrap.

#### Fichiers a garder

- `WORKFLOW_00`, `WORKFLOW_03`, `WORKFLOW_04`, `WORKFLOW_05`, `WORKFLOW_06`,
  `WORKFLOW_07`, `WORKFLOW_08`, `WORKFLOW_10`
- `SETUP_PRODUCT_00` a `SETUP_PRODUCT_07`

#### Renommages executes en `CO_003`

- `MP_00_INDEX` -> `SETUP_PRODUCT_00_INDEX`
- `MP_01_PRODUCT_BOOTSTRAP` -> `SETUP_PRODUCT_01_BOOTSTRAP`
- `MP_02_PROFILE_SELECTION` -> `SETUP_PRODUCT_02_PROFILE_SELECTION`
- `MP_03_ROUTINE_OPERATIONS` -> `SETUP_PRODUCT_03_ROUTINE_OPERATIONS`
- `MP_04_PRODUCT_DESTINATION_POLICY` -> `SETUP_PRODUCT_04_DESTINATION_POLICY`
- `MP_05_LIFECYCLE_POLICY` -> `SETUP_PRODUCT_05_LIFECYCLE_POLICY`
- `MP_06_MERGE_OUT_POLICY` -> `SETUP_PRODUCT_06_MERGE_OUT_POLICY`
- `MP_07_GOVERNANCE_RULES` -> `SETUP_PRODUCT_07_GOVERNANCE_RULES`

#### Fichiers a declasser ou recadrer

- `WORKFLOW_01_COMPOSANTS`
- `WORKFLOW_02_CHECKLISTS`

#### Impacts sur les index SYSTEM

- `INDEX_01_ARCHITECTURE` doit expliciter la place de `SYSTEM_20_MULTI_PRODUCT`
  dans les familles SYSTEM et rappeler la doctrine `WORKFLOW` vs
  `SETUP_PRODUCT`.
- `INDEX_02_REPOSITORY` doit lister `WORKFLOW_06`, `WORKFLOW_07`, `WORKFLOW_08`,
  `BACKLOG_01` et tout le lot `SYSTEM_20_MULTI_PRODUCT`.
- `INDEX_02_REPOSITORY` doit signaler la numerotation active
  `SETUP_PRODUCT_00..07`.

## CO_002 - Stabiliser le noyau WORKFLOW

- Statut : DONE
- Goal : distinguer clairement les runbooks coeur des annexes
- DoD :
  - `WORKFLOW_00/03/04/05/06/07/08/10` qualifies
  - `WORKFLOW_01` et `WORKFLOW_02` declasses ou recadres
  - coherence avec les preuves `SYSTEM_10_EVIDENCE`
- Fichiers cibles :
  - `WORKFLOW_01_COMPOSANTS`
  - `WORKFLOW_02_CHECKLISTS`
  - `WORKFLOW_03_START_SESSION`
  - `WORKFLOW_10_COMMANDES`

### Execution CO_002 - Noyau WORKFLOW stabilise

#### Decisions appliquees

- `WORKFLOW_01_COMPOSANTS` passe en `DEPRECATED` puis sort du scope actif vers
  `CACHE_SYSTEM_01_RUN`.
- `WORKFLOW_02_CHECKLISTS` passe en `DEPRECATED` puis sort du scope actif vers
  `CACHE_SYSTEM_01_RUN`.
- `WORKFLOW_03_START_SESSION` reste un runbook coeur, mais ne depend plus de
  `WORKFLOW_01`; la source canonique du CO y est recablee vers
  `PIPELINE_03_BACKLOG_COMPOSANTS`.
- `WORKFLOW_04_END_SESSION` reste un runbook coeur et ne depend plus de
  `WORKFLOW_01`; la requalification mentor renvoie vers `WORKFLOW_07_TESTS_LLM`.
- `WORKFLOW_10_COMMANDES` reste un runbook coeur, ses references sont alignees
  sur `WORKFLOW_03`, `WORKFLOW_04`, `WORKFLOW_05`, `WORKFLOW_06`, `WORKFLOW_07`,
  `WORKFLOW_08`, `PIPELINE_03_BACKLOG_COMPOSANTS` et les `CHECKLIST_*` reelles.

#### Verdict

- noyau `WORKFLOW` qualifie : `WORKFLOW_00/03/04/05/06/07/08/10`
- annexes hors noyau : `WORKFLOW_01`, `WORKFLOW_02`
- coherence evidence : aucune evidence active ne depend de `WORKFLOW_01` ou
  `WORKFLOW_02`

## CO_003 - Renommer la couche multi-product en `SETUP_PRODUCT`

- Statut : DONE
- Goal : remplacer la famille `MP_*` par une famille lisible `SETUP_PRODUCT_*`
- DoD :
  - nouvelle nomenclature validee
  - ids et filenames alignes
  - references internes recablees
- Fichiers cibles :
  - `MP_00_INDEX`
  - `MP_01_PRODUCT_BOOTSTRAP`
  - `MP_02_PROFILE_SELECTION`
  - `MP_03_ROUTINE_OPERATIONS`
  - `MP_04_PRODUCT_DESTINATION_POLICY`
  - `MP_05_LIFECYCLE_POLICY`
  - `MP_06_MERGE_OUT_POLICY`
  - `MP_07_GOVERNANCE_RULES`

### Execution CO_003 - Renommage applique

#### Arbitrage

- la famille adopte une numerotation stable `SETUP_PRODUCT_00_INDEX` puis
  `SETUP_PRODUCT_01..07`
- le host folder reste `SYSTEM_20_MULTI_PRODUCT`
- les frontmatters passent de `type: MP` a `type: SETUP_PRODUCT`

#### Resultat

- ids et filenames alignes sur `SETUP_PRODUCT_*`
- references internes recablees
- collision `00_INDEX` vs `00_BOOTSTRAP` resolue sans nomenclature hors serie

## CO_004 - Definir la doctrine d integration `WORKFLOW` vs `SETUP_PRODUCT`

- Statut : DONE
- Goal : verrouiller ce qui reste en runbook quotidien et ce qui devient setup
  multi-product
- DoD :
  - frontieres fonctionnelles explicites
  - plus de recouvrement ambigu
  - dependances doc integrity propres
- Fichiers cibles :
  - `WORKFLOW_00_PIPELINE`
  - `SETUP_PRODUCT_03_ROUTINE_OPERATIONS`
  - `SETUP_PRODUCT_05_LIFECYCLE_POLICY`
  - `SETUP_PRODUCT_07_GOVERNANCE_RULES`

### Execution CO_004 - Doctrine verrouillee

#### Doctrine retenue

- `WORKFLOW_*` = execution quotidienne, session, checks, reruns, incident,
  commandes.
- `SETUP_PRODUCT_*` = composition produit, maintien, cycle de vie, merge-out,
  gouvernance.
- `WORKFLOW_*` execute.
- `SETUP_PRODUCT_*` decide ce qui doit etre maintenu, revalide ou promu.

#### Frontieres explicites

- `WORKFLOW_00_PIPELINE` porte la doctrine generale et les points d entree
  operatoires.
- `SETUP_PRODUCT_03_ROUTINE_OPERATIONS` declare les reruns obligatoires, sans
  decrire le pas-a-pas.
- `SETUP_PRODUCT_05_LIFECYCLE_POLICY` declare les passages d etat, sans
  dupliquer les checks d execution.
- `SETUP_PRODUCT_07_GOVERNANCE_RULES` declare les obligations d isolation et de
  revalidation, sans remplacer les runbooks quotidiens.

#### Verdict

- plus de recouvrement ambigu entre routine produit et routine de session
- dependances doctrinales explicites vers `WORKFLOW_03`, `WORKFLOW_04`,
  `WORKFLOW_05`, `WORKFLOW_06`, `WORKFLOW_07`, `WORKFLOW_08`

## CO_005 - Raccorder les index SYSTEM

- Statut : DONE
- Goal : mettre les index systeme en conformite avec la nouvelle organisation
- DoD :
  - `INDEX_01_ARCHITECTURE` a jour
  - `INDEX_02_REPOSITORY` a jour
  - references obsoletes retirees
- Fichiers cibles :
  - `INDEX_01_ARCHITECTURE`
  - `INDEX_02_REPOSITORY`

### Execution CO_005 - Index SYSTEM raccordes

#### Actions appliquees

- `INDEX_01_ARCHITECTURE` explicite le noyau `WORKFLOW`, les annexes legacy
  `WORKFLOW_01` / `WORKFLOW_02`, et la frontiere finale `WORKFLOW` vs
  `SETUP_PRODUCT`.
- `INDEX_02_REPOSITORY` aligne la liste `SYSTEM_20_MULTI_PRODUCT` sur
  `SETUP_PRODUCT_00..07`.
- `INDEX_02_REPOSITORY` retire la reference obsolete `CHECKLIST_00_INDEX.md`.

#### Verdict

- les index SYSTEM reflectent le cadre final de migration
- les references obsoletes visibles dans les index sont retirees

## CO_006 - Verifier les preuves et le cadre final

- Statut : DONE
- Goal : garantir que la nouvelle organisation est exploitable et verifiable
- DoD :
  - validator PASS
  - doc integrity PASS
  - runbooks `WORKFLOW_07` et `WORKFLOW_08` toujours raccordes
  - `SYSTEM_10_EVIDENCE` coherent avec les nouveaux ids
- Fichiers cibles :
  - `SYSTEM_10_EVIDENCE/*`
  - `WORKFLOW_07_TESTS_LLM`
  - `WORKFLOW_08_TESTS_CODEX`

### Execution CO_006 - Preuves et cadre final verifies

#### Actions appliquees

- `SYSTEM_10_EVIDENCE` trace explicitement la convergence `WORKFLOW +
  SETUP_PRODUCT`.
- `WORKFLOW_07_TESTS_LLM` et `WORKFLOW_08_TESTS_CODEX` portent un raccord final
  vers la doctrine `WORKFLOW` vs `SETUP_PRODUCT`.
- les preuves framework globales confirment que le cadre final reste exploitable
  et verifiable.

#### Verifications

- `ValidateFrontmatter` : PASS
- `DocIntegrityChecker` : PASS
- aucune incoherence P0/P1/P2 detectee sur le vault cible

#### Verdict

- cadre final exploitable
- preuves SYSTEM raccordees
- runbooks de qualification toujours alignes

## Patch post-backlog - Rehost `SETUP_PRODUCT` sous `RUN_01_SETUP_PRODUCT`

- Statut : DONE
- Goal : fusionner l ancien host `SYSTEM_20_MULTI_PRODUCT` dans `SYSTEM_01_RUN`
- DoD :
  - fichiers `SETUP_PRODUCT_*` deplaces
  - `scope` recables
  - index SYSTEM alignes sur `RUN_01_SETUP_PRODUCT`
- Fichiers cibles :
  - `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT/*`
  - `INDEX_01_ARCHITECTURE`
  - `INDEX_02_REPOSITORY`
  - `SYSTEM_10_EVIDENCE/*`

### Execution patch post-backlog - Rehost applique

#### Actions appliquees

- le host folder actif devient `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT`
- `SYSTEM_20_MULTI_PRODUCT` sort du repository actif
- la doctrine `WORKFLOW` vs `SETUP_PRODUCT` est conservee sans changement de
  perimetre

#### Verdict

- convergence physique et documentaire sur `SYSTEM_01_RUN`
- aucune famille `MULTI_PRODUCT` active restante

## Ordre recommande

1. `CO_001`
2. `CO_002`
3. `CO_003`
4. `CO_004`
5. `CO_005`
6. `CO_006`

## Risques

- collision d ids lors du renommage `MP_* -> SETUP_PRODUCT_*`
- duplication temporaire entre `WORKFLOW` et `SETUP_PRODUCT`
- index systeme obsoletes pendant la transition

## Verdict de pilotage

- backlog exploitable
- `CO_001` execute et trace
- decoupage suffisamment atomique pour execution progressive

## Next step unique

- maintenir ce cadre via `WORKFLOW_06_VAULT_HEALTH_CHECK` et rerun `WORKFLOW_07`
  / `WORKFLOW_08` a chaque lot structurant.

## Changelog

- v1.13 (13-03-2026) : archive en `CACHE_SYSTEM_20_BACKLOG` avec `status:
  DEPRECATED` apres cloture du chantier.
- v1.12 (13-03-2026) : renomme le backlog `SYSTEM_WORKFLOW_SETUP_PRODUCT` en
  `SYSTEM_RUN_SETUP_PRODUCT` pour aligner le host SYSTEM canonique.
- v1.11 (13-03-2026) : archive `WORKFLOW_01` et `WORKFLOW_02` en `99_CACHE`
  apres leur declassement.
- v1.10 (13-03-2026) : renomme le backlog `RUN_SETUP_PRODUCT` en
  `WORKFLOW_SETUP_PRODUCT` pour aligner le lexical canonique.
- v1.8 (13-03-2026) : rehoste `SETUP_PRODUCT_*` sous
  `SYSTEM_01_RUN/RUN_01_SETUP_PRODUCT` apres cloture du backlog initial.
- v1.7 (13-03-2026) : execution de `CO_006`, preuves SYSTEM et runbooks de
  qualification raccordes au cadre final.
- v1.6 (13-03-2026) : execution de `CO_005`, index SYSTEM raccordes au cadre
  final et references obsoletes retirees.
- v1.5 (13-03-2026) : execution de `CO_004`, doctrine `WORKFLOW` vs
  `SETUP_PRODUCT` explicitee et dependances recadrees.
- v1.4 (13-03-2026) : patch P0 post-`CO_003`, retire les mentions obsoletes
  `MP_*` encore actives dans le backlog.
- v1.3 (13-03-2026) : execution de `CO_003`, renommage effectif `MP_*` vers
  `SETUP_PRODUCT_*` avec arbitrage `00_INDEX`.
- v1.2 (13-03-2026) : execution de `CO_002`, noyau `WORKFLOW` stabilise et
  annexes `WORKFLOW_01` / `WORKFLOW_02` declasses.
- v1.1 (13-03-2026) : execution de `CO_001`, cartographie `WORKFLOW / MP /
  SETUP_PRODUCT`, impacts index documentes.
- v1.0 (13-03-2026) : creation du backlog de migration `WORKFLOW +
  SETUP_PRODUCT`.
