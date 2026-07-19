---
status: Historical
authority: Approved Creature Catalog and Random Encounter Change Archive
version: 1.0
last_reviewed: 2026-07-19
implementation_status: Prepared as a strictly validated changed-files package for user upload
---

# Pending Changes Archived 08 — Batch I Creature Catalog and Random Encounter Tables

## Approved Scope

The user approved integration of the supplied Elyndria creature catalog and d6 roll-table packages as repository-native operational references.

## Implemented Structure

- Added `creatures/` as the single creature-repository entry point.
- Added 161 synchronized creature records across 23 category files.
- Added alphabetical, regional, encounter, dead-zone, and source lookup views.
- Added synchronized JSON and CSV creature records and a checksum manifest.
- Added 23 linked d6 random encounter tables containing 138 results.
- Added a table-selection guide, structured roll data, schema, and checksum manifest.
- Added `guidelines/Guideline_Creature_Catalog_Management.md`.
- Updated repository navigation, authority ownership, AI loading rules, and validation documentation.
- Added creature-catalog and roll-table integrity checks to `scripts/validate_repository.py`.

## Approved Operating Rules

1. The catalog and roll tables are operational References, not automatic setting-wide Canon.
2. A random encounter request begins with `creatures/roll_tables/Roll_Table_Index.md`.
3. The table is selected and rolled before creature entries are opened.
4. Every creature linked by the rolled result is then consulted in the creature catalog.
5. Complete live statistics come from an owned official source or the custom combat repository.
6. Creature-specific dead-zone recommendations remain subordinate to the World Bible and DM adjudication.
7. Giant Elk, Giant Owl, and listed timing questions remain deferred.
8. Official magical constructs require separate approval before being treated as nonmagical Elyndrian variants.

## Validation Requirement

The prepared repository must pass:

```bash
python scripts/validate_repository.py --strict-warnings
```

The active Pending file is reset only after the changed-files package passes strict validation.
