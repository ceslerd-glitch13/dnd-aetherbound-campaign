---
status: Reference
authority: Repository Navigation and Verified Status
version: 7.0
last_reviewed: 2026-07-17
review_state: Batch H shop and settlement equipment reference implemented and locally validated; post-upload GitHub verification pending
---

# Campaign Index and Quick Reference

## Purpose

This file provides navigation and a factual snapshot of the repository. It does **not** override campaign canon and is not a historical changelog.

Start with `README.md` for the user-and-ChatGPT package workflow. Read `GOVERNANCE.md` for authority order, `SKILL.md` for the operating procedure, and `VALIDATION.md` for repository checks.

## Current Project State

- **Campaign/repository name:** Aetherbound
- **Continent:** Elyndria
- **Rules foundation:** Dungeons & Dragons 5th Edition with targeted homebrew
- **Current condition:** Batch B setting canon, Batch C playability, Batch D validation, Batch E scene anchors, Batch G folder organization, and Batch H shop and equipment integration are implemented in this repository; post-upload GitHub verification is pending
- **Geography:** Map-aligned, with ten publicly known dead zones and eight hidden dead zones, for eighteen physical zones total
- **Cities:** Ravensport, Deepanvil, Faerindel, and Ironforge meet mandatory city-profile requirements and contain flexible DM scene anchors
- **Starter material:** Session 0 and Captain Rurik's Request are ready to run with named evidence and recovery locations
- **Open-world material:** Five quests have synchronized starting locations, information sources, and clue destinations for on-demand expansion
- **Items and shops:** Table-ready inventories, settlement availability, permit rules, restricted goods, black-market guidance, and dead-zone purchasing rules are synchronized in the item authority
- **Combat:** Starter-arc enemies, complications, dead-zone variants, Silas, and an early-Veyne contingency are actionable
- **Validation:** Folder-aware local validator and GitHub Actions workflow are implemented
- **Pending changes:** No active proposals in the prepared package

## Authority Order

1. `GOVERNANCE.md` — repository process and authority ownership
2. `canon/DnD_Campaign_World_Bible.md` — setting-wide canon and mechanics
3. `canon/World_Geography.md` — spatial canon
4. Dedicated city, NPC, quest, tracker, combat, and item files — detail within their scopes
5. This Index — navigation and verified status only
6. Session plans and drafts — preparation, not automatic setting canon
7. Pending and archived change logs — proposals and history, not canon

## File Directory and Verified Status

### Governance and operation

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `GOVERNANCE.md` | 1.2 | Reference | Authority hierarchy, ownership, metadata, approval workflow, and validation requirement | Paths synchronized |
| `AGENTS.md` | 2.2 | Reference | Entry instructions for repository-aware assistants | Folder-aware |
| `SKILL.md` | 2.2 | Reference | Detailed campaign operating procedure | Folder-aware |
| `VALIDATION.md` | 1.2 | Reference | Validator usage, dual dead-zone counts, automation, and maintenance | Folder-aware |
| `Pending_Changes.md` | 7.0 | Active Reference | Active unimplemented proposals | Empty after combined-batch closure |
| `history/Pending_Changes_Archived_*.md` | varies | Historical | Historical approved-change records | Archives 01–07 exist |

### Core canon and reference

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `canon/DnD_Campaign_World_Bible.md` | 3.2 | Canon | Setting-wide lore and mechanics | Known-versus-hidden dead-zone reality synchronized |
| `canon/World_Geography.md` | 1.4 | Canon | Terrain, routes, settlements, travel, dead zones, and local route anchors | Map-aligned and folder-migrated |
| `Campaign_Index_and_Quick_Reference.md` | 7.0 | Reference | Navigation, metadata inventory, and verified readiness | Current organized state |

### Cities and NPCs

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `cities/Ravensport_City_Profile.md` | 2.2 | Canon | Primary mixed gate city, starter hub, and urban scene anchors | Playable anchors synchronized |
| `cities/Deepanvil_City_Profile.md` | 2.2 | Canon | Dead-zone mining settlement and quest anchors | Playable anchors synchronized |
| `cities/Faerindel_City_Profile.md` | 2.2 | Canon | Elven gate city and grove/research anchors | Playable anchors synchronized |
| `cities/Ironforge_City_Profile.md` | 2.2 | Canon | Dwarven gate city and workshop/forge anchors | Playable anchors synchronized |
| `npcs/NPC_Backstory_Personality_file.md` | 2.1 | Canon | Canonical NPC identity and personality database | Four utility NPCs added |

