---
name: dnd-campaign-helper
description: Use this skill for almost any question about the D&D campaign world, NPCs, quests, player decisions, combat, or related content. Triggers on campaign terms (Ravensport, Faerindel, Ironforge, Deepanvil, dead zones, gates, Lord Veyne, Aetherbound, Captain Rurik) or when the user discusses NPCs, quests, player actions, or world interactions.
---

# D&D Campaign Helper Skill

**System Overview**:
1. Skill activates on any campaign-related query.
2. Always check **Pending_Changes.md** first (all changes live here until approved).
3. Load relevant core files (World Bible, NPC database, Quest/Decision tracker, city profiles).
4. For NPCs/quests/decisions: Use the dedicated rules below + tracker for attitudes and progression.
5. When changes are requested → Log in Pending_Changes.md only.
6. Only apply changes when user explicitly approves the change log.

This skill ensures consistent, accurate responses by loading the right campaign files automatically.

## Core Files to Load
- **DnD_Campaign_World_Bible.md** — Master lore and plot.
- **NPC_Backstory_Personality_file.md** — All NPCs (check for quest connections).
- **Quests_Player_Decisions_Impacts.md** — Master tracker for quests, decisions, progression, and NPC attitudes.
- **Ravensport_City_Profile.md**, **Faerindel_City_Profile.md**, **Ironforge_City_Profile.md**, **Deepanvil_City_Profile.md** — City details.
- **Enemy_Encounters_Stat_Blocks.md** — Combat.
- All **Guideline_*.md** files.

## Quest, Decision & NPC Relationship Tracking Rules (Critical)
When the user mentions an NPC, player conversation, quest, decision, or progression:
1. Check **NPC_Backstory_Personality_file.md** for the NPC’s details and quest connections.
2. Check **Quests_Player_Decisions_Impacts.md** for:
   - Current quest status and progression
   - Recent player decisions and their impacts
   - That NPC’s attitude toward the party or specific players (likes/dislikes)
3. Cross-reference the **World Bible** for ongoing plot threads and Aetherbound activity.
4. In your response, clearly note:
   - Whether the NPC should reveal quest information now (based on current progress and attitude)
   - Any long-term consequences of recent player decisions
   - How the NPC currently feels about the players (and why)
5. Suggest updates to the tracker file when new decisions or quest developments occur.

**Quick Triggers**:
- Player talks to an NPC → Check quest status + current attitude in tracker.
- Player makes a decision → Note ripple effects and update tracker.
- User asks about quest progress or reputation → Summarize from World Bible + tracker.

## General Rules
- Always load relevant files before answering.
- Maintain consistency across all campaign files.
- For combat in dead zones: Adjust enemy capabilities accordingly.
- Keep responses clear and actionable for the DM.

## Change Log / Pending Changes Workflow (Strict)
- All changes (big or small) are first written only to **Pending_Changes.md**. When logging, always specify the exact file(s) affected and the precise change needed in each one.
- Nothing is applied to other files until you explicitly say you accept/approve the change log.
- When approved:
  1. Apply all changes to the relevant documents.
  2. Rename the current `Pending_Changes.md` to an archived version (e.g. `Pending_Changes_Archived_01.md`).
  3. Create a fresh `Pending_Changes.md` containing **only the lines that start with >**. All other lines are cleared.
- Archived logs are kept for history but are no longer active.

Use this skill to handle quest tracking and decision impacts efficiently.