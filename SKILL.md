---
name: dnd-campaign-helper
description: Repository operating manual for the Aetherbound D&D campaign. Use for campaign lore, NPCs, quests, player decisions, combat, cities, geography, and repository edits.
status: Reference
authority: Campaign Operating Procedure
version: 2.2
last_reviewed: 2026-07-17
---

# Aetherbound Campaign Helper

## Important Loading Note

This file is usable by ChatGPT and other repository-aware assistants **after it is explicitly opened**. The filename alone does not guarantee automatic activation on every platform. `AGENTS.md` therefore directs agents to read this file at the start of substantive campaign work.

`GOVERNANCE.md` outranks this file if a process rule conflicts.

## Startup Checklist

1. Open `GOVERNANCE.md` and follow its authority hierarchy.
2. Inspect `Pending_Changes.md` for active proposals that may affect the request.
3. Classify the task as read-only analysis, a proposed repository change, or an approved implementation.
4. Load the relevant files from the matrix below.
5. Check status metadata and unresolved-conflict notes before treating a document as complete canon.

Do not load every file by default. Load all files needed to verify the specific answer or edit.

## File-Loading Matrix

| Request type | Minimum files to inspect |
|---|---|
| Setting lore or world mechanics | World Bible, Geography when spatial, relevant dedicated profiles, applicable guideline |
| City/location | Relevant city profile, World Bible, Geography, NPC database, City guideline |
| NPC or relationship | NPC database, tracker, relevant city/quest/session files, NPC guideline |
| Quest/session/progression | Dedicated quest/session file, tracker, NPC database, relevant city profile, stat blocks, Quest guideline |
| Combat or encounter | Stat-block repository, relevant world mechanics, encounter/quest file, Battle guideline |
| Geography/map | Geography, World Bible city/dead-zone lists, relevant city profiles, Geography guideline |
| Repository edit/process | Governance, Pending Changes, target files, World Update guideline, Campaign Index |

## Read-Only Questions and Audits

For explanations, audits, summaries, and recommendations:

- read the relevant files;
- cite or name the files supporting the answer;
- distinguish canon, draft material, and unresolved conflicts;
- do not create a pending entry unless a repository edit is requested.

## NPC, Quest, and Decision Tracking

When the user asks about an NPC, quest, player choice, reputation, or progression:

1. Check `npcs/NPC_Backstory_Personality_file.md` for identity, motives, and connections.
2. Check `quests/Quests_Player_Decisions_Impacts.md` for current status, decisions, reactions, and attitudes.
3. Check the relevant quest/session and city files.
4. Cross-reference the World Bible for campaign-wide plot threads.
5. Explain, when relevant:
   - what the NPC currently knows;
   - whether the NPC should reveal it now;
   - the NPC's current attitude and why;
   - immediate and long-term consequences;
   - what tracker update would be needed after play.

Do not invent a tracker state when the tracker is empty. State that the information has not yet been recorded.

## Combat and Dead Zones

Before using a custom stat block:

1. Check `combat/Enemy_Encounters_Stat_Blocks.md`.
2. Follow `guidelines/Guideline_Battle_Stat_Block_Management.md`.
3. Apply only dead-zone mechanics approved in the World Bible.
4. If draft session material introduces a conflicting exception, flag it rather than applying it silently.
5. Ensure the final encounter entry is actionable for the DM.

## Repository Change Workflow

### Proposed change

When the user requests an edit that has not yet been approved as an exact batch:

1. Add a file-specific proposal to `Pending_Changes.md`.
2. Include every affected file, exact changes, and cross-reference work.
3. Do not modify target files.
4. Summarize the proposal and ask for approval.

### Approved implementation

When the user explicitly approves the active proposals or a previously documented exact batch:

1. Re-read the current target files before editing.
2. Apply only the approved scope.
3. Run the ripple checks in `guidelines/Guideline_World_Update_Change_Management.md`.
4. Update the Campaign Index to reflect only the verified final state and exact metadata versions/statuses.
5. Run `python scripts/validate_repository.py --strict-warnings`.
6. Resolve validation errors before closing the batch.
7. Create the next numbered archived change record.
8. Reset `Pending_Changes.md` to an empty active template.
9. Report exactly what changed and identify any decisions that remain unresolved.

If repository write access is unavailable, produce a patch or replacement files and clearly state that nothing was committed.

## Content-Creation Rules

- Use the applicable guideline.
- Treat mandatory requirements as requirements, default guidance as guidance, and optional fields as optional.
- Preserve player agency in quests.
- Keep minor NPCs concise; use fuller profiles for important or recurring NPCs.
- Prefer a single authoritative definition with cross-references over duplicated facts.
- Do not turn a session idea into setting-wide canon without approval and synchronization.
- Do not claim a file is complete unless its mandatory requirements are actually present.

## Final Validation Checklist

Before answering or committing:

- [ ] Real files were inspected.
- [ ] Authority and status metadata were respected.
- [ ] Relevant tracker/profile/guideline files were checked.
- [ ] `python scripts/validate_repository.py --strict-warnings` passed for repository changes.
- [ ] Contradictions were flagged rather than silently resolved.
- [ ] All referenced filenames and paths exist.
- [ ] No unavailable previous-version placeholder is being relied upon.
- [ ] No unapproved canon choice was added.
- [ ] The Campaign Index, pending log, and archive reflect the actual final state when files were changed.