### Quests, sessions, tracking, combat, and items

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `quests/Captain_Ruriks_Request_Session_0-1.md` | 2.1 | Draft | Opening scene, investigation, recovery, and orb decision | Named scene anchors ready |
| `quests/Early_Sessions_Plan_Sessions_0_to_5.md` | 2.1 | Draft | Open-world opening structure and five quest frameworks | Primary anchors synchronized |
| `quests/Quests_Player_Decisions_Impacts.md` | 2.1 | Active Reference | Quest states, decisions, attitudes, orb state, and antagonist interest | Pre-play state retained; anchors added |
| `combat/Enemy_Encounters_Stat_Blocks.md` | 2.0 | Draft | Campaign combat repository | Starter entries actionable |
| `items/Shop_Inventory_and_Items.md` | 1.0 | Reference | Shop inventories, settlement availability, permits, restricted equipment, and price guidance | Complete approved snapshot |

### Guidelines

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `guidelines/City_Creation_Guidelines.md` | 1.0 | Reference | Mandatory city and major-settlement requirements | Current |
| `guidelines/Guideline_Battle_Stat_Block_Management.md` | 1.0 | Reference | Combat and stat-block preparation process | Current |
| `guidelines/Guideline_NPC_Character_Creation.md` | 1.0 | Reference | NPC creation and three-line profile process | Current |
| `guidelines/Guideline_Quest_Creation.md` | 1.0 | Reference | Quest design and resolution structure | Current |
| `guidelines/Guideline_World_Geography_Map_Creation.md` | 1.0 | Reference | Geography and map creation checklist | Current |
| `guidelines/Guideline_World_Update_Change_Management.md` | 2.1 | Reference | Approved-change synchronization and closure | Current |

### Validation and handoff resources

| Resource | Purpose | Verified state |
|---|---|---|
| `README.md` | User-and-ChatGPT batch handoff and folder-layout guide | Current |
| `scripts/validate_repository.py` | Standard-library folder-aware repository validator | Implemented |
| `.github/workflows/validate-repository.yml` | Automatic validation for push, pull request, and manual runs | Implemented |
| `validation/dead_zones.json` | Audited map checksum, organized map path, and dual dead-zone count manifest | Current |
| `assets/maps/Elyndria_DND_World_Map.png` | Canonical campaign map | Bytes unchanged during migration |

## Current Open Decisions and Future Development

The implemented Batch B through Batch G decisions should not be reopened without a new approved proposal.

Known future topics include:

1. A permanent in-world name for Veyne's secret organization
2. A final campaign title if `Aetherbound` is replaced as the working title
3. Discovery and public naming of hidden dead zones through play or later approved development
4. Detailed maps and encounter layouts only after players choose a quest
5. New enemies and stat blocks only when upcoming play requires them

## Quick Navigation by Task

- **Package upload or verification:** `README.md`
- **World lore or mechanics:** `canon/DnD_Campaign_World_Bible.md` + relevant guideline
- **Map, route, distance, settlement, or dead-zone placement:** `canon/World_Geography.md` + World Bible
- **City preparation:** relevant file in `cities/` + Geography + NPC database
- **NPC interaction:** `npcs/NPC_Backstory_Personality_file.md` + tracker + relevant city or quest
- **Starter session:** `quests/Captain_Ruriks_Request_Session_0-1.md` + Early Sessions + Ravensport profile
- **Quest status or consequences:** `quests/Quests_Player_Decisions_Impacts.md` + selected quest/session file
- **Combat:** `combat/Enemy_Encounters_Stat_Blocks.md` + World Bible mechanics
- **Shops and item availability:** `items/Shop_Inventory_and_Items.md`
- **Repository edit:** Governance + Skill + Pending Changes + target files + update guideline
- **Validation:** `VALIDATION.md` + `scripts/validate_repository.py`

## Verified Implemented Work

- map-aligned Elyndria geography and dual dead-zone knowledge model;
- governance, file ownership, staged approval, and archive workflow;
- Batch B setting and antagonist mechanics;
- Batch C city playability, NPC consolidation, starter quest, open-world quests, and encounter preparation;
- Batch D deterministic validation, automation, hidden-zone manifest, and package workflow;
- Batch E named DM scene anchors and information-source locations;
- Batch G functional folder organization with synchronized references and validator paths;
- Batch H complete shop inventories, settlement availability, and restricted-equipment guidance;
- Batches E–G archived in `history/Pending_Changes_Archived_06.md`;
- Batch H shop and equipment integration archived in `history/Pending_Changes_Archived_07.md`; post-upload GitHub verification remains.
