---
status: Reference
authority: Repository Navigation and Verified Status
version: 5.0
last_reviewed: 2026-07-16
review_state: Batch D validation, automation, hidden-zone model, and package handoff implemented; repository ready for future staging
---

# Campaign Index and Quick Reference

## Purpose

This file provides navigation and a factual snapshot of the repository. It does **not** override campaign canon and is not a historical changelog.

Start with `README.md` for the user-and-ChatGPT package workflow. Read `GOVERNANCE.md` for authority order, `SKILL.md` for the operating procedure, and `VALIDATION.md` for repository checks.

## Current Project State

- **Campaign/repository name:** Aetherbound
- **Continent:** Elyndria
- **Rules foundation:** Dungeons & Dragons 5th Edition with targeted homebrew
- **Current condition:** Batch B setting canon, Batch C playability, and Batch D validation and maintenance are implemented
- **Geography:** Map-aligned, with ten publicly known dead zones and eight hidden dead zones, for eighteen physical zones total
- **Cities:** Ravensport, Deepanvil, Faerindel, and Ironforge meet the mandatory city-profile requirements
- **Starter material:** Session 0 and Captain Rurik's Request are ready to run; five open-world quests are prepared for on-demand expansion
- **Combat:** Starter-arc enemies, complications, dead-zone variants, Silas, and an early-Veyne contingency are actionable
- **Validation:** Local validator and GitHub Actions workflow are implemented
- **Pending changes:** No active proposals

## Authority Order

1. `GOVERNANCE.md` — repository process and authority ownership
2. `DnD_Campaign_World_Bible.md` — setting-wide canon and mechanics
3. `World_Geography.md` — spatial canon
4. Dedicated city, NPC, quest, tracker, and combat files — detail within their scopes
5. This Index — navigation and verified status only
6. Session plans and drafts — preparation, not automatic setting canon
7. Pending and archived change logs — proposals and history, not canon

## File Directory and Verified Status

### Governance and operation

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `GOVERNANCE.md` | 1.1 | Reference | Authority hierarchy, ownership, metadata, approval workflow, and validation requirement | Current |
| `AGENTS.md` | 2.1 | Reference | Entry instructions for repository-aware assistants | Current |
| `SKILL.md` | 2.1 | Reference | Detailed campaign operating procedure | Current |
| `VALIDATION.md` | 1.1 | Reference | Validator usage, dual dead-zone counts, automation, and maintenance | Current |
| `Pending_Changes.md` | 5.0 | Active Reference | Active unimplemented proposals | Empty after Batch D closure |
| `Pending_Changes_Archived_*.md` | varies | Historical | Historical approved-change records | Archives 01–05 exist |

### Core canon and reference

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `DnD_Campaign_World_Bible.md` | 3.2 | Canon | Setting-wide lore and mechanics | Known-versus-hidden dead-zone reality synchronized |
| `World_Geography.md` | 1.3 | Canon | Terrain, routes, settlements, travel, known zones, and hidden zones | Map-aligned |
| `Campaign_Index_and_Quick_Reference.md` | 5.0 | Reference | Navigation, metadata inventory, and verified readiness | Current |

### Cities and NPCs

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `Ravensport_City_Profile.md` | 2.0 | Canon | Primary mixed gate city and starter hub | Complete for current play |
| `Deepanvil_City_Profile.md` | 2.0 | Canon | Dwarven mining settlement inside a dead zone | Complete for current play |
| `Faerindel_City_Profile.md` | 2.0 | Canon | Elven gate city | Complete for current play |
| `Ironforge_City_Profile.md` | 2.0 | Canon | Dwarven gate city | Complete for current play |
| `NPC_Backstory_Personality_file.md` | 2.0 | Canon | Canonical NPC identity and personality database | Major profiles playable |

### Quests, sessions, tracking, and combat

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `Captain_Ruriks_Request_Session_0-1.md` | 2.0 | Draft | Opening scene, investigation, recovery, and orb decision | Ready to run |
| `Early_Sessions_Plan_Sessions_0_to_5.md` | 2.0 | Draft | Open-world opening structure and five quest frameworks | Ready for on-demand development |
| `Quests_Player_Decisions_Impacts.md` | 2.0 | Active Reference | Quest states, decisions, attitudes, orb state, and antagonist interest | Pre-play state seeded |
| `Enemy_Encounters_Stat_Blocks.md` | 2.0 | Draft | Campaign combat repository | Starter entries actionable |

### Guidelines

| File | Version | Metadata status | Purpose | Verified state |
|---|---:|---|---|---|
| `City_Creation_Guidelines.md` | 1.0 | Reference | Mandatory city and major-settlement requirements | Current |
| `Guideline_Battle_Stat_Block_Management.md` | 1.0 | Reference | Combat and stat-block preparation process | Current |
| `Guideline_NPC_Character_Creation.md` | 1.0 | Reference | NPC creation and three-line profile process | Current |
| `Guideline_Quest_Creation.md` | 1.0 | Reference | Quest design and resolution structure | Current |
| `Guideline_World_Geography_Map_Creation.md` | 1.0 | Reference | Geography and map creation checklist | Current |
| `Guideline_World_Update_Change_Management.md` | 2.1 | Reference | Approved-change synchronization and closure | Current |

### Validation and handoff resources

| Resource | Purpose | Verified state |
|---|---|---|
| `README.md` | User-and-ChatGPT batch handoff guide | Current |
| `scripts/validate_repository.py` | Standard-library repository validator | Implemented |
| `.github/workflows/validate-repository.yml` | Automatic validation for push, pull request, and manual runs | Implemented |
| `validation/dead_zones.json` | Audited map checksum and dual dead-zone count manifest | Current |

## Current Open Decisions and Future Development

The implemented Batch B, Batch C, and Batch D decisions should not be reopened without a new approved proposal.

Known future topics include:

1. A permanent in-world name for Veyne's secret organization
2. A final campaign title if `Aetherbound` is replaced as the working title
3. Discovery and public naming of hidden dead zones through play or later approved development
4. Detailed maps, encounter layouts, and expanded session preparation only after players choose a quest
5. New enemies and stat blocks only when upcoming play requires them

## Quick Navigation by Task

- **Package upload or verification:** `README.md`
- **World lore or mechanics:** World Bible + relevant guideline
- **Map, route, distance, settlement, or dead-zone placement:** Geography + World Bible
- **City preparation:** relevant city profile + Geography + NPC database
- **NPC interaction:** NPC database + tracker + relevant city or quest
- **Starter session:** Captain Rurik file + Early Sessions + Ravensport profile
- **Quest status or consequences:** tracker + selected quest/session file
- **Combat:** encounter repository + World Bible mechanics
- **Repository edit:** Governance + Skill + Pending Changes + target files + update guideline
- **Validation:** `VALIDATION.md` + `scripts/validate_repository.py`

## Verified Implemented Work

- map-aligned Elyndria geography and dual dead-zone knowledge model;
- governance, file ownership, staged approval, and archive workflow;
- Batch B dead-zone mechanics, beacon, Aetherite, Veyne, terminology, Ravensport government, and Rurik canon;
- Batch C city playability, NPC consolidation, starter quest, open-world quests, and encounter preparation;
- deterministic repository validation with text and JSON results;
- automatic GitHub validation for pushes and pull requests;
- user-and-ChatGPT changed-files package workflow with base-commit verification;
- Batch D archived in `Pending_Changes_Archived_05.md`.
