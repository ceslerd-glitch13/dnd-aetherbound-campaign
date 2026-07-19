---
status: Reference
authority: Creature Catalog Management Guideline
version: 1.0
last_reviewed: 2026-07-19
---

# Guideline: Creature Catalog Management

## Purpose

This guideline controls how official creatures, regional placement recommendations, source baselines, dead-zone notes, and search views are added to or maintained in the creature repository.

## Authority Boundaries

- `../canon/DnD_Campaign_World_Bible.md` owns setting-wide creature effects caused by dead zones, gates, Aetherite, and other world mechanics.
- `../canon/World_Geography.md` owns place names, regions, routes, climates, and spatial relationships.
- `../creatures/Creature_Catalog_Index.md` owns creature-catalog navigation, status rules, and the current approved catalog snapshot.
- `../creatures/data/creatures.json` is the structured per-creature record.
- Category pages and lookup files are synchronized human-readable views.
- `../combat/Enemy_Encounters_Stat_Blocks.md` owns custom or materially altered campaign statistics.
- An owned official source owns the complete published stat block.

## Required Fields for a Catalog Entry

Every creature record must include:

1. unique creature name;
2. catalog category and repository group;
3. selected statistics baseline and availability note;
4. CR, size, creature type, AC, HP, speed, and ability scores;
5. habitat and proposed Elyndrian placement;
6. campaign classification;
7. physical viability, magical dependency, connection severance, and dead-zone recommendation;
8. DM adjudication note;
9. recommended party levels and suitable gate-city context;
10. strengths, weaknesses, and verification status;
11. category-file path and entry anchor.

## Search and File Placement

- Put each creature in exactly one category page.
- Use semantic repository groups rather than numbered folders.
- Link every creature from `../creatures/Creature_Catalog_Index.md`.
- Regenerate the regional, encounter, and dead-zone/source lookup files after changing data.
- Keep CSV and JSON synchronized.
- Do not create a second independent creature list in a city, quest, or session file. Those files should link to the catalog entry.


## Random Encounter Roll Tables

- `../creatures/roll_tables/Roll_Table_Index.md` owns random-encounter table navigation and the mandatory roll-first procedure.
- `../creatures/roll_tables/data/roll_tables.json` is the structured roll-result record.
- When a random encounter roll is requested, select and roll on the appropriate table **before** opening individual creature entries.
- After the roll, open every linked catalog entry in the result and use those records for CR, recommended level, source, placement, dead-zone behavior, strengths, and weaknesses.
- A roll-table result is an encounter prompt, not an automatically balanced combat.
- Every creature named in a roll result must resolve to exactly one record in `../creatures/data/creatures.json`.
- Gate-invasion results are campaign-scale scenarios of at least 50 creatures and must not be treated as routine party combats.

## Official Statistics and Copyright

- Record only the planning fields needed to select and compare a creature.
- Do not reproduce complete copyrighted action text or full sourcebook lore.
- Identify the official source and open the owned stat block before live play.
- When an official creature is materially changed, recurring, or requires campaign-specific actions, create an actionable custom entry in `../combat/Enemy_Encounters_Stat_Blocks.md`.

## Dead-Zone Review

For each creature, test:

1. whether its body is physically self-sustaining;
2. which traits require active magic;
3. which external magical connections are severed;
4. whether World Bible drain applies;
5. whether the timing or result remains a DM decision;
6. whether a resonance or beacon-core field could create an approved exception.

Never use a category page to create a setting-wide dead-zone rule.

## Tokens and Images

- Track token work separately from catalog approval.
- Approved assets belong under `../assets/tokens/creatures/`.
- Record source and usage rights.
- Do not create a second token solely because magic is suppressed unless the creature's visible physical form changes.

## Update Procedure

1. Update `../creatures/data/creatures.json`.
2. Regenerate `../creatures/data/creatures.csv`.
3. Regenerate the relevant category page and lookup views.
4. Regenerate affected files under `../creatures/roll_tables/` when a table or catalog name changes.
5. Update both `../creatures/roll_tables/manifest.json` and `../creatures/manifest.json` counts and checksums.
6. Update the Campaign Index only when catalog status or metadata changes.
7. Run `python scripts/validate_repository.py --strict-warnings`.
8. Resolve every catalog and roll-table integrity error before closing the change batch.
