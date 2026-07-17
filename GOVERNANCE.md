---
status: Reference
authority: Repository Governance
version: 1.1
last_reviewed: 2026-07-16
---

# Aetherbound Repository Governance

## Purpose

This file is the highest authority for **repository behavior, document ownership, and change control**. It does not decide campaign lore. World lore remains in the appropriate canonical campaign files.

## Required Instruction Loading

Repository-aware assistants must not assume that a file named `SKILL.md` loads automatically.

Before substantive campaign work:

1. Read `AGENTS.md`.
2. Read this file, `GOVERNANCE.md`.
3. Read `SKILL.md` as the detailed operating manual.
4. Check `Pending_Changes.md` for active proposals.
5. Read the relevant canon, profile, tracker, and guideline files for the request.

If repository access is unavailable, the assistant must disclose that limitation and must not invent file contents, filenames, or canon.

## Authority Hierarchy

When documents disagree, use this order:

1. **`GOVERNANCE.md`** — repository process, status meanings, authority ownership, and approval workflow.
2. **`DnD_Campaign_World_Bible.md`** — setting-wide lore, history, world mechanics, and campaign-wide facts.
3. **`World_Geography.md`** — spatial relationships, terrain, roads, rivers, ports, distances, and dead-zone placement.
4. **Dedicated authority files** — detailed city profiles, NPC database, quest files, tracker, and combat repository within their defined scopes.
5. **`Campaign_Index_and_Quick_Reference.md`** — navigation and factual project status only. It does not override canon.
6. **Session plans and drafts** — preparation material. New claims in a draft do not become canon until approved and synchronized.
7. **`Pending_Changes.md`** — proposals only; never canon.
8. **Archived pending logs** — historical records only; never active instructions or canon.

If two files at the same level conflict, do not silently select one. Report the conflict and stage a proposed resolution.

## Canon Ownership by Subject

| Subject | Primary authority | Supporting files |
|---|---|---|
| Setting-wide lore and world mechanics | `DnD_Campaign_World_Bible.md` | Geography, profiles, quests |
| Terrain, placement, routes, and distance | `World_Geography.md` | World Bible, city profiles |
| Detailed city operations and locations | Relevant `*_City_Profile.md` | World Bible, Geography, NPC database |
| NPC identity, personality, and relationships | `NPC_Backstory_Personality_file.md` | City profiles, quests, tracker |
| Current quest state, decisions, attitudes, and session outcomes | `Quests_Player_Decisions_Impacts.md` | Quest and session files |
| Quest design and prepared scenes | Dedicated quest/session file | Tracker, NPC database, city profile |
| Combat-ready custom statistics | `Enemy_Encounters_Stat_Blocks.md` | World mechanics and encounter files |
| Project navigation and readiness | `Campaign_Index_and_Quick_Reference.md` | All current files |

Supporting summaries must point back to the primary authority rather than creating a second independent definition.

## Document Status

Major documents should begin with metadata containing at least:

- `status`
- `authority`
- `version`
- `last_reviewed`
- `review_state` when unresolved work must be visible

Status meanings:

- **Canon** — approved campaign truth within the file's authority scope.
- **Draft** — preparation or proposed content that is not automatically canon.
- **Active Reference** — operational record that changes during play, such as the quest tracker.
- **Reference** — instructions, navigation, templates, or supporting information; not world canon.
- **Historical** — preserved record; not active instructions or canon.
- **Superseded** — retained only for traceability and must point to its replacement.

A document marked Canon may still have a `review_state` noting unresolved conflicts. Those conflicts must not be silently resolved.

## Change Modes

### 1. Read-only analysis

Questions, audits, summaries, and recommendations do not require a pending-change entry when no repository file is being modified.

### 2. Proposed repository change

When the user requests an edit but has not approved an exact change batch:

1. Record the proposal in `Pending_Changes.md`.
2. Name every affected file.
3. Describe the exact edit and required cross-references.
4. Do not edit target files yet.

### 3. Approved implementation

Implementation may begin when the user explicitly approves:

- the active pending-change entries; or
- a previously documented batch whose affected files and scope are already clear.

After approval:

1. Apply only the approved changes.
2. Perform the ripple and consistency checks in `Guideline_World_Update_Change_Management.md`.
3. Update factual status and file metadata in the Campaign Index.
4. Run `python scripts/validate_repository.py --strict-warnings`.
5. Resolve validation errors before closing the batch.
6. Archive the approved batch in the next numbered `Pending_Changes_Archived_XX.md` file.
7. Reset `Pending_Changes.md` to an empty active template.

## Safe Structural Changes vs. Canon Decisions

Structural changes may correct filenames, paths, document status, navigation, duplicate sections, inaccurate project-status claims, and governance instructions without selecting unresolved lore.

A structural cleanup must not decide among competing canon versions. Those choices require an explicit canon proposal and approval.

## Campaign Index Restrictions

The Campaign Index may contain only:

- real file navigation;
- current status verified against the files;
- current document versions;
- known unresolved decisions;
- clearly labeled future work.

It must not claim that work was completed merely because it was planned, requested, or attempted. Git history and archived change logs hold historical implementation records.

## Final Consistency Check

Before completing an approved edit, verify:

- `python scripts/validate_repository.py --strict-warnings` completes successfully;
- every referenced filename exists;
- authority files agree or unresolved conflicts are clearly flagged;
- no active file depends on an unavailable “previous version”;
- the Index describes the actual current state;
- `Pending_Changes.md` has been reset and the approved batch archived;
- no unapproved canon decision was introduced.
