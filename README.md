# Aetherbound Campaign Repository

Homebrew D&D 5e campaign centered on Ravensport, dimensional gates, magic dead zones, Aetherite technology, Aetheron, and Lord Cassian Veyne.

For the verified current state, read [`Campaign_Index_and_Quick_Reference.md`](Campaign_Index_and_Quick_Reference.md).

## Start Here

Before changing campaign material, read:

1. [`GOVERNANCE.md`](GOVERNANCE.md)
2. [`SKILL.md`](SKILL.md)
3. [`Pending_Changes.md`](Pending_Changes.md)
4. The relevant campaign and guideline files

## Working With ChatGPT

ChatGPT currently does **not** directly commit or push changes to this repository.

The normal workflow is:

1. The user requests or approves a batch.
2. ChatGPT checks the latest commit on GitHub `main`.
3. ChatGPT fetches the current files affected by the batch.
4. ChatGPT prepares a **changed-files ZIP** based on that exact commit.
5. ChatGPT provides an implementation note containing the base commit SHA, included paths, upload instructions, expected validation result, and confirmation that nothing was committed by ChatGPT.
6. The user downloads and extracts the ZIP.
7. The user uploads the extracted files through GitHub.
8. The user returns to chat and reports that the batch was pushed.
9. ChatGPT verifies the new commit, changed files, archive, `Pending_Changes.md`, Campaign Index, and validation result.

## Important Upload Rules

- Upload the **extracted files**, not the ZIP itself.
- Preserve folder paths, especially `.github/workflows/`, `scripts/`, and `validation/`.
- Use the changed-files ZIP for normal updates.
- Do not overwrite the entire repository with an older complete-repository ZIP.
- Creating or downloading a package does not mean GitHub has changed.
- A batch is complete only after the GitHub commit is visible and verified.

## Base Commit Rule

Every generated package is tied to a specific GitHub commit.

When `main` changes after the package is generated, stop and have ChatGPT rebuild or reconcile the package before uploading it. This prevents an older package from replacing newer repository work.

## Validation

Before packaging, ChatGPT runs the repository validator against the prepared working copy. After the user pushes, GitHub Actions runs the validator against the committed repository state.

- A green check means the committed version passed the implemented structural checks.
- A red X means the workflow or repository validation failed and must be reviewed.

See [`VALIDATION.md`](VALIDATION.md) for details.

## Core Files

| Subject | Primary file |
|---|---|
| Setting lore and mechanics | [`DnD_Campaign_World_Bible.md`](DnD_Campaign_World_Bible.md) |
| Geography and dead zones | [`World_Geography.md`](World_Geography.md) |
| Current repository status | [`Campaign_Index_and_Quick_Reference.md`](Campaign_Index_and_Quick_Reference.md) |
| NPCs | [`NPC_Backstory_Personality_file.md`](NPC_Backstory_Personality_file.md) |
| Quest decisions and consequences | [`Quests_Player_Decisions_Impacts.md`](Quests_Player_Decisions_Impacts.md) |
| Custom encounters | [`Enemy_Encounters_Stat_Blocks.md`](Enemy_Encounters_Stat_Blocks.md) |
| Active proposals | [`Pending_Changes.md`](Pending_Changes.md) |

## Batch Completion Checklist

A batch is complete only when:

- [ ] The package base matched the repository before upload.
- [ ] The user uploaded the extracted changed files.
- [ ] A new GitHub commit exists.
- [ ] ChatGPT verified the expected changed files.
- [ ] GitHub validation passed.
- [ ] The batch was archived.
- [ ] `Pending_Changes.md` was reset.
- [ ] The Campaign Index reflects the real repository state.
