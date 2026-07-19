---
status: Reference
authority: Repository Validation Guide
version: 1.3
last_reviewed: 2026-07-19
---

# Repository Validation

## Purpose

`scripts/validate_repository.py` checks repository structure and maintenance rules without choosing campaign canon. It uses only the Python standard library.

## Chat-to-GitHub Workflow

For the current user-and-ChatGPT handoff:

1. ChatGPT verifies the latest GitHub `main` commit and fetches current target files.
2. ChatGPT applies the approved batch to a working copy based on that commit.
3. ChatGPT runs strict validation before creating the changed-files ZIP.
4. The user extracts and uploads the files through GitHub.
5. GitHub Actions runs the same strict validator against the committed state.
6. The user reports the push, and ChatGPT verifies the commit and validation result.

A generated package is not a GitHub update. The update exists only after a visible GitHub commit.

## Run Locally

From the repository root:

```bash
python scripts/validate_repository.py --strict-warnings
```

Write a machine-readable report:

```bash
python scripts/validate_repository.py \
  --strict-warnings \
  --json validation-results.json
```

## Validation Scope

The validator checks:

1. Internal Markdown links and filename references.
2. Forbidden drafting markers in active Markdown.
3. City counts and the dual dead-zone knowledge model.
4. Mandatory headings in every `cities/*_City_Profile.md` file.
5. Required fields, attack bonuses, and damage expressions in every CR-bearing stat block.
6. Campaign Index version and metadata-status values against file front matter.
7. Duplicate authority claims, canonical NPC entries, city-profile ownership, location ownership, and proprietor ownership.
8. Active `Pending_Changes.md` inventory against real repository paths and the required proposal structure.
9. Creature-catalog integrity across 161 JSON and CSV records, 23 category pages, direct index links, anchors, groups, and manifest checksums.
10. Random encounter integrity across 23 d6 tables, 138 synchronized results, catalog resolution, gate-invasion minimums, and manifest checksums.

The creature and roll-table manifests under `creatures/` are deterministic maintenance records. Any approved catalog or table edit must regenerate the synchronized Markdown, JSON, CSV, indexes, and checksum records.

Historical and superseded files are excluded from active-content checks so retired names and paths can remain preserved for traceability.

## Known and Hidden Dead Zones

The validator tracks separate physical and in-world knowledge counts through [`validation/dead_zones.json`](validation/dead_zones.json):

- `known = 10`
- `hidden = 8`
- `actual = 18`

The canonical map visibly contains eighteen patches, while its legend intentionally reports the ten zones recognized by accepted Elyndrian knowledge. The validator therefore preserves the legend at ten and requires DM-facing authorities to preserve the full hidden reality.

The manifest also stores the map SHA-256 checksum. A changed map checksum requires a new visual audit and manifest update rather than automatic image guessing.

## Results and Exit Codes

- `PASS` indicates a completed validation category.
- `WARN` indicates maintenance work that does not make the repository structurally invalid.
- `ERROR` indicates a failed required check.
- Exit code `0`: no errors.
- Exit code `1`: one or more errors.
- Exit code `2`: warnings were found while `--strict-warnings` was enabled.

Validation success proves that the implemented structural rules pass. It does not prove that an unapproved creative decision should become canon.

## GitHub Actions

[`.github/workflows/validate-repository.yml`](.github/workflows/validate-repository.yml) runs strict validation when:

- a change is pushed to `main`;
- a pull request targets `main`;
- the workflow is started manually.

A green check means the tested commit passed. A red X means validation found a problem or the workflow could not run. The workflow uploads `validation-output.txt` and `validation-results.json` for fourteen days even when the run fails.

The workflow reports problems but does not edit files, repair canon, undo pushes, or merge changes.

## Maintenance Rule

When a new file, city, dead-zone discovery, creature record, roll table, stat-block format, metadata field, or naming convention is approved, update the validator and its manifest in the same change batch. Do not weaken a check merely to hide a real repository inconsistency.
