---
status: Reference
authority: Agent Entry Point
version: 2.1
last_reviewed: 2026-07-16
---

# Aetherbound Campaign Repository — Agent Instructions

## Mandatory Start

For any substantive campaign task, use repository tools on the real files. Do not rely on memory or invent filenames.

Read in this order:

1. `GOVERNANCE.md`
2. `SKILL.md`
3. `Pending_Changes.md`
4. The relevant canon, profile, tracker, quest/session, combat, and guideline files

`SKILL.md` is a repository operating manual. Some assistants do not automatically activate arbitrary skill files, so **open it explicitly**.

If file access fails, disclose the failure and do not fabricate campaign content.

## Authority and Conflict Handling

- Follow the hierarchy and ownership rules in `GOVERNANCE.md`.
- Preserve established canon within each file's authority scope.
- Flag contradictions rather than silently choosing or overwriting one version.
- Session plans and drafts do not override the World Bible, Geography, or dedicated authority files.
- The Campaign Index is navigation and factual status, not a lore authority.

## Change Control

- Read-only questions and audits do not require a pending entry.
- Unapproved repository edits must be staged in `Pending_Changes.md` with exact files and exact changes.
- Apply edits only after the user approves the pending entries or an already documented exact batch.
- After implementation, run `python scripts/validate_repository.py --strict-warnings`.
- Resolve validation errors before describing a batch as complete.
- Archive the approved batch and reset the active pending file only after validation passes.
- Use `Guideline_World_Update_Change_Management.md` for cross-file ripple checks after approval.

## Current Core Files

- `DnD_Campaign_World_Bible.md`
- `World_Geography.md`
- `Campaign_Index_and_Quick_Reference.md`
- `NPC_Backstory_Personality_file.md`
- `Quests_Player_Decisions_Impacts.md`
- `Enemy_Encounters_Stat_Blocks.md`
- `Early_Sessions_Plan_Sessions_0_to_5.md`
- `Captain_Ruriks_Request_Session_0-1.md`
- `Ravensport_City_Profile.md`
- `Deepanvil_City_Profile.md`
- `Faerindel_City_Profile.md`
- `Ironforge_City_Profile.md`
- all applicable guideline files

## Style

- Keep DM-facing output clear and actionable.
- Prefer updating an existing authority file over creating duplicate definitions.
- Follow the applicable guideline and distinguish mandatory requirements from recommendations.
- Never describe incomplete or unverified work as complete.
