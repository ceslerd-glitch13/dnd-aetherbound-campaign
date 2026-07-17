---
status: Reference
authority: Approved Change Implementation Guideline
version: 2.1
last_reviewed: 2026-07-16
---

# Guideline: World Update and Change Management

## Purpose

This guideline explains how to apply an **approved** campaign change completely and consistently. `../GOVERNANCE.md` and `../SKILL.md` control whether an edit is still a proposal or has been approved for implementation.

## Core Rule

Respect the user's creative decision while protecting repository consistency.

- Do not debate the user's preferred direction merely because another design choice is possible.
- Do flag an existing contradiction, missing decision, or mechanical consequence before implementation when it affects the requested result.
- Do not silently choose between competing canon versions.

## Stage Before Editing

Unless the user has already approved an exact documented batch:

1. Record the requested change in `../Pending_Changes.md`.
2. Name every affected file.
3. Describe the exact change and required follow-up work.
4. Wait for explicit approval before editing target files.

Read-only analysis and recommendations do not require a pending entry.

## Apply an Approved Change

### 1. Confirm the approved scope

- Re-read the approved pending entry or documented batch.
- Apply only what was approved.
- Ask for clarification only when the approved scope cannot be implemented without selecting an unresolved canon option.

### 2. Identify all affected authority files

Check, as applicable:

- `../canon/DnD_Campaign_World_Bible.md`
- `../canon/World_Geography.md`
- relevant city profiles
- `../npcs/NPC_Backstory_Personality_file.md`
- `../quests/Quests_Player_Decisions_Impacts.md`
- quest and session files
- `../combat/Enemy_Encounters_Stat_Blocks.md`
- applicable guidelines
- `../Campaign_Index_and_Quick_Reference.md`

Use the ownership table in `../GOVERNANCE.md` to decide where the primary definition belongs.

### 3. Update the primary authority first

- Add or revise the fact in its primary authority file.
- Edit existing references rather than creating a parallel definition.
- Update relationships, distances, trade, politics, military effects, NPCs, and quest dependencies when relevant.

### 4. Update geography when spatial

- Record the relative position or coordinates.
- Update roads, rivers, ports, trade routes, and travel times.
- Update dead-zone placement or route effects when applicable.
- Preserve the map-interpretation rules in `../canon/World_Geography.md`.

### 5. Apply ripple effects

Check whether the approved change affects:

- existing quests or hooks;
- player-known information;
- city services, trade, politics, or military movement;
- NPC identities, motives, attitudes, or relationships;
- encounter statistics or dead-zone variants;
- status claims in the Campaign Index.

Update only the files actually affected.

### 6. Keep the change minimal but complete

- Do not overbuild beyond the approved request.
- Do not omit required synchronization.
- Leave unresolved canon decisions visibly unresolved.

### 7. Validate and close the batch

Before reporting completion, run:

```bash
python scripts/validate_repository.py --strict-warnings
```

Then verify:

- [ ] The validation script completed successfully.
- [ ] The primary authority file was updated.
- [ ] Geography was updated if spatial.
- [ ] Existing references were synchronized.
- [ ] New key locations or recurring NPCs have appropriate records.
- [ ] Quest, tracker, and combat effects were addressed where applicable.
- [ ] Every referenced filename exists.
- [ ] The Campaign Index reflects the real current state.
- [ ] The approved batch was archived.
- [ ] `../Pending_Changes.md` was reset.

## Common Change Examples

| Request | Primary update | Typical supporting updates |
|---|---|---|
| Add or move a city | World Bible and Geography | City profile, NPC database, quests, Index |
| Add a major road | Geography | City trade/travel notes, quests, Index |
| Change a dead zone | World Bible and Geography | Combat rules, nearby cities, quests, Index |
| Change an NPC's role | NPC database | City profile, quests, tracker, Index |
| Add a world mechanic | World Bible | Sessions, combat, items, tracker, Index |

## Final Principle

**Stage the exact proposal → receive approval → update the primary authority → synchronize every affected file → validate and archive the batch.**
