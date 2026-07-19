---
status: Reference
authority: Agent Entry Point
version: 2.3
last_reviewed: 2026-07-19
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
- Use `guidelines/Guideline_World_Update_Change_Management.md` for cross-file ripple checks after approval.

## Current Core Files

- `canon/` — World Bible and Geography
- `cities/` — four featured city profiles
- `npcs/` — canonical NPC master database
- `quests/` — starter quest, early-session plan, and live tracker
- `combat/` — custom encounter statistics
- `creatures/` — creature catalog, targeted lookup views, structured records, and random encounter roll tables
- `items/` — shop and item inventory authority
- `guidelines/` — campaign creation and update guidelines
- `Campaign_Index_and_Quick_Reference.md` — verified navigation and status

For random encounter requests, begin with `creatures/roll_tables/Roll_Table_Index.md`, roll first, then open the linked creature catalog entries before presenting or running the result.

## Style

- Keep DM-facing output clear and actionable.
- Prefer updating an existing authority file over creating duplicate definitions.
- Follow the applicable guideline and distinguish mandatory requirements from recommendations.
- Never describe incomplete or unverified work as complete.
