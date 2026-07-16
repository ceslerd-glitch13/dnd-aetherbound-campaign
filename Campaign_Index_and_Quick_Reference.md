---
status: Reference
authority: Repository Navigation and Verified Status
version: 3.0
last_reviewed: 2026-07-16
review_state: Safe structural cleanup complete; canon decisions remain unresolved
---

# Campaign Index and Quick Reference

## Purpose

This file provides navigation and a factual snapshot of the repository. It does **not** override campaign canon and is not a historical changelog.

Read `GOVERNANCE.md` for authority order and `SKILL.md` for the operating procedure.

## Current Project State

- **Campaign/repository name:** Aetherbound
- **Continent:** Elyndria
- **Rules foundation:** Dungeons & Dragons 5th Edition with targeted homebrew
- **Current condition:** Structured campaign draft with partially synchronized canon
- **Geography:** Updated to match the Elyndria map and document all ten dead zones, major routes, ports, and canonical settlements
- **Starter material:** Hook and branching concepts exist, but the starter quest and Sessions 1–5 are not yet complete enough to run without additional preparation

## Authority Order

1. `GOVERNANCE.md` — repository process and authority ownership
2. `DnD_Campaign_World_Bible.md` — setting-wide canon and mechanics
3. `World_Geography.md` — spatial canon
4. Dedicated city, NPC, quest, tracker, and combat files — detail within their scopes
5. This Index — navigation and verified status only
6. Session plans/drafts — preparation, not automatic canon
7. Pending and archived change logs — proposals/history, not canon

## File Directory and Verified Status

### Governance and operation

| File | Purpose | Status |
|---|---|---|
| `GOVERNANCE.md` | Authority hierarchy, ownership, metadata, approval workflow | Reference |
| `AGENTS.md` | Entry instructions for repository-aware assistants | Reference |
| `SKILL.md` | Detailed campaign operating procedure | Reference |
| `Pending_Changes.md` | Active unapproved proposals | Active Reference; currently empty |
| `Pending_Changes_Archived_*.md` | Historical approved-change records | Historical |

### Core canon and reference

| File | Purpose | Verified state |
|---|---|---|
| `DnD_Campaign_World_Bible.md` | Setting-wide lore and mechanics | Canon with unresolved conflicts flagged; structural duplicate removed |
| `World_Geography.md` | Elyndria placement, terrain, routes, waters, ports, travel, and dead zones | Canon; map-aligned |
| `Campaign_Index_and_Quick_Reference.md` | Navigation and verified readiness | Reference |

### Cities and NPCs

| File | Purpose | Verified state |
|---|---|---|
| `Ravensport_City_Profile.md` | Detailed primary hub | Draft; mandatory city sections remain incomplete and leadership conflicts remain unresolved |
| `Deepanvil_City_Profile.md` | Western mining city inside the Deepanvil Dead Zone | Draft; mandatory city sections remain incomplete |
| `Faerindel_City_Profile.md` | Central elven gate city | Draft; mandatory city sections remain incomplete |
| `Ironforge_City_Profile.md` | Northern dwarven gate city | Draft; mandatory city sections remain incomplete |
| `NPC_Backstory_Personality_file.md` | Named NPC database | Draft; useful early profiles exist, but identity and leadership conflicts remain |

### Quests, sessions, and tracking

| File | Purpose | Verified state |
|---|---|---|
| `Captain_Ruriks_Request_Session_0-1.md` | Starter hook and medallion theft | Draft; investigation, conflict, and outcomes remain incomplete |
| `Early_Sessions_Plan_Sessions_0_to_5.md` | Session 0 outline and four branch concepts | Draft outline; not complete Sessions 1–5 preparation |
| `Quests_Player_Decisions_Impacts.md` | Quest state, decisions, attitudes, and session record | Active Reference; template exists but known pre-play entries are not yet seeded |
| `Enemy_Encounters_Stat_Blocks.md` | Campaign combat repository | Draft; current entries lack required actionable attack/ability details |

### Guidelines

- `City_Creation_Guidelines.md`
- `Guideline_Battle_Stat_Block_Management.md`
- `Guideline_NPC_Character_Creation.md`
- `Guideline_Quest_Creation.md`
- `Guideline_World_Geography_Map_Creation.md`
- `Guideline_World_Update_Change_Management.md`

Guidelines define mandatory, default, and optional content standards. They do not override approved canon.

## Known Unresolved Canon Decisions

Do not silently resolve these items:

1. How gods and divine power interact with dead zones
2. Whether beacon cores create a local magic exception and, if so, its mechanics
3. Exact Resonance Medallion mechanics and relationship to Aetherite technology
4. Ravensport government and military command structure
5. The canonical identity of the Rusty Anchor's Captain Rurik
6. Definitions of Aetheron, Aetherite, Aetherians/Aetheronians, and the Aetherbound

These decisions require a proposed canon batch and explicit approval before synchronization.

## Quick Navigation by Task

- **World lore/mechanics:** World Bible + relevant guideline
- **Map, route, distance, or settlement placement:** Geography + World Bible
- **City preparation:** relevant city profile + Geography + NPC database + City guideline
- **NPC interaction:** NPC database + tracker + relevant city/quest
- **Quest/session preparation:** starter/early-session file + tracker + NPC database + stat blocks + Quest guideline
- **Combat:** stat-block repository + World Bible mechanics + Battle guideline
- **Repository edit:** Governance + Skill + Pending Changes + target files + World Update guideline

## Verified Safe Structural Work

The following structural work is reflected in the current files:

- map-aligned Elyndria geography;
- corrected starter-quest filename;
- corrected governance and file-loading instructions;
- one staged approval workflow;
- accurate active pending inventory;
- archived logs clearly marked historical;
- duplicate World Bible directory removed;
- false completion claims removed from this Index;
- major-document status metadata added.

This section reports only structural work. It does not imply that the known canon or playability issues have been resolved.
