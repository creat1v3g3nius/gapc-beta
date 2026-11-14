---
id: STUDIO_TOOLING_EXTENSION_02_ASSET_NAMING_ADDON
type: TOOLING
title: StudioAssetNamingAddon
version: v1.0
status: DRAFT
created: 14-11-2026
updated: 14-11-2026
tags: [package, studio, tooling, extension, naming, assets]
depends_on: 
  - EXTENSION_05_ASSET_NAMING_POLICY
arc: PACKAGE
scope: vault/02_PACKAGE/PACKAGE_02_STUDIO/STUDIO_04_TOOLING/STUDIO_TOOLING_04_EXTENSION
---

# STUDIO_TOOLING_EXTENSION_02 - Asset Naming Addon

## Objet

Preciser la convention CORE `EXTENSION_05_ASSET_NAMING_POLICY` pour les assets
du studio. Le format de base est inchange.

## Format

`P<NN>_CO<NNN>_<TYPE>_<desc>_v<N>[_<suffixe>].<ext>`

- `<TYPE>` : `IMG` image, `VID` video, `MOT` motion, `WEB` prototype,

  `TYP` typographie / layout, `AUD` audio, `3D` volume

- `<desc>` : minuscules, sans espace ni nom de client
- `_v<N>` : version, incrementee a chaque correction
- suffixes optionnels : `_varA..Z` variante, `_<ratio>` (ex `_9x16`),

  `_master` fichier source

## Exemples

- `P03_CO004_IMG_kv-launch_v2.png`
- `P03_CO007_VID_teaser_v1_9x16.mp4`
- `P03_CO004_IMG_kv-launch_v2_master.psd`

## Regles

- une version livree n est jamais ecrasee : correction = `_v<N+1>`,
- pas de donnee personnelle ni de nom de client dans un nom de fichier.

## Changelog

- v1.0 (14-11-2026) : creation de l add-on nommage des assets studio.
